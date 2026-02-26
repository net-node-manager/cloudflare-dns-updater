import requests

# SOURCE: Cloudflare Clean IPs
IP_SOURCE_URL = "https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/list.txt"

def get_clean_ips():
    try:
        response = requests.get(IP_SOURCE_URL)
        if response.status_code != 200:
            print(f"FAILED: Status Code {response.status_code}")
            return []
            
        all_lines = response.text.split('\n')
        
        # Filter for US and EU Regions (GB, DE, NL, FR, US)
        target_regions = ['GB', 'DE', 'NL', 'FR', 'US']
        clean_ips = [
            line.split(' ')[0] 
            for line in all_lines 
            if any(region in line for region in target_regions)
        ]
        
        return clean_ips[:25] # Return top 25 stable IPs
    except Exception as e:
        print(f"CRITICAL_ERROR: {e}")
        return []

def save_to_disk(ip_list):
    try:
        # Create list.txt for Cloudflare Worker access
        with open('list.txt', 'w') as f:
            for ip in ip_list:
                f.write(f"{ip}\n")
        return True
    except Exception as e:
        print(f"FILE_SAVE_ERROR: {e}")
        return False

if __name__ == "__main__":
    print(">> INITIALIZING NET-NODE-MANAGER UPDATE...")
    ips = get_clean_ips()
    
    if ips:
        if save_to_disk(ips):
            print(f"SUCCESS: list.txt updated with {len(ips)} nodes.")
        else:
            print("FAILED: Could not write to disk.")
    else:
        print("WARNING: No matching IPs discovered.")
