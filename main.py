import requests
import re
def get_ips():
    url = "https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/list.txt"
    try:
        r = requests.get(url, timeout=15)
        ips = re.findall(r'\d+\.\d+\.\d+\.\d+', r.text)
        with open('list.txt', 'w') as f:
            f.write('\n'.join(ips[:20]))
    except: pass
if __name__ == "__main__":
    get_ips()
