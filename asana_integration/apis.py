import logging

import asana
from asana.rest import ApiException

logger = logging.getLogger(__name__)


def get_asana_api_client(access_token):
    configuration = asana.Configuration()
    configuration.access_token = access_token
    return asana.ApiClient(configuration)


def get_all_workspaces(access_token, limit=100, opt_fields='email_domains,is_organization,name,offset,path,uri') -> list or None:
    """
    Get all workspaces for the user
    :param access_token: Asana API access token
    :param limit: Limit the number of workspaces returned
    :param opt_fields: Some fields to include in the response
    :return: List of workspaces
    """
    api_client = get_asana_api_client(access_token)
    workspaces_api_instance = asana.WorkspacesApi(api_client)
    opts = {
        'limit': limit,
        'opt_fields': opt_fields
    }
    try:
        api_response = workspaces_api_instance.get_workspaces(opts)
        return api_response
    except ApiException as e:
        logger.error(f"Exception when calling WorkspacesApi->get_workspaces: {e}")
        return None
