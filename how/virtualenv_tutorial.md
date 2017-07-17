# Ref: http://simononsoftware.com/virtualenv-tutorial/

## Test on
```
$ python --version
Python 2.7.9
```

## Install virtualenv 
```
$ pip install virtualenv 
```

## Note
-Windows can use git shell

## Create virtualenv
```
$ virtualenv virt_01
```

จะมี folder ชื่อ virt_01 โผล่ขึ้นมาใน path ปัจจุบัน
Note:
--no-site-packages option is depricated and already set as default.

## To activate virtualenv
```
$ source virt_01/Scripts/activate (หรืออาจจะเป็น $ source virt_01/bin/activate )
(virt_01) $ 
Note: (virt_01) will now prompt in front $
```

## To deactivate
```
(virt_01) $ deactivate
$
```

## Example install package to virtualenv
```
$ source virt_01/Scripts/activate 
(virt_01) $ pip install yolk
(virt_01) $ pip list
pip (6.1.1)
setuptools (15.0)
yolk (0.4.3)
Note
yolk is a simple console program which can list installed packages.
usage:
(virt_01) $ yolk -l
pip 6.1.1 has no metadata
setuptools 15.0 has no metadata
yolk            - 0.4.3        - active
```

## Test virtual install
```
(virt_01) $ deactivate
$ pip list
pip (1.5.6)
setuptools (7.0)
virtualenv (12.1.1)
virtualenvwrapper-win (1.2.0)
$ yolk -l
sh: yolk: command not found
$ virtualenv virt_02
$ source virt_02/Scripts/activate
(virt_02) $ pip install Pylons SqlAlchemy yolk
(virt_02) $ yolk -l
Beaker          - 1.6.5.post1  - active
FormEncode      - 1.3.0        - active
Mako            - 1.0.1        - active
MarkupSafe      - 0.23         - active
Paste           - 1.7.5.1      - active
PasteDeploy 1.5.2 has no metadata
PasteScript     - 1.7.5        - active
Pygments 2.0.2 has no metadata
Pylons          - 1.0.1        - active
Routes          - 2.1          - active
SQLAlchemy      - 0.9.9        - active
Tempita         - 0.5.2        - active
WebError        - 0.10.3       - active
WebHelpers      - 1.3          - active
WebOb           - 1.4          - active
WebTest         - 2.0.18       - active
beautifulsoup4  - 4.3.2        - active
decorator       - 3.4.2        - active
nose 1.3.6 has no metadata
pip 6.1.1 has no metadata
repoze.lru      - 0.6          - active
setuptools 15.0 has no metadata
simplejson      - 3.6.5        - active
six 1.9.0 has no metadata
waitress        - 0.8.9        - active
yolk            - 0.4.3        - active
(virt_02) $ deactivate
```

## Test install specific version of SqlAlchemy to virt_01
```
$ source virt_01/Scripts/activate
(virt_01) $ pip install "SQLAlchemy==0.5.0"
(virt_01) $ pip list
pip (6.1.1)
setuptools (15.0)
SQLAlchemy (0.5.0)
yolk (0.4.3)
(virt_01) $ yolk -l | grep SQLAlchemy
SQLAlchemy      - 0.5.0        - active
(virt_01) $ deactivate
$ pip list
pip (1.5.6)
setuptools (7.0)
virtualenv (12.1.1)
virtualenvwrapper-win (1.2.0)
```
As you can see, switching between another virtual environment is fussy.
จะเห็นว่าการเปลี่ยน env ไปมาค่อนข้างลำบาก

So virtualenvweapper is coming...

## Install virtualenvwrapper on windows
```
$ pip install virtualenvwrapper-win
```

## Install virtualenvwrapper on linux | unix (need to config os env)
```
$ pip install virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
source /usr/local/bin/virtualenvwrapper.sh
export PIP_VIRTUALENV_BASE=$WORKON_HOME
```

**คำสั่งของ virtualenvwrapper จะใช้จาก git shell ไม่ได้ ต้องกลับไปใช้ shell ของ windows แทน**
mkvirtualenv (สร้าง virtualenv ใหม่ )
rmvirtualenv (เอา virtualenv ที่มีอยู่ออก )
workon (เปลี่ยน virtualenv ปัจจุบัน )
add2virtualenv (เพิ่มแพคเกจภายนอกในไฟล์ . / virtualenv ปัจจุบัน )
cdsitepackages (เข้าไปในพื้นที่ไดเรกทอรีของแพคเกจ virtualenv ปัจจุบัน )
cdvirtualenv (เข้าไปในรากของ virtualenv ปัจจุบัน )
deactivate (ปิด virtualenv)

## Ex: To create 
```
> mkvirtualenv virt_03
(virt_03) > mkvirtualenv virt_04
(virt_04) >
```

## Note
Unlike virtualenv that create virtual directory at working path, virt_03 and virt_04 directory now created on path <user home>\Envs.
And automatic activate created virtualenv.

## Ex: To switch
```
(virt_04) > workon virt_03
(virt_03) >
```

-------------------------------------------


การ copy virtualenv ไปทำงานโปรเจคใหม่โดยที่ package ที่ลงไว้ยังเหมือนเดิม
ข้อดีของวิธีการนี้คือทำงานแบบ offline ได้เลย

## Ref
http://askubuntu.com/questions/737098/create-a-copy-of-virtualenv-locally-without-pip-install


มีทางเลือกอีกวิธีที่เป็นที่นิยมคือใช้ pip install -r requirements.txt สั่ง install จาก virtualenv ใหม่ได้เลย
แต่มีข้อด้อยคือต้อง online เพื่อติดต่อกับ packages server ได้และใช้ได้เฉพาะ package ที่มีเก็บไว้ใน remote server เท่านั้น
อาจจะข้อผิดพลาดให้มีโอกาสได้ venv ที่ไม่เหมือนกับต้นฉบับเด๊ะๆแบบวิธี copy ตรงๆซึ่งสามารถทำงานแบบ  offline ได้ดังนี้

ขั้นตอน

1. copy old_path/venv new_path/venv
2. cd new_path/venv/Scripts/ หรือ new_path/venv/bin/ แล้วแต่ os
3. edit path ใน activate , activate.bin ให้เรียบร้อย
สามารถค้นหา path ที่จะต้องแก้ด้วยคำว่า "VIRTUAL_ENV="



เสร็จ

แต่ก็มีอีกวิธีหนึ่งคือใช้ virtualenv-clone ช่วย


wget https://pypi.python.org/packages/source/v/virtualenv-clone/virtualenv-clone-0.2.6.tar.gz
tar -zxvf virtualenv-clone-0.2.6.tar.gz
cd virtualenv-clone-0.2.6
virtualenv newenv           
source newenv/bin/activate
(newenv): python setup.py install
(newenv): virtualenv-clone venvA venvB 
(newenv): deactivate


จบ...
