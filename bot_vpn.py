from flask import Flask
from threading import Thread
import telebot
from telebot import types
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run():
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)

def keep_alive():
    t = Thread(target=run, daemon=True)
    t.start()

TOKEN = "8521576609:AAGu3UrMws0F4ZYJjCjHaXJzy4CPWK-PQlw"
bot = telebot.TeleBot(TOKEN)

# file_id
KONENADR_ID = "BQACAgUAAyEFAATnEEqeAAMCaamVbVy2blbOWYtO2Tq7-znj6-gAApMdAAKlpEhV-phXgFIhJEs6BA"

# SETTINGNPV images
SETTINGNPV_IMG1 = "AgACAgUAAyEFAATnEEqeAANZabGelKnL5CXBq3BcAAEJSbd6ZfQOAAJMDWsb1ViQVfC2NRL_9PeSAQADAgADeQADOgQ"
SETTINGNPV_IMG2 = "AgACAgUAAyEFAATnEEqeAANYabGelJewdvU4s0rEqdiDKBA34iQAAksNaxvVWJBV4JZk0CjVkMABAAMCAAN5AAM6BA"
SETTINGNPV_IMG3 = "AgACAgUAAyEFAATnEEqeAANaabGelIagKs4NXaQlwtinLD49QdgAAk0NaxvVWJBV5VTEhLFnP4cBAAMCAAN5AAM6BA"

# SETTINGSHADOW video
HDSHADOW_VIDEO_ID = "BAACAgUAAyEFAATnEEqeAANUabGXtdLfawXP-kxZR2jonGvNRxIAAqckAALVWJBVJSu1BEzOkkk6BA"

# PHATSHADOW video
PHATSHADOW_VIDEO_ID = "BAACAgUAAyEFAATnEEqeAAMXaambDprhrVsYAAHXaOfLL4Hwk5JBAAJYHAACbDpRVb00Mjtja22tOgQ"

# NPV Tunnel video
HDNPV_VIDEO_ID = "BAACAgUAAyEFAATnEEqeAANWabGaUJO67fP5kpFcWAwSaBgcWRoAAq8kAALVWJBV5Zez2GdIbZQ6BA"

# SGMODULE file
SGMODULE_FILE_ID = "BQACAgUAAyEFAATnEEqeAAM4aasSTJfLF4Bgx6yXnipLAu2XD1AAAlEeAAJsOllV8M_NAr1Cd7g6BA"

# HDKONENADR video
HDKONENADR_VIDEO_ID = "BAACAgUAAyEFAATnEEqeAANJaa2xm5mYCLypjcQxRGrzJvL-tjUAAtEgAAKdyXFVfnRFzgJ1u686BA"

HELP_TEXT = """DANH SÁCH LỆNH HỖ TRỢ:
/notes : Danh sách lệnh hỗ trợ
#NENTIKTOK : Hướng dẫn đăng ký nền tiktok
#KONENADR : File app không nền android mới nhất
#SETTINGNPV : Setting app NPV Tunnel
#KEYKONEN : Cách lấy key(adr) hoặc file(ios) gói không nền
#SGMODULE : file .sgmodule dùng để unlock premium một số app
#HDKONENADR : Video hướng dẫn sử dụng app không nền android mới nhất
#TIMEOUTSHADOW : Hướng dẫn fix timeout Shadowrocket
#TIMEOUTNPV : Hướng dẫn fix timeout NPV Tunnel
#HDNPV : Video hướng dẫn tải và sử dụng app NPV Tunnel(IOS)
#PHATSHADOW : Video hướng dẫn phát wifi bằng app Shadowrocket
#HDSHADOW : Video hướng dẫn sử dụng và settings shadowrocket
"""
TIMEOUTSHADOW_TEXT = """❤️‍🔥Fix Timeout👑
🔥Shadowrocket✈️
 ✈️ Chế độ máy bay ✈️
   🟢Bật/Tắt-3 lần🔴
 🇻🇳Kiểu kết nối Proxy❤️‍🔥
  🇻🇳Kiểm tra kết nối❤️‍🔥
 🇻🇳Kiểu kết nối Cấu hình❤️‍🔥
  🇻🇳Kiểm tra kết nối❤️‍🔥
 🇻🇳Kiểu kết nối Cấu hình❤️‍🔥
  🇻🇳Kiểm tra kết nối❤️‍🔥
 🇻🇳Kiểu kết nối Proxy❤️‍🔥
  🇻🇳Kiểm tra kết nối❤️‍🔥
  """

KEYKONEN_TEXT = """❤️‍🔥Cách lấy key(adr) hoặc file(ios) gói không nền👑
Gửi ảnh chụp ở trang chủ web + bill + gmail cho Admin, Admin sẽ đưa lại key(adr) hoặc file(ios) gói không nền cho bạn
"""

TIMEOUTNPV_TEXT = """❤️👑Npv Tunnel✈️
Nhận biết Timeout Npv Tunnel
Ping -1 ms,10000 ms
Fix Timeout Npv Tunnel
Bật,Tắt chế độ máy bay (3 lần) + vuốt tap vào kết nối rồi check ping 5 lần
"""

NEN_TIKTOK = """🌐 TỔNG HỢP GÓI VPN NỀN 4G/5G 2026 – VIETTEL | VINA | MOBI | LOCAL | SAYMEE
Dùng tốt cho: TikTok – Facebook – YouTube – Game – VPN mọi app – LiveStream
Tốc độ khỏe, ổn định, ít bóp băng thông.

🟩 1. VIETTEL – Nền TikTok siêu ổn định
T5K: 15GB/ngày – 5.000đ
→ Soạn T5K gửi 191 (gói mạnh – cực hợp dùng VPN)

T15KN: 25GB/tuần – 15.000đ
→ Soạn T15KN gửi 191 (tiết kiệm → 100GB/tháng)

T50K: 50GB/tháng – 50.000đ
→ Soạn T50K gửi 191 (ổn định lâu dài)

MXH100: Không giới hạn TikTok/Facebook/Instagram – 100K/tháng
→ Soạn MXH100 DK8 gửi 290

(sau 15GB, tốc độ ~5Mbps vẫn xem HD ok)

GIC90N: Không giới hạn dung lượng & tốc độ – 90K
→ Soạn GIC90N MO gửi 290 (áp dụng 6–12 tuổi)

🟦 2. VINAPHONE – Rẻ – Lì – Rất hợp chạy TikTok + VPN

TK1: 3K/ngày → Soạn TK1 gửi 888
TK7: 10K/tuần → Soạn TK7 gửi 888
TK30: 30K/tháng → Soạn TK30 ON3 gửi 888

🟧 3. MOBIFONE – Siêu khỏe – Ping thấp – Rất hợp cho VPN

TT1: 3K/ngày → Soạn DK TT1 gửi 9199
TT80: 80K/tháng → Soạn DK TT80 gửi 9199

🟪 4. SIM SAYMEE – Miễn phí TikTok tốc độ cao

ME70: 70K/tháng → Soạn DK ME70 gửi 9394
TIK10: 10K/tháng → Soạn DK TIK10 gửi 9394

🟥 5. SIM LOCAL

MAY89S: 77K/tháng
→ Soạn DK MAY89S gửi 8968
"""

@bot.message_handler(commands=["notes"])
def notes_command(message):
    bot.reply_to(message, HELP_TEXT)

@bot.message_handler(commands=["help"])
def help_command(message):
    bot.reply_to(message, HELP_TEXT)

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#TIMEOUTSHADOW")
def timeout_shadow(message):
    bot.reply_to(message, TIMEOUTSHADOW_TEXT)

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#NENTIKTOK")
def nen_tiktok(message):
    bot.reply_to(message, NEN_TIKTOK)

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#HDKONENADR")
def hd_konen_adr(message):
    bot.send_video(
        message.chat.id,
        HDKONENADR_VIDEO_ID,
        reply_to_message_id=message.message_id
    )

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#SGMODULE")
def sgmodule(message):
    bot.send_document(
        message.chat.id,
        SGMODULE_FILE_ID,
        reply_to_message_id=message.message_id
    )

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#TIMEOUTNPV")
def timeout_npv(message):
    bot.reply_to(message, TIMEOUTNPV_TEXT)

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#KONENADR")
def konen_adr(message):
    bot.send_document(
        message.chat.id,
        KONENADR_ID,
        reply_to_message_id=message.message_id
    )

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#KEYKONEN")
def konen(message):
    bot.reply_to(message, KEYKONEN_TEXT)

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#HDNPV")
def hd_npv(message):
    bot.send_video(
        message.chat.id,
        HDNPV_VIDEO_ID,
        reply_to_message_id=message.message_id
    )

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#SETTINGNPV")
def setting_npv(message):
    media = [
        types.InputMediaPhoto(SETTINGNPV_IMG1),
        types.InputMediaPhoto(SETTINGNPV_IMG2),
        types.InputMediaPhoto(SETTINGNPV_IMG3),
    ]
    bot.send_media_group(
        message.chat.id,
        media,
        reply_to_message_id=message.message_id
    )

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#PHATSHADOW")
def phat_shadow(message):
    bot.send_video(
        message.chat.id,
        PHATSHADOW_VIDEO_ID,
        reply_to_message_id=message.message_id
    )

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#HDSHADOW")
def hd_shadow(message):
    bot.send_video(
        message.chat.id,
        HDSHADOW_VIDEO_ID,
        reply_to_message_id=message.message_id
    )

if __name__ == "__main__":
    keep_alive()
    print("Bot đang khởi động...")
    bot.remove_webhook()
    bot.infinity_polling(skip_pending=True, timeout=30, long_polling_timeout=30)
