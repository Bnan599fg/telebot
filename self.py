#_________________________LEVI_____________________
from pyrogram import Client, filters, idle , errors ,enums
from pyrogram.types import Message , ChatPermissions
from pyrogram.raw import functions , base , types
from pyrogram.raw.functions.auth import ResetAuthorizations
from pyrogram.raw.functions.contacts import GetBlocked
from pyrogram.raw.functions.messages import GetAllStickers
from requests import get as GET
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from wikipedia import search,page
from pytz import timezone
from datetime import date,datetime
import instagram_private_api as insta
from pyrogram.filters import create
from random import choice
import instagram_private_api as insta
from os import name
from plugins import font, fosh_saz, ghalb_saz, DLX,fontinname,create_time,create_time2,get_size,generateimage,snippet,read,write,if_not_exist_creat,run_codi,create_tarikh,moon_or_sun,json_read,dast_del,have_sec,write_a
from time import time
from gtts import gTTS
import os
from ipapi import location
from PIL import Image
from socket import gethostbyname
from platform import python_version,uname
from urllib.request import Request
from uptime import uptime
from time import strftime, gmtime
from re import match,findall
from time import sleep
from qrcode import make
from psutil import virtual_memory,cpu_freq,cpu_percent,cpu_count
from base64 import b64encode
from decimal import Decimal,getcontext
import ffmpeg
import json
import sys
from io import StringIO
os.chdir(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
enemy = []
krashh = []
mutey = []
now = ""
galbe = ["🤍","🖤","🤎","💜","💙","💚","💛","🧡","❤️"]
ez_emoji = ["😀", "😃", "😄", "😁", "😆", "😅", "🗿", "🤣", "😭", "😗", "😙", "😚", "😘", "🥰", "😍", "🤩", "🥳", "🤗", "🙃", "🙂", "☺️", "😊", "😏", "😌", "😉", "🤭", "😶", "🤔", "🤪", "😜", "😝", "😛", "😋", "😔", "😑", "😐", "🤨", "🧐", "🙄", "😒", "😤", "😠", "😡", "🤬", "☹️", "😰", "🤫", "🤐", "😬", "😳", "🥺", "😟", "😕", "🙁", "😨", "😧", "😦", "😮", "😯", "😲", "😱", "🤯", "😢", "😥", "😓", "😞", "😣", "😖", "😩", "😫", "🤤", "🥱", "🤮", "😇", "😵", "🤥", "🤓", "😎", "🤑", "🤠"]
eb_emoji = ["🗿","🦦"]
eg_emoji = ["🧛🏻‍♀️", "🧸", "🦦"]
answer = []
javab = []
Src_vrsion = "v1.2"
  

if not os.path.isfile("data.json"):
 with open("data.json" , "w") as fjr:
  fjr.write('{"limitDel": 4, "welcomeen": "off", "welcomefa": "off", "firstcom": "off", "timename1": "off", "timename2": "off", "timename3": "off", "timebio1": "off", "timebio2": "off", "timebio3": "off", "fontname": "off", "fuck": "off", "anti_del": "off", "autoan": "off", "boldmode": "off", "emojimode": "off", "emojigirl": "off", "emojiboy": "off", "underline": "off", "italicmode": "off", "codemode": "off", "strike": "off", "spoilermode": "off"}')
  fjr.close() 
if not os.path.isfile("fucking.json"):
 with open("fucking.json" , "w") as fjr:
  fjr.write('{"fuck": "off"}')
  fjr.close() 
if_not_exist_creat("time.txt")
if_not_exist_creat("user.txt")
if_not_exist_creat("db.txt")
if_not_exist_creat("anti_del_chat.txt")
if_not_exist_creat("send_time_text.txt")
if_not_exist_creat("firstcommentmsg.txt")
if_not_exist_creat("welcomeen_add_text.txt")
if_not_exist_creat("welcomefa_add_text.txt")


api_id = 4301543 #ايبي ايدي
api_hash = 'a778af67524f43e00f9863df91f86ebc' # ايبي هاش
app = Client("Winston_Abol", api_id, api_hash,device_model="iPhone 11 pro",system_version="Linux")


    
    
def mak():
 with app:
  m =  app.send_message("me" , ".").message_id
  app.delete_messages("me" , m) 
  
def job():
 a = json_read("data.json")
 if read("time.txt") != datetime.now(timezone("Asia/Baghdad")).strftime("%H:%M"):
  try:
   if (a["timename1"] == "on"):app.invoke(functions.account.UpdateProfile(last_name=f'{create_time()}'))
   if (a["timename2"] == "on"):app.invoke(functions.account.UpdateProfile(last_name=f'{create_time2()}'))
   if (a["timename3"] == "on"):app.invoke(functions.account.UpdateProfile(last_name=f'{create_time3()}'))
   if (a["timebio1"] == "on"):app.invoke(functions.account.UpdateProfile(about=f'{read("userbio.txt")} {create_time()}'))
   if (a["timebio2"] == "on"):app.invoke(functions.account.UpdateProfile(about=f'{read("userbio.txt")} {create_time2()}'))
   if (a["timebio3"] == "on"):app.invoke(functions.account.UpdateProfile(about=f'{moon_or_sun()} | {read("userbio.txt")} | {create_time2()} | {create_tarikh()}'))
   if (a["fontname"] == "on"):app.invoke(functions.account.UpdateProfile(first_name=f'{fontinname(read("user.txt"))}'))
  except :
   pass
  write("time.txt" , datetime.now(timezone("Asia/Baghdad")).strftime("%H:%M"))
def antidelmember():
 a = json_read("data.json")
 chat_id_kiri = read("anti_del_chat.txt")
 if a["anti_del"] == "on":
  ban_konande = []
  band = []
  kok = []
  db = ""
  chif = app.get_chat_members(chat_id_kiri, filter=enums.ChatMembersFilter.BANNED)
  for i in chif:
   ban_konande.append(i.restricted_by.id)
   band.append(i.user.id)
  for b in ban_konande:
   kir = f"{b}:{ban_konande.count(b)}\n"
   if kir not in db:
    db += f"{b}:{ban_konande.count(b)}\n"   
    kok.append(b)
  write("db.txt", db)
  database = open("db.txt", "r")
  for k in range(1,len(kok)+1):
   kirkhar = database.readline().split(":")
   if int(kirkhar[1]) >= a['limitDel']: 
    try:
      app.ban_chat_member(chat_id_kiri , kirkhar[0])
      app.send_message(chat_id_kiri , f'**تم حظري: {kirkhar[0]}**\n لأنه قام بحظر الأعضاء فوق الحد المسموح\n\n  **@Q_B_H**')
      for i in band:
        app.unban_chat_member(chat_id_kiri, i)
    except Exception as er:
      app.send_message("me" , f"❋ **error** :\n(`{er}`)")
      
@app.on_message(filters.linked_channel)
def first(app, m:Message):
 chat_id , text = m.chat.id , m.text
 a = json_read("data.json")
 if a["firstcom"] == "on":
  msgr = read("firstcommentmsg.txt").split(":")
  if text != "@BotLevi":
    if msgr[0] == "text":
       m.reply(msgr[1])
    elif msgr[0] == "sticker":
       m.reply_sticker(msgr[1])
    elif msgr[0] == "animation":
       m.reply_animation(msgr[1])
    else:
       m.reply("__error:__\nلم يتم تعيين الرسالة\n ****")

def filt(_ , __ , m:Message):
 try:
  if m.from_user.id in krashh :
   return True
  else:
   return False 
 except:
  pass

if_user_is_krashh = filters.create(filt)
@app.on_message(if_user_is_krashh)
def enym(app, m:Message):
 app.send_message(m.chat.id , ghalb_saz(text="‌") , reply_to_message_id=m.id)
 
def filt(_ , __ , m:Message):
 try:
  if m.from_user.id in enemy :
   return True
  else:
   return False 
 except:
  pass

if_user_is_enemy = filters.create(filt)
@app.on_message(if_user_is_enemy)
def enym(app, m:Message):
 app.send_message(m.chat.id , fosh_saz(text="‌") , reply_to_message_id=m.id)


def fbky(_ , __ , m:Message):
 try:
  if m.from_user.id in mutey :
   return True
  else:
   return False 
 except:
  pass

if_user_is_mutey = filters.create(fbky)
@app.on_message(if_user_is_mutey)
def muty(app, m:Message):
 app.delete_messages(m.chat.id , m.id)

@app.on_message(filters.new_chat_members,group=6)
def welcomeenbot(app, m:Message) :
 text = m.text 
 a = json_read("data.json")
 welcomeen_kos = read("welcomeen_add_text.txt")
 welcomeen_message = (f"""Hi {m.from_user.mention} 🗿\nWelcome To **{m.chat.title}** 🎀\n🎈Date: `{date.today().strftime("%Y/%m/%d")}`\n🌸Time: `{datetime.now(timezone("Asia/Baghdad")).strftime("%H:%M:%S")}`\n{welcome_kos if welcomeen_kos else ""}""")
 if a["welcomeen"] == "on":
   app.send_message(m.chat.id , welcomeen_message)

@app.on_message(filters.new_chat_members,group=6)
def welcomefabot(app, m:Message) :
 text = m.text 
 a = json_read("data.json")
 welcomefa_kos = read("welcomefa_add_text.txt")
 welcomefa_message = (f"""مرحبًا بك في **{m.chat.title}** 🎀\n🎈التاريخ: `{date.today().strftime("%Y/%m/%d")}`\n🌸الوقت:`{datetime.now(timezone("Asia/Baghdad")).strftime("%H:%M:%S")}`""")
 if a["welcomefa"] == "on":
   app.send_message(m.chat.id , welcomefa_message)

@app.on_message(filters.text,group=6)
def autoanwer(app, m:Message):
  text = m.text 
  a = json_read("data.json")
  if a["autoan"] == "on":
   if text in answer:
    num = answer.index(text)
    app.send_message(m.chat.id , javab[num], reply_to_message_id=m.id)
    sleep(9)
    num = 0
    
@app.on_message(filters.text & filters.me)
@app.on_edited_message(filters.text & filters.me)
def updates(app, m:Message):
 global api
 global enemy
 global krashh
 global mutey
 global lang
 global now
 text = m.text 

 json_database = json_read("data.json")
 if (json_database["boldmode"] == "on"):
  m.edit_text(f"**{text}**")
 elif (json_database["italicmode"] == "on"):
  m.edit_text(f"__{text}__")
 elif (json_database["codemode"] == "on"):
  m.edit_text(f"`{text}`")
 elif (json_database["underline"] == "on"):
  m.edit_text(f"<u>{text}</u>")
 elif (json_database["emojimode"] == "on"):
  m.edit_text(f"{text} {choice(ez_emoji)}")
 elif (json_database["emojiboy"] == "on"):
  m.edit_text(f"{text} {choice(eb_emoji)}")
 elif (json_database["emojigirl"] == "on"):
  m.edit_text(f"{text} {choice(eg_emoji)}")
 elif (json_database["strike"] == "on"):
  m.edit_text(f"~~{text}~~")
 elif (json_database["spoilermode"] == "on"):
  m.edit_text(f"||{text}||")

 if text.startswith("fontfa"):
  lang = "fa"
  kobs = font(text=text.replace("fontfa " , "") , lang=lang)
  app.edit_message_text(m.chat.id , m.id ,kobs)
  
 elif text.startswith("fonten"):
  lang = ""
  kobs = font(text=text.replace("fonten " , "") , lang=lang)
  app.edit_message_text(m.chat.id , m.id ,kobs)

 elif text.startswith("اللغة العربية"):
  lang = "fa"
  kobs = font(text=text.replace("عربي مو عراقي  " , "") , lang=lang)
  app.edit_message_text(m.chat.id , m.id ,kobs)

 elif text.startswith("اللغة الانكليزية"):
  lang = ""
  kobs = font(text=text.replace("الخط الإنجليزي " , "") , lang=lang)
  app.edit_message_text(m.chat.id , m.id ,kobs)


 elif text.startswith("clone"):
   try:
    if m.reply_to_message:
     userSelfp = m.reply_to_message.from_user.id
     b = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(userSelfp)))
     kiri = app.get_users(m.reply_to_message.from_user.id)
     user_id_get = m.reply_to_message.from_user.id
    else:
     text = text.replace(" ","").replace("clone","")
     user_id_get = app.get_users(text).id
     kiri = app.get_users(user_id_get)
     b = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(user_id_get)))
    app.edit_message_text(m.chat.id , m.id , text=f"""
    **Cloner**
❋ `الاسم الاول`⤳ (`{b.users[0].first_name if b.users[0].first_name else '--'}`)
❋ `الاسم الثاني`⤳ (`{(b.users[0].last_name if b.users[0].last_name else '--')}`)
❋ `bio`⤳ (`{(b.full_user.about if b.full_user.about else '--')}`)""")
    loudo = app.download_media(kiri.photo.big_file_id)
    app.set_profile_photo(photo=loudo)
    app.update_profile(first_name=b.users[0].first_name)
    app.update_profile(last_name=(b.users[0].last_name if b.users[0].last_name else ""))
    app.update_profile(bio=(b.full_user.about if b.full_user.about else ""))
    app.edit_message_text(m.chat.id , m.id , "❋ Clone Successfully Completed")
    os.remove(loudo)
   except errors.exceptions.bad_request_400.UsernameNotOccupied: 
    app.send_message(m.chat.id , f"❋ Username Not Valid ❋") 
   except Exception as er:
    m.edit_text(f"❋ **error** :\n(`{er}`)")

 elif text.startswith("لنسخ"):
   try:
    if m.reply_to_message:
     userSelfp = m.reply_to_message.from_user.id
     b = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(userSelfp)))
     kiri = app.get_users(m.reply_to_message.from_user.id)
     user_id_get = m.reply_to_message.from_user.id
    else:
     text = text.replace(" ","").replace("لنسخ","")
     user_id_get = app.get_users(text).id
     kiri = app.get_users(user_id_get)
     b = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(user_id_get)))
    app.edit_message_text(m.chat.id , m.id , text=f"""
    **Cloner**
❋ `الاسم الاول`⤳ (`{b.users[0].first_name if b.users[0].first_name else '--'}`)
❋ `الاسم الثاني`⤳ (`{(b.users[0].last_name if b.users[0].last_name else '--')}`)
❋ `bio`⤳ (`{(b.full_user.about if b.full_user.about else '--')}`)""")
    loudo = app.download_media(kiri.photo.big_file_id)
    app.set_profile_photo(photo=loudo)
    app.update_profile(first_name=b.users[0].first_name)
    app.update_profile(last_name=(b.users[0].last_name if b.users[0].last_name else ""))
    app.update_profile(bio=(b.full_user.about if b.full_user.about else ""))
    app.edit_message_text(m.chat.id , m.id , "❋ Clone Successfully Completed")
    os.remove(loudo)
   except errors.exceptions.bad_request_400.UsernameNotOccupied: 
    app.send_message(m.chat.id , f"❋ Username Not Valid ❋") 
   except Exception as er:
    m.edit_text(f"❋ **error** :\n(`{er}`)")



 elif text.startswith("block"):
  app.block_user(m.reply_to_message.from_user.id if m.reply_to_message else text.split()[1])
  m.edit_text(f"💣 {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} تم حظره") 

 elif text.startswith("unblock"):
  app.unblock_user(m.reply_to_message.from_user.id if m.reply_to_message else text.split()[1])
  m.edit_text(f"🩷 {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} لقد جاء من كتلة") 

 elif text.startswith("left"):
  try:
   if text.split()[1]:
    app.leave_chat( text.split()[1] , delete=True)
    m.edit_text(f"🥺تم الرفع بنجاح من[ `{text.split()[1]}` ]")
   else:
    app.send_message(m.chat.id , f"Bye :)") 
    app.leave_chat(m.chat.id , delete=True) 
  except Exception as er:
   m.edit_text(f"**تحذير**: بالنسبة للدور العلوي، يجب علينا استخدام القناة أو المجموعة قبل الأمر | المجموعة والقناة العامة")
   
 elif text.startswith("join "):
  try:
   link = text.replace("join ","")
   link = link.replace('+','joinchat/')
   app.join_chat(link)
   app.send_message(m.chat.id , f'😍 لقد قمت بإدخال [ {link} ] بنجاح. ' ,disable_web_page_preview=True)
  except Exception as er:
   m.edit_text(f"**تحذير**: للانضمام يجب عليك استخدام القناة أو المجموعة أمام الأمر | المجموعة والقناة العامة")
   
 elif text == ".delethistory":
  try: 
   app.invoke(functions.channels.DeletHistory(app.resolve_peer(channel=m.chat.id)))
  except Exception as er:
   m.edit_text(f"❋ **error** :\n(`{er}`)")
  else:
   app.send_message(m.chat.id , f"❋ Chat Leared") 
#
 elif text.startswith("ban"):
  try:
   app.ban_chat_member(m.chat.id , (m.reply_to_message.from_user.id if m.reply_to_message else text.split()[1]))
   app.send_message(m.chat.id , f"✿ مستخدم {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} تم الحظر بنجاح!")
  except Exception as er:
   m.edit_text(f"الرجاء الرد على المستخدم")
   
 elif text.startswith("unban"):
  try:
   app.unban_chat_member(m.chat.id , (m.reply_to_message.from_user.id if m.reply_to_message else text.split()[1]))
   app.send_message(m.chat.id , f"✿ مستخدم {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} تم بنجاح  !")
  except Exception as er:
   m.edit_text(f"الرجاء الرد على المستخدم")
#
 elif text.startswith(".clear_member"):
   target = text.split()[1]
   m.edit_text(f"❋ Target Chat: `{target}`\n__Start Ban members__ . . .")
   for member in app.get_chat_members(target):
     try:
       app.ban_chat_member(target , member.user.id)
     except errors.FloodWait as e:
       app.send_message("me",f"❋ Wait For {e.x} Seconds")
       sleep(e.x)
       app.send_message("me",f"❋ **Flood Wait Has Ended**🥳\nSend [ `.clear_member {target}` ] Again")
     except errors.exceptions.bad_request_400.UserAdminInvalid:
       app.send_message("me",f"**❋ You Are Not Admin in** ( `{target}` )")
       pass
     except errors.exceptions.bad_request_400.BadRequest:
       app.send_message("me",f"**❋ Clear Members of ( {target} ) Has Been Ended**")
       pass
     except Exception as er:
       app.send_message("me",f"❋ **error** :\n(`{er}`)")
#
 elif text.startswith("delmute"):
  try:
   app.unban_chat_member(m.chat.id , (m.reply_to_message.from_user.id if m.reply_to_message else text.split()[1]))
   app.send_message(m.chat.id , f"❋ User {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} Successfully UnMuted !")
  except Exception as er:
   m.edit_text(f"يرجى إعادة التشغيل لتحرير الضغط")

 elif text.startswith("setmute"):
   try:
    app.restrict_chat_member(m.chat.id, m.reply_to_message.from_user.id, ChatPermissions())
    app.send_message(m.chat.id , f"✿ مستخدم  {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} اختنق")
   except:
    m.edit_text(f"الرجاء الرد لإسكات المستخدم")

 elif text.startswith("setchatphoto"):
   try:
     if m.reply_to_message.photo:
       app.set_chat_photo(chat_id=m.chat.id,photo=m.reply_to_message.photo.file_id)
       app.send_message(m.chat.id , f"✿ تم تغيير صورة الدردشة الخاصة بك بنجاح !")
     else:
       app.set_chat_photo(chat_id=m.chat.id,video=m.reply_to_message.video.file_id)
       app.send_message(m.chat.id , f"✿ تم تغيير صورة الدردشة الخاصة بك بنجاح !")
   except:
     m.edit_text(f"✿الرجاء الرد لتغيير الصورة!")
     

 elif text.startswith("setprofile"):
  try:
    if m.reply_to_message.photo:
     down = app.download_media(m.reply_to_message)
     app.set_profile_photo(photo=down)
     app.send_message(m.chat.id , f"✿ تمت إزالة الصورة من ملفاتك الشخصية!")
     os.remove(down)
  except :
    m.edit_text(f"✿الرجاء الرد لتغيير الصورة!")

 elif text.startswith("ست پروفایل"):
  try:
    if m.reply_to_message.photo:
     down = app.download_media(m.reply_to_message)
     app.set_profile_photo(photo=down)
     app.send_message(m.chat.id , f"✿ تمت إزالة الصورة من ملفاتك الشخصية!")
     os.remove(down)
  except :
    m.edit_text(f"✿الرجاء الرد لتغيير الصورة!")

 elif text.startswith("delprofile"):
  try:
    photos = app.get_chat_photos("me")
    app.delete_profile_photos(next(photos).file_id)
    app.send_message(m.chat.id , f"✿ تمت إزالة الصورة من ملفاتك الشخصية!")
  except Exception as er:
    m.edit_text(f"سيتم استخدامه لإزالة الصورة من ملفك الشخصيد")

 elif text.startswith("حذف بروفايل مالتك"):
  try:
    photos = app.get_chat_photos("me")
    app.delete_profile_photos(next(photos).file_id)
    app.send_message(m.chat.id , f"✿ تمت إزالة الصورة من ملفاتك الشخصية!")
  except Exception as er:
    m.edit_text(f"سيتم استخدامه لإزالة الصورة من ملفك الشخصيد")



 elif "delchatphoto" == text:
  try:
   app.delete_chat_photo(m.chat.id)
   m.reply(f"✿ تم حذف صورة الدردشة بنجاح!")
  except Exception as er:
   m.edit_text(f"✿ **خطأ** :\n(`{er}`)")

 elif text.startswith("setchatname"):
  try:
   kx = text.replace("setchatname" , "")[1::]
   app.set_chat_title(m.chat.id, kx.strip())
   m.reply(f"✿ تم تغيير اسم المجموعة بنجاح° `{kx}` °")
  except Exception as er:
   m.edit_text(f"✿ **خطأ** :\n(`{er}`)")

 elif text.startswith("setchatbio"):
  try:
   kx = text.replace("setchatbio","")[1::]
   app.set_chat_description(m.chat.id, kx)
   m.reply(f"✿ تم تغير بنجاح` °")
  except Exception as er:
   m.edit_text(f"✿ **خطأ** :\n(`{er}`)")

 elif "pin" == text:
  if m.reply_to_message:
   try:
    m.pin(disable_notification=False)
    m.edit_text(f'✿ پین شد ')
   except Exception as er:
    m.edit_text(f"✿ **خطأ** :\n(`{er}`)")
  else:
   m.edit_text(f"✿ الرجاء الرد على الرسالةد")

 elif "unpin" == text:
  if m.reply_to_message:
   try:
    m.unpin()
    m.edit_text(f'✿ پین تم الحذف')
   except Exception as er:
    m.edit_text(f"❋ **error** :\n(`{er}`)")
  else:
   m.edit_text(f"✿ الرجاء الرد على الرسالةد")

 elif "unpinall" == text:
  try:
   app.unpin_all_chat_messages(m.chat.id)
   

 elif text.startswith("setchatusername"):
  try:
   kx = text.split()[1]
   app.set_chat_username(m.chat.id, kx)
   m.edit_text(f'✿ تم تغيير اسم مستخدم الدردشة بنجاح° `{kx}` °')
  except Exception as er:
   m.edit_text(f"✿ لا يمكن استخدام هذا الأمر إلا من قبل صاحب الدردشة")   

 elif text.startswith("creatchannel"):
  try:
   kx = text.split()[1]
   app.create_channel(title=f'{kx}')
   m.edit_text(f'✿ تم إنشاء القناة المسماة [ `{kx}` ].!')
  except Exception as er:
   m.edit_text(f"✿ لاستخدام هذا الأمر يجب عليك وضع الاسم أمام قناة creatchannel .")

 elif text.startswith("creatsupergroup"):
  try:
   kx = text.split()[1]
   app.create_supergroup(title=f'{kx}')
   m.edit_text( f'✿ تم إنشاء المجموعة الفائقة المسماة [`{kx}`')
  except Exception as er:
   m.edit_text(f"✿ لاستخدام هذا الأمر، يجب عليك وضع الاسم أمام creatsupergroup.")

 elif text.startswith("creatgroup"):
  try:
   kx = text.split()[1]
   app.create_group(title=f'{kx}')
   m.edit_text( f'✿تم إنشاء المجموعة تحت اسم [`{kx}`). !')
  except Exception as er:
   m.edit_text(f"✿ لاستخدام هذا الأمر، يجب عليك وضع الاسم أمام creatsupergroup. .")

 elif text.startswith("delallmsguser"):
  try:
   app.delete_user_history(m.chat.id , (m.reply_to_message.from_user.id if m.reply_to_message else text.split()[1]))
   m.edit_text(f"✿ کل پیام های مستخدم  {(m.reply_to_message.from_user.mention if m.reply_to_message else f'<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>')} تم الحذف .")
  except Exception as er:
   m.edit_text(f"✿ **خطأ**: يرجى الرد على المستخدم لحذف جميع الرسائل من الدردشة. ")


 elif text.startswith("setname"):
  try:
   kx = text.replace("setname","")[1::]
   app.invoke(functions.account.UpdateProfile(first_name=kx))
   write("user.txt" , text.replace("setname","")[1::])
   m.edit_text(f'✿ تم تحديث وتغيير اسم حسابك بنجاح < `{kx}` ✄✄')
  except Exception as er:
   m.edit_text(f"✿ **خطأ**: لتغيير اسم حسابك، يرجى كتابة الاسم أمام [setname] وتوثيقه.")

 elif text.startswith("ضبط الاسم"):
  try:
   kx = text.replace("ضبط الاسم","")[1::]
   app.invoke(functions.account.UpdateProfile(first_name=kx))
   write("user.txt" , text.replace("ضبط الاسم","")[1::])
   m.edit_text(f'✿ تم تحديث وتغيير اسم حسابك بنجاح < `{kx}` ✄✄')
  except Exception as er:
   m.edit_text(f"✿ **خطأ**: لتغيير اسم حسابك، يرجى كتابة الاسم أمام [setname] وتوثيقه.")



 elif text.startswith("setالاسم الثاني"):
  try:
   kx = text.replace("setالاسم الثاني","")[1::]
   app.invoke(functions.account.UpdateProfile(last_name=kx))
   m.edit_text(f'✿ تم تحديث وتغيير حساب عائلتك بنجاح < `{kx}` ✄')
  except Exception as er:
   m.edit_text(f"✿ **خطأ**: لتغيير الاسم الأخير لحسابك، يرجى كتابة [تعيين اسم العائلة] وتوثيقه.")

 elif text.startswith("ترتيب الأسرة"):
  try:
   kx = text.replace("ترتيب الأسرة","")[1::]
   app.invoke(functions.account.UpdateProfile(last_name=kx))
   m.edit_text(f'✿ تم تحديث وتغيير حساب عائلتك بنجاح < `{kx}` ✄')
  except Exception as er:
   m.edit_text(f"✿ **خطأ**: لتغيير الاسم الأخير لحسابك، يرجى كتابة [تعيين اسم العائلة] وتوثيقه.")


 elif text.startswith("setbio"):
  try:
   kx = text.replace("setbio","")[1::]
   app.invoke(functions.account.UpdateProfile(about=kx))
   write("userbio.txt" , text.replace("setbio","")[1::])
   m.edit_text(f'✿ تم تحديث وتغيير السيرة الذاتية لحسابك بنجاح < `{kx}` ✄')
  except Exception as er:
   m.edit_text(f"✿ **خطأ**: لتغيير سيرتك الذاتية يرجى كتابة الtext الخاص بك أمام الأمر [ضبط البيو سيدة] ثم توثيقه. .")

 elif text.startswith("إعداد السيرة الذاتية"):
  try:
   kx = text.replace("إعداد السيرة الذاتية","")[1::]
   app.invoke(functions.account.UpdateProfile(about=kx))
   write("userbio.txt" , text.replace("إعداد السيرة الذاتية","")[1::])
   m.edit_text(f'✿ تم تحديث وتغيير السيرة الذاتية لحسابك بنجاح < `{kx}` ✄')
  except Exception as er:
   m.edit_text(f"✿ **خطأ**: لتغيير سيرتك الذاتية يرجى كتابة الtext الخاص بك أمام الأمر [ضبط البيو سيدة] ثم توثيقه. .")


 elif text.startswith("bold"):
  if text.split()[1] == "on":
   json_database.update({"boldmode":"on"})
   write("data.json", json.dumps(json_database))
m.edit_text(f"✿ تم تشغيل الخط العريض للtext** 🩷")
   elif text.split()[1] == "إيقاف":
    json_database.update({"boldmode": "off"})
    write ("data.json"، json.dumps (json_database))
    m.edit_text(f"✿ الخط العريض للtext **متوقف** 🩶")
   else:
    m.edit_text(f"✿ **خطأ**: استخدم ``تشغيل'' لتشغيله، و``إيقاف'' لإيقاف تشغيله.")

 elif text.startswith("spoiler"):
  if text.split()[1] == "on":
   json_database.update({"spoilermode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"✿وضع المفسد **قيد التشغيل** 🩷")
   elif text.split()[1] == "إيقاف":
    json_database.update({"spoilermode": "إيقاف"})
    write ("data.json"، json.dumps (json_database))
    m.edit_text(f"✿وضع المفسد **متوقف** 🩶")
   else:
    m.edit_text(f"✿ **خطأ**: استخدم ``تشغيل'' لتشغيله، و``إيقاف'' لإيقاف تشغيله.")

 elif text.startswith("italic"):
  if text.split()[1] == "on":
   json_database.update({"italicmode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"✿وضع الإمالة **قيد التشغيل** 🩷")
   elif text.split()[1] == "إيقاف":
    json_database.update({"italicmode": "off"})
    write ("data.json"، json.dumps (json_database))
    m.edit_text(f"✿وضع الإمالة **متوقف** 🩶")
   else:
    m.edit_text(f"✿ **خطأ**: استخدم ``تشغيل'' لتشغيله، و``إيقاف'' لإيقاف تشغيله.")

 elif text.startswith("code"):
  if text.split()[1] == "on":
   json_database.update({"codemode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"✿وضع الكود **قيد التشغيل** 🩷")
   elif text.split()[1] == "إيقاف":
    json_database.update({"codemode": "off"})
    write ("data.json"، json.dumps (json_database))
    m.edit_text(f"✿وضع الكود **متوقف** 🩶")
   else:
    m.edit_text(f"✿ **خطأ**: استخدم ``تشغيل'' لتشغيله، و``إيقاف'' لإيقاف تشغيله.")
   
 elif text.startswith("strike"):
  if text.split()[1] == "on":
   json_database.update({"strike":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"✿وضع write **قيد التشغيل** 🩷")
   elif text.split()[1] == "إيقاف":
    json_database.update({"strike": "off"})
    write ("data.json"، json.dumps (json_database))
    m.edit_text(f"✿وضع write **متوقف** 🩶")
   else:
    m.edit_text(f"✿ **خطأ**: استخدم ``تشغيل'' لتشغيله، و``إيقاف'' لإيقاف تشغيله.")

 elif text.startswith("underline"):
  if text.split()[1] == "on":
   json_database.update({"underline":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"✿وضع التسطير **قيد التشغيل** 🩷")
   elif text.split()[1] == "إيقاف":
    json_database.update({"underline": "off"})
    write ("data.json"، json.dumps (json_database))
    m.edit_text(f"✿وضع التسطير **متوقف** 🩶")
   else:
    m.edit_text(f"✿ **خطأ**: استخدم ``تشغيل'' لتشغيله، و``إيقاف'' لإيقاف تشغيله.")

 elif text.startswith("emoji"): 
  if text.split()[1] == "on":
   json_database.update({"emojimode":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"✿ وضع الرموز التعبيرية التلقائي **قيد التشغيل** 🩷")
   elif text.split()[1] == "إيقاف":
    json_database.update({"emojimode": "off"})
    write ("data.json"، json.dumps (json_database))
    m.edit_text(f"✿ وضع الرموز التعبيرية التلقائي **متوقف** 🩶")
   else:
    m.edit_text(f"✿ **خطأ**: استخدم ``تشغيل'' لتشغيله، و``إيقاف'' لإيقاف تشغيله.")

 elif text.startswith(".emojib"): 
  if text.split()[1] == "on":
   json_database.update({"emojiboy":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"✿ وضع الرموز التعبيرية التلقائي للصبي ** قيد التشغيل ** 🩷")
   elif text.split()[1] == "إيقاف":
    json_database.update({"emojiboy": "off"})
    write ("data.json"، json.dumps (json_database))
    m.edit_text(f"✿ وضع الرموز التعبيرية التلقائي للصبي **متوقف** 🤎")
   else:
    m.edit_text(f"✿ **خطأ**: استخدم ``تشغيل'' لتشغيله، و``إيقاف'' لإيقاف تشغيله.")

 elif text.startswith(".emojig"): 
  if text.split()[1] == "on":
   json_database.update({"emojigirl":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"✿ وضع الرموز التعبيرية التلقائي للفتيات ** قيد التشغيل** 🩷")
   elif text.split()[1] == "إيقاف":
    json_database.update({"emojigirl": "off"})
    write ("data.json"، json.dumps (json_database))
    m.edit_text(f"✿ وضع الرموز التعبيرية التلقائي للفتيات **متوقف** 🩷")
   else:
    m.edit_text(f"✿ **خطأ**: استخدم ``تشغيل'' لتشغيله، و``إيقاف'' لإيقاف تشغيله.")

 elif text.startswith("ip"):
  try:
   HOSTNAME = m.reply_to_message.text if m.reply_to_message else text.split()[1]
   app.edit_message_text(m.chat.id, m.id, f'✿ name °`{HOSTNAME}`° عنوان IP: `{gethostbyname(HOSTNAME)}`')
   except:
    app.edit_message_text(m.chat.id, m.id, f'✿ هذا `{HOSTNAME}` خطأ')
   
 elif text.startswith("whoisip"):
  try:
   HOSTIP = m.reply_to_message.text if m.reply_to_message else text.split()[1]
   source = location(ip=HOSTIP, key=None)
   app.edit_message_text(m.chat.id, m.id, f"""
🩶 IP : (`{مصدر["ip"]}`)
 🩶 المدينة: (`{المصدر["المدينة"]}`)
 🩶 الدولة: (`{المصدر["المنطقة"]}`)
 🩶 اللغة الأصلية: (`{source["country"]}`)\n(`{source["country_name"]}`)
 🩶 رمز البلد: (`{source["country_calling_code"]}`)
 🩶 اللغات: (`{المصدر["languages"]}`)
 🩶 مالك IP: (`{source["org"]}`)""")
  except:
   app.edit_message_text(m.chat.id, m.id, f'✿ هذا `{HOSTIP}` خاطئ')


 elif text.startswith(".firstcomment"):
  try:
   if text.split()[1] == "on":
    json_database.update({"firstcom":"on"})
    write("data.json", json.dumps(json_database))
    m.edit_text(f"❋ First comment is **ON**")
   elif text.split()[1] == "off":
    json_database.update({"firstcom":"off"})
    write("data.json", json.dumps(json_database))
    m.edit_text(f"❋ First comment is **OFF**")
  except Exception as er:
   m.edit_text(f"❋ **error** :\n(`{er}`)")

 elif text.startswith(".antich"):
  try:
   write("anti_del_chat.txt" , text.split()[1])
   m.edit_text(f"֍ 𝗢𝗸 :)\nChat ID: `{text.split()[1]}`") 
  except Exception as er:
   m.edit_text(f"├ • `error` ⤳\n(`{er}`)") 



 elif text.startswith("youname"):
  if m.reply_to_message:
   try:
    m.edit_text(f"{m.reply_to_message.from_user.mention}") 
   except:
    m.edit_text(f"⚠️ **خطأ**: يرجى الرد على رسالة المستخدم أو وضع أمر أمام اسم المستخدم")
  else:
   try:
    m.edit_text(f"<a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name}</a>") 
   except:
    m.edit_text(f"⚠️ **خطأ**: يرجى الرد على رسالة المستخدم أو وضع أمر أمام اسم المستخدم")



 elif text == "bashe":
  try:
   down = app.download_media(m.reply_to_message)
   app.send_document("me" , down , caption="|| 🌠 أنقذ 🎥 ||")
   os.remove(down)
  except Exception as er:
   m.edit_text(f"**hom**")



 elif text == "tlpho":
  try:
    down = app.download_media(m.reply_to_message)
    if down == None:
     m.edit_text(f"""⚠️ **خطأ**: يرجى استخدام هذا الأمر على الفيديو أو الملصق
 الأمر: ["تحويل إلى صورة"]-["tlpho"]""")
    else:
     os.rename(down ,'sticker.jpg')
     app.send_photo(m.chat.id , f"sticker.jpg" ,caption="|| 📸 تبدیل به عکس شد 📸 ||", reply_to_message_id=m.id)
     os.remove(f"sticker.jpg")
  except Exception as er:
   m.edit_text(f"""⚠️ **خطأ**: يرجى استخدام هذا الأمر على الفيديو أو الملصق
 الأمر: ["تحويل إلى صورة"]-["tlpho"]""")

 elif text == "تحويل إلى الصورة":
  try:
    down = app.download_media(m.reply_to_message)
    if down == None:
     m.edit_text(f"""⚠️ **خطأ**: يرجى استخدام هذا الأمر على الفيديو أو الملصق
 الأمر: ["تحويل إلى صورة"]-["tlpho"]""")
    else:
     os.rename(down ,'sticker.jpg')
     app.send_photo(m.chat.id , f"sticker.jpg" ,caption="|| 📸 تحولت إلى صورة؟����||", reply_to_message_id=m.id)
     os.remove(f"sticker.jpg")
  except Exception as er:
   m.edit_text(f"""⚠️ **خطأ**: يرجى استخدام هذا الأمر على الفيديو أو الملصق
 الأمر: ["تحويل إلى صورة"]-["tlpho"]""")
   
 

 elif text == "tlskr":
  try:
    down = app.download_media(m.reply_to_message)
    if down == None:
     m.edit_text(f"""⚠️ **خطأ**: الرجاء استخدام هذا الأمر على الصورة
 الأمر: [`تحويل إلى ملصق']-[`tlskr']""")
    else:
     os.rename(down ,'sticker.webp')
     app.send_sticker(m.chat.id , f"sticker.webp" , reply_to_message_id=m.id)
     os.remove(f"sticker.webp")
  except Exception as er:
   m.edit_text(f"""⚠️ **خطأ**: الرجاء استخدام هذا الأمر على الصورة
 الأمر: [`تحويل إلى ملصق']-[`tlskr']""")

 elif text == "تحويل إلى ملصق":
  try:
    down = app.download_media(m.reply_to_message)
    if down == None:
     m.edit_text(f"""⚠️ **خطأ**: الرجاء استخدام هذا الأمر على الصورة
 الأمر: [`تحويل إلى ملصق']-[`tlskr']""")
    else:
     os.rename(down ,'sticker.webp')
     app.send_sticker(m.chat.id , f"sticker.webp" , reply_to_message_id=m.id)
     os.remove(f"sticker.webp")
  except Exception as er:
   m.edit_text(f"""⚠️ **خطأ**: الرجاء استخدام هذا الأمر على الصورة
 الأمر: [`تحويل إلى ملصق']-[`tlskr']""")



 elif text == "tlgif":
  try:
    down = app.download_media(m.reply_to_message)
    if down == None:
     m.edit_text(f"""⚠️ **خطأ**: يرجى استخدام هذا الأمر على الصورة أو الفيديو
 الأمر: [`التحويل إلى gif`]-[`tlgif`]""")
    else:
     os.rename(down ,'animation.gif')
     app.send_animation(m.chat.id , f"animation.gif" , reply_to_message_id=m.id)
     os.remove(f"animation.gif")
  except Exception as er:
   m.edit_text(f"""⚠️ **خطأ**: يرجى استخدام هذا الأمر على الصورة أو الفيديو
 الأمر: [`التحويل إلى gif`]-[`tlgif`]""")

 elif text == "تحويل إلى GIF":
  try:
    down = app.download_media(m.reply_to_message)
    if down == None:
     m.edit_text(f"""⚠️ **خطأ**: يرجى استخدام هذا الأمر على الصورة أو الفيديو
 الأمر: [`التحويل إلى gif`]-[`tlgif`]""")
    else:
     os.rename(down ,'animation.gif')
     app.send_animation(m.chat.id , f"animation.gif" , reply_to_message_id=m.id)
     os.remove(f"animation.gif")
  except Exception as er:
   m.edit_text(f"""⚠️ **خطأ**: يرجى استخدام هذا الأمر على الصورة أو الفيديو
 الأمر: [`التحويل إلى gif`]-[`tlgif`]""")


 elif text.startswith("download"):
  i = 1
  url=(m.reply_to_message.text if m.reply_to_message else text.split()[1])
  try:
   if url.find('/'):
    filename=url.split('/')[-1]
    r = GET(url, allow_redirects=True , stream=True)
    total = int(r.headers.get('content-length'))
    app.edit_message_text(m.chat.id , m.id , f"""**Downloader**\n✿ الاسم: {filename}\n✿ المجلد: {total/1024/1024:.3f} ᴍʙ\n✿ الوقت: {datetime.now(timezone("Asia/Baghdad")) .strftime("%H:%M")}\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n✿ الرجاء الانتظار بينما أقوم بالتنزيل!  لا تعطي أي أوامر ✿""")
    with open(filename, 'wb') as file:
     for data in r.iter_content(chunk_size=1024):
      size = file.write(data)
    m.edit_text(f"""**Downloader**\n✿ الاسم : `{اسم الملف}`\n✿ الحجم : `{total/1024/1024:.3f} ᴍʙ`\n✿ الوقت : `{datetime. now(timezone("Asia/Baghdad")).strftime("%H:%M")}`\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n✿يرجى الانتظار أثناء التنزيل! لا تعطي أي أوامر ✿ \n الرجاء الانتظار بينما أقوم بالتحميل!""")
     app.send_document(m.chat.id , f"{filename}" , caption=f"""**تحميل**\n✿ الاسم: `{اسم الملف}`\n✿ الحجم: `{total/1024/1024 :.3f} ᴍʙ`\n✿ الوقت : `{datetime.now(timezone("Asia/Baghdad")).strftime("%H:%M")}`/n BotLevi""")
    app.delete_messages(m.chat.id , m.id)
    os.remove(filename)
  except:
   m.edit_text(f"✿ رابط التنزيل معطل!")
   
 elif text.startswith("تحميل"):
  i = 1
  url=(m.reply_to_message.text if m.reply_to_message else text.split()[1])
  try:
   if url.find('/'):
    filename=url.split('/')[-1]
    r = GET(url, allow_redirects=True , stream=True)
    total = int(r.headers.get('content-length'))
    app.edit_message_text(m.chat.id , m.id , f"""**أداة التنزيل**\n✿ الاسم: {اسم الملف}\n✿ المجلد: {total/1024/1024:.3f} ᴍʙ\n✿ الوقت: {datetime.now(timezone("Asia/Baghdad")).strftime( "%H:%M")}\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n✿ يرجى الانتظار بينما أقوم بالتنزيل!  لا تعطي أي أوامر""")
    with open(filename, 'wb') as file:
     for data in r.iter_content(chunk_size=1024):
      size = file.write(data)
    m.edit_text(f"""**Downloader**\n✿ الاسم : `{اسم الملف}`\n✿ الحجم : `{total/1024/1024:.3f} ᴍʙ`\n✿ الوقت : `{datetime. now(timezone("Asia/Baghdad")).strftime("%H:%M")}`\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n✿يرجى الانتظار أثناء التنزيل! لا تعطي أي أوامر ✿ \n الرجاء الانتظار بينما أقوم بالتحميل!""")
     app.send_document(m.chat.id , f"{filename}" , caption=f"""**تحميل**\n✿ الاسم: `{اسم الملف}`\n✿ الحجم: `{total/1024/1024 :.3f} ᴍʙ`\n✿ الوقت : `{datetime.now(timezone("Asia/Baghdad")).strftime("%H:%M")}`/n BotLevi""")
    app.delete_messages(m.chat.id , m.id)
    os.remove(filename)
  except:
   m.edit_text(f"✿ رابط التحميل معطل!")

 elif text.startswith("sticker"):
  try:
   im = Image.open(GET(f"http://www.flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=colgate-logo&&text={text.replace('sticker' , '')[1::]}&fontsize=100", stream=True).raw) 
   im.save('sticker.png')
   os.rename('sticker.png' ,'sticker.webp')
   app.send_sticker(m.chat.id , f"sticker.webp" , reply_to_message_id=m.id)
   os.remove(f"sticker.webp")
  except Exception as er:
   m.edit_text(f"خطأ: لقد قمت بوضع اسم أو .. أمام الملصق~الملصق")   

 elif text.startswith("ملصق"):
  try:
   im = Image.open(GET(f"http://www.flamingtext.com/net-fu/proxy_form.cgi?imageoutput=true&script=colgate-logo&&text={text.replace('ملصق' , '')[1::]}&fontsize=100", stream=True).raw) 
   im.save('sticker.png')
   os.rename('sticker.png' ,'sticker.webp')
   app.send_sticker(m.chat.id , f"sticker.webp" , reply_to_message_id=m.id)
   os.remove(f"sticker.webp")
  except Exception as er:
   m.edit_text(f"خطأ: لقد قمت بوضع اسم أو .. أمام الملصق~الملصق")   
 
 elif m.text == "time":
  try:
    for i in range(0,20):
      kir = datetime.now(timezone("Asia/Baghdad")).strftime("%H:%M:%S")
      app.edit_message_text(m.chat.id , m.id , f"**🌸Time:** `{kir}`")
      sleep(1)
  except Exception as er:
   m.edit_text(er)
 
 elif m.text == "الساعة":
  try:
    for i in range(0,20):
      kir = datetime.now(timezone("Asia/Baghdad")).strftime("%H:%M:%S")
      app.edit_message_text(m.chat.id , m.id , f"**🌸الساعة:** `{kir}`")
      sleep(1)
  except Exception as er:
   m.edit_text(er)

 elif text == "ping":
  try:
    up_a = (strftime('%H:%M:%S', gmtime(uptime())))
    svmem = virtual_memory()
    app.edit_message_text(m.chat.id , m.id , f"""
✅Online BotLevi
StArT BotLevi : `{up_a}`
NoSkHe SELF : `{Src_vrsion}`
""")
  except Exception as er:
   m.edit_text(er)

 elif text == "البنك (سرعة نت ضلعي)":
  try:
    up_a = (strftime('%H:%M:%S', gmtime(uptime())))
    svmem = virtual_memory()
    app.edit_message_text(m.chat.id , m.id , f"""
✅Online BotLevi
StArT BotLevi : `{up_a}`
NoSkHe SELF : `{Src_vrsion}`
""")
  except Exception as er:
   m.edit_text(er)
#c#
 elif text == "cpu":
  try:
    cpufreq = cpu_freq()
    app.edit_message_text(m.chat.id , m.id , f"""
✿ `CPU` ~  (`{cpu_percent()}%`)""")
  except Exception as er: 
   m.edit_text(er)
   #c#
 elif text == "help":
  try:
    app.edit_message_text(m.chat.id , m.id , f"""
**🧸 مرحبا بكم في قسم الدليل الذاتي 🧸**

 ✿ المدخلات:
 ........
 ``الإعدادات''
 ``الإعداد''
 ........
 ``قائمة المستخدم''
 ``مينوك''
 ........
 ``الترفيه''
 ""الألعاب""
 ........
``مودمونو''
  ``حالة القائمة''
  ........
  ""منجاب""
  ""حدوث ايجابي""
 ........

 ||  🩷 BY : @Q_B_H 🩷 ||
""")
  except Exception as er: 
   m.edit_text(er)
   
 elif text == ("مرشد"):
  try:
    app.edit_message_text(m.chat.id , m.id , f"""
**🧸 مرحبا بكم في قسم الدليل الذاتي 🧸**

 ✿ المدخلات:
 ........
 ``الإعدادات''
 ``الإعداد''
 ........
 ``قائمة المستخدم''
 ``مينوك''
 ........
 ``الترفيه''
 ""الألعاب""
 ........
 ``مودمونو''
 ``وضع القائمة''
 ........
 ``مينوجب''
 ``تحدث معي''
 ........

|| 🩷 by @Q_B_H 🩷 ||
""")
  except Exception as er: 
   m.edit_text(er)
   
 elif text == ("setting"):
  try:
    app.edit_message_text(m.chat.id , m.id , f"""
**مرحبًا بك في قسم إعدادات الصور الشخصية ⚙**
 "بينغ" |  ``البنك (سرعة الملاحظة الجانبية)''

 ``وحدة المعالجة المركزية''

 الإنجليزية "صوت" صوت المغير

 "file_info" لتحديد المواصفات.  .  .

 ``حالة_الإيقاف_الإيقاف''

 ||جميع اوامر  ☃️||

 ||  الصدرة 🚔||
""")
  except Exception as er: 
   m.edit_text(er)

 elif text == ("إعدادات"):
  try:
    app.edit_message_text(m.chat.id , m.id , f"""
**مرحبًا بك في قسم إعدادات الصور الشخصية ⚙**
 "بينغ" |  ``البنك (سرعة الملاحظة الجانبية)''

 ``وحدة المعالجة المركزية''

 الإنجليزية "صوت" صوت المغير

 "file_info" لتحديد المواصفات.  .  .

 ``حالة_الإيقاف_الإيقاف''

 ||جميع اوامر  ☃️||

 ||مالك بوتسورس 🚔||
""")
  except Exception as er: 
   m.edit_text(er)

 elif text == ("gaming"):
  try:
    app.edit_message_text(m.chat.id , m.id , f"""
**مرحبا بكم في قسم الترفيه الذاتي 🎪**

 ----------------------------
 النكتة وجانب الموظف بالمحطة 😂🩷:


 ----------------------------
 😂💋 المزاح مع الآخرين واستخدام:

 ``اللعنة'' |  ''اقتل الوغد''

 ``الحب1'' |  الحب1

 ``الحب |  حب

 ``ابدأ جغ'' |  ""يصرخ""

 ``إعادة التحميل'' [بدون أمر فارسي]
 ----------------------------
 [ملاحظة: لأداء كرة القدم، سجل 4 أهداف
 لا تدع الزهور تتقدم، الأمر 1]:
 ``كرة القدم'' |  ''كرة القدم''
 ----------------------------
 ``كرة السلة'' |  ''كرة السلة''
 ----------------------------
 ``البولينج'' |  ``البولينج''
 ----------------------------
 ``السهام'' |  سهم
 ----------------------------
 [ملاحظة: لتشغيل النرد عليك أن تضع أمامه الأرقام من 1 إلى 6 حتى يرمي لك هذا الرقم، مثلاً <النرد 1>]:
 ``تاس'' |  ``النرد''
 ----------------------------
 🖥 صنع الخطوط العربية والإنجليزية:

 ``الخط'' |  ``الخط الفارسي''
 ``الفونتن'' |  ``الخط الإنجليزي''
 ----------------------------
 [**ملاحظة مهمة:** هذا الأمر له جانب المروحة والنسخ / يأخذ هذا الأمر الصورة الشخصية للشخص الذي نستخدمه، ويضعها أمام الأمر، ويضعها في ملفك الشخصي واسم الطرف حساب وسيرة الحزب]:

 ``استنساخ'' |  ``حذف''

 ||  🩷تم انتهاء اوامر ||
""")
  except Exception as er: 
   m.edit_text(er)
   
 elif text == ("ترفيه"):
  try:
    app.edit_message_text(m.chat.id , m.id , f"""
**مرحبا بكم في قسم الترفيه الذاتي 🎪**

 ----------------------------
 النكتة وجانب الموظف بالمحطة 😂🩷:


 ----------------------------
 😂💋 المزاح مع الآخرين واستخدام:

 ``اللعنة'' |  ''اقتل الوغد''

 ``الحب1'' |  الحب1

 ``الحب |  حب

 ``ابدأ جغ'' |  ""يصرخ""

 ``إعادة التحميل'' [بدون أمر فارسي]
 ----------------------------
 [ملاحظة: لأداء كرة القدم، سجل 4 أهداف
 لا تدع الزهور تتقدم، الأمر 1]:
 ``كرة القدم'' |  ''كرة القدم''
 ----------------------------
 ``كرة السلة'' |  ''كرة السلة''
 ----------------------------
 ``البولينج'' |  ``البولينج''
 ----------------------------
 ``السهام'' |  سهم
 ----------------------------
 [ملاحظة: لتشغيل النرد عليك أن تضع أمامه الأرقام من 1 إلى 6 حتى يرمي لك هذا الرقم، مثلاً <النرد 1>]:
 ``تاس'' |  ``النرد''
 ----------------------------
 🖥 صنع الخطوط العربية والإنجليزية:

 ``الخط'' |  ``الخط الفارسي''
 ``الفونتن'' |  ``الخط الإنجليزي''
 ----------------------------
 [**ملاحظة مهمة:** هذا الأمر له جانب المروحة والنسخ / يأخذ هذا الأمر الصورة الشخصية للشخص الذي نستخدمه، ويضعها أمام الأمر، ويضعها في ملفك الشخصي واسم الطرف حساب وسيرة الحزب]:

 ``استنساخ'' |  ``حذف''

 ||  🩷تم انتهاء اوامر ||
""")
  except Exception as er: 
   m.edit_text(er)
   
 elif text == ("modmuno"):
  try:
    app.edit_message_text(m.chat.id , m.id , f"""
**مرحبًا بكم في قسم التعديل الخاص بي 🔋**

 ----------------------------
 كتابة أوضاع التشغيل، الإيقاف، ضع الأمر التالي:

 ``جريئة''

 "المفسد"

 ``مائل''

 ``الرمز''

 ""الإضراب""

 ``تسطير''

 ""الرموز التعبيرية""
 ----------------------------
 تعليمات الحساب:

 "تعيين الملف الشخصي" |  مجموعة الملف الشخصي

 `ديلبروفايل` |  ``إزالة ملف التعريف الخاص بك''

 "اسم المجموعة" |  ``تسجيل الاسم``

 ``ضبط الأعصم الثاني'' |  ``الترتيب العائلي``

 ``سيت bio'' |  ``تجميع السيرة الذاتية''

 الحصول على اسم الحساب الدقيق للآخرين باستخدام الأمر ~>

 اسم المستخدم ``youname'' أمام الأمر أو الرد.

 احفظ مقاطع الفيديو والصور الخاصة بالأشخاص الآخرين باستخدام المؤقت باستخدام الأمر ~>
 أعد تشغيل "bashe" على صورة أو مقطع فيديو باستخدام مؤقت.
 [ملاحظة: إذا كتبت أمر bash وأجاب **hom**، فلا توجد مشكلة، فهذا يعني أنك لم ترد أو تركت الأمر حرًا]

 يمكنك التحويل بالأوامر التالية:

 ``تلفو'' |  ``التحويل إلى الصورة''

 ``تلسكر'' |  ``تتحول إلى ملصق''

 ``تلغيف'' |  تحويل إلى GIF

 ⏰ الطلبات بالساعة في السيرة الذاتية للاسم:
 `1timename` <~ اسم الوقت واحد

 `2timename` <~ اسم الوقت الثاني

 `1مرة البيو سيدنة' <~زمن في سيرة أحد

 `2زمن البيو سيدنة' <~الزمن في سيرة إثنين

 `3زمن البيو سيدنا' <~الزمن في سيرة ثلاثة

 `!fontname` <~ اسم الخط التلقائي

 🔌 موظف:
 ``تنزيل'' |  ``تنزيل''

 [ملاحظة: للتحميل ضع رابط التحميل أمام أمر التحميل  تحميل]

 ``ملصق'' |  ""ملصق""

 [ملاحظة: لإنشاء ملصق، يكون الاسم موجودًا أمام أمر الملصق  ضع ملصق الاسم]

 ``الوقت'' |  ""الساعة""

 [ملاحظة: يتم احتساب 20 ثانية باستخدام أمر الوقت عبر الإنترنت]


 || تم انتهاء اوامر 🩵 ||
""")
  except Exception as er: 
   m.edit_text(er)

 elif text == ("وضع القائمة"):
  try:
    app.edit_message_text(m.chat.id , m.id , f"""
**مرحبًا بكم في قسم التعديل الخاص بي 🔋**

 ----------------------------
 كتابة أوضاع التشغيل، الإيقاف، ضع الأمر التالي:

 ``جريئة''

 "المفسد"

 ``مائل''

 ``الرمز''

 ""الإضراب""

 ``تسطير''

 ""الرموز التعبيرية""
 ----------------------------
 تعليمات الحساب:

 "تعيين الملف الشخصي" |  مجموعة الملف الشخصي

 `ديلبروفايل` |  ``إزالة ملف التعريف الخاص بك''

 "اسم المجموعة" |  ``تسجيل الاسم``

 ``ضبط الأعصم الثاني'' |  ``الترتيب العائلي``

 ``سيت bio'' |  ``تجميع السيرة الذاتية''

 الحصول على اسم الحساب الدقيق للآخرين باستخدام الأمر ~>

 اسم المستخدم ``youname'' أمام الأمر أو الرد.

 احفظ مقاطع الفيديو والصور الخاصة بالأشخاص الآخرين باستخدام المؤقت باستخدام الأمر ~>
 أعد تشغيل "bashe" على صورة أو مقطع فيديو باستخدام مؤقت.
 [ملاحظة: إذا كتبت أمر bash وأجاب **hom**، فلا توجد مشكلة، فهذا يعني أنك لم ترد أو تركت الأمر حرًا]

 يمكنك التحويل بالأوامر التالية:

 ``تلفو'' |  ``التحويل إلى الصورة''

 ``تلسكر'' |  ``تتحول إلى ملصق''

 ``تلغيف'' |  تحويل إلى GIF

 ⏰ الطلبات بالساعة في السيرة الذاتية للاسم:
 `1timename` <~ اسم الوقت واحد

 `2timename` <~ اسم الوقت الثاني

 `1مرة البيو سيدنة' <~زمن في سيرة أحد

 `2زمن البيو سيدنة' <~الزمن في سيرة إثنين

 `3زمن البيو سيدنا' <~الزمن في سيرة ثلاثة

 `!fontname` <~ اسم الخط التلقائي

 🔌 موظف:
 ``تنزيل'' |  ``تنزيل''

 [ملاحظة: للتحميل ضع رابط التحميل أمام أمر التحميل  تحميل]

 ``ملصق'' |  ""ملصق""

 [ملاحظة: لإنشاء ملصق، يكون الاسم موجودًا أمام أمر الملصق  ضع ملصق الاسم]

 ``الوقت'' |  ""الساعة""

 [ملاحظة: يتم احتساب 20 ثانية باستخدام أمر الوقت عبر الإنترنت]


 || تم انتهاء اوامر 🩵 ||
""")
  except Exception as er: 
   m.edit_text(er)

 elif text == ("تحدث معي"):
  try:
    app.edit_message_text(m.chat.id , m.id , f"""
** مرحبا بكم في الدردشة الذاتية 🎵 **

 "dellmsguser".

 [لحذف رسالة المستخدم بالكامل في الدردشة]

 |

 [لعمل مجموعة بسيطة من الأوامر]

 "إنشاء مجموعة".

 |

 ``إنشاء مجموعة خارقة''

 [لإنشاء مجموعة فائقة من الأمر]

 |

 [لعمل قناة خام من الأمر]

 "إنشاء قناة".

 |

 "تعيين اسم المستخدم".

 [يتم استخدامه لتغيير اسم مستخدم القناة والمجموعة  هذا الأمر لصاحب الدردشة أو القناة]

 |
 تثبيت رسالة ~> `دبوس`

 إزالة التثبيت ~> `إزالة التثبيت`

 قم بإزالة كافة الدبابيس ~> `unpinall`
 |
 لتغيير السيرة الذاتية للدردشة ~> `ستات البيو سيدنا'

 لتغيير اسم الدردشة ~> `setchatname`

 لتغيير اسم الدردشة ~> `setchatphoto`

 لحذف صورة الدردشة ~>`delchatphoto`

 |
 [أمر بحذف الرسائل التي يصل عددها إلى 1000 رقم في المقدمة]
 ``حذف''

 |
 معلومات المستخدم في الدردشة ~> `inf`
 |

 إسكات المستخدم ~> `كتم الصوت` |  ""الصمت""

 إزالة صمت المستخدم ~> `إلغاء كتم الصوت` |  ""القضاء على الصمت""

 قم بإزالة جميع عمليات كتم الصوت ~> ``allunmute``
 |
 مرحباً بك
 "مرحبا" باللغة الإنجليزية

 العربية "مرحبا"

 |
 استخدم الأوامر التالية لحذفها وإلغاء ربطها ~>
 ""الحظر""

 ``غير الحظر``
 |
 عدد مسؤولي المجموعة ~>
 ``تدمين''

 || تم انتهاء اوامر ❄️ ||
""")
  except Exception as er: 
   m.edit_text(er)
   
 elif text == ("menogp"):
  try:
    app.edit_message_text(m.chat.id , m.id , f"""
** مرحبا بكم في الدردشة الذاتية 🎵 **

 "dellmsguser".

 [لحذف رسالة المستخدم بالكامل في الدردشة]

 |

 [لعمل مجموعة بسيطة من الأوامر]

 "إنشاء مجموعة".

 |

 ``إنشاء مجموعة خارقة''

 [لإنشاء مجموعة فائقة من الأمر]

 |

 [لعمل قناة خام من الأمر]

 "إنشاء قناة".

 |

 "تعيين اسم المستخدم".

 [يتم استخدامه لتغيير اسم مستخدم القناة والمجموعة  هذا الأمر لصاحب الدردشة أو القناة]

 |
 تثبيت رسالة ~> `دبوس`

 إزالة التثبيت ~> `إزالة التثبيت`

 قم بإزالة كافة الدبابيس ~> `unpinall`
 |
 لتغيير السيرة الذاتية للدردشة ~> `ستات البيو سيدنا'

 لتغيير اسم الدردشة ~> `setchatname`

 لتغيير اسم الدردشة ~> `setchatphoto`

 لحذف صورة الدردشة ~>`delchatphoto`

 |
 [أمر بحذف الرسائل التي يصل عددها إلى 1000 رقم في المقدمة]
 ``حذف''

 |
 معلومات المستخدم في الدردشة ~> `inf`
 |

 إسكات المستخدم ~> `كتم الصوت` |  ""الصمت""

 إزالة صمت المستخدم ~> `إلغاء كتم الصوت` |  ""القضاء على الصمت""

 قم بإزالة جميع عمليات كتم الصوت ~> ``allunmute``
 |
 مرحباً بك
 "مرحبا" باللغة الإنجليزية

 العربية "مرحبا"

 |
 استخدم الأوامر التالية لحذفها وإلغاء ربطها ~>
 ""الحظر""

 ``غير الحظر``
 |
 عدد مسؤولي المجموعة ~>
 ``تدمين''


 || تم انتهاء اوامر ❄️ ||
""")
  except Exception as er: 
   m.edit_text(er)

 elif text == ("قائمة المستخدم"):
  try:
    app.edit_message_text(m.chat.id , m.id , f"""
*مرحبًا بكم في قائمة العاملين لحسابهم الخاص 💣*

 ✿ ``كتلة''

 [أمام الأمر، أدخل الرقم التعريفي أو اسم المستخدم الخاص بالطرف أو قم بالرد ليتم حظره تلقائيًا.]

 ✿ ``إلغاء الحظر''

 [أمام الأمر، أدخل معرفًا رقميًا أو اسم المستخدم أو قم بالرد ليتم إلغاء حظره تلقائيًا.]
 ..............................
 ✿ "يسار"

 [للحصول على دور علوي من قناة أو مجموعة عامة، ضع المعرف أمام الأمر أعلاه لإعطاء دور علوي]
 ✿ "الانضمام"

 [للانضمام إلى القناة أو المجموعة العامة ضع المعرف أمام الأمر أعلاه لتصبح عضوا]
 ..............................
 ``الملكية الفكرية''
 ~> للحصول على IP الخاص بالموقع، ضع رابط الموقع أمام الأمر

 ``الويسيب''

 [باستخدام الأمر أعلاه، يمكنك الحصول على معلومات IP، على سبيل المثال، ضع 185.88.181.58 أمام الأمر وشاهد معلوماته لتتعلم]
 ..............................
 ``معرف'' |  ``المعرف``

 [الرجاء الرد على المستخدم أو وضع المعرف أمام الأمر]
 ..............................
 ``الكل'' |  ``إزالة الأعداء''

 [الرجاء الرد على المستخدم أو وضع المعرف أمام الأمر]
 ``حذف الضحية'' |  ``إزالة الضحية''

 ``سيتينيمي'' |  ``إعداد الضحية''
 ..............................
 ""الصوت""

 [يرجى كتابة الكلمات الإنجليزية قبل الأمر، فهو لا يدعم الكلمات العربية]
 ..............................
 `emoji` => `لا` ° `إيقاف`

 `emojig` => `no` ° `إيقاف`

 ||جميع اوامر  🤎||
""")
  except Exception as er: 
   m.edit_text(er)
   
 elif text == ("menok"):
  try:
    app.edit_message_text(m.chat.id , m.id , f"""
*مرحبًا بكم في قائمة العاملين لحسابهم الخاص 💣*

 ✿ ``كتلة''

 [أمام الأمر، أدخل الرقم التعريفي أو اسم المستخدم الخاص بالطرف أو قم بالرد ليتم حظره تلقائيًا.]

 ✿ ``إلغاء الحظر''

 [أمام الأمر، أدخل معرفًا رقميًا أو اسم المستخدم أو قم بالرد ليتم إلغاء حظره تلقائيًا.]
 ..............................
 ✿ "يسار"

 [للحصول على دور علوي من قناة أو مجموعة عامة، ضع المعرف أمام الأمر أعلاه لإعطاء دور علوي]
 ✿ "الانضمام"

 [للانضمام إلى القناة أو المجموعة العامة ضع المعرف أمام الأمر أعلاه لتصبح عضوا]
 ..............................
 ``الملكية الفكرية''
 ~> للحصول على IP الخاص بالموقع، ضع رابط الموقع أمام الأمر

 ``الويسيب''

 [باستخدام الأمر أعلاه، يمكنك الحصول على معلومات IP، على سبيل المثال، ضع 185.88.181.58 أمام الأمر وشاهد معلوماته لتتعلم]
 ..............................
 ``معرف'' |  ``المعرف``

 [الرجاء الرد على المستخدم أو وضع المعرف أمام الأمر]
 ..............................
 ``الكل'' |  ``إزالة الأعداء''
 ``كل الحب'' |  ""إزالة الحب""

 [الرجاء الرد على المستخدم أو وضع المعرف أمام الأمر]
 ``حذف الضحية'' |  ``إزالة الضحية''

 ``سيتينيمي'' |  ``إعداد الضحية''

 ``ضبط الحب'' |  ``ضبط الحب''

 ``حذف الحب'' |  ""إزالة الحب""
 ..............................
 ""الصوت""

 [يرجى كتابة الكلمات الإنجليزية قبل الأمر، فهو لا يدعم الكلمات العربية]
 ..............................
 `.emojib` => `no` ° `إيقاف`

 `.emojig` => `no` ° `إيقاف`

 ||جميع اوامر  🤎||
""")
  except Exception as er: 
   m.edit_text(er)
   

 elif text.startswith("voice"):
  try:
   audio = gTTS(text=text.replace("voice","")[1::] , lang='en')
   audio.save("voice.ogg")
   app.send_audio(m.chat.id , "voice.ogg")
   app.delete_messages(m.chat.id , m.id)
   os.remove(f"voice.ogg")
  except Exception as er:
   m.edit_text(f"الرجاء استخدام الكلمات الإنجليزية، العربية غير مسموح بها")   
   
   

 elif text.startswith("delete"):
   mmd = app.get_chat_member(m.chat.id, "me")
   rasi = dast_del(text=mmd)
   if rasi:
     try:
       reu = int(text.replace("delete",""))
       if type(reu) == int:
         kalc = 0
         for m in app.get_chat_history(m.chat.id):
            if reu != kalc:
              m.delete(revoke=True)
              kalc += 1
            else:
              break
         m.reply(f"🍒 **بنجاح** `{kalc}` **تم مسح الرسالة في قناتك أو مجموعتك** ", quote=False)
       else:
         m.reply("الرجاء إدخال رقم يصل إلى 1000")
      except Exception as er:
        app.send_message(m.chat.id , f"❋ **خطأ** :\n(`{er}`)")
    else:
      m.reply("موضعك هنا لا يكفي لحذف رسائل الآخرين، من فضلك اطلب أن تصبح مشرفًا")

 elif text.startswith("file_info"):
  getcontext().prec = 3
  try:
   if m.reply_to_message.document: 
     m.edit_text(f"""❋ الاسم ⤳ (`{m.reply_to_message.document.file_name}`)
 ❋ اكتب ⤳ (`{m.reply_to_message.document.mime_type}`)
 ❋ حجم الملف ⤳ ((`{Decimal(int(m.reply_to_message.document.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
 ❋ التاريخ ⤳ (`{m.reply_to_message.document.date}`)
 ❋ معرف الملف ⤳ (`{m.reply_to_message.document.file_id}`)""")
    elif m.reply_to_message.photo: 
      m.edit_text(f"""❋ الحجم ⤳ (`{m.reply_to_message.photo.width}×{m.reply_to_message.photo.height}`)
 ❋ حجم الملف ⤳ ((`{Decimal(int(m.reply_to_message.photo.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
 ❋ التاريخ ⤳ (`{m.reply_to_message.photo.date}`)
 ❋ معرف الملف ⤳ (`{m.reply_to_message.photo.file_id}`)""")
    elif m.reply_to_message.video: 
      m.edit_text(f"""❋ النوع ⤳ (`{m.reply_to_message.video.mime_type}`)
 ❋ الحجم ⤳ (`{m.reply_to_message.video.width}×{m.reply_to_message.video.height}`)
 ❋ المدة ⤳ (`{m.reply_to_message.video.duration}s`)
 ❋ حجم الملف ⤳ ((`{Decimal(int(m.reply_to_message.video.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
 ❋ التاريخ ⤳ (`{m.reply_to_message.video.date}`)
 ❋ دعم البث ⤳ (`{m.reply_to_message.video.supports_streaming}`)
 ❋ معرف الملف ⤳ (`{m.reply_to_message.video.file_id}`)""")
    elif m.reply_to_message.animation: 
      m.edit_text(f"""❋ الحجم ⤳ (`{m.reply_to_message.animation.width}×{m.reply_to_message.animation.height}`)
 ❋ اكتب ⤳ (`{m.reply_to_message.animation.mime_type}`)
 ❋ حجم الملف ⤳ ((`{Decimal(int(m.reply_to_message.animation.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
 ❋ المدة ⤳ (`{m.reply_to_message.animation.duration}s`)
 ❋ التاريخ ⤳ (`{m.reply_to_message.animation.date}`)
 ❋ معرف الملف ⤳ (`{m.reply_to_message.animation.file_id}`)""")
    elif m.reply_to_message.sticker: 
      m.edit_text(f"""❋ الحجم ⤳ (`{m.reply_to_message.sticker.width}×{m.reply_to_message.sticker.height}`)
 ❋ الاسم ⤳ (`{m.reply_to_message.sticker.file_name}`)
 ❋ اكتب ⤳ (`{m.reply_to_message.sticker.mime_type}`)
 ❋ حجم الملف ⤳ ((`{Decimal(int(m.reply_to_message.sticker.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
 ❋ الرموز التعبيرية ⤳ (`{m.reply_to_message.sticker.emoji}`)
 ❋ رسوم متحركة ⤳ (`{m.reply_to_message.sticker.is_animated}`)
 ❋ هو الفيديو ⤳ (`{m.reply_to_message.sticker.is_video}`)
 ❋ مجموعة الملصقات ⤳ (`{"https://t.me/addstickers/"+m.reply_to_message.sticker.set_name if m.reply_to_message.sticker.set_name else "-"}`)
 ❋ التاريخ ⤳ (`{m.reply_to_message.sticker.date}`)
 ❋ معرف الملف ⤳ (`{m.reply_to_message.sticker.file_id}`)""")
    elif m.reply_to_message.voice: 
      m.edit_text(f"""❋ النوع ⤳ (`{m.reply_to_message.voice.mime_type}`)
 ❋ حجم الملف ⤳ ((`{Decimal(int(m.reply_to_message.voice.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
 ❋ المدة ⤳ (`{m.reply_to_message.voice.duration}s`)
 ❋ التاريخ ⤳ (`{m.reply_to_message.voice.date}`)
 ❋ معرف الملف ⤳ (`{m.reply_to_message.voice.file_id}`)""")
    elif m.reply_to_message.audio: 
      m.edit_text(f"""❋ العنوان ⤳ (`{m.reply_to_message.audio.title}`)
 ❋ المؤدي ⤳ (`{m.reply_to_message.audio.performer}`)
 ❋ اكتب ⤳ (`{m.reply_to_message.audio.mime_type}`)
 ❋ اسم الملف ⤳ (`{m.reply_to_message.audio.file_name}`)
 ❋ حجم الملف ⤳ ((`{Decimal(int(m.reply_to_message.audio.file_size))/Decimal(1024)/Decimal(1024)}ᴍʙ`)
 ❋ المدة ⤳ (`{m.reply_to_message.audio.duration}s`)
 ❋ التاريخ ⤳ (`{m.reply_to_message.audio.date}`)
 ❋ معرف الملف ⤳ (`{m.reply_to_message.audio.file_id}`)""")
   elif m.reply_to_message.text: 
     m.edit_text(f"**Please Reply To A Media/file**")
  except Exception as er:
   m.edit_text(er)

 elif text == "tadmin":
  try:
     b = "❋ **المشرفين** :\n\n"
     c = 1;k = 0
     a = app.get_chat_members(m.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS)
     for i in a:
        if i.user.is_deleted == False:
          b += "☐"+str(c)+" ↬ °"+(i.user.mention if i.user.id else "--")+"°\n"
          c += 1
        else:
          k += 1
     if k != 0:
       b += f"☐ **Deleted Account Admin** : `{k}`\n└— **Count** : `{k + c - 1}`"
     else:
       b += f" ☐  \n **رقم : ** : `{k + c - 1}`"
     m.reply(b)
  except Exception as er:
   m.edit_text(f"❋ **error** :\n(`{er}`)")

 elif text.startswith("inf"):
  if text.split()[1] == "@this":
    user = m.chat.id
  else:
    user = text.split()[1]
  user = app.get_chat(user)
  try:
   if user.photo:
     down = app.download_media(user.photo.big_file_id)
     app.send_photo(m.chat.id , down , f"""info 

✿ **Title** : `{user.title}`
✿ **ID** : `{user.id}`
✿ **Username** : `@{user.username if user.username else '--'}`
✿ **Members** : `{user.members_count}`
✿ **Dc ID** : `{user.dc_id}`
✿ **Is Creator** : `{user.is_creator}`
✿ **Is Verified** : `{user.is_verified}`
✿ **Is Restricted** : `{user.is_restricted}`
✿ **Is Scam** : `{user.is_scam}`
✿ **Is Fake** : `{user.is_fake}`
✿ **Sticker Set** : `{"https://t.me/addstickers/"+user.sticker_set_name if user.sticker_set_name else "--"}`
✿ **Description** : `{user.description}`""", reply_to_message_id=m.id)
     os.remove(down)
   else:
     app.send_message(m.chat.id , f"""||معلومات الحساب||

 ✿ **العنوان** : `{user.title}`
 ✿ **المعرف** : `{user.id}`
 ✿ **اسم المستخدم** : `@{user.username if user.username else '--'}`
 ✿ **الأعضاء** : `{user.members_count}`
 ✿ **معرف Dc** : `{user.dc_id}`
 ✿ **هو الخالق** : `{user.is_creator}`
 ✿ **تم التحقق** : `{user.is_verified}`
 ✿ **مقيد** : `{user.is_restricted}`
 ✿ **عملية احتيال** : `{user.is_scam}`
 ✿ **مزيف** : `{user.is_fake}`
 ✿ **مجموعة الملصقات** : `{"https://t.me/addstickers/"+user.sticker_set_name if user.sticker_set_name else "--"}`
 ✿ **الوصف**`{user.description}`""", reply_to_message_id=m.id)
  except Exception as er:
   m.edit_text(f"يرجى وضع المستخدم أولا")

 elif text.startswith("id"):
  try:
   user_id_get = (m.reply_to_message.from_user.id if m.reply_to_message else app.get_users(text.split()[1]).id)
   user = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(user_id_get)))
   count_photo = app.get_chat_photos_count(user_id_get)
   kiri = app.get_users(user_id_get)
   if kiri.photo:
     down = app.download_media(kiri.photo.big_file_id)
     app.send_photo(m.chat.id , down , f"""__User info__

❋ **Name** : `{user.users[0].first_name if user.users[0].first_name else "--"}`
❋ **الاسم الثاني** : `{user.users[0].last_name if user.users[0].last_name else "--"}`
❋ **Id** : `{user.users[0].id if user.users[0].id else "--"}`
❋ **Username** : `@{user.users[0].username if user.users[0].username else "--"}`
❋ **Profile Picture Count** : `{count_photo}`
❋ **Common Chats Count** : `{user.full_user.common_chats_count if user.full_user.common_chats_count else "0"}`
❋ **bio** : `{user.full_user.about if user.full_user.about else "--"}`
❋ **Scam** : `{user.users[0].scam}`
❋ **Can pin message** : `{user.full_user.can_pin_message}`
❋ **Contact** : `{user.users[0].contact}`
❋ **Bot** : `{user.users[0].bot}`
❋ **Verified** : `{user.users[0].verified}`
❋ **Deleted** : `{user.users[0].deleted}`
❋ **Phone Calls Available** : `{user.full_user.phone_calls_available}`
❋ **Phone Calls Private** : `{user.full_user.phone_calls_private}`
❋ **Video Calls Available** : `{user.full_user.video_calls_available}`
❋ **Access hash** : `{user.users[0].access_hash}`
❋ **Blocked** : `{user.full_user.blocked}`
`{f"❋ **Current ChatID**: {m.chat.id}" if m.chat.id != user.users[0].id else ""}`""" , reply_to_message_id=m.id)
   else:
     app.send_message(m.chat.id , f"""__معلومات المستخدم__

 ❋ **Name** : `{user.users[0].first_name if user.users[0].first_name else "--"}`
 ❋ **الثاني ** : `{user.users[0].last_name if user.users[0].last_name else "--"}`
 ❋ **المعرف** : `{user.users[0].id if user.users[0].id else "--"}`
 ❋ **اسم المستخدم** : `@{user.users[0].username if user.users[0].username else "--"}`
 ❋ **عدد صور الملف الشخصي** : `{count_photo}`
 ❋ **عدد الدردشات الشائعة** : `{user.full_user.common_chats_count if user.full_user.common_chats_count else "0"}`
 ❋ **bio** : `{user.full_user.about if user.full_user.about else "--"}`
 ❋ **احتيال** : `{user.users[0].scam}`
 ❋ **يمكن تثبيت الرسالة** : `{user.full_user.can_pin_message}`
 ❋ **جهة الاتصال** : `{user.users[0].contact}`
 ❋ **البوت** : `{user.users[0].bot}`
 ❋ **تم التحقق** : `{user.users[0].verified}`
 ❋ **Deleted** : `{user.users[0].deleted}`
 ❋ **المكالمات الهاتفية متاحة** : `{user.full_user.phone_calls_available}`
 ❋ **المكالمات الهاتفية الخاصة** : `{user.full_user.phone_calls_private}`
 ❋ **مكالمات الفيديو متاحة** : `{user.full_user.video_calls_available}`
 ❋ **تجزئة الوصول** : `{user.users[0].access_hash}`
 ❋ **محظور** : `{user.full_user.blocked}`
`{f"❋ **Current ChatID**: {m.chat.id}" if m.chat.id != user.users[0].id else ""}`""" , reply_to_message_id=m.id)
   os.remove(down)
  except errors.exceptions.bad_request_400.UsernameNotOccupied:
   app.send_message(m.chat.id , f"المستخدم نصف مخطئ")
  except Exception as er:
   m.edit_text(f"الرجاء الرد بشكل صحيح أو وضع المعرف أو المستخدم أمام الأمر")

 elif text.startswith("ايدي"):
  try:
   user_id_get = (m.reply_to_message.from_user.id if m.reply_to_message else app.get_users(text.split()[1]).id)
   user = app.invoke(functions.users.GetFullUser(id=app.resolve_peer(user_id_get)))
   count_photo = app.get_chat_photos_count(user_id_get)
   kiri = app.get_users(user_id_get)
   if kiri.photo:
     down = app.download_media(kiri.photo.big_file_id)
     app.send_photo(m.chat.id , down , f"""__User info__

❋ **Name** : `{user.users[0].first_name if user.users[0].first_name else "--"}`
❋ **الاسم الثاني** : `{user.users[0].last_name if user.users[0].last_name else "--"}`
❋ **Id** : `{user.users[0].id if user.users[0].id else "--"}`
❋ **Username** : `@{user.users[0].username if user.users[0].username else "--"}`
❋ **Profile Picture Count** : `{count_photo}`
❋ **Common Chats Count** : `{user.full_user.common_chats_count if user.full_user.common_chats_count else "0"}`
❋ **bio** : `{user.full_user.about if user.full_user.about else "--"}`
❋ **Scam** : `{user.users[0].scam}`
❋ **Can pin message** : `{user.full_user.can_pin_message}`
❋ **Contact** : `{user.users[0].contact}`
❋ **Bot** : `{user.users[0].bot}`
❋ **Verified** : `{user.users[0].verified}`
❋ **Deleted** : `{user.users[0].deleted}`
❋ **Phone Calls Available** : `{user.full_user.phone_calls_available}`
❋ **Phone Calls Private** : `{user.full_user.phone_calls_private}`
❋ **Video Calls Available** : `{user.full_user.video_calls_available}`
❋ **Access hash** : `{user.users[0].access_hash}`
❋ **Blocked** : `{user.full_user.blocked}`
`{f"❋ **Current ChatID**: {m.chat.id}" if m.chat.id != user.users[0].id else ""}`""" , reply_to_message_id=m.id)
   else:
     app.send_message(m.chat.id , f"""__معلومات المستخدم__

 ❋ **Name** : `{user.users[0].first_name if user.users[0].first_name else "--"}`
 ❋ **الثاني ** : `{user.users[0].last_name if user.users[0].last_name else "--"}`
 ❋ **المعرف** : `{user.users[0].id if user.users[0].id else "--"}`
 ❋ **اسم المستخدم** : `@{user.users[0].username if user.users[0].username else "--"}`
 ❋ **عدد صور الملف الشخصي** : `{count_photo}`
 ❋ **عدد الدردشات الشائعة** : `{user.full_user.common_chats_count if user.full_user.common_chats_count else "0"}`
 ❋ **bio** : `{user.full_user.about if user.full_user.about else "--"}`
 ❋ **احتيال** : `{user.users[0].scam}`
 ❋ **يمكن تثبيت الرسالة** : `{user.full_user.can_pin_message}`
 ❋ **جهة الاتصال** : `{user.users[0].contact}`
 ❋ **البوت** : `{user.users[0].bot}`
 ❋ **تم التحقق** : `{user.users[0].verified}`
 ❋ **Deleted** : `{user.users[0].deleted}`
 ❋ **المكالمات الهاتفية متاحة** : `{user.full_user.phone_calls_available}`
 ❋ **المكالمات الهاتفية الخاصة** : `{user.full_user.phone_calls_private}`
 ❋ **مكالمات الفيديو متاحة** : `{user.full_user.video_calls_available}`
 ❋ **تجزئة الوصول** : `{user.users[0].access_hash}`
 ❋ **محظور** : `{user.full_user.blocked}`
 `{f"❋ **معرف الدردشة الحالي**: {m.chat.id}" if m.chat.id != user.users[0].id else ""}`""" , reply_to_message_id=m.id)
   os.remove(down)
  except errors.exceptions.bad_request_400.UsernameNotOccupied:
   app.send_message(m.chat.id , f"المستخدم نصف مخطئ")
  except Exception as er:
   m.edit_text(f"الرجاء الرد بشكل صحيح أو وضع المعرف أو المستخدم أمام الأمر")

 elif text.startswith("setenemy"):
  try:
   if m.reply_to_message:
    if m.reply_to_message.from_user.id not in enemy:
     if m.reply_to_message.from_user.id != app.get_me().id:
      enemy.append(m.reply_to_message.from_user.id)
      app.edit_message_text(m.chat.id , m.id , f'✿ تمت إضافة {m.reply_to_message.from_user.mention} إلى قائمة الكراهية')
     else:
      app.edit_message_text(m.chat.id , m.id , f'✿ هذا المستخدم {m.reply_to_message.from_user.mention} كان موجودًا بالفعل في قائمة الأعداء')
   else :
    if app.get_users(text.split()[1]).id not in enemy :
     if app.get_users(text.split()[1]).id != app.get_me().id:
      enemy.append(app.get_users(text.split()[1]).id)
      app.edit_message_text(m.chat.id , m.id , f'😔🩵 <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app تمت إضافة .get_users(text.split()[1]).first_name</a> إلى قائمة الأنمي')
     else:
      app.edit_message_text(m.chat.id , m.id , f'😔🩵 هذا المعرف<a href=tg://user?id={app.get_users(text.split()[1]).id}> {app.get_users(text.split()[1]).first_name</a> كان موجودًا بالفعل في قائمة الأعداء')
   except Exception as er:
    m.edit_text(f"الرجاء إدخال معرف رقمي أو اسم مستخدم أو الرد")

  elif text.startswith("تعيين الضحية"):
  try:
   if m.reply_to_message:
    if m.reply_to_message.from_user.id not in enemy:
     if m.reply_to_message.from_user.id != app.get_me().id:
      enemy.append(m.reply_to_message.from_user.id)
      app.edit_message_text(m.chat.id , m.id , f'✿ تمت إضافة {m.reply_to_message.from_user.mention} إلى قائمة الأعداء')
     else:
      app.edit_message_text(m.chat.id , m.id , f'✿ هذا المستخدم {m.reply_to_message.from_user.mention} كان موجودًا بالفعل في قائمة الأعداء')
   else :
    if app.get_users(text.split()[1]).id not in enemy :
     if app.get_users(text.split()[1]).id != app.get_me().id:
      enemy.append(app.get_users(text.split()[1]).id)
      app.edit_message_text(m.chat.id , m.id , f'😔🩵 <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app.get_users(text.split()[1]).first_name </a> تمت إضافته إلى قائمة الأنمي')
     else:
      app.edit_message_text(m.chat.id , m.id , f'😔🩵 هذا المعرف<a href=tg://user?id={app.get_users(text.split()[1]).id}> {app.get_users(text.split()[1]).first_name</a> كان موجودًا بالفعل في قائمة الأعداء')
   except Exception as er:
    m.edit_text(f"الرجاء إدخال معرف رقمي أو اسم مستخدم أو الرد")

 elif text.startswith("delenemy"):
  try:
   if m.reply_to_message:
    if m.reply_to_message.from_user.id in enemy:
     enemy.remove(m.reply_to_message.from_user.id)
     app.edit_message_text(m.chat.id, m.id, f'🤍 تمت إزالة هذا المستخدم {m.reply_to_message.from_user.mention} من قائمة الأنمي')
     else:
      app.edit_message_text(m.chat.id, m.id, f'🤍 هذا المستخدم {m.reply_to_message.from_user.mention} غير موجود في قائمة الأعداء')
    else
     if app.get_users(text.split()[1]).id in enemy :
     enemy.remove(app.get_users(text.split()[1]).id)
      app.edit_message_text(m.chat.id , m.id , f'🩷هذا المستخدم <a href=tg://user?id={app.get_users(text.split()[1]).id}>{ app.get_users(text.split()[1]).first_name</a> تم حذف السمة بنجاح')
     else:
      app.edit_message_text(m.chat.id , m.id , f'🩷هذا المستخدم<a href=tg://user?id={app.get_users(text.split()[1]).id}>{ app.get_users(text.split()[1]).first_name</a> غير موجود في قائمة enami     ')
   except Exception as er:
    m.edit_text(f"الرجاء إدخال معرف رقمي أو اسم مستخدم أو الرد")

  elif text.startswith("إزالة الضحية"):
  try:
   if m.reply_to_message:
    if m.reply_to_message.from_user.id in enemy:
     enemy.remove(m.reply_to_message.from_user.id)
     app.edit_message_text(m.chat.id, m.id, f'🤍 تمت إزالة هذا المستخدم {m.reply_to_message.from_user.mention} من قائمة الأنمي')
     else:
      app.edit_message_text(m.chat.id, m.id, f'🤍 هذا المستخدم {m.reply_to_message.from_user.mention} غير موجود في قائمة الأعداء')
   else :
    if app.get_users(text.split()[1]).id in enemy :
     enemy.remove(app.get_users(text.split()[1]).id)
     app.edit_message_text(m.chat.id , m.id , f'🩷هذا المستخدم <a href=tg://user?id={app.get_users(text.split()[1]).id}>{ app.get_users(text.split()[1]).first_name</a> تم حذف السمة بنجاح')
     else:
      app.edit_message_text(m.chat.id , m.id , f'🩷هذا المستخدم<a href=tg://user?id={app.get_users(text.split()[1]).id}>{ app.get_users(text.split()[1]).first_name</a> غير موجود في قائمة enami     ')
  except Exception as er:
   m.edit_text(f"الرجاء إدخال معرف رقمي أو اسم مستخدم أو الرد")

 elif text.startswith("mute"):
  try:
   if m.reply_to_message:
    if m.reply_to_message.from_user.id not in mutey:
     if m.reply_to_message.from_user.id != app.get_me().id:
      mutey.append(m.reply_to_message.from_user.id)
      app.edit_message_text(m.chat.id , m.id , f'✿ تم إسكات المستخدم {m.reply_to_message.from_user.mention} بنجاح')
     else:
      app.edit_message_text(m.chat.id , m.id , f'✿ المستخدم {m.reply_to_message.from_user.mention} موجود في القائمة الصامتة')
   else :
    if app.get_users(text.split()[1]).id not in mutey :
     if app.get_users(text.split()[1]).id != app.get_me().id:
      mutey.append(app.get_users(text.split()[1]).id)
      app.edit_message_text(m.chat.id , m.id , f'✿ user <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app تم إسكات .get_users(text.split()[1]).first_name</a> بنجاح')
     else:
      app.edit_message_text(m.chat.id , m.id , f'✿ user <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app .get_users(text.split()[1]).first_name</a> ليسوا في قائمة الصمت')
   except Exception as er:
    m.edit_text(f"الرجاء الرد على المستخدم أو وضع معرف رقمي قبل الأمر أو اسم المستخدم قبل الأمر")

  elif text.startswith("الصمت"):
  try:
   if m.reply_to_message:
    if m.reply_to_message.from_user.id not in mutey:
     if m.reply_to_message.from_user.id != app.get_me().id:
      mutey.append(m.reply_to_message.from_user.id)
      app.edit_message_text(m.chat.id , m.id , f'✿ تم إسكات المستخدم {m.reply_to_message.from_user.mention} بنجاح')
     else:
      app.edit_message_text(m.chat.id , m.id , f'✿ المستخدم {m.reply_to_message.from_user.mention} موجود في القائمة الصامتة')
   else :
    if app.get_users(text.split()[1]).id not in mutey :
     if app.get_users(text.split()[1]).id != app.get_me().id:
      mutey.append(app.get_users(text.split()[1]).id)
      app.edit_message_text(m.chat.id , m.id , f'✿ user <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app تم إسكات .get_users(text.split()[1]).first_name</a> بنجاح')
     else:
      app.edit_message_text(m.chat.id , m.id , f'✿ user <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app .get_users(text.split()[1]).first_name</a> موجود في قائمة الصمت')
   except Exception as er:
    m.edit_text(f"الرجاء الرد على المستخدم أو وضع معرف رقمي قبل الأمر أو اسم المستخدم قبل الأمر")


 elif text.startswith("unmute"):
  try:
   if m.reply_to_message:
    if m.reply_to_message.from_user.id in mutey:
     mutey.remove(m.reply_to_message.from_user.id)
     app.edit_message_text(m.chat.id, m.id, f'✿ المستخدم {m.reply_to_message.from_user.mention} خرج من حالة الصمت')
     else:
      app.edit_message_text(m.chat.id, m.id, f'✿ المستخدم {m.reply_to_message.from_user.mention} غير موجود في قائمة الصمت')
   else :
    if app.get_users(text.split()[1]).id in mutey :
     mutey.remove(app.get_users(text.split()[1]).id)
     app.edit_message_text(m.chat.id , m.id , f'✿ user <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app .get_users(text.split()[1]).first_name</a> خرج من حالة الصمت')
     else:
      app.edit_message_text(m.chat.id , m.id , f'✿ user <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app .get_users(text.split()[1]).first_name</a> غير موجود في قائمة الصمت')
   except Exception as er:
    m.edit_text(f"الرجاء الرد على المستخدم أو وضع معرف رقمي قبل الأمر أو اسم المستخدم قبل الأمر")

  elif text.startswith("إزالة الصمت"):
  try:
   if m.reply_to_message:
    if m.reply_to_message.from_user.id in mutey:
     mutey.remove(m.reply_to_message.from_user.id)
     app.edit_message_text(m.chat.id, m.id, f'✿ المستخدم {m.reply_to_message.from_user.mention} خرج من حالة الصمت')
     else:
      app.edit_message_text(m.chat.id, m.id, f'✿ المستخدم {m.reply_to_message.from_user.mention} غير موجود في قائمة الصمت')
   else :
    if app.get_users(text.split()[1]).id in mutey :
     mutey.remove(app.get_users(text.split()[1]).id)
     app.edit_message_text(m.chat.id , m.id , f'✿ user <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app .get_users(text.split()[1]).first_name</a> خرج من حالة الصمت')
     else:
      app.edit_message_text(m.chat.id , m.id , f'✿ user <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app .get_users(text.split()[1]).first_name</a> غير موجود في قائمة الصمت')
   except Exception as er:
    m.edit_text(f"الرجاء الرد على المستخدم أو وضع معرف رقمي قبل الأمر أو اسم المستخدم قبل الأمر")

 elif text == "allf":
  een = ""
  t_een = 1
  if len(enemy) >= 1:
   for user in enemy:
    een += f"{t_een} - <a href=tg://user?id={user}>{app.get_users(user).first_name}</a>\n"
    t_een += 1
   app.edit_message_text(m.chat.id , m.id , f"❋ Enemy List is cleaned\n{een}")
   enemy.clear()
  else:
   app.edit_message_text(m.chat.id , m.id , f"❋ Enemy List is Empty ") 

 elif text == "القضاء على الأعداء":
  een = ""
  t_een = 1
  if len(enemy) >= 1:
   for user in enemy:
    een += f"{t_een} - <a href=tg://user?id={user}>{app.get_users(user).first_name}</a>\n"
    t_een += 1
   app.edit_message_text(m.chat.id , m.id , f"❋ Enemy List is cleaned\n{een}")
   enemy.clear()
  else:
   app.edit_message_text(m.chat.id , m.id , f"❋ Enemy List is Empty ") 
  
 elif text == "allunmute":
  eem = ""
  t_eem = 1
  if len(mutey) >= 1:
   for user in mutey:
    eem += f"{t_eem} - <a href=tg://user?id={user}>{app.get_users(user).first_name}</a>\n"
    t_eem += 1
   app.edit_message_text(m.chat.id , m.id , f"✿ تم مسح قائمة الصمت\n{eem}")
    mutey.clear()
   else:
    app.edit_message_text(m.chat.id, m.id, f"✿ لا يوجد مستخدمون في قائمة الصمت")
   
 elif text.startswith("setlove"):
  try:
   if m.reply_to_message:
    if m.reply_to_message.from_user.id not in krashh:
     if m.reply_to_message.from_user.id != app.get_me().id:
      krashh.append(m.reply_to_message.from_user.id)
      app.edit_message_text(m.chat.id , m.id , f'✿ {m.reply_to_message.from_user.mention} تمت إضافته إلى قائمة الأعطال')
     else:
      app.edit_message_text(m.chat.id , m.id , f'✿ هذا المستخدم {m.reply_to_message.from_user.mention} موجود بالفعل في قائمة الأعطال')
   else :
    if app.get_users(text.split()[1]).id not in krashh :
     if app.get_users(text.split()[1]).id != app.get_me().id:
      krashh.append(app.get_users(text.split()[1]).id)
      app.edit_message_text(m.chat.id , m.id , f'🩵 <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app. تمت إضافة get_users(text.split()[1]).first_name</a> إلى قائمة الأعطال')
     else:
      app.edit_message_text(m.chat.id , m.id , f'🩵 هذا المعرف<a href=tg://user?id={app.get_users(text.split()[1]).id}>{ app.get_users(text.split()[1]).first_name</a> كان موجودًا بالفعل في قائمة الأعطال')
   except Exception as er:
    m.edit_text(f"الرجاء إدخال معرف رقمي أو اسم مستخدم أو الرد")

  elif text.startswith("وضع الحب"):
  try:
   if m.reply_to_message:
    if m.reply_to_message.from_user.id not in krashh:
     if m.reply_to_message.from_user.id != app.get_me().id:
      krashh.append(m.reply_to_message.from_user.id)
      app.edit_message_text(m.chat.id , m.id , f'✿ {m.reply_to_message.from_user.mention} تمت إضافته إلى قائمة الأعطال')
     else:
      app.edit_message_text(m.chat.id , m.id , f'✿ هذا المستخدم {m.reply_to_message.from_user.mention} موجود بالفعل في قائمة الأعطال')
   else :
    if app.get_users(text.split()[1]).id not in krashh :
     if app.get_users(text.split()[1]).id != app.get_me().id:
      krashh.append(app.get_users(text.split()[1]).id)
      app.edit_message_text(m.chat.id , m.id , f'🩵 <a href=tg://user?id={app.get_users(text.split()[1]).id}>{app. تمت إضافة get_users(text.split()[1]).first_name</a> إلى قائمة الأعطال')
     else:
      app.edit_message_text(m.chat.id , m.id , f'🩵 هذا المعرف<a href=tg://user?id={app.get_users(text.split()[1]).id}>{ app.get_users(text.split()[1]).first_name</a> كان موجودًا بالفعل في قائمة الأعطال')
   except Exception as er:
    m.edit_text(f"الرجاء إدخال معرف رقمي أو اسم مستخدم أو الرد")

 elif text.startswith("deletlove"):
  try:
   if m.reply_to_message:
    if m.reply_to_message.from_user.id in krashh:
     krashh.remove(m.reply_to_message.from_user.id)
     app.edit_message_text(m.chat.id, m.id, f'🤍 تمت إزالة هذا المستخدم {m.reply_to_message.from_user.mention} من قائمة سمات الأعطال')
     else:
      app.edit_message_text(m.chat.id, m.id, f'🤍 هذا المستخدم {m.reply_to_message.from_user.mention} غير موجود في قائمة الأعطال')
   else :
    if app.get_users(text.split()[1]).id in krashh :
     krashh.remove(app.get_users(text.split()[1]).id)
     app.edit_message_text(m.chat.id , m.id , f'🩷هذا المستخدم <a href=tg://user?id={app.get_users(text.split()[1]).id}>{ app.get_users(text.split()[1]).first_name</a> تم حذف السمة بنجاح')
     else:
      app.edit_message_text(m.chat.id , m.id , f'🩷هذا المستخدم<a href=tg://user?id={app.get_users(text.split()[1]).id}>{ app.get_users(text.split()[1]).first_name</a> غير موجود في قائمة الأعطال')
   except Exception as er:
    m.edit_text(f"الرجاء إدخال معرف رقمي أو اسم مستخدم أو الرد")

  elif text.startswith("إزالة الحب"):
  try:
   if m.reply_to_message:
    if m.reply_to_message.from_user.id in krashh:
     krashh.remove(m.reply_to_message.from_user.id)
     app.edit_message_text(m.chat.id, m.id, f'🤍 تمت إزالة هذا المستخدم {m.reply_to_message.from_user.mention} من قائمة سمات الأعطال')
     else:
      app.edit_message_text(m.chat.id, m.id, f'🤍 هذا المستخدم {m.reply_to_message.from_user.mention} غير موجود في قائمة الأعطال')
   else :
    if app.get_users(text.split()[1]).id in krashh :
     krashh.remove(app.get_users(text.split()[1]).id)
     app.edit_message_text(m.chat.id , m.id , f'🩷هذا المستخدم <a href=tg://user?id={app.get_users(text.split()[1]).id}>{ app.get_users(text.split()[1]).first_name</a> تم حذف السمة بنجاح')
     else:
      app.edit_message_text(m.chat.id , m.id , f'🩷هذا المستخدم<a href=tg://user?id={app.get_users(text.split()[1]).id}>{ app.get_users(text.split()[1]).first_name</a> غير موجود في قائمة الأعطال')
   except Exception as er:
    m.edit_text(f"الرجاء إدخال معرف رقمي أو اسم مستخدم أو الرد")

 elif text == "alllove":
  een = ""
  t_een = 1
  if len(krashh) >= 1:
   for user in krashh:
    een += f"{t_een} - <a href=tg://user?id={user}>{app.get_users(user).first_name}</a>\n"
    t_een += 1
   app.edit_message_text(m.chat.id , m.id , f"❋ Enemy List is cleaned\n{een}")
   krashh.clear()
  else:
   app.edit_message_text(m.chat.id, m.id, f "قائمة الأعطال فارغة")

  elif text == "حذف الحب":
  een = ""
  t_een = 1
  if len(krashh) >= 1:
   for user in krashh:
    een += f"{t_een} - <a href=tg://user?id={user}>{app.get_users(user).first_name}</a>\n"
    t_een += 1
   app.edit_message_text(m.chat.id , m.id , f"❋ Enemy List is cleaned\n{een}")
   krashh.clear()
  else:
   app.edit_message_text(m.chat.id, m.id, f "❋ قائمة الأعطال فارغة")

 elif text.startswith("1timename"):
  if text.split()[1] == "on":
   json_database.update({"timename1":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋زمن اسم **مشغل** 🩶")
   elif text.split()[1] == "إيقاف":
    json_database.update({"timename1": "off"})
    write ("data.json"، json.dumps (json_database))
    m.edit_text(f"❋ زمن اسم **مطفأ** 🩶")
   else:
    m.edit_text(f"الرجاء إدخال الأمر بشكل صحيح")
   
 elif text.startswith("2timename"):
  if text.split()[1] == "on":
   json_database.update({"timename2":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ اسم الوقت الثاني **قيد التشغيل** 🩵")
   elif text.split()[1] == "إيقاف":
    json_database.update({"timename2": "off"})
    write ("data.json"، json.dumps (json_database))
    m.edit_text(f"❋ اسم الوقت الثاني **متوقف** 🩵")
   else:
    m.edit_text(f"الرجاء إدخال الأمر بشكل صحيح")

 elif text.startswith("3timename"):
  if text.split()[1] == "on":
   json_database.update({"timename3":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ زمن اسم ثلاثة **مشغل**")
   elif text.split()[1] == "إيقاف":
    json_database.update({"timename3": "off"})
    write ("data.json"، json.dumps (json_database))
    m.edit_text(f"❋ اسم الوقت الثالث ** متوقف **")
   else:
    m.edit_text(f"الرجاء إدخال الأمر بشكل صحيح")

 elif text.startswith("1timebio"):
  if text.split()[1] == "on":
   json_database.update({"timebio1":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"الوقت في السيرة الذاتية [1] **مفعل** 🩶")
  elif text.split()[1] == "off":
   json_database.update({"timebio1":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"الوقت في السيرة الذاتية [1] **متوقف** ❤️‍🩹")
   else:
    m.edit_text(f"الرجاء إدخال الأمر بشكل صحيح")

 elif text.startswith("2timebio"):
  if text.split()[1] == "on":
   json_database.update({"timebio2":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"الوقت في السيرة الذاتية [2] **مفعل** 🩷")
  elif text.split()[1] == "off":
   json_database.update({"timebio2":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"الوقت في السيرة الذاتية [2] **متوقف** 💙")
   else:
    m.edit_text(f"الرجاء إدخال الأمر بشكل صحيح")

 elif text.startswith("3timebio"):
  if text.split()[1] == "on":
   json_database.update({"timebio3":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"الوقت في السيرة الذاتية [3] **مفعل** 🩷")
  elif text.split()[1] == "off":
   json_database.update({"timebio3":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"الوقت في السيرة الذاتية [3] **متوقف** 🩵")
   else:
    m.edit_text(f"الرجاء إدخال الأمر بشكل صحيح")

 elif text.startswith(".limit_del"):
  b = int(text.split()[1])
  if type(b) == int:
     json_database.update({"limitDel":b})
     write("data.json", json.dumps(json_database))
     m.edit_text(f"❋ Anti Del Member Limit Successfully Updated to {b} ❋")
  else:
     m.edit_text(f"❋ Please Enter A Number ❋")

 elif text.startswith("!fontname"):
  if text.split()[1] == "on":
   json_database.update({"fontname":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"تم تشغيل الخط التلقائي 🎧") 
  elif text.split()[1] == "off":
   json_database.update({"fontname":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"الخط التلقائي **متوقف** 🎵")
   else:
    m.edit_text(f"الرجاء إدخال الأمر بشكل صحيح")

 elif text.startswith("welcomeen"): 
  s = ""
  try:
   if text.split()[1] == "on":
     json_database.update({"welcomeen":"on"})
     write("data.json", json.dumps(json_database))
     m.edit_text(f"مرحبًا بك في التحدث باللغة الإنجليزية **قيد التشغيل**")
   elif text.split()[1] == "off":
     json_database.update({"welcomeen":"off"})
     write("data.json", json.dumps(json_database))
     m.edit_text(f"مرحبًا بك في التحدث باللغة الإنجليزية **متوقف عن العمل**")
   elif text.split()[1] == None:
     m.edit_text(f"التحكم في هذا الأمر مع إيقاف التشغيل")
   except Exception as er:
    m.edit_text(f"التحكم في هذا الأمر مع إيقاف التشغيل")

 elif text.startswith("welcomefa"): 
  s = ""
  try:
   if text.split()[1] == "on":
     json_database.update({"welcomefa":"on"})
     write("data.json", json.dumps(json_database))
     m.edit_text(f"مرحبًا بك في التحدث باللغة العربية **قيد التشغيل**")
   elif text.split()[1] == "off":
     json_database.update({"welcomefa":"off"})
     write("data.json", json.dumps(json_database))
     m.edit_text(f"مرحبًا بك في التحدث باللغة العربية **متوقفة**")
    elif text.split()[1] == لا شيء:
      m.edit_text(f"التحكم في هذا الأمر مع إيقاف التشغيل")
   except Exception as er:
    m.edit_text(f"التحكم في هذا الأمر مع إيقاف التشغيل")
####
 elif text.startswith(".firstcom"):
  if text.split()[1] == "on":
   json_database.update({"firstcom":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ First Comment is **ON**") 
  elif text.split()[1] == "off":
   json_database.update({"firstcom":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ First Comment is **OFF**")
  else:
   m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")
#######
 elif text.startswith(".anti_fuck"):
  if text.split()[1] == "on":
   json_database.update({"anti_del":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ Anti Delete Member Mode  is **ON**") 
  elif text.split()[1] == "off":
   json_database.update({"anti_del":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ Anti Delete Member Mode **OFF**")
  else:
   m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")   
   
 elif text.startswith("on_off_status"):
  mh = ""
  a = json_read("data.json")
  pairs = a.items()
  for key, value in pairs:
    mh += f"❋ {key} -> {value}\n"
  m.edit_text(f"{mh}")
  ###########

 elif text.startswith(".answer"):
  if text.split()[1] == "on":
   json_database.update({"autoan":"on"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ Auto Answer is **ON**") 
  elif text.split()[1] == "off":
   json_database.update({"autoan":"off"})
   write("data.json", json.dumps(json_database))
   m.edit_text(f"❋ Auto Answer is **OFF**")
  else:
   m.edit_text(f"❋ ʀᴇsᴜʟᴛs [ `ᴇʀʀᴏʀ` ] ❋")

 elif text.startswith(".addan"):
   an = text.replace(".addan" , "")[1::].split(":")[0]
   en = text.replace(".addan" , "")[1::].split(":")[1]
   answer.append(an)
   javab.append(en)
   m.edit_text(f"❋ Answer Successfully Added\n[{an} -> {en}]") 
   
 elif text.startswith(".anclear"):
   if len(answer) >= 1:
    answer.clear()
    javab.clear()
    m.edit_text(f"❋ Successful!\nAnswer List Cleared") 
   else:
    app.edit_message_text(m.chat.id , m.id , f"❋ Answer List is Empty ")  
   
 elif text.startswith(".delan"):
   if text.replace(".delan" , "")[1::] in answer:
    num = answer.index(text.replace(".delan" , "")[1::])
    answer.remove(answer[num])
    javab.remove(javab[num])
    m.edit_text(f"❋ Successfully\nRemoved From Asnwer List") 
   else:
    m.edit_text(f"❋ This is Not in Asnwer List") 
   
 elif text.startswith(".anlist"):
   s = ""
   op = 1
   if len(answer) >= 1:
    for i in range(0,int(len(answer))):
      s += f"❋ {op}: {answer[i]} -> {javab[i]}\n"
      op += 1
    m.edit_text(f"❋ **Answer List:**\n{s}") 
   else:
    app.edit_message_text(m.chat.id , m.id , f"❋ Answer List is Empty ") 
  
 reloadl = ["`start Reloading`",
"░░░░░░░░░░░░░░",
"▒░░░░░░░░░░░░░",
"▒▒░░░░░░░░░░░░",
"▒▒▒░░░░░░░░░░░",
"▒▒▒▒░░░░░░░░░░",
"▒▒▒▒▒░░░░░░░░░",
"▒▒▒▒▒▒░░░░░░░░",
"▒▒▒▒▒▒▒░░░░░░░",
"▒▒▒▒▒▒▒▒░░░░░░",
"▒▒▒▒▒▒▒▒▒░░░░░",
"▒▒▒▒▒▒▒▒▒▒░░░░",
"▒▒▒▒▒▒▒▒▒▒▒░░░",
"▒▒▒▒▒▒▒▒▒▒▒▒░░",
"▒▒▒▒▒▒▒▒▒▒▒▒▒░",
"▒▒▒▒▒▒▒▒▒▒▒▒▒▒",
"▓▒▒▒▒▒▒▒▒▒▒▒▒▒",
"▓▓▒▒▒▒▒▒▒▒▒▒▒▒",
"▓▓▓▒▒▒▒▒▒▒▒▒▒▒",
"▓▓▓▓▒▒▒▒▒▒▒▒▒▒",
"▓▓▓▓▓▒▒▒▒▒▒▒▒▒",
"▓▓▓▓▓▓▒▒▒▒▒▒▒▒",
"▓▓▓▓▓▓▓▒▒▒▒▒▒▒",
"▓▓▓▓▓▓▓▓▒▒▒▒▒▒",
"▓▓▓▓▓▓▓▓▓▒▒▒▒▒",
"▓▓▓▓▓▓▓▓▓▓▒▒▒▒",
"▓▓▓▓▓▓▓▓▓▓▓▒▒▒",
"▓▓▓▓▓▓▓▓▓▓▓▓▒▒",
"▓▓▓▓▓▓▓▓▓▓▓▓▓▒",
"▓▓▓▓▓▓▓▓▓▓▓▓▓▓",
"Reloading.",
"Reloading..",
"Reloading...",
"Reloading.",
"Reloading..",
"Reloading...",
"Reloading.",
"Reloading..",
"Reloading...",
"`:)`",
]

 if text == "Reload":
  for i in reloadl:
   app.edit_message_text(m.chat.id,m.id,i)
   
 reloadllll = ["``البدء''",
"🤚_ _ _ _ _ _ _ _ _ _ _ _ _💍",
"🤚_ _ _ _ _ _ _ _ _ _ _ _ 💍_",
"🤚_ _ _ _ _ _ _ _ _ _ _ 💍_ _",
"🤚_ _ _ _ _ _ _ _ _ _ 💍_ _ _",
"🤚_ _ _ _ _ _ _ _ _ 💍_ _ _ _",
"🤚_ _ _ _ _ _ _ _ 💍_ _ _ _ _",
"🤚_ _ _ _ _ _ _ 💍_ _ _ _ _ _",
"🤚_ _ _ _ _ _ 💍_ _ _ _ _ _ _",
"🤚_ _ _ _ _ 💍_ _ _ _ _ _ _ _",
"🤚_ _ _ _ 💍_ _ _ _ _ _ _ _ _",
"🤚_ _ _ 💍_ _ _ _ _ _ _ _ _ _",
"🤚_ _ 💍_ _ _ _ _ _ _ _ _ _ _",
"🤚_ 💍_ _ _ _ _ _ _ _ _ _ _ _",
"🤚💍_ _ _ _ _ _ _ _ _ _ _ _ _",
"_ _ _ _ _ _ _ 💏_ _ _ _ _ _ _ _",
]

 if text == "love":
  for i in reloadllll:
   app.edit_message_text(m.chat.id,m.id,i)

 if text == "حب":
  for i in reloadllll:
   app.edit_message_text(m.chat.id,m.id,i)
   
 reloadlllll = ["`البدء`",
"💦_ _ _ _ _ _ _ _ _ _ _ _ _𓂸",
"💦_ _ _ _ _ _ _ _ _ _ _ _ 𓂸_",
"💦_ _ _ _ _ _ _ _ _ _ _ 𓂸_ _",
"💦_ _ _ _ _ _ _ _ _ _ 𓂸_ _ _",
"💦_ _ _ _ _ _ _ _ _ 𓂸_ _ _ _",
"💦_ _ _ _ _ _ _ _ 𓂸_ _ _ _ _",
"💦_ _ _ _ _ _ _ 𓂸_ _ _ _ _ _",
"💦_ _ _ _ _ _ 𓂸_ _ _ _ _ _ _",
"💦_ _ _ _ _ 𓂸_ _ _ _ _ _ _ _",
"💦_ _ _ _ 𓂸_ _ _ _ _ _ _ _ _",
"💦_ _ _ 𓂸_ _ _ _ _ _ _ _ _ _",
"💦_ _ 𓂸_ _ _ _ _ _ _ _ _ _ _",
"💦_ 𓂸_ _ _ _ _ _ _ _ _ _ _ _",
"💦𓂸_ _ _ _ _ _ _ _ _ _ _ _ _",
"_ _ _ _ _ _ _ 𓂺 _ _ _ _ _ _ _",
]

 if text == "start jgh":
  for i in reloadlllll:
   app.edit_message_text(m.chat.id,m.id,i)

 if text == "الصراخ":
  for i in reloadlllll:
   app.edit_message_text(m.chat.id,m.id,i)
   
 reloadllllll = ["`البدء`",
"😂                 • 🔫🤠",
"😂                •  🔫🤠",
"😂               •   🔫🤠",
"😂              •    🔫🤠",
"😂             •     🔫🤠",
"😂            •      🔫🤠",
"😂           •       🔫🤠",
"😂          •        🔫🤠",
"😂         •         🔫🤠",
"😂        •          🔫🤠",
"😂       •           🔫🤠",
"😂      •            🔫🤠",
"😂     •             🔫🤠",
"😂    •              🔫🤠",
"😂   •               🔫🤠",
"😂  •                🔫🤠",
"😂 •                 🔫🤠",
"😂•                  🔫🤠",
"🤯                  🔫 🤠",
"ليفاي حطة الك كلة 🔞😂 🍌",
]

 if text == "fuckkh":
  for i in reloadllllll:
   app.edit_message_text(m.chat.id,m.id,i)
   
 if text == "اقتل الوغد":
  for i in reloadllllll:
   app.edit_message_text(m.chat.id,m.id,i)
   
 reloadlllllll = ["`البدء`",
 "🚶🏻‍♀_ _ _ _ _ _ _ _ _ _ _ _ _ _🏃🏻‍♂",
 "🚶🏻‍♀_ _ _ _ _ _ _ _ _ _ _ _ _ 🏃🏻‍♂_",
 "🚶🏻‍♀_ _ _ _ _ _ _ _ _ _ _ _ 🏃🏻‍♂_ _",
"🚶🏻‍♀_ _ _ _ _ _ _ _ _ _ _ 🏃🏻‍♂_ _ _",
"🚶🏻‍♀_ _ _ _ _ _ _ _ _ _ 🏃🏻‍♂_ _ _ _",
"🚶🏻‍♀_ _ _ _ _ _ _ _ _ 🏃🏻‍♂_ _ _ _ _",
"🚶🏻‍♀_ _ _ _ _ _ _ _ 🏃🏻‍♂_ _ _ _ _ _",
"🚶🏻‍♀_ _ _ _ _ _ _ 🏃🏻‍♂_ _ _ _ _ _ _",
"🚶🏻‍♀_ _ _ _ _ _ 🏃🏻‍♂_ _ _ _ _ _ _ _",
"🚶🏻‍♀_ _ _ _ _ 🏃🏻‍♂_ _ _ _ _ _ _ _ _",
"🚶🏻‍♀_ _ _ _ 🏃🏻‍♂_ _ _ _ _ _ _ _ _ _",
"🚶🏻‍♀_ _ _ 🏃🏻‍♂_ _ _ _ _ _ _ _ _ _ _",
"🚶🏻‍♀_ _ 🏃🏻‍♂_ _ _ _ _ _ _ _ _ _ _ _",
"🚶🏻‍♀_ 🏃🏻‍♂_ _ _ _ _ _ _ _ _ _ _ _ _",
"_ _ _ _ _ _ _🧍🏻‍♀🧍🏻‍♂_ _ _ _ _ _ _",
"LOVE 🩷",
]

 if text == "love1":
  for i in reloadlllllll:
   app.edit_message_text(m.chat.id,m.id,i)

 if text == "حب1":
  for i in reloadlllllll:
   app.edit_message_text(m.chat.id,m.id,i)
 
 elif text.startswith("tas"):
  if 0 < int(text.split()[1]) < 7:   
    app.delete_messages(m.chat.id , m.id)
    while True:
     msg = app.send_dice(m.chat.id, "🎲")
     if msg.dice.value != int(text.split()[1]):
       msg.delete()
     else:
       break
  else:
    m.edit_text(f"""⚠️ **خطأ**: يرجى وضع الأرقام من 1 إلى 6 أمام الأمر
 الأمر المستخدم: [tas]~[tas]""")

 elif text.startswith("dart"):
  app.delete_messages(m.chat.id , m.id)
  while True:
   msg = app.send_dice(m.chat.id, "🎯")
   if msg.dice.value != 6:
     msg.delete()
   else:
     break
     
 elif text.startswith("bowling"):
  app.delete_messages(m.chat.id , m.id) 
  while True:
   msg = app.send_dice(m.chat.id, "🎳")
   if msg.dice.value != 6:
     msg.delete()
   else:
     break

 elif text.startswith("basketball"):
  app.delete_messages(m.chat.id , m.id)
  while True:
   msg = app.send_dice(m.chat.id, "🏀")
   if msg.dice.value != 4:
     msg.delete()
   else:
     break

 elif text.startswith("football"):
  if int(text.split()[1]) == 1 or int(text.split()[1]) == 4:   
    app.delete_messages(m.chat.id , m.id)
    while True:
     msg = app.send_dice(m.chat.id, "⚽")
     if msg.dice.value != int(text.split()[1]):
       msg.delete()
     else:
       break
  else:
    m.edit_text(f"""⚠️ **خطأ**: يرجى وضع الرقم 1 أو 4 أمام الأمر
 الأمر المستخدم: [`football`]~[`football`]""")


  elif text.startswith("addkhaymal"):
   m.edit_text(f"لقد تم التعرف عليك على أنك ازبل من زبالة 😐😄")

  elif text.startswith("إد الوغد"):
   m.edit_text(f"لقد تم التعرف عليك على أنك ازبل من زبالة 😐😄")
  
  

scheduler = AsyncIOScheduler()
scheduler.add_job(job, "interval", seconds=5)
scheduler.add_job(antidelmember, "interval", seconds=5)
scheduler.add_job(mak, "interval", hours=2)
scheduler.start()
app.start(), print("tool levi "), app.send_message("me" , "It was made by a Levi programmer: X\n\n.      **👩🏻‍✈️ @Q_B_H 👩🏻‍✈️**"),idle(), app.stop()
#______________________________LEVI________________________________