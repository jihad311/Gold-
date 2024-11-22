import telebot
import random
import time
import requests
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "7602779485:AAG9AXAxhJqOjUaMJdLIfQe5TsKyv23QkDQ"
CHANNEL_ID = "@y_kd_z"  

bot = telebot.TeleBot(TOKEN)
def get_user_agent():
    models = [
        "SM-S908B",  
        "SM-G996B",  
        "SM-G998B",  
        "Pixel 6",   
        "Pixel 7 Pro",  
        "OnePlus 10 Pro",  
        "Xiaomi 12 Pro",  
        "Vivo X90 Pro",  
        "Oppo Find X6 Pro",  
        "Sony Xperia 1 V",  
        "Galaxy Z Fold4",  
        "Galaxy A73 5G",  
        "Huawei P50 Pro"  
    ]

    
    version = random.choice(["11", "12", "13", "14"])


    build_id = f"{random.choice(['SP1A', 'TP1A', 'UP1A'])}.{random.randint(100000, 999999)}.{random.randint(100, 999)}"

   
    dpi = random.choice([420, 480, 560, 640])  
    resolution = random.choice(["1080x2400", "1440x3200", "1280x2800"])  

    
    manufacturer = random.choice(["Samsung", "Google", "OnePlus", "Xiaomi", "Vivo", "Oppo", "Sony", "Huawei"])
    chipset = random.choice(["Exynos990", "Snapdragon888", "Tensor G2", "Dimensity9000", "Kirin9000"])
 
    model = random.choice(models)
    return (f"Dalvik/2.1.0 (Linux; U; Android {version}; {model} Build/{build_id}) "
            f"Instagram 317.0.0.45.111 Android (7.9.4; {dpi}dpi; {resolution}; {manufacturer}; {model}; {chipset}; en_US; 564194091)")



def generate_username():
    patterns = [
        lambda: ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(4)) + '_' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(2)),
        lambda: ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3)) + '_' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(2)),
        lambda: '_' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(1)) + '.' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(2)),
        lambda: random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + '_' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(1)) + '_' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(1)),
        lambda: ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(2)) + '_' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(1)) + '_' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(1)),
    ]
    return random.choice(patterns)()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("📢 الاشتراك في القناة", url=f"https://t.me/{CHANNEL_ID[1:]}"))
    bot.send_message(
        message.chat.id,
        f"مرحبًا {message.chat.first_name}!\n"
        "اشترك في القناة أولًا لتفعيل الأداة:\n\n"
        "بعد الاشتراك، أرسل /check لتفعيل الأداة.",
        reply_markup=keyboard
    )


@bot.message_handler(commands=['check'])
def check_subscription(message):
    user_id = message.chat.id
    try:
        member = bot.get_chat_member(CHANNEL_ID, user_id)
        if member.status in ['creator', 'administrator', 'member']:
            keyboard = InlineKeyboardMarkup()
            keyboard.add(
                InlineKeyboardButton("🎲 توليد يوزرات", callback_data="generate"),
                InlineKeyboardButton("🔍 بدء الفحص", callback_data="start_tool")
            )
            bot.send_message(
                message.chat.id,
                "✅ تم التحقق من اشتراكك! يمكنك الآن استخدام الأداة.\n"
                "اختر أحد الخيارات:",
                reply_markup=keyboard
            )
        else:
            bot.send_message(
                message.chat.id,
                f"❌ يجب الاشتراك في القناة: {CHANNEL_ID}\nثم أعد المحاولة بإرسال /check"
            )
    except:
        bot.send_message(
            message.chat.id,
            f"❌ تعذر التحقق. تأكد من اشتراكك في القناة: {CHANNEL_ID}\nثم أعد المحاولة"
        )


@bot.callback_query_handler(func=lambda call: call.data == "generate")
def generate_usernames(call):
    usernames = [generate_username() for _ in range(5)]
    bot.send_message(
        call.message.chat.id,
        "🎉 تم توليد اليوزرات:\n" + "\n".join(usernames)
    )

@bot.callback_query_handler(func=lambda call: call.data == "start_tool")
def start_tool(call):
    bot.send_message(call.message.chat.id, "🚀 بدأ الفحص...")
    while True:
        user = generate_username()
        bot.send_message(call.message.chat.id, f"تفحص المستخدم: {user}")
        
        cookies = {'csrftoken': 'qQNPm4sW1eTy1sPgTlPtqQ'}
        headers = {
	        'authority': 'www.instagram.com',
	        'accept': '*/*',
	        'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	        'content-type': 'application/x-www-form-urlencoded',
	        'origin': 'https://www.instagram.com',
	        'referer': 'https://www.instagram.com/accounts/password/reset/',
	        'sec-ch-prefers-color-scheme': 'dark',
	        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	        'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.1"',
	        'sec-ch-ua-mobile': '?1',
	        'sec-ch-ua-model': '"SM-A145P"',
	        'sec-ch-ua-platform': '"Android"',
	        'sec-ch-ua-platform-version': '"13.0.0"',
	        'sec-fetch-dest': 'empty',
	        'sec-fetch-mode': 'cors',
	        'sec-fetch-site': 'same-origin',
	        'user-agent': get_user_agent(),
	        'x-asbd-id': '129477',
	        'x-csrftoken': 'qQNPm4sW1eTy1sPgTlPtqQ',
	        'x-ig-app-id': '1217981644879628',
	        'x-ig-www-claim': '0',
	        'x-instagram-ajax': '1018397609',
	        'x-requested-with': 'XMLHttpRequest',
	        'x-web-device-id': '56218ADD-9EA6-41B2-8676-3AEF4DB71B59',
	    }
        data = {'email_or_username': user}
        
        res = requests.post(
            'https://www.instagram.com/api/v1/web/accounts/account_recovery_send_ajax/',
            cookies=cookies,
            headers=headers,
            data=data,
        )
        
        response_text = res.text
        if "لم يتم العثور على مستخدمين" in response_text:
            bot.send_message(call.message.chat.id, f"✅ يوزر متاح: {user}")
        elif "تم إرسال البريد الإكتروني" in response_text:
            bot.send_message(call.message.chat.id, f"❌ يوزر غير متاح: {user}")
        else:
            bot.send_message(call.message.chat.id, f"⚠️ استجابة غير متوقعة: {response_text}")
        
        time.sleep(2)

bot.polling()