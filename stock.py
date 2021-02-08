#stock.py

from urllib.request import urlopen as req
from bs4 import BeautifulSoup as soup
from songline import Sendline

# ส่งไลน์
# ตัวเลข Token เอามาจาก https://notify-bot.line.me/my/
# เลือกกรุ้ปไลน์ที่มี line notification
token ='cTsymiG0DrXFkXrUewMGesmrk2U9d6IvFNuKB8nZPKL'
messenger = Sendline(token) #messenger ผู้ส่ง


def Checkprice(CODE):
	url = 'https://www.settrade.com/C04_02_stock_historical_p1.jsp?txtSymbol={}&ssoPageId=10&selectPage=2'.format(CODE)

	webopen = req(url) # req คือ เปิด web โดยไม่ต้องเปิด web browser (google chrome)
	page_html = webopen.read() # ข้อมูลดิบ
	webopen.close() # ปิดการ request

	#serch ข้อมูลในส่วนที่เราอยากหา
	data = soup (page_html,'html.parser') # มันจะทำให้ html ที่เราได้มาเปิดง่ายขึ้นอ่านงาย
	result = data.find_all('div','col-xs-6')


	price = float(result[2].text) 
	change = result[3].text
	change = change.replace('\n','') # replace คือการแทนที่ \n ด้วย ... ว่าไป
	change = change.replace('\t','')
	change = change.replace('\r','')
	change = change.replace(' ','')
	change = change.replace('เปลี่ยนแปลง','')


	pchange =result[4].text
	pchange=pchange.replace('\n','')
	pchange=pchange.replace('\r','')
	pchange=pchange.replace(' ','')
	pchange =pchange.replace('%เปลี่ยนแปลง','')

	update = data.find_all('span','stt-remark')
	update = update[0].text.replace('ข้อมูลล่าสุด','')[1:]

	print(CODE)
	print(change)
	print(pchange)
	print(price)
	print(update)
	textline = 'CODE: {}\nPrice: {}\nChange: {}\n'.format(CODE,price,change)
	textline2 = '%Change: {}\nUpdate: {}'.format(pchange,update)
	messenger.sendtext(textline+textline2)
	print('-------')



Checkprice('PTT')
Checkprice('SCB')
Checkprice('CPALL')
Checkprice('AOT')
Checkprice('PTG')





# print(len(update)) # นับว่าใน list มีข้อมูลกี่ชุด








# print(len(update)) # นับว่าใน list มีข้อมูลกี่ชุด
# print(change[11:]) # [11:]คือการเริ่มเอาตัวอักษรหลังตัวที่ 11 เป็นต้นไปมาแสดง
#float แปลงจากข้อความเป็นจุดทศนิยม
#int แปลงจากข้อความเป็นตัวเลขจำนวนเต็ม
# print(type(price)) #คำสั่งเช็คชริดของข้อมูล

