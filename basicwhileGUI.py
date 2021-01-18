money = 1000
transfer = 2000
service = 15
# print ('Condition:', money < transfer)
print('ต้องการโอนเงิน', 2000)
while money < transfer + service:
	print('คุณมีเงิน',money)
	print('กรุณาโอนเงินเข้าบัญชี เงินไม่พอโอน มีค่าบริการโอนเงิน 15 บาท')
	getmoney = int(input('ฝากเงินเท่าไร'))
	money = money + getmoney # 998 + xxx
	print ('----')

print('โอนเงินได้เลย')
print('เหลือเงินในบัญชี: ', money - transfer - service)
print('ค่าบริการในการโอนเงิน', service)