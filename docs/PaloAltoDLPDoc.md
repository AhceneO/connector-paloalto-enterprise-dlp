## About the connector

Palo Alto Enterprise DLP discovers and protects company data across every data channel and repository.
<p>This document provides information about the Palo Alto Enterprise DLP Connector, which facilitates automated interactions, with a Palo Alto Enterprise DLP server using FortiSOAR&trade; playbooks. Add the Palo Alto Enterprise DLP Connector as a step in FortiSOAR&trade; playbooks and perform automated operations with Palo Alto Enterprise DLP.</p>

### Version information

Connector Version: 1.0.1

Authored By: Fortinet

Certified: No

## Installing the connector

<p>Use the <strong>Content Hub</strong> to install the connector. For the detailed procedure to install a connector, click <a href="https://docs.fortinet.com/document/fortisoar/0.0.0/installing-a-connector/1/installing-a-connector" target="_top">here</a>.</p><p>You can also use the <code>yum</code> command as a root user to install the connector:</p>
<pre>yum install cyops-connector-paloalto-enterprise-dlp</pre>

## Prerequisites to configuring the connector

- You must have the credentials of Palo Alto Enterprise DLP server to which you will connect and perform automated operations.
- The FortiSOAR&trade; server should have outbound connectivity to port 443 on the Palo Alto Enterprise DLP server.

## Minimum Permissions Required

- Not applicable

## Configuring the connector

For the procedure to configure a connector, click [here](https://docs.fortinet.com/document/fortisoar/0.0.0/configuring-a-connector/1/configuring-a-connector)

### Configuration parameters

<p>In FortiSOAR&trade;, on the Connectors page, click the <strong>Palo Alto Enterprise DLP</strong> connector row (if you are in the <strong>Grid</strong> view on the Connectors page) and in the <strong>Configurations</strong> tab enter the required configuration details:</p>
<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Server URL</td><td>Specify the URL of the Palo Alto Enterprise DLP server to connect and perform automated operations.
</td>
</tr><tr><td>Client ID</td><td>Specify the client ID to access the Palo Alto Enterprise DLP server to connect and perform automated operations.
</td>
</tr><tr><td>Client Secret</td><td>Specify the client secret to access the Palo Alto Enterprise DLP server to connect and perform automated operations.
</td>
</tr><tr><td>Verify SSL</td><td>Specifies whether the SSL certificate for the server is to be verified or not. <br/>By default, this option is set to True.</td></tr>
</tbody></table>

## Actions supported by the connector

The following automated operations can be included in playbooks and you can also use the annotations to access operations from FortiSOAR&trade; release 4.10.0 and onwards:
<table border=1><thead><tr><th>Function</th><th>Description</th><th>Annotation and Category</th></tr></thead><tbody><tr><td>Get Report Details</td><td>Retrieves the specific report information from Palo Alto Enterprise DLP based on the report ID you have specified.</td><td>get_report_details <br/>Investigation</td></tr>
</tbody></table>

### operation: Get Report Details

#### Input parameters

<table border=1><thead><tr><th>Parameter</th><th>Description</th></tr></thead><tbody><tr><td>Report ID</td><td>Specify the ID of the report based on which you want to retrieve details from Palo Alto Enterprise DLP.
</td></tr><tr><td>Fetch Snippets</td><td>Select the option, if you want to retrieves snippets from the DLP report. By default, it set as True.
</td></tr></tbody></table>

#### Output

The output contains the following populated JSON schema:

<pre>{
    "txn_id": "",
    "report_id": "",
    "data_profile_id": "",
    "data_profile_name": "",
    "type": "",
    "tenant_id": "",
    "fileSha": "",
    "file_name": "",
    "file_type": "",
    "file_size_in_bytes": "",
    "extracted_file_size_in_bytes": "",
    "detection_time": "",
    "data_pattern_rule_1_verdict": "",
    "data_pattern_rule_2_verdict": "",
    "scanContentRawReport": {
        "data_pattern_rule_1_results": [
            {
                "data_pattern_id": "",
                "version": "",
                "name": "",
                "technique": "",
                "type": "",
                "strict_detection_frequency": "",
                "proximity_detection_frequency": "",
                "detection_frequency": "",
                "unique_strict_detection_frequency": "",
                "unique_checksum_detection_frequency": "",
                "unique_proximity_detection_frequency": "",
                "unique_detection_frequency": "",
                "weighted_frequency": "",
                "score": "",
                "high_confidence_frequency": "",
                "medium_confidence_frequency": "",
                "low_confidence_frequency": "",
                "unique_high_confidence_frequency": "",
                "unique_medium_confidence_frequency": "",
                "unique_low_confidence_frequency": "",
                "state": ""
            }
        ],
        "data_pattern_rule_2_results": []
    },
    "message": "",
    "time": "",
    "scan_request_received_time": "",
    "file_download_start_time": "",
    "file_download_finish_time": "",
    "extraction_start_time": "",
    "extraction_finish_time": "",
    "get_profile_patterns_start_time": "",
    "get_profile_patterns_finish_time": "",
    "scanning_start_time": "",
    "scanning_finish_time": "",
    "generate_verdict_start_time": "",
    "generate_verdict_finish_time": "",
    "scan_request_finished_time": ""
}</pre>

## Included playbooks

The `Sample - paloalto-enterprise-dlp - 1.0.1` playbook collection comes bundled with the Palo Alto Enterprise DLP connector. These playbooks contain steps using which you can perform all supported actions. You can see bundled playbooks in the **Automation** > **Playbooks** section in FortiSOAR&trade; after importing the Palo Alto Enterprise DLP connector.

- Get Report Details

**Note**: If you are planning to use any of the sample playbooks in your environment, ensure that you clone those playbooks and move them to a different collection since the sample playbook collection gets deleted during connector upgrade and delete.
