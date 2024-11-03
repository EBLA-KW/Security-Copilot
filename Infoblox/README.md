# Infoblox BloxOne DNS Data API Integration

This repository contains OpenAPI specifications for interacting with the **Infoblox BloxOne DNS Data API**. The DNS Data API provides primary authoritative zone support, allowing management of DNS resource records. This integration includes endpoints to retrieve DNS records, access individual records, and increment the serial number of an SOA record.

## Endpoints

### 1. Retrieve DNS Resource Records
- **Endpoint**: `GET /dns/record`
- **Description**: Retrieves a collection of DNS resource records.
- **Usage**: Use this endpoint to list DNS records in an authoritative zone with optional filtering, pagination, and sorting.
- **YAML Specification**: [infoblox_dns_records.yaml](./DNS_records.yaml)

### 2. Retrieve a DNS Resource Record by ID
- **Endpoint**: `GET /dns/record/{id}`
- **Description**: Retrieves a specific DNS resource record by its ID.
- **Usage**: Use this endpoint to get details of an individual DNS record in an authoritative zone.
- **YAML Specification**: [infoblox_dns_record.yaml](./DNS_record.yaml)

### 3. Increment Serial Number for SOA Record
- **Endpoint**: `POST /dns/record/{id}/serial_increment`
- **Description**: Increments the serial number for a specific SOA (Start of Authority) record.
- **Usage**: Use this endpoint to update the serial number of an SOA record in an authoritative zone.
- **YAML Specification**: [infoblox_soa_serial_increment.yaml](./SOA_serial_increment.yaml)

For more info please visit: https://docs.infoblox.com/space/BloxOneDDI/186745633/Universal+DDI+API+Guide

## Requirements

- **Infoblox BloxOne** account with API access
- **API Key** for authorization

## Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/EBLA-KW/infoblox-bloxone-dns-api.git
   cd infoblox-bloxone-dns-api
   ```

2. **API Access**:
   - Configure API credentials in your application to interact with the Infoblox API.
   - Refer to Infoblox documentation for detailed API authentication.

## License

This project is licensed under the MIT License.

---

These OpenAPI specifications can be imported into tools like Postman or Swagger for testing and exploring the API.

