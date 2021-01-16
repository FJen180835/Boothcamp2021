# GUITranslator.py
from tkinter import *
#จากไลบรารี่ชื่อ tkinter, * คือให้ดึงความสามารถหลักมาทั้งหมด
from tkinter import ttk # tkk is name of tk ทันสมัยกว่า
###-----Google Translate -----
from googletrans import Translator
translator = Translator()


GUI = Tk() #ใช้สร้างหน้าต่างหลัก from __int__py
GUI.geometry('500x300') #กว้าง x ยาว
GUI.title('โปรแกรมแปลภาษา by FJen')
#---config---
FONT = ('Angsana New',15)

#----Label----
L = ttk.Label(GUI,text='กรุณากรอกคำศัพท์ที่ต้องการแปล',font=FONT)
L.pack()


#-----Entry (ช่องกรอกข้อความ)-----
v_vocab = StringVar() #กล่องเก็บข้อความ

E1 = ttk.Entry(GUI,textvariable = v_vocab, font=FONT,width=40)
E1.pack(pady=20) #pady ขยับแกน y 20pixel ห่างนอกกล่อง


#-----Button (ปุ่มแปล)-----
def Translate():
    vocab = v_vocab.get() #.get คือคำสั่งให้แสดงผลออกมา
    meaning = translator.translate(vocab,dest='th')
    print(vocab + ':' + meaning.text) #ต้อง . text เพื่อให้มันแสดงผลเป็นข้อความได้
    print(meaning.pronunciation)
    v_result.set(vocab + ':' + meaning.text)

   
B1 = ttk.Button(GUI,text='Translate',command=Translate)#สร้างปุ่ม
B1.pack(ipadx=20, ipady=10) #show button ปุ่มขึ้นมาวางจากบนลงล่าง, ipad is internal padding x-axis, y-axis

#----Label----
L = ttk.Label(GUI,text='คำแปล',font=FONT)
L.pack()
#----Result----
v_result = StringVar()#กล่องสำหรับเก็บคำแปล
FONT2 = ('Angsana New',20)
R1 = ttk.Label(GUI,textvariable=v_result,font=FONT, foreground='green')
R1.pack()









GUI.mainloop() #เพื่อให้มันสามารถรันใหม่ได้เรื่อยๆ จนกว่าเราจะปิด  บรรทัดสุดท้ายเท่านั้น

