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
        try:
            bot.send_video(message.chat.id, VIDEO_SETTING_SHADOW_ID, reply_to_message_id=message.message_id)
        except: pass

    elif '#DANGKYNEN' in text:
        nen_text = (
            "🌐 <b>TỔNG HỢP GÓI VPN NỀN 2026</b>\n"
            "4G/5G – VIETTEL | VINA | MOBI | LOCAL | SAYMEE\n\n"
            "🟩 <b>1. VIETTEL – Nền TikTok</b>\n"
            "• <code>T5K</code> gửi <b>191</b>\n"
            "• <code>T15KN</code> gửi <b>191</b>\n"
            "• <code>T50K</code> gửi <b>191</b>\n"
            "• <code>MXH100 DK8</code> gửi <b>290</b>\n\n"
            "🟦 <b>2. VINAPHONE</b>\n"
            "• <code>TK1</code> gửi <b>888</b>\n"
            "• <code>TK30 ON3</code> gửi <b>888</b>\n\n"
            "🟧 <b>3. MOBIFONE</b>\n"
            "• <code>DK TT1</code> gửi <b>9199</b>\n"
            "• <code>DK TT80</code> gửi <b>9199</b>\n\n"
            "🟪 <b>4. SIM SAYMEE</b>\n"
            "• <code>DK ME70</code> gửi <b>9394</b> sau đó <code>DK TIK10</code> gửi <b>9394</b>"
        )
        bot.reply_to(message, nen_text, parse_mode='HTML')

    elif '#TIMEOUTSHADOW' in text:
        shadow_text = "❤️‍🔥 <b>Fix Timeout Shadowrocket</b>\n✈️ Bật/Tắt máy bay 3 lần."
        bot.reply_to(message, shadow_text, parse_mode='HTML')

    elif '#TIMEOUTNPV' in text:
        npv_text = "👑 <b>Npv Tunnel - IOS</b>\nBật/Tắt máy bay 3 lần + vuốt tắt app."
        bot.reply_to(message, npv_text, parse_mode='HTML')

    elif '#APPKHONGNEN' in text:
        try:
            bot.send_document(message.chat.id, APPKONEN_ID, reply_to_message_id=message.message_id)
        except: pass

    elif '#MTUNNEL' in text:
        try:
            bot.send_document(message.chat.id, MTUNNEL_VPN_ID, reply_to_message_id=message.message_id)
        except: pass

if __name__ == "__main__":
    keep_alive()
    print("Bot đang khởi động với Token mới...")
    # Lệnh quan trọng để xóa mọi kết nối cũ đang bị xung đột
    bot.remove_webhook()
    bot.infinity_polling(skip_pending=True)
