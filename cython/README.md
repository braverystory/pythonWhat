


# Installation
```
pip install cython
```

# Howto cython module
1. เขียน source code แบบเดียวกับ python module ด้วย cython syntax ลงในไฟล์ .pyx
2. เรียกใช้งาน module .pyx แบบเดียวกับ python module ได้เลยเพียงแต่ต้อง เพิ่ม
```
import pyximport; pyximport.install()
```
ลงในโปรแกรมเด้วย สามารถดูตัวอย่างได้จากโฟลเดอร์ `basic_primecal`  

# Reference:
https://medium.com/@konpat/ใครว่า-python-ช้า-ถ้าเรารู้จักเขียน-cython-bb3529194a6  
http://docs.cython.org/en/latest/src/quickstart/cythonize.html  
https://github.com/cython/cython/wiki  
https://python3.wannaphong.com/2014/09/การสร้าง-python-extension-cc-ด้วย-cython.html  


