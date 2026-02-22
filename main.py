import requests

# The source for clean Cloudflare IPs
url = "https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/list.txt"

def get_european_ips():
    response = requests.get(url)
    all_ips = response.text.split('\n')
    
    # Filter for European countries: Germany (DE), Netherlands (NL), United Kingdom (GB), France (FR)
    target_countries = ['DE', 'NL', 'GB', 'FR']
    eu_only_list = [line.split(' ')[0] for line in all_ips if any(c in line for c in target_countries)]
    
    # Return the top 5 IPs for stability
    return eu_only_list[:5]