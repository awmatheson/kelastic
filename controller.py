from pprint import pprint
import itertools
import json
from kubernetes import client, config
from kubernetes import watch as kwatch
from kubernetes.config.config_exception import ConfigException
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

RESOURCE_PLURALS = ['workflows']
GROUP = "argoproj.io"
VERSION = "v1alpha1"

try:
    config.load_incluster_config()
except ConfigException:
    logger.debug("loading local kube config")
    config.load_kube_config()

api_client = client.ApiClient()
custom_api = client.CustomObjectsApi(api_client)

def update_bulk_resources(plural):
    api_response = custom_api.list_cluster_custom_object('argoproj.io', 'v1alpha1', plural)
    pprint(api_response)

def update_stream(plural):
    w = kwatch.Watch()
    for item in w.stream(custom_api.list_cluster_custom_object, 'argoproj.io', 'v1alpha1',
                         'default', 'workflows'):
        if item['object']['kind'] == 'Status':
            continue

def main():
    # TODO Make multi-threaded for multiple resources
    update_bulk_resources('workflows')

if __name__ == '__main__':
    main()