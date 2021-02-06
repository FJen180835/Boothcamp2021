# autogoogle.py
import webbrowser
import pyautogui as pg
import time
import pyperclip

# กรณีจ้องการเปิด browser โดนตรง
# from subprocess import Popen
# path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs(ใส่ r เพื่อให้ค่า \ me'kowfh)

# 1- open web broowser (google)
url = 'httP://www.google.com'
webbrowser.open(url)
time.sleep(3) # หน่วงเวลาไว้เพื่อให้มันสามารถพิมพ์ได้

# 2-type key word
# pg.write('thailand',interval = 0.25)
keyword = 'ประเทศไทย'
pyperclip.copy(keyword) # copy ลง clipbord 
time.sleep(0.5)
pg.hotkey('ctrl', 'v') #ห้ามใช้เครื่องหมาย +
time.sleep(1)


# 3- press enter
pg.press('enter')
time.sleep(10)

# 4-screenshot
pg.screenshot('thailand.png')