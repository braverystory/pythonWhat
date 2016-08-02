
# การสร้าง python module

## Requirements
```
# Default package@ python 3.5.2
$ pip install setuptools wheel 
# Needed when what to push to pip
$ pip install twine
```


## โครงสร้างอย่างง่ายของโปรเจค

```
<distributetions>
│   setup.cfg
│   setup.py
├───module01
│       bar.py
│       foo.py
│       __init__.py
├───module02
│       bar.py
│       foo.py
│       __init__.py
└───venv_gitbash_package
    │   ...
  ...
```

==============================

Tutorial

```
$ cd distributetions
$ virtualenv venv_gitbash_package
$ source venv_gitbash_package/Scripts/activate
$ python setup.py bdist_wheel
$ pip install --upgrade dist/distSample-2016.8.1-py3-none-any.whl
$ pip list
$ python
>>> 
>>> import module01 as m1
>>> dir(m1)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'main']
>>> m1.main()
1...Calling main application...
>>>
>>> import module02 as m2
>>> dir(m2)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'main']
>>> m2.main()
2...Calling main application...
>>>
>>> from module01 import *
Hello from foo
Hello from bar
>>> dir(m1)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'bar', 'foo', 'main']
>>> m1.foo.printstr('abc')
1 foo: abc
>>> m1.bar.printstr('abc')
1 bar: abc
>>> foo.printstr('abc')
1 foo: abc
>>> bar.printstr('abc')
1 bar: abc
>>>
>>> from module02 import *		# foo will from m1 to m2
Hello from foo
>>> dir(m2)
['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 'foo', '
main']
>>> m2.foo.printstr('xyz')
2 foo: xyz
>>> foo.printstr('xyz')			# plug with m2
2 foo: xyz
>>> bar.printstr('xyz')			# still plug with m1
1 bar: xyz
>>>
```


==============================

### สามารถดูการเขียน setup.py ได้ที่ 
[Click](https://packaging.python.org/distributing/)


## การแจกจ่ายซอดโค๊ด **distributetion source code (sdist):** unbuilt package
สร้าง tar หรือ zip เพื่อแจกจ่าย source code ซึ่งยังไม่ได้ถูก Built
`$ python setup.py sdist`

## การแจกจ่าย Wheels file: built package(.whl)
Wheels file สามารถใช้ติดตั้งโดยที่ไม่ต้องผ่านกระบวนการ build ใดๆอีก แบ่งออกเป็น 3 ประเภทดังนี้

1.**Pure Python Wheels**

คือ package ที่ไม่มีไฟล์ที่ถูกคอมไพล์เป็นส่วนประกอบอยู่ และ source code ไม้ได้เขียนให้ support python 2 และ 3 พร้อมกัน

Contains no compiled extensions, but don’t natively support both Python 2 and 3.

```
#To build 
python setup.py bdist_wheel
```
 
2.Universal Wheels: 

คือ package ที่ไม่มีไฟล์ที่ถูกคอมไพล์เป็นส่วนประกอบอยู่ และ source code เขียนให้ support python 2 และ 3 พร้อมกัน

Are pure python support Python 2 and 3. This is a wheel that can be installed anywhere by pip.

```
#To build 
python setup.py bdist_wheel --universal
```

3.Platform Wheels:  

คือ package ที่มีการรวมเอาไฟล์สำหรับ os ใดๆเข้าไปด้วย ทำให้ไฟล์ .whl ที่ได้จะสามารถใช้ได้แค่กับ platform นั้นๆเท่านั้น

Are wheels that are specific to a certain platform like linux, OSX, or Windows, usually due to containing compiled extensions.

```
#To build 
python setup.py bdist_wheel
```

**อ๊อปชัน `bdist_wheel` จะทำการตรวจสอบว่าเป็น pure python หรือไม่และสร้างไฟล์ wheel ออกมาให้เหมาะสมออกมาให้เอง**

**bdist_wheel will detect that the code is not pure Python, and build a wheel that’s named such that it’s only usable on the platform that it was built on**


## การติดตั้ง package จาก .whl

```
pip install SomePackage-1.0-py2.py3-none-any.whl
```

==============================

# การ Upload python module ขึ้น pypi

## Requirements
`$ pip install twine`

ขึ้นตอนสามารถดูได้จาก

https://packaging.python.org/distributing/#uploading-your-project-to-pypi

==============================

## Reference
1. https://docs.python.org/3/distributing/index.html
1. https://packaging.python.org/distributing/
1. https://pip.pypa.io/en/latest/user_guide/#installing-from-wheels

