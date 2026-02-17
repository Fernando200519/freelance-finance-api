import requests
import time

# --- CONFIGURACIÓN ---
TOKEN = "8378184565:AAHYaQ-mHv2vdwtQ126jGmbM_3C8o2tDF5g"
CHAT_ID = "8518780954"
URL_API = "http://localhost:80/health"

def send_telegram_msg(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Error enviando a Telegram: {e}")

def check_health():
    try:
        response = requests.get(URL_API, timeout=10)
        if response.status_code == 200:
            print(f"[{time.ctime()}] API Saludable")
        else:
            send_telegram_msg(f"Alerta: La API respondió con código {response.status_code}")
    except Exception:
        send_telegram_msg("URGENTE: La API no responde. El contenedor podría estar detenido.")

if __name__ == "__main__":
    check_health()
