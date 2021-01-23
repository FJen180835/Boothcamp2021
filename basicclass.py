# basiclass.py

class Student:
    def __init__(self,name): #self คือคำพิเศษใช้แทนตัวมันเอง
        self.name = name
        self.exp = 0
        self.lesson = 0

    def Hello(self):
        print('สวัสดีจ้า ผมชื่อ {}'.format(self.name))

    def Coding(self):
        print('{}: กำลังเขียนโปรแกรม..'.format(self.name))
        self.exp += 5
        self.lesson += 1

    def ShowEXP(self):
        print(' - {} มีประสบการณ์ {} EXP'.format(self.name,self.exp))
        print(' - เรียนไป {} ครั้งแล้ว'.format(self.lesson))


print('============== 1 Jan 2021===========')
student1 = Student('Albert') #เอา student1 ไปแทน self
print(student1.name)
student1.Hello()

student2 = Student('Jenny') 
print(student2.name)
student2.Hello()

print('============== 2 Jan 2021===========')
print('----ใครอยากเรียน coding บ้าง?---(10xp)-----')
student1.exp += 10 #student1.exp = studen1.exp + 10

print('============== 3 Jan 2021===========')
print('ตอนนี้ exp ของแต่ละคนได้เท่าไรกันแล้ว?')

print(student1.name,student1.exp)

print('============== 4 Jan 2021===========')
for i in range(5):
    student2.Coding()

student1.ShowEXP()
student2.ShowEXP()


