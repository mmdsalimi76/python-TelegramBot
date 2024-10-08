import telebot
from telebot import types

# Get token from environment variable
bot = telebot.TeleBot('yourToken')

# List of villas with their names, image URLs, and descriptions
villas = {
    'آب گرم🔥': {
        '🔱سه خواب آبگرم فلورانس قلات🔱': {
            'images': [
                'https://freeimage.host/i/dI5zR6v',
                'https://freeimage.host/i/dI5zuna',
                'https://freeimage.host/i/dI5zIZg',
                'https://freeimage.host/i/dI5zAMJ',
                'https://freeimage.host/i/dI5zYap',
                'https://freeimage.host/i/dI5z7FR',
                'https://freeimage.host/i/dI5zl9I',
                'https://freeimage.host/i/dI5za8N',
                'https://freeimage.host/i/dI5zEtn',
                'https://freeimage.host/i/dI5zMns'

            ],
            'description': '''سه خواب و یک خواب مستر دار🏡
استخر ابگرم🔥
آسمان مجازی😍
تصفیه 24 ساعته استخر ♻
الاچیق ⛱
فول امکانات اقامتی ✅
300 متر ویلا دوبلکس 🏠
فضای سبز🏕
فوتبال دستی حرفه ای ⚽
باربیکیو 🍗🍢
نورپردازی تو شب 🌃
سیستم سرمایش🥶 و گرمایش🥵
کوچه شخصی با امنیت بالا💂🏻‍♂
 تراس بزرگ 🏞
2500 ویلا باغ 🏠
ادرس: ابتدا قلات

'''
        },
        '🔱دو خواب آبگرم صدرا جردن روباز🔱': {
            'images': [
                'https://freeimage.host/i/dIRy9ig',
                'https://freeimage.host/i/dIRyd0J',
                'https://freeimage.host/i/dIRyJfa',
                'https://freeimage.host/i/dIRpyWF',
                'https://freeimage.host/i/dIRyfON',
                'https://freeimage.host/i/dIRy2Uv',
                'https://freeimage.host/i/dIRyKRp',
                'https://freeimage.host/i/dIRyFJR',
                'https://freeimage.host/i/dIRyqbI'
            ],
            'description': '''دو خواب فوق لوکس با نما تمام شیشه🏠
تمامی وسایل ها نو هستن ✅
استخر ابگرم رو باز🔥
نور پردازی در شب🌃
فول امکانات اقامت👑
سه تا سرویس بهداشتی ✅
سیستم گرمایش و سرمایش ✅
تراس بزرگ 🌅
باربیکیو🍗🍢
آلاچیق ⛩
فضای باغی بزرگ 🏕
آدرس : اهل بیت صدرا



تعداد زیر 8 نفر ⛔
نفرات بیشتر هر نفر 300 تومان'''
        },
        '🔱سه خواب آبگرم قلات بهشت🔱': {
            'images': [
                'https://freeimage.host/i/dIAkzZX',
                'https://freeimage.host/i/dIAkTnn',
                'https://freeimage.host/i/dIAkxjt',
                'https://freeimage.host/i/dIAkouI',
                'https://freeimage.host/i/dIAkY8l',
                'https://freeimage.host/i/dIAk0w7',
                'https://freeimage.host/i/dIAkMMu',
                'https://freeimage.host/i/dIAkXFj',
                'https://freeimage.host/i/dIAkhcx'
            ],
            'description': '''سه خواب 🏠
استخر ابگرم سر پوشیده 🔥
فوتبال دستی حرفه ای 🎱
نور پردازی در شب🌃
فول امکانات اقامت👑
سیستم گرمایش و سرمایش ✅
تراس بزرگ 🌅
باربیکیو🍗🍢
آلاچیق ⛩
فضای باغی بزرگ 🏕
آدرس : ابتدای جاده قلات



تعداد زیر 10 نفر ⛔
نفرات بیشتر هر نفر 300 تومان'''
        },
        '🔱سه خواب آبگرم صدرا پارسیان🔱': {
            'images': [
                'https://freeimage.host/i/dIRlb19',
                'https://freeimage.host/i/dIRlmge',
                'https://freeimage.host/i/dIRlQX2',
                'https://freeimage.host/i/dIRlZsS',
                'https://freeimage.host/i/dIRlydu',
                'https://freeimage.host/i/dIR02zQ',
                'https://freeimage.host/i/dIR0Hej'
            ],
            'description': '''سه خواب مستر دار🏠
استخر ابگرم سرپوشیده 🔥
جکوزی 🔥
تصفیه آب استخر و ساختمان ✅
نور پردازی در شب🌃
فول امکانات اقامت👑
سیستم سرمایش 🥶 گرمایش 🥵
فضای باغی بزرگ و سر سبز🏕
مناسب برای خانواده ✅
آدرس : جاده صدرا



تعداد زیر 10 نفر ⛔
نفرات بیشتر هر نفر 350 تومان'''
        }
    },
    'آب سرد': {
        '🔱دوخواب آبسرد آپادانا صدرا🔱': {
            'images': [
                'https://freeimage.host/i/dI51Ysp',
                'https://freeimage.host/i/dI51cqN',
                'https://freeimage.host/i/dI517XR',
                'https://freeimage.host/i/dI51l1I',
                'https://freeimage.host/i/dI510gt',
                'https://freeimage.host/i/dI51EdX',
                'https://freeimage.host/i/dI51Mes',
                'https://freeimage.host/i/dI51G7n',
                'https://freeimage.host/i/dI51VmG',
                'https://freeimage.host/i/dI51XIf'
            ],
            'description': '''دو خواب🏠
استخر روباز 🌊
نور پردازی در شب🌃
دوتا سرویس بهداشتی ✅
فول امکانات اقامت👑
سیستم گرمایش 🥵 و سرمایش 🥶
تاب و تخت بیرون🏀⚽
باربیکیو🍗🍢
فضای باغی بزرگ و سر سبز🏕
آدرس : ابتدا جاده صدرا


'''
        },
        '🔱سه خواب آب سرد سرو قلات🔱': {
            'images': [
                'https://freeimage.host/i/dI5Vcjs',
                'https://freeimage.host/i/dI5Vaun',
                'https://freeimage.host/i/dI5VlZG',
                'https://freeimage.host/i/dI5V7yX',
                'https://freeimage.host/i/dI5V1nf',
                'https://freeimage.host/i/dI5VEG4',
                'https://freeimage.host/i/dI5VG6l',
                'https://freeimage.host/i/dI5VVF2',
                'https://freeimage.host/i/dI5VWaS',
                'https://freeimage.host/i/dI5VX87'
            ],
            'description': '''مشخصات 👇🏻👇🏻
سه خواب🏠
دو تا سرویس بهداشتی ✅
استخر روباز آبسرد 🌊
نور پردازی در شب 🌃
فول امکانات اقامت 👑
باربیکیو 🍗🍢
فضای باغی بزرگ و سر سبز 🏕
آدرس : ابتدای جاده قلات



تعداد زیر 10 نفر ⛔
نفرات بیشتر هر نفر 250 تومان
محدودیت نفرات تا 25 نفر'''
        }
    }
}


# Command handlers
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, '''به شیراز ویلا خوش آمدید😍
لطفا برای دیدن ویلا ها از قسمت منو گزینه ویلا را انتخاب کنید🏡
در صورت نیاز به راهنمایی از قسمت منو گزینه پشتیبانی را انتخاب کنید👨🏻‍💻
    ''')



@bot.message_handler(commands=['help'])
def send_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('درباره ما')
    item2 = types.KeyboardButton('تماس با ما')
    item3 = types.KeyboardButton('⬅️')
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'چطور میتونم کمکتون کنم؟', reply_markup=markup)


@bot.message_handler(commands=['villa'])
def send_villa_types(message):
    markup = types.InlineKeyboardMarkup()
    for villa_type in villas.keys():
        markup.add(types.InlineKeyboardButton(villa_type, callback_data=villa_type))
    bot.send_message(message.chat.id, 'لطفا نوع ویلا را انتخاب کنید:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: call.data in villas.keys())
def send_villa_list(call):
    villa_type = call.data
    markup = types.InlineKeyboardMarkup()
    for villa_name in villas[villa_type].keys():
        markup.add(types.InlineKeyboardButton(villa_name, callback_data=villa_name))
    bot.send_message(call.message.chat.id, f'لیست ویلاهای {villa_type}:', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: any(call.data in villas[villa_type] for villa_type in villas))
def send_villa_details(call):
    for villa_type in villas:
        if call.data in villas[villa_type]:
            villa_name = call.data
            villa_details = villas[villa_type][villa_name]
            media_group = [types.InputMediaPhoto(image_url) for image_url in villa_details['images']]
            bot.send_media_group(call.message.chat.id, media_group)
            bot.send_message(call.message.chat.id, f'{villa_name}:\n\n{villa_details["description"]}')
            break


@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    if message.text == 'درباره ما':
        bot.send_message(message.chat.id, '✅شیراز ویلا با 5 سال سابقه فعالیت،آماده خدمت رسانی به مشتریان عزیز در خصوص رزرو باغ ویلا می باشد ')
    elif message.text == 'تماس با ما':
        phone = 'phone: 09164125718'
        email = 'Telegram ID:@mhmdsaliimii'
        contact = f'{phone}\n{email}'
        bot.send_message(message.chat.id, contact)
    elif message.text == "⬅️":
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, 'شما به صفحه اصلی باز گشتید', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'متوجه منظورتون نشدم :/')


if __name__ == '__main__':
    try:
        bot.polling(interval=1)
    except Exception as e:
        print(f'Error: {e}')
