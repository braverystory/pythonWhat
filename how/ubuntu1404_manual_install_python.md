
ในกรร๊ที่เราต้องการใช้งาน Python version ใหม่ๆซึ่งไม่สามารถใช้ apt-get install ลงได้แล้วเราก็จะต้องนำ source code จาก python.org มาคอมไพล์และลงใน linux เอง  
ตัวอย่างเช่น ubuntu 14.04 จะสามารถลง python version ใหม่สุดได้แถวๆเวอร์ชั่น 3.4.x 
แต่เมื่อเราต้องการใช้งาน python 3.6.x ซึ่งได้รับการปรับปรุงในหลายๆด้านเราสามารถทำได้ดังนี้
  
```
cd packages
wget https://www.python.org/ftp/python/3.6.3/Python-3.6.3.tgz
tar -xvzf Python-3.6.3.tgz
cd Python-3.6.3
./configure --enable-loadable-sqlite-extensions && make && sudo make install
```
  
จะเห็นว่าในที่นี้ในขั้นตอน configure ได้ตั้งค่าให้ลง sqlite ลงไปด้วยเลย ซึ่งแนะนำให้ติดตั้งไปเลยนะ
เนื่องจากในปัจจุบัน sqlite จะถูกแพ็คติดมากับ python version ใหม่ๆเสมอทำให้ไม่สามารถลงผ่าน pypi ได้อีกง่ายๆอีกแล้ว จึงแนะนำให้ติดตั้งไปเลยจะได้ไม่เจอปัญหาเวลาต้องการจะใช้งานนะ  
  
Ref:  
- https://askubuntu.com/questions/922644/install-pip3-latest-version-for-python3-6
- http://ubuntuhandbook.org/index.php/2017/07/install-python-3-6-1-in-ubuntu-16-04-lts/
- https://stackoverflow.com/questions/1210664/no-module-named-sqlite3
  
  
