#basic-ifelse.py

# money = int(input('How much money do u have?:'))
from pprint import pprint # pretty print
import random 

restaurant = {'high':[{'name':'shitsuka sushi', 'price':200},
						{'name':'Peporini','price' :500}],
			'medium':[{'name':'เสวย','price':200},
						{'name':'รสดี','price':250}],
			'low':[{'name':'ป้าส้ม','price':40},
						{'name':'ป้าเล็กกะเพรา','price':50}]}

# pprint(restaurant)

money = 100

if money >= 500:
	select = random.choice(restaurant['high'])
	print('คุณผู้หญิงทานร้าน')
elif money >=200:
	print('เสวย' + 'รสชาติดีมาก ลองเลย')
else:
	print('ป้าส้ม' +'Good price')
