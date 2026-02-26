import requests

def update_node_list():
    source_url = "https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/list.txt"
    try:
        response = requests.get(source_url)
        if response.status_code == 200:
            # Extract first 20 IPs
            lines = response.text.split('\n')
            ips = [line.split(' ')[0] for line in lines if line.strip()]
            
            with open('list.txt', 'w') as f:
                f.write('\n'.join(ips[:20]))
            print("SUCCESS: list.txt created locally.")
        else:
            print("FAILED: Source unreachable.")
    except Exception as e:
        print(f"CRITICAL ERROR: {e}")

if __name__ == "__main__":
    update_node_list()
