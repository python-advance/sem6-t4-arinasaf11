import pyqrcode

url = pyqrcode.create('https://www.google.com')
url.svg('uca-url.svg', scale=2, module_color='#177d00') #зеленый цвет
print(url.terminal(quiet_zone=1))
