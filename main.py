import requests

def get_ips():
    url = "https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/list.txt"
    try:
        r = requests.get(url)
        # Filtering top 20 stable IPs
        ips = [l.split(' ')[0] for l in r.text.split('\n') if l]
        return ips[:20]
    except:
        return []

if __name__ == "__main__":
    clean_ips = get_ips()
    if clean_ips:
        with open('list.txt', 'w') as f:
            f.write('\n'.join(clean_ips))
        print("Done: list.txt created.")
