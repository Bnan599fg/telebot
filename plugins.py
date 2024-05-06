
from requests import get,post
from os import name
from threading import Thread
from pytz import timezone
from datetime import date,datetime
import json 
from os import name
import os
from random import choice
from bs4 import BeautifulSoup
from re import findall
from PIL import Image, ImageDraw, ImageFont
from urllib.request import Request, urlopen
from urllib.parse import quote
from time import time
from rextester_Api import Rextester
import jdatetime
import pyPrivnote as pn

org = [":","0","1","2","3","4","5","6","7","8","9"]
fonts = [[":","𝟶","𝟷","𝟸","𝟹","𝟺","𝟻","𝟼","𝟽","𝟾","𝟿"],
[":","⓪","①","②","③","④","⑤","⑥","⑦","⑧","⑨"],
[":","𝟬","𝟭","𝟮","𝟯","𝟰","𝟱","𝟲","𝟳","𝟴","𝟵"],
[":","０","１","２","３","４","５","６","７","８","９"],
[":","₀","₁","₂","₃","₄","₅","₆","₇","₈","₉"],
[":","𝟎","𝟏","𝟐","𝟑","𝟒","𝟓","𝟔","𝟕","𝟖","𝟗"]]
fonts2 = [[':','⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹']]
org_eng = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
name_font = [["𝕬","𝕭","𝕮","𝕯","𝕰","𝕱","𝕲","𝕳","𝕴","𝕵","𝕶","𝕷","𝕸","𝕹","𝕺","𝕻","𝕼","𝕽","𝕾","𝕿","𝖀","𝖁","𝖂","𝖃","𝖄","𝖅"],
["𝓐","𝓑","𝓒","𝓓","𝓔","𝓕","𝓖","𝓗","𝓘","𝓙","𝓚","𝓛","𝓜","𝓝","𝓞","𝓟","𝓠","𝓡","𝓢","𝓣","𝓤","𝓥","𝓦","𝓧","𝓨","𝓩"],
["ꪖ","᥇","ᥴ","ᦔ","ꫀ","ᠻ","ᧁ","ꫝ","ⅈ","𝕛","𝕜","ꪶ","ꪑ","ꪀ","ꪮ","ρ","𝕢","𝕣","ડ","𝕥","ꪊ","ꪜ","᭙","᥊","ꪗ","𝕫"],
["𝔸","𝔹","ℂ","𝔻","𝔼","𝔽","𝔾","ℍ","𝕀","𝕁","𝕂","𝕃","𝕄","ℕ","𝕆","ℙ","ℚ","ℝ","𝕊","𝕋","𝕌","𝕍","𝕎","𝕏","𝕐","ℤ"],
["Ａ","Ｂ","Ｃ","Ｄ","Ｅ","Ｆ","Ｇ","Ｈ","Ｉ","Ｊ","Ｋ","Ｌ","Ｍ","Ｎ","Ｏ","Ｐ","Ｑ","Ｒ","Ｓ","Ｔ","Ｕ","Ｖ","Ｗ","Ｘ","Ｙ","Ｚ"],
["🄰","🄱","🄲","🄳","🄴","🄵","🄶","🄷","🄸","🄹","🄺","🄻","🄼","🄽","🄾","🄿","🅀","🅁","🅂","🅃","🅄","🅅","🅆","🅇","🅈","🅉"],
["Ⓐ","Ⓑ","Ⓒ","Ⓓ","Ⓔ","Ⓕ","Ⓖ","Ⓗ","Ⓘ","Ⓙ","Ⓚ","Ⓛ","Ⓜ","Ⓝ","Ⓞ","Ⓟ","Ⓠ","Ⓡ","Ⓢ","Ⓣ","Ⓤ","Ⓥ","Ⓦ","Ⓧ","Ⓨ","Ⓩ"],
["ᴬ","ᴮ","ᶜ","ᴰ","ᴱ","ᶠ","ᴳ","ᴴ","ᴵ","ᴶ","ᴷ","ᴸ","ᴹ","ᴺ","ᴼ","ᴾ","Q","ᴿ","ˢ","ᵀ","ᵁ","ⱽ","ᵂ","ˣ","ʸ","ᶻ"],
['ᴀ','ʙ','ᴄ','ᴅ','ᴇ','ꜰ','ɢ','ʜ','ɪ','ᴊ','ᴋ','ʟ','ᴍ','ɴ','ᴏ','ᴘ','Q','ʀ','ꜱ','ᴛ','ᴜ','ᴠ','ᴡ','x','ʏ','ᴢ'],
["ₐ","B","C","D","ₑ","F","G","ₕ","ᵢ","ⱼ","ₖ","ₗ","ₘ","ₙ","ₒ","ₚ","Q","ᵣ","ₛ","ₜ","ᵤ","ᵥ","W","ₓ","Y","Z"],
["𝐀","𝐁","𝐂","𝐃","𝐄","𝐅","𝐆","𝐇","𝐈","𝐉","𝐊","𝐋","𝐌","𝐍","𝐎","𝐏","𝐐","𝐑","𝐒","𝐓","𝐔","𝐕","𝐖","𝐗","𝐘","𝐙"],
["𝗔","𝗕","𝗖","𝗗","𝗘","𝗙","𝗚","𝗛","𝗜","𝗝","𝗞","𝗟","𝗠","𝗡","𝗢","𝗣","𝗤","𝗥","𝗦","𝗧","𝗨","𝗩","𝗪","𝗫","𝗬","𝗭"],
["卂","乃","匚","ᗪ","乇","千","Ꮆ","卄","丨","ﾌ","Ҝ","ㄥ","爪","几","ㄖ","卩","Ɋ","尺","丂","ㄒ","ㄩ","ᐯ","山","乂","ㄚ","乙"],
["A҉","B҉","C҉","D҉","E҉","F҉","G҉","H҉","I҉","J҉","K҉","L҉","M҉","N҉","O҉","P҉","Q҉","R҉","S҉","T҉","U҉","V҉","W҉","X҉","Y҉","Z҉"]]
Orgtarikh = ["/","0","1","2","3","4","5","6","7","8","9"]
ftarikh = [['/','⁰','¹','²','³','⁴','⁵','⁶','⁷','⁸','⁹']]

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'www.qqxnxx.com',
    'Origin': 'http://www.qqxnxx.com',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 OPR/82.0.4227.33'
}
url = 'http://www.qqxnxx.com/download.php'

one = [" ن كيس", "بيضة الكلب", "والد الكلب", "والد الكلب", "كلب الأب", "الكلب الأب", "كلب الجدة", "الكلب الأم", "الأم" "كلب", "أم كلب", "أم كلب", "أم سيئة", "ضاجعت أمك", "بيضة جني", "بيضة كلب", "ضاجعت أمك", "نيني ", "فرخخخخ" , "اه دخلة كلة", "نيني جاشاد", "نين خايخور", "تهاهاهاهاهاهاهاهاهاهاهاهاها", "نانميم", "كسيييييي", "كيس كيش", "كيس بيبي", "كيس أومات", "كيس خالات", " تعال موطليكيس حمار", "كيس كون", "كيس ماميت", "كيس مادرين", "قصدة الأم", "كس امك", "تههههههههههه", "نيني كيس", "عير بيك", "بي"]
onee = ["❤️", "🧡", "💛", "💚", "🩵", "💜", "🩶", "🤍"]

def fosh_saz(text):
 return f"{choice(one)}{text}"
 
def ghalb_saz(text):
 return f"{choice(onee)}{text}"

def font(text, lang):
 request = get('http://fonts.googleapis.com/css?family={}'.format(lang, text))
 if request.json()['Ok' if lang else 'ok'] == True:
  results = "🌜 ᴛʜᴇʀᴇ's ʏᴏᴜʀ ʀᴇsᴜʟᴛ 🌛 \n\n"
  for key, value in request.json()['Result' if lang else 'result'].items():
   results += f"├ • {key} | `{value}`\n"
 return results

def create_time():
 a = datetime.now(timezone("Asia/Baghdad")).strftime("%H:%M")
 ran = choice(fonts)
 for char in a :
  a = a.replace(char , ran[int(org.index(str(char)))])
 return a

def create_time2():
 a = datetime.now(timezone("Asia/Baghdad")).strftime("%H:%M")
 ran = choice(fonts2)
 for char in a :
  a = a.replace(char , ran[int(org.index(str(char)))])
 return a

def create_tarikh():
 a = jdatetime.date.today().strftime("%Y/%m/%d")
 ran = choice(ftarikh)
 for char in a :
  a = a.replace(char , ran[int(Orgtarikh.index(str(char)))])
 return a

def fontinname(name):
 name = name.upper()
 rnd = choice(name_font)
 for char in name:
  try:
   name = name.replace(char , rnd[org_eng.index(char)])
  except:
   pass
 return name

def DLX(Url):
    data = {'videoid': Url}
    soup = BeautifulSoup(post(url=url, headers=headers, data=data).text, 'html.parser')
    link = findall(r'"(https://video-hw.xnxx-cdn.com/videos/flv/.*)"', str(soup.find('script', {'type': 'application/ld+json'})))[0].split('"')[0]
    FileName = link.split('/')[-1]
    FileName = FileName[:FileName.find('?')]
    return link

def snippet(params):
    url = 'https://api.crabon.io/v1/snippet'
    path = 'i.png'
    response = post('https://carbonara-42.herokuapp.com/api/cook', json=params)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in response:
                f.write(chunk)
    print(response.status_code)
    
def generateimage(text):
    rand_img = ["image1.jpg","image2.jpg","image3.jpg","image4.jpg","image5.jpg","image6.jpg"]
    image = Image.open(choice(rand_img))
    image.load()
    W, H = image.size
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font='font.ttf', size=190)
    wt, ht = draw.textsize(text, font=font)
    draw.text(((W - wt) / 2, (H - ht) / 2 ), text, font=font, fill=choice(["#00c7a4","#0071c7","#c7a200","#728593","#943633","#6495ed","#43f70a","#e1b2ae","#527130","#629f5d","#3d4e90","#9a9ec4",]))
    image.save('time_image.jpg')

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def if_not_exist_creat(filename):
 if not os.path.isfile(filename):
  with open(filename , "w") as f:
   f.write("")
   f.close() 
def write(filename , text):
 with open(filename , "w", encoding="utf-8") as f:
   f.write(text)
   f.close() 
def write_a(filename , text):
 with open(filename , "a", encoding="utf-8") as f:
   f.write(text)
   f.close() 
def read(filename):
 with open(filename , "r", encoding="utf-8") as f:
   return f.read()
def json_read(filename):
 with open(filename , "r", encoding="utf-8") as f:
   return json.load(f)
   
def run_codi(lang , code):
    a = Rextester(lang , code)
    k = a.stats;k = k.replace(",","")
    run_time = k.index("running time:")
    cpu_time = k.index("cpu time:")
    used_memory = k.index("memory peak:")
    kossher = k.index("absolute service time")
    mamad = f"**Result**: \n`{a.result if a.result else '--'}`{f'**ERROR**: `{a.errors}`' if a.errors else ''}\n**State**:\n__{k[run_time:cpu_time]}\n{k[cpu_time:used_memory]}\n{k[used_memory:kossher]}__"
    return mamad

def moon_or_sun():
  a = datetime.now(timezone("Asia/Baghdad")).strftime("%H");a = int(a)
  if a in[20,21,22,23,00,1,2,3,4,5]:
    b = "🌑"
  elif a in[6,7]:
    b = "🌒"
  elif a in[8,9,10,11]:
    b = "🌔"
  elif a in[12,13,14,15,16,17]:
    b = "🌕"
  elif a in[18,19]:
    b = "🌒"
  return b

def dast_del(text):
  if text.privileges:
     if text.privileges.can_delete_messages == True:
        return True

def have_sec(t):
  if len(t.split(":")) == 3:
    return str(t)
  else:
    return str(t) +":00"
    
def read_note(url):
  b = str()   
  for j in url.split("\n"):
    try: 
      n = pn.read_note(j) 
      b += f"\n({j}) --> ({n})"
    except Exception as er:
      b += f"\n({j}) --> ({er})"
  return b


