# Taegis Vulnerability Management API Integration

This repository contains OpenAPI specifications for interacting with the **Taegis Vulnerability Management API**. The Taegis API provides endpoints for managing and retrieving vulnerability data, including individual vulnerabilities and vulnerability groups. These specifications enable enhanced automation and integration with vulnerability management workflows.

## Endpoints

### 1. Retrieve Vulnerability by ID
- **Endpoint**: `GET /api/v2/vulnerabilities/{id}`
- **Description**: Retrieves detailed information about a specific vulnerability by its ID.
- **Usage**: Use this endpoint to get full vulnerability details for analysis and management.
- **YAML Specification**: [taegis_vulnerability.yaml](./Vulnerability.yaml)

### 2. Vulnerability Group List
- **Endpoint**: `GET /api/v2/vulnerability-groups`
- **Description**: Retrieves a paginated list of vulnerability groups with optional filtering and sorting.
- **Usage**: This endpoint provides an overview of vulnerability groups, allowing prioritization and grouping based on asset, severity, and more.
- **YAML Specification**: [taegis_vulnerability_group_list.yaml](./Vulnerability_group_list.yaml)

## Requirements

- **Taegis API Access**: API access for the Taegis Vulnerability Management system
- **API Key**: Obtain an API key for authentication with Taegis

## Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/EBLA-KW/taegis-vulnerability-api.git
   cd taegis-vulnerability-api
   ```

2. **API Access**:
   - Configure API credentials in your application or tool to authenticate with Taegis.
   - Refer to Taegis documentation for detailed API authentication steps.

## License

This project is licensed under the MIT License.

---

These OpenAPI specifications can be imported into tools like Postman or Swagger to explore and test the API.

