# Project Name: Cortex XDR 
# Author: Hassan Al Faisal "Software Developer" | Mohamed Sami Saoud "Technical Lead" | Omar Sabri "Security Engineer"
# Company: EBLA Kuwait 
# Date Created: Dec. 4 2024
# Last Updated: Dec. 5 2024
# Description: Use direct API calls to Cortex to get the data required to reason over in Json format and leverage Azure function to add custom security coplot plugin. Additionally, this approach will consume significantly fewer SUKs, benefiting the customer by reducing Security Copilot's resource consumption.

import requests
import logging
import json
import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# URL /?op='<code>'&data='<data>'

# Http Trigger
@app.route(route="cortex_xdr_sami")
def http_cortex_xdr_sami(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    op = req.params.get('op')
    data = req.params.get('data')

    cortex = Cortex()
    response = ""
    match op: # Call the function based on the op and pass in data
        case "GetIncidents":
            # default code block
            response = cortex.get_incidents(data)
        case _:
            response = "Input data is missing"

    return func.HttpResponse(response,status_code=200)


class Cortex:
    def __init__(self):
        self.authorizationkey = ""
        self.authid = ""
        self.url = ""
        self.baseurl = ""

 
    def get_incidents(self, data=""):
        try:
            request_body = {
                "request_data": {
                    "search_from": 0,
                    "search_to": 5
                }
            }

            response = requests.post(
                url=self.baseurl + "/public_api/v1/incidents/get_incidents",
                json=request_body,
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": self.authorizationkey,
                    "x-xdr-auth-id": self.authid,
                }
            )

            # Will raise an HTTPError if the HTTP request returned an unsuccessful status code
            response.raise_for_status()  

            json_response = response.json()
            reply = json_response["reply"]
            total_count = reply["total_count"]
            result_count = reply["result_count"]
            incidents:list = reply["incidents"]



            print(incidents[0])
            # response_str = json.dumps(response_obj)
            return json.dumps(incidents)

        except Exception as e:
            # raise SystemExit(f"Failed to make the request. Error: {e}") # Will result in HTTP 500
            return str(e)



