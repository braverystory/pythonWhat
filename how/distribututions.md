
# การสร้าง python module

## Requirements
`$ pip install setuptools twine`


## โครงสร้างอย่างง่ายของโปรเจค



### สามารถดูการเขียน setup.py ได้ที่ 
[Click](https://packaging.python.org/distributing/)


## การแจกจ่า distributetion source code (sdist): unbuilt package
สร้าง tar หรือ zip เพื่อแจกจ่าย source code ซึ่งยังไม่ได้ถูก Built
`$ python setup.py sdist`

## การแจกจ่าย Wheels: built package(.whl)
wheels file สามารถใช้ติดตั้งโดยที่ไม่จำเป็นจะต้องผ่านกระบวนการ build ใดๆอีกแบ่งออกเป็น 3 ประเภทดังนี้

1.**Pure Python Wheels**

คือ package ที่ไม่มีไฟล์ที่ถูกคอมไพล์เป็นส่วนประกอบอยู่ และ source code ไม้ได้เขียนให้ support python 2 และ 3 พร้อมกัน

contains no compiled extensions, but don’t natively support both Python 2 and 3.

```
#To build 
python setup.py bdist_wheel
```
 
2.Universal Wheels: 

คือ package ที่ไม่มีไฟล์ที่ถูกคอมไพล์เป็นส่วนประกอบอยู่ และ source code เขียนให้ support python 2 และ 3 พร้อมกัน

are pure python support Python 2 and 3. This is a wheel that can be installed anywhere by pip.

```
#To build 
python setup.py bdist_wheel --universal
```

3.Platform Wheels:  

คือ package ที่มีการรวมเอาไฟล์สำหรับ os ใดๆเข้าไปด้วย ทำให้ไฟล์ .whl ที่ได้จะสามารถใช้ได้แค่กับ platform นั้นๆเท่านั้น

are wheels that are specific to a certain platform like linux, OSX, or Windows, usually due to containing compiled extensions.

```
#To build 
python setup.py bdist_wheel
```

Note:
Option `bdist_wheel` จะทำการตรวจสอบว่าเป็น pure python หรือไม่และสร้างไฟล์ wheel ออกมาให้เหมาะสมออกมาให้เอง

bdist_wheel will detect that the code is not pure Python, and build a wheel that’s named such that it’s only usable on the platform that it was built on


## Reference
https://docs.python.org/3/distributing/index.html
https://packaging.python.org/distributing/


