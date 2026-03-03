from flask import Flask
from threading import Thread
import telebot

# --- ĐOẠN CODE GIỮ BOT LUÔN SỐNG ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    # Render sẽ tự cấp PORT, nếu không có sẽ dùng 8080
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ----------------------------------

# ĐÃ CẬP NHẬT TOKEN MỚI CỦA BẠN TẠI ĐÂY
TOKEN = '8521576609:AAE06Bt3K5CFc1HoBV6IWrmfpkTiS4AWJiA'
bot = telebot.TeleBot(TOKEN)

# File IDs
APPKONEN_ID = 'BQACAgUAAyEFAATmOJBdAAOiaaJv3HMkpzecpKtBcpwQ5JV0VcYAAvUdAAI0ZhhVlBhdOTkVpmc6BA'
MTUNNEL_VPN_ID = 'BQACAgUAAyEFAATmOJBdAANNaaHAzbgcjXQ1sNGMPhn7ZvUN5CsAAhMfAAI0ZhBVC3AAAQNAAqmtOgQ'
VIDEO_SETTING_SHADOW_ID = 'BAACAgUAAyEFAATmOJBdAAO6aaL2hidAmqh8ZfTKNeSIPcN7CvAAAnQfAAI0ZhhVyP44ChiubTY6BA'

@bot.message_handler(commands=['help', 'start'])
def send_help(message):
    help_text = (
        "<b>DANH SÁCH LỆNH HỖ TRỢ:</b>\n\n"
        "👉 <code>/help</code> : Danh sách lệnh hỗ trợ\n"
        "👉 <code>#DANGKYNEN</code> : Tổng hợp gói vpn nền 4G/5G\n"
        "👉 <code>#SETTINGSHADOW</code> : Video hướng dẫn cài Shadowrocket\n"
        "👉 <code>#TIMEOUTSHADOW</code> : Fix Timeout Shadowrocket\n"
        "👉 <code>#TIMEOUTNPV</code> : Fix Timeout Npv Tunnel\n"
        "👉 <code>#APPKHONGNEN</code> : Tải app vpn không nền mới nhất\n"
        "👉 <code>#MTUNNEL</code> : Tải app mtunnel"
    )
    bot.reply_to(message, help_text, parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text is not None)
def handle_messages(message):
    text = message.text.upper()
    if '#SETTINGSHADOW' in text:
        try: bot.send_video(message.chat.id, VIDEO_SETTING_SHADOW_ID, reply_to_message_id=message.message_id)
        except: pass
    elif '#DANGKYNEN' in text:
        nen_text = "🌐 <b>TỔNG HỢP GÓI VPN NỀN 2026</b>\n..." # (Giữ nguyên nội dung cũ của bạn)
        bot.reply_to(message, nen_text, parse_mode='HTML')
    # ... (Các lệnh khác giữ nguyên)

if __name__ == "__main__":
    keep_alive()
    print("Bot đang khởi động với Token mới...")
    # Lệnh quan trọng để xóa mọi kết nối cũ đang bị xung đột
    bot.remove_webhook()
    bot.infinity_polling(skip_pending=True)
