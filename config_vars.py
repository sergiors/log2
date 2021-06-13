import os
import yaml

from glom import glom


if not os.path.exists('config.yaml'):
    raise Exception("The file 'config.yaml' does not exist.")


with open(r'config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

token = glom(config, 'cloudflare.token')
zone_id = glom(config, 'cloudflare.zone_id')
dns_name = glom(config, 'cloudflare.dns_name')
