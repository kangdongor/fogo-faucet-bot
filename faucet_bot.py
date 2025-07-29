import requests
import time
import random

# Alamat wallet Fogo kamu
wallet_address = "4hgVomMpKCSj337gNCRwhcJ9uCNZdC..."

# URL faucet
faucet_url = "https://faucet.fogo.io/api/faucet"

# Header standar
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

# Data request
payload = {
    "address": wallet_address
}

# Load proxy dari file proxies.txt
def load_proxy_list():
    try:
        with open("proxies.txt", "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []

proxy_list = load_proxy_list()

def get_random_proxy():
    if not proxy_list:
        return None
    proxy = random.choice(proxy_list)
    return {
        "http": proxy,
        "https": proxy
    }

def claim_faucet():
    proxies = get_random_proxy()
    print("🔄 Using proxy:", proxies["http"] if proxies else "No proxy")

    try:
        response = requests.post(faucet_url, json=payload, headers=headers, proxies=proxies, timeout=30)
        if response.status_code == 200:
            print("✅ Faucet claimed successfully!")
            print("Response:", response.json())
        elif response.status_code == 429:
            print("⚠️ Too many requests. Waiting before retrying...")
        else:
            print(f"❌ Error {response.status_code}: {response.text}")
    except requests.exceptions.ProxyError:
        print("❌ Proxy Error: Please check your proxy.")
    except requests.exceptions.ConnectTimeout:
        print("⏰ Timeout. Proxy or server may be slow.")
    except Exception as e:
        print("❌ Error:", e)

while True:
    claim_faucet()
    time.sleep(600)
