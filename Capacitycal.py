#Calculation Aircondition Performance (Sensible heat)

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI =Tk()
GUI.title('โปรแกรมคำนวณ Sensible heat of aircondition by FJen')
GUI.geometry('400x500')

#config
FONT1 =('Angsana New', 15)
FONT2 = ('Angsana New', 20) 

#คำอธิบาย
L= ttk.Label(GUI, text ='Calculation Aircondition Sensible heat', font =FONT1)
L.pack()

v_airflow = IntVar()
D1 = ttk.Label(GUI, text = 'Dry airflow rate (m3/min)', font=FONT1)
D1.pack(pady=10)
D2 = ttk.Entry(GUI,textvariable = v_airflow, font=FONT1, width = 40)
D2.pack(pady=2)

v_h1 = IntVar()
A1 = ttk.Label(GUI, text = 'Air Enthalpy h1', font=FONT1)
A1.pack(pady=10)
A2 = ttk.Entry(GUI,textvariable = v_h1, font=FONT1, width = 40)
A2.pack(pady=2)

v_h2 = IntVar()
H1 = ttk.Label(GUI, text = 'Air Enthalpy h2', font=FONT1)
H1.pack(pady=10)
H2 = ttk.Entry(GUI,textvariable = v_h2, font=FONT1, width = 40)
H2.pack(pady=2)

#calculatate Button
def Cal():
    airflow = v_airflow.get()
    h1 = v_h1.get()
    h2 = v_h2.get()
    calsensible = "Sensible heat: {} kW".format(airflow * (h2-h1))
    v_result.set(calsensible) #แสดงผลลัพธ์
    
        
B1 = ttk.Button(GUI, text ='Calculate', command = Cal)
B1.pack(ipadx=20,ipady=10)

v_result = StringVar()
R1 = ttk.Label(GUI,textvariable = v_result, font=FONT2)
R1.pack(pady=20)

GUI.mainloop()
