from tkinter import *
from tkinter import ttk # ttk is theme of tk
import csv 

# with ใช้กับไฟล์ที่ต้องการ เปิด หรือ เขียนไหล์
# mode a ค่าอะไรก็ได้
# mode w ต้อองการ write ทับเล
# csv file
def WritetoCSV(data):
    with open('data.csv','a', newline ='',encoding='utf-8') as file:
        fw = csv.writer(file) # fw = filw writer
        fw.writerow(data) # เก็บทีละบรรทัด
    print('บันทึกไฟล์สำเร็จ')


# Main program
GUI = Tk()
GUI.title('My program')
GUI.geometry('500x300')

# font 
FONT1 = ('Angsana New',20, 'bold')
FONT2 = ('Angsana New',15)

# Header1
L1 = ttk.Label(GUI,text='หัวข้อ',font=FONT1, foreground ='green') 
# foreground text color background = bg color
L1.pack() # นำ L1 ไปติดกับโปรแกรมหลัก

# text box 1
v_title = StringVar() # SringVar ตัวแปรพิเศษใช้เก็บข้อมูล
E1 = ttk.Entry(GUI,textvariable = v_title ,font=FONT2,width = 30)
E1.pack()

L2 = ttk.Label(GUI,text='รายละเอียด',font=FONT1,foreground ='green')
L2.pack(pady = 10) 

# text box 2
v_detail = StringVar()
E2 = ttk.Entry(GUI,textvariable = v_detail ,font=FONT2, width = 50)
E2.pack()

# Button save
# event ใส่เพื่อให้มันส่งข้อมูลอะไรเข้าไปก็ได้
def SaveButton(event=None):
	title = v_title.get() # .get ดึงข้อมูลจากตัวแปร v_title ใช้คู่กับ StringVar
	detail = v_detail.get()
	print(title)
	print(detail)
	dt = [title,detail] # list because we will using data
	WritetoCSV(dt)
	print('กำลังบันทึกข้อมูล...')
	# clear data
	v_title.set('') # clear data
	v_detail.set('')
	E1.focus() # ทำให้ cursor อยู่กล่อง E1

E2.bind('<Return>',SaveButton) 
# เป็นการเช็คว่ามีการกดปุ่ม enter หรือไม่ หากกดให้ทำการเรียก fuction SaveButton
# มสามารถกดปุ่ม Enter แทนการใช้ปุ่ม Save ในหน้าโปรแกรม


B1 = ttk.Button(GUI,text = 'save', command = SaveButton)
B1.pack(ipadx = 20, ipady = 5, pady = 40) 
# ipad ระยะห่างภายในปุ่ม หรือกล่อง pad เฉยๆ ระยะห่างภายนอกปุ่ม


























GUI.mainloop()