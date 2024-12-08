# Project Name: Cortex XDR 
# Author: Mohamed Sami Saoud "Technical Lead" | Omar Hasan Sabri "Security Engineer" | Hassan Al Faisal "Software Developer"
# Company: EBLA Kuwait 
# Date Created: Dec. 8 2024
# Last Updated: Dec. 8 2024
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
    match op:  # Call the function based on the operation
        case "GetIncidents":
            response = cortex.get_incidents(data)
        case "GetIncidentExtraData":
            response = cortex.get_incident_extra_data(data)
        case _:
            response = "Invalid operation. Supported operations are 'GetIncidents' and 'GetIncidentExtraData'."

    return func.HttpResponse(response, status_code=200)


class Cortex:
    def __init__(self):
        self.authorizationkey = ""
        self.authid = ""
        self.url = ""
        self.baseurl = ""

    def get_incidents(self, data=""):
        try:
            request_body = {
                "request_data": {}
            }

            response = requests.post(
                url=self.baseurl + "public_api/v1/incidents/get_incidents",
                json=request_body,
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": self.authorizationkey,
                    "x-xdr-auth-id": self.authid,
                }
            )

            response.raise_for_status()
            json_response = response.json()
            incidents = json_response["reply"].get("incidents", [])

            return json.dumps(incidents)

        except Exception as e:
            return str(e)

    def get_incident_extra_data(self, data=""):
        try:
            # Check if data is provided
            if not data:
                return json.dumps({"error": "'data' must be provided and should include an incident_id."})

            # Handle simple string input (e.g., '2818')
            if isinstance(data, str) and data.isdigit():
                incident_id = data
                alerts_limit = 5  # Default alerts limit
            else:
                # Parse data as JSON for complex input
                input_data = json.loads(data)
                incident_id = input_data.get("incident_id", None)
                alerts_limit = input_data.get("alerts_limit", 5)

            if not incident_id:
                return json.dumps({"error": "'incident_id' must be provided in the request data."})

            # Construct the request body
            request_body = {
                "request_data": {
                    "incident_id": incident_id,
                    "alerts_limit": alerts_limit
                }
            }

            # Make the API call
            response = requests.post(
                url=self.baseurl + "public_api/v1/incidents/get_incident_extra_data/",
                json=request_body,
                headers={
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "Authorization": self.authorizationkey,
                    "x-xdr-auth-id": self.authid,
                }
            )

            response.raise_for_status()
            json_response = response.json()
            incident_extra_data = json_response.get("reply", {})

            return json.dumps(incident_extra_data)

        except Exception as e:
            return str(e)


# Example usage
# if __name__ == "__main__":
#     cortext = Cortex()
#     # Test GetIncidents
#     print(cortext.get_incidents())
#     # Test GetIncidentExtraData with simple input
#     print(cortext.get_incident_extra_data("2818"))
#     # Test GetIncidentExtraData with complex input
#     print(cortext.get_incident_extra_data(json.dumps({"incident_id": "2818", "alerts_limit": 10})))
