
Note: Copy from my old facebook notes date<TUESDAY, SEPTEMBER 29, 2015>

# Abstract
ทดสอบติดตั้ง python สองเวอร์ชัน(2.7.9 และ 3.5.0) ลงบน windows 7 และได้ใช้งาน pip, virtualenv ของ python แต่ละเวอร์ชันได้อย่างอิสระด้วย python launcher for Windows ที่ถูกติดตั้งมาพร้อมกับ python 3
Key Words: python, windows, multiple, launcher, virtualenv, pip

# First to Know
ตั้งแต่ python 2.7.9 ขึ้นไป pip จะถูกรวมมาด้วยตั้งแต่ตอนติดตั้ง python เลย
ตั้งแต่ python 3.3.0 ขึ้นไป python launcher(py.exe,pyw.exe) จะถูกติดตั้งโดย default ลงที่ตำแหน่ง C:\Windows\ ซึ่งเป็น path default ของ windows อยู่แล้วจึงสามารถเรียกใช้งานได้โดยไม่จำเป็นต้องแอด path ใดๆเพิ่มเติม
ในขั้นตอนติดตั้ง python ทั้งสองเวอร์ชันให้เลือกแอด path เข้าไปเลยสะดวกดี
การใช้งาน python launcher
## python2 ##

[[ python shell ]]
C:\Users\Joe_jj> py
Python 2.7.9 (default, Dec 10 2014, 12:24:55) [MSC v.1500 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
[[ pip ]]
C:\Users\Joe_jj>py -2 -m pip --version
pip 7.1.2 from C:\Python27\lib\site-packages (python 2.7)
[[ virtualenv ]]
C:\myapp> py -m venv venv_myapp_p279
หรือ
C:\myapp> virtualenv -p "c:\Python27\python.exe" venv_myapp_p279
## python3 ##

[[ python shell ]]
```
C:\Users\Joe_jj> py -3
Python 3.5.0 (v3.5.0:374f501f4567, Sep 13 2015, 02:16:59) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

[[ pip ]]
```
C:\Users\Joe_jj> py -3 -m pip --version
pip 7.1.2 from C:\Program Files (x86)\Python 3.5\lib\site-packages (python 3.5)
```

[[ virtualenv ]]
```
C:\myapp> py -3 -m venv venv_myapp_p350
```
หรือ
```
C:\myapp> virtualenv -p "c:\Program Files (x86)\Python 3.5\python.exe" venv_myapp_p350
```

Reference
- https://docs.python.org/3/using/windows.html
- http://stackoverflow.com/questions/22793650/using-virtualenv-with-multiple-python-versions-on-windows

-------------------------------------------------------------

# UBUNTU
  
บน linux จะมี symbolic link  /usr/bin/python  ที่โดย default จะชี้ไป python2 และมี /usr/bin/python2 กับ /usr/bin/python3 อยู่ แต่การ switch version ของ python จะไม่แนะนำให้แก้ค่าของ symbolic link ดังกล่าวเนื่องจาก package อื่นๆจะได้รับผลกระทบไปด้วย
ดังนั้นเราจะใช้ alias เข้ามาช่วยในการ switch version ดังนี้
```
$ python --version
Python 2.7.6
$ alias python=python3
$ python --version
Python 3.4.3
$ alias python=python2
$ python --version
Python 2.7.6
```

หากต้องการตั้งให้เป็นค่าเริ่มต้นเลยสามารถนำ `alias python=python3` ไปใส่ไว้ในไฟล์ `~/.bashrc` หรือ `~/.bash_aliases` ก็ได้ 

## การใช้งาน pip3 
ลง pip3 ให้เรียกร้อยและใช้งานได้ด้วยคำสั่งดังนี้  
```
$ sudo apt-get install python3-pip
$ sudo pip3 install virtualenv
```

## To custom Python interpreter 
สำหรับการเลือก virtualenv version นั้นสามารถใช้แฟลก -p ได้ดังนี้
```
$ virtualenv -p python2 venv
```

## To activating a virtual environment 
```
$ source venv/bin/activate
```
