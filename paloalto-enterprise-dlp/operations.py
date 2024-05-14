"""
This file will be auto-generated on each "new operation action", so avoid editing in this file.
"""

from .paloalto_api_auth import *
from connectors.core.connector import get_logger, ConnectorError
import requests, json

logger = get_logger('paloalto-enterprise-dlp')


def make_rest_call(endpoint, method, connector_info, config, data=None, params=None):
    try:
        co = PaloAlto(config)
        url = co.host + endpoint
        token = co.validate_token(config, connector_info)
        headers = {
            'Content-Type': 'application/json',
            'Authorization': token
        }
        logger.debug("Action Header: {0}".format(headers))
        logger.debug("Action Endpoint: {0}".format(url))
        response = requests.request(method, url, headers=headers, verify=co.verify_ssl, data=data, params=params)
        logger.debug("Action Response: {0}".format(response.status_code))
        if response.status_code in [200, 201, 204]:
            if response.text != "":
                return response.json()
            else:
                return {}
        elif response.status_code == 404:
            return {'Not Found'}
        else:
            raise ConnectorError("Response: {0}: {1}".format(response.status_code, response.content))
    except requests.exceptions.SSLError:
        raise ConnectorError('SSL certificate validation failed')
    except requests.exceptions.ConnectTimeout:
        raise ConnectorError('The request timed out while trying to connect to the server')
    except requests.exceptions.ReadTimeout:
        raise ConnectorError(
            'The server did not send any data in the allotted amount of time')
    except requests.exceptions.ConnectionError:
        raise ConnectorError('Invalid endpoint or credentials')
    except Exception as err:
        raise ConnectorError(str(err))


def get_report_details(config, params, connector_info):
    try:
        endpoint = "/v1/public/report/{0}".format(params.pop('report_id'))
        response = make_rest_call(endpoint, 'GET', connector_info, config, params=params)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))

def get_incidents(config: dict, params: dict) -> dict:
    try:
        endpoint = ""  # edit endpoint
        method = "GET"  # GET/POST/PUT/DELETE
        # write your code here, if needed.
        MK = MakeRestApiCall(config=config)
        response = MK.make_request(endpoint=endpoint, method=method, params=params)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))

def update_incident_resolution(config: dict, params: dict) -> dict:
    try:
        endpoint = ""  # edit endpoint
        method = "PUT"  # GET/POST/PUT/DELETE
        # write your code here, if needed.
        MK = MakeRestApiCall(config=config)
        response = MK.make_request(endpoint=endpoint, method=method, params=params)
        return response
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))

def _check_health(config, connector_info):
    try:
        return check(config, connector_info)
    except Exception as err:
        logger.exception("{0}".format(str(err)))
        raise ConnectorError("{0}".format(str(err)))

operations = {
    "get_report_details": get_report_details,
    "update_incident_resolution": update_incident_resolution,
    "get_incidents": get_incidents,
}
