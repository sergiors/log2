#!/usr/bin/env python
from dns import update_dynamic_dns
from config_vars import dns_name, zone_id, token


try:
    update_dynamic_dns(dns_name, zone_id, token)
except Exception:
    pass
