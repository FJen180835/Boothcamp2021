 # writecsv.py

import csv 

# with ใช้กับไฟล์ที่ต้องการ เปิด หรือ เขียนไหล์
# mode a ค่าอะไรก็ได้
# mode w ต้อองการ write ทับเล

def WritetoCSV(data):
    with open('test.csv','a', newline ='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = filw writer
        fw.writerow(data) # เก็บทีละบรรทัด
    print('บันทึกไฟล์สำเร็จ')

data = ['print () คืออะไร?' , 'คำสั่งในการแสดงผลจข้อความ']
WritetoCSV(data)
