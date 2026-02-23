import requests

# منبع آی‌پی‌های تمیز کلودفلر
url = "https://raw.githubusercontent.com/vfarid/cf-clean-ips/main/list.txt"

def get_european_ips():
    response = requests.get(url)
    all_ips = response.text.split('\n')
    
    # اضافه کردن لوکیشن آمریکا (US) برای کارهای کلود در کنار اروپا
    target_countries = ['GB', 'DE', 'NL', 'FR', 'US']
    
    # فیلتر کردن آی‌پی‌ها بر اساس کشورهای هدف
    clean_list = [line.split(' ')[0] for line in all_ips if any(c in line for c in target_countries)]
    
    # نمایش ۲۰ آی‌پی برای پایداری بیشتر در ایران و افزایش شانس اتصال
    return clean_list[:20]
