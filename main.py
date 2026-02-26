import requests
import re

def get_clean_ips():
    url = "https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/list.txt"
    try:
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            ips = re.findall(r'\d+\.\d+\.\d+\.\d+', response.text)
            with open('list.txt', 'w') as f:
                f.write('\n'.join(ips[:20]))
            print("Successfully updated list.txt with new IPs")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_clean_ips()
