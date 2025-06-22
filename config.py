import os

# Telegram Bot tokeni renderdagi environment variable'dan olinadi
API_TOKEN = os.getenv("7752977498:AAFznqjVgNQjEpWJ1IUZi5NVpC8YJG8n4nE")

# Admin ID (agar mavjud bo'lmasa, default 7766045121)
ADMIN_ID = int(os.getenv("ADMIN_ID", "7766045121"))

# Render external URL (render avtomatik beradi)
RENDER_EXTERNAL_URL = os.getenv("RENDER_EXTERNAL_URL")

# Webhook sozlamalari
WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = f"{RENDER_EXTERNAL_URL}{WEBHOOK_PATH}"

# Webapp (FastAPI yoki Flask) uchun host va port
WEBAPP_HOST = "0.0.0.0"
WEBAPP_PORT = int(os.getenv("PORT", 10000))
