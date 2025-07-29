# Fogo Faucet Bot

Script Python untuk klaim otomatis faucet dari https://faucet.fogo.io menggunakan proxy.

## Cara Pakai

1. Edit `wallet_address` di `faucet_bot.py`
2. Tambahkan proxy di `proxies.txt`
3. Jalankan dengan:

```
pip install -r requirements.txt
python faucet_bot.py
```

Script akan otomatis mencoba claim setiap 10 menit.
