import requests

def update_node_list():
    source = "https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/list.txt"
    try:
        response = requests.get(source)
        # Filtering top 20 IPs
        ips = [line.split(' ')[0] for line in response.text.split('\n') if line.strip()]
        
        with open('list.txt', 'w') as f:
            f.write('\n'.join(ips[:20]))
        print("SUCCESS: list.txt created.")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    update_node_list()
