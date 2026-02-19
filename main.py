import requests

API_TOKEN = "06kGgur7YygIkdY8IXdMnsrdGAQNTqNleqPmcLQ1"
ZONE_ID = "b0749ce6ac82ddf6faae2b907a20e96a"
DOMAIN_NAME = "hesaart.shop"
SOURCE_URL = "https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/list.txt"

def update_dns():
try:
response = requests.get(SOURCE_URL, timeout=10)
new_ip = response.text.split('\n')[0].split()[0].strip()
headers = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}
url = f"{ZONE_ID}/dns_records?name={DOMAIN_NAME}"
res = requests.get(url, headers=headers).json()
record_id = res['result'][0]['id']
update_url = f"{ZONE_ID}/dns_records/{record_id}"
data = {"type": "A", "name": DOMAIN_NAME, "content": new_ip, "ttl": 1, "proxied": True}
requests.put(update_url, headers=headers, json=data)
print(f"Updated to {new_ip}")
except Exception as e:
print(f"Error: {e}")

if name == "main":
update_dns()
