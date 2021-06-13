import requests
import CloudFlare


def ip_address():
    url = 'https://api.ipify.org'
    try:
        r = requests.get(url)
        r.raise_for_status()
        ip_address = r.text
    except Exception:
        raise '%s: failed' % (url)

    if ip_address == '':
        raise '%s: failed' % (url)

    if ':' in ip_address:
        ip_address_type = 'AAAA'
    else:
        ip_address_type = 'A'

    return ip_address, ip_address_type


def update_dynamic_dns(token, zone_id, dns_name):
    cloudflare = CloudFlare.CloudFlare(token=token)
    ip, ip_address_type = ip_address()
    params = {
        'name': dns_name,
        'match': 'all',
        'type': ip_address_type,
    }
    dns_records = cloudflare.zones.dns_records.get(zone_id, params=params)

    for dns_record in dns_records:
        dns_record_id = dns_record['id']
        dns_record = {
            'name': dns_name,
            'type': ip_address_type,
            'content': ip,
            'proxied': dns_record['proxied'],
        }

        try:
            dns_record = cloudflare.zones.dns_records.put(
                zone_id,
                dns_record_id,
                data=dns_record,
            )
        except CloudFlare.exceptions.CloudFlareAPIError:
            raise
