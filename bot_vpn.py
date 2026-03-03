from flask import Flask
from threading import Thread
import telebot

# --- ĐOẠN CODE GIỮ BOT LUÔN SỐNG ---
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
# ----------------------------------

TOKEN = '8521576609:AAFpHUGUqFda2xbUrdLNu08Bgi6VDExeKOk'
bot = telebot.TeleBot(TOKEN)

# Định nghĩa các File ID (Document & Video)
APPKONEN_ID = 'BQACAgUAAyEFAATmOJBdAAOiaaJv3HMkpzecpKtBcpwQ5JV0VcYAAvUdAAI0ZhhVlBhdOTkVpmc6BA'
MTUNNEL_VPN_ID = 'BQACAgUAAyEFAATmOJBdAANNaaHAzbgcjXQ1sNGMPhn7ZvUN5CsAAhMfAAI0ZhBVC3AAAQNAAqmtOgQ'
VIDEO_SETTING_SHADOW_ID = 'BAACAgUAAyEFAATmOJBdAAO6aaL2hidAmqh8ZfTKNeSIPcN7CvAAAnQfAAI0ZhhVyP44ChiubTY6BA'

# 1. LỆNH /HELP HOẶC /START
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

# 2. XỬ LÝ CÁC LỆNH NHẮN TIN
@bot.message_handler(func=lambda message: message.text is not None)
def handle_messages(message):
    text = message.text.upper()

    # LỆNH GỬI VIDEO SETTING SHADOWROCKET
    if '#SETTINGSHADOW' in text:
        try:
            bot.send_video(
                message.chat.id, 
                VIDEO_SETTING_SHADOW_ID, 
                reply_to_message_id=message.message_id
            )
        except: pass

    # LỆNH ĐĂNG KÝ NỀN
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

    # FIX TIMEOUT SHADOWROCKET
    elif '#TIMEOUTSHADOW' in text:
        shadow_text = (
            "❤️‍🔥 <b>Fix Timeout Shadowrocket</b> 👑\n"
            "✈️ <b>Chế độ máy bay:</b> Bật/Tắt - 3 lần 🔴🟢\n"
            "🇻🇳 Kiểm tra kết nối Proxy & Cấu hình ❤️‍🔥"
        )
        bot.reply_to(message, shadow_text, parse_mode='HTML')

    # FIX TIMEOUT NPV
    elif '#TIMEOUTNPV' in text:
        npv_text = (
            "👑 <b>Npv Tunnel - IOS</b> ✈️\n"
            "Bật/Tắt máy bay 3 lần + vuốt tắt app rồi check ping 5 lần."
        )
        bot.reply_to(message, npv_text, parse_mode='HTML')

    # GỬI FILE APK (KHÔNG CAPTION)
    elif '#APPKHONGNEN' in text:
        try:
            bot.send_document(message.chat.id, APPKONEN_ID, reply_to_message_id=message.message_id)
        except: pass

    elif '#MTUNNEL' in text:
        try:
            bot.send_document(message.chat.id, MTUNNEL_VPN_ID, reply_to_message_id=message.message_id)
        except: pass

if __name__ == "__main__":
    keep_alive() # Chạy web server song song với bot
    print("Bot đang chạy...")
    # Thêm dòng này để xóa các kết nối thừa trước đó
    bot.remove_webhook()
    # Thêm skip_pending=True để bot không trả lời dồn dập các tin nhắn cũ lúc bot đang offline
    bot.infinity_polling(skip_pending=True)
