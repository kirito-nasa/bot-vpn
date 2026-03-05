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

TOKEN = "8521576609:AAE06Bt3K5CFc1HoBV6IWrmfpkTiS4AWJiA"
bot = telebot.TeleBot(TOKEN)

# file_id
APK_FILE_ID = "BQACAgUAAyEFAATmOJBdAAICYWmpVFQfUTtTLg_OpDg_1kggY9CnAAIaHAACfE5RVVDKDuwnZc53OgQ"
SPEEDVPN_FILE_ID = "BQACAgUAAyEFAATmOJBdAAICZmmpVZzUAmvyggyKEbqixuTOBjZaAAIdHAACfE5RVfdc26pB08GjOgQ"
MTUNNEL_FILE_ID = "BQACAgUAAyEFAATmOJBdAAICimmpZY-jrk2OO7BVKxIQZaOzD0BvAAKZHAACfE5RVXPWKzeWwhPxOgQ"

# SETTINGNPV images
SETTINGNPV_IMG1 = "AgACAgUAAyEFAATmOJBdAAICa2mpWykqtq9MmPmGToMKhUvPBvOBAAL2DWsbfE5RVXWrLv5fTyv6AQADAgADeQADOgQ"
SETTINGNPV_IMG2 = "AgACAgUAAyEFAATmOJBdAAICbGmpWykZbVQgMcIpVlCr5bs5CKuwAAL3DWsbfE5RVXzKrXAbEr7qAQADAgADeQADOgQ"
SETTINGNPV_IMG3 = "AgACAgUAAyEFAATmOJBdAAICbWmpWylUwJ27hzhUJP30lljhDfhKAAL4DWsbfE5RVWxGNkFh4YPAAQADAgADeQADOgQ"

# SETTINGSHADOW video
SETTINGSHADOW_VIDEO_ID = "BAACAgUAAyEFAATmOJBdAAICe2mpYXAks4vjtR7314vVPfIakiH6AAKFHAACfE5RVeu_X6VE4VJaOgQ"

HELP_TEXT = """DANH SÁCH LỆNH HỖ TRỢ:
/notes : Danh sách lệnh hỗ trợ
#NENTIKTOK : Hướng dẫn đăng ký nền tiktok
#APPKONEN : File app không nền android
#SPEEDVPN : File app SPEEDVPN (app cũ không nền)
#SETTINGNPV : Setting app NPV Tunnel
#MTUNNEL : File app Mtunnel
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

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#APPKONEN")
def app_konen(message):
    bot.send_document(
        message.chat.id,
        APK_FILE_ID,
        reply_to_message_id=message.message_id
    )

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#SPEEDVPN")
def speedvpn(message):
    bot.send_document(
        message.chat.id,
        SPEEDVPN_FILE_ID,
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

@bot.message_handler(func=lambda m: m.text and m.text.strip().upper() == "#MTUNNEL")
def mtunnel(message):
    bot.send_document(
        message.chat.id,
        MTUNNEL_FILE_ID,
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
