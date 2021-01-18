# autotransplate.py

# pip install googletrans==3.1.0a0

from googletrans import Translator, LANGUAGES
# print(LANGUAGES) #เอาไว้ดูวาภาษทาที่ต้องการแปลย่อว่ายังไง
from openpyxl import Workbook
from datetime import datetime

translator = Translator()
# result = translator.translate('แมว')
# print(result.text)

article = open('article.txt','r',encoding= 'utf-8')
article = article.read() # readline จะมาบรรทัดเดียว read มาทั้งบทความ
article = article.split() # split เพื่อตัดคำ

print('Count:', len(article))# lens เพื่อนับจำนวน split

result = []

for word in article:
	# print (word)
	res = translator.translate(word,dest='th')
	if res != None:
		# print(res.text)
		result.append([word,res])
# print (result)	
excelfile = Workbook()
sheet = excelfile.active #sheetล่าสุด

header = ['Vocab','Translate']
sheet.append(header)

for rs in result:
	sheet.append(rs)

dt = datetime.now().strftime('%Y-%m-%d %H%M%S')
excelfile.save('Vocab - {}.xlsx'.format(dt))