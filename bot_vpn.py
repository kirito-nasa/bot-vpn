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

TOKEN = "8521576609:AAGX3e63KZgjzx3On3hPrqwAi1hnyTwGxsk"
bot = telebot.TeleBot(TOKEN)

# file_id
KONENADR_ID = "BQACAgUAAyEFAATnEEqeAAMCaamVbVy2blbOWYtO2Tq7-znj6-gAApMdAAKlpEhV-phXgFIhJEs6BA"

# SETTINGNPV images
SETTINGNPV_IMG1 = "AgACAgUAAyEFAATnEEqeAAMFaamWTq04OFr8E1lTCCrbvKTO_ZsAArMPaxulpEhVoZ0k-SnG1qgBAAMCAAN5AAM6BA"
SETTINGNPV_IMG2 = "AgACAgUAAyEFAATmOJBdAAICbGmpWykZbVQgMcIpVlCr5bs5CKuwAAL3DWsbfE5RVXzKrXAbEr7qAQADAgADeQADOgQ"
SETTINGNPV_IMG3 = "AgACAgUAAyEFAATnEEqeAAMHaamWTmmHuXx918203c6rVNVlKgUAArQPaxulpEhVQO1UrZlGUuYBAAMCAAN5AAM6BA"

# SETTINGSHADOW video
SETTINGSHADOW_VIDEO_ID = "BAACAgUAAyEFAATnEEqeAAMDaamWD5bA4tr6LP7f5MzCd08CMzMAApUdAAKlpEhVbve8R6DStuM6BA"

# PHATSHADOW video
PHATSHADOW_VIDEO_ID = "BAACAgUAAyEFAATnEEqeAAMXaambDprhrVsYAAHXaOfLL4Hwk5JBAAJYHAACbDpRVb00Mjtja22tOgQ"

HELP_TEXT = """DANH SÁCH LỆNH HỖ TRỢ:
/notes : Danh sách lệnh hỗ trợ
#NENTIKTOK : Hướng dẫn đăng ký nền tiktok
#KONENADR : File app không nền android mới nhất
#SETTINGNPV : Setting app NPV Tunnel
#PHATSHADOW : Video hướng dẫn phát wifi bằng app Shadowrocket
#SETTINGSHADOW : Video hướng dẫn sử dụng nền tiktok và settings shadowrocket
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

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#NENTIKTOK")
def nen_tiktok(message):
    bot.reply_to(message, NEN_TIKTOK)

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#KONENADR")
def konen_adr(message):
    bot.send_document(
        message.chat.id,
        KONENADR_ID,
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

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#SETTINGSHADOW")
def setting_shadow(message):
    bot.send_video(
        message.chat.id,
        SETTINGSHADOW_VIDEO_ID,
        reply_to_message_id=message.message_id
    )

if __name__ == "__main__":
    keep_alive()
    print("Bot đang khởi động...")
    bot.remove_webhook()
    bot.infinity_polling(skip_pending=True, timeout=30, long_polling_timeout=30)
