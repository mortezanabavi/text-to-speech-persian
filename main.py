import requests

def TextToSpeech():
    TOKEN = '' # Get your Bearer token from web.igap.net

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://web.igap.net',
        'Referer': 'https://web.igap.net/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'authorization': F'Bearer {TOKEN}',
        'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'input_text': 'امتحان شدم غلط نداشتم نکردم اشتباه\nفانوس درون روشن بلند شیون اژدها\nغلط معقول مغلطه دو رو اعیون اجتماع\nهمیشه شلوغ میکنم شرورم به اصطلاح\n\nبازی واسه تو شروع ولی واسه من تمومه\nجنس خواسته های من از جنس عادی نبوده\nقله رو میرم بالا ندارم ترس از ارتفاع\nمیپرم تا شاید بشم قهرمان قصه ها\n\nماه و سال و هفته ها گرفتن وقت ما رو\nهرچی داد زدیم هیچ کسی نشنید حرف ما رو\nهرچی نوشتیم فقط گرفتن نقص کارو\nمیگفتن داریم کج میکنیم ریل بچه ها رو\n\nریش سفید قلب شیر مغز رد\nسیم به سیم کینه ای طلبت\nاین به این اون به این\nنیش زیر لبمون تیز تیز دندونا\nمثِ گرگ میخوریم ما بره ها رو\n\nجر دادم رفتم همه جاصدا من میاد همه جا\nارزون دست نمیدم ، میگیرم و پس نمیدم\nجاده رو دستی یهو ، نه نمیخوام تصدیقشو\n\nنگران نیستم اگه وزیر بازی رو زدم\nچون حرکاتام آزاد و مسیر بازی رو بلد\nبهتره بکنی ازین احساسِ خطر\nروبه روم وای نستا چون من فریبت دادم اَ قبل\nمهره هامو با جادو حرکت میدم\nملوانام توو دریا با پارو الافم میشن\nبا موندن توو حقیقت آرومم اما سریعم\nچون به چشم خیلی دیدم زانو زدن با تغییرم\n\nباروت ازم خریدن و با موندم غریبه ان\nپیچیدن و خوابیدم باز تا اومدم پریدم\nمن ندیدم جاده ای داغون تر از مسیرم\nهمه پی عن قضیه ان و بده وضعیت\n\nمیدونی آوردن ماموتا رو جای فیل\nمیتونی بیاری تابوتا رو پای میز\nاگه تانک بیاری با بازوکا توو راهتیم\nاین بازی مریض و ما هم داروساز واژه ایم\n\nجر دادم رفتم همه جا صدا من میاد همه جا\nارزون دست نمیدم میگیرم و پس نم',
    }

    response = requests.post('https://ai.igap.net/api/v1/voice/tts/', headers=headers, json=json_data)
    if response.status_code == 200:
        # Specify the file path where you want to save the TTS audio file
        filename = 'output.wav'

        # Save the response content to a file
        with open(filename, 'wb') as f:
            f.write(response.content)

        print(f'TTS audio saved to {filename}')
    else:
        print('Error occurred while making the request')
        
        
if __name__ == "__main__":
    TextToSpeech()