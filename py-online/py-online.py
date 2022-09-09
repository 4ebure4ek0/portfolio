#!C:\Users\white\AppData\Local\Programs\Python\Python310\python.exe
print("Content-type: text/html\r\n")
import os
import sys
from urllib.parse import parse_qs

file = open("py-online.html", "r")
html = file.read()
file.close()
file = open("../menu.html", "r")
menu = file.read()
file.close
html = html.replace("<!--#menu-->", menu)

data = sys.stdin.read()
if data=="":
    code="print('')"
else:
    parts = parse_qs(data)
    code = parts["code"][0]

file = open("input.py", "w")
input = file.write(code)
file.close()

os.system('python input.py > output.txt')

file = open("output.txt", "r")
res = file.read()
file.close()

html = html.replace("<!--#res-->", res)
print(html)