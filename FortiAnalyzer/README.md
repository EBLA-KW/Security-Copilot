# FortiAnalyzer Custom Plugin for Copilot for Security

This repository contains a custom plugin to integrate **FortiAnalyzer** with **Copilot for Security**. This plugin enables security teams to access FortiAnalyzer data directly in Copilot, enhancing capabilities for incident response, threat detection, and network security monitoring.

## Features

- Retrieve and analyze incident and log data from FortiAnalyzer
- Fetch threat intelligence and IOCs (Indicators of Compromise)
- Enable automated responses to FortiAnalyzer security events in Copilot

## Requirements

- FortiAnalyzer with API access enabled
- API Key and API Key ID for FortiAnalyzer
- Microsoft Copilot for Security access

## Setup

1. **Clone this repository**:
   ```bash
   git clone https://github.com/EBLA-KW/security-copilot.git
   cd fortianalyzer-copilot-plugin
   ```

2. **Configure API Credentials**:
   - Add your FortiAnalyzer **API Key** and **API Key ID** to the plugin configuration file.

3. **Install dependencies** (if required):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

After setup, you can start using the FortiAnalyzer plugin in Copilot to retrieve incidents, logs, and threat data.

## License

This project is licensed under the MIT License.
