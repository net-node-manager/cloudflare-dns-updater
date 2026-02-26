import requests

def update_ips():
    # Source of filtered IPs for Iran
    url = "https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/list.txt"
    try:
        r = requests.get(url)
        # Get first 30 healthy IPs
        ips = [line.split(' ')[0] for line in r.text.split('\n') if line.strip()]
        with open('list.txt', 'w') as f:
            f.write('\n'.join(ips[:30]))
        print("Success: list.txt updated with clean IPs.")
    except:
        print("Error: Could not fetch IPs.")

if __name__ == "__main__":
    update_ips()
