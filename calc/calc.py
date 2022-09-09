#!C:\Users\white\AppData\Local\Programs\Python\Python310\python.exe
print("Content-type: text/html\r\n")
file = open("calc.html", "r")
html = file.read()
file.close
file = open("../menu.html", "r")
menu = file.read()
file.close()
html = html.replace("<!--#menu-->", menu)
import sys
from os import getenv
query_string = getenv("QUERY_STRING")
#query_string="a=34&b=65&op=s
#query_string = ""
if query_string == "":
    print(html)
    sys.exit(0)
parts = query_string.split("&")
parts_a = parts[0].split("=")
a = parts_a[1]
parts_b = parts[1].split("=")
b = parts_b[1]
parts_op = parts[2].split("=")
op = parts_op[1]

a = int(a)
b = int(b)
res = 0

if op == "sum":
    res = a + b
if op == "sub":
    res = a - b
if op == "mul":
    res = a * b
if op == "div":
    res = a / b

html = html.replace("<!--answer-->", "{}".format(res))
print(html)