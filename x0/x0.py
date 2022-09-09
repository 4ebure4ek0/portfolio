#!C:\Users\white\AppData\Local\Programs\Python\Python310\python.exe
print("Content-type: text/html\r\n")

#import sys
#print(sys.executable)
#sys.exit(0)

def display(a, highlight_cells):
    html_cells = ""
    r = range(0, 3)
    for str_num in r:
        for col_num in r:
            if [str_num, col_num] in highlight_cells:
                html_cells = html_cells + '<input type="submit" value="{}" name="cell_{}{}" class="highlight"/>\r\n'.format(a[str_num][col_num], str_num, col_num)  
            else:
                html_cells = html_cells + '<input type="submit" value="{}" name="cell_{}{}"/>\r\n'.format(a[str_num][col_num], str_num, col_num)  
        html_cells = html_cells + "<br />\r\n"
    file = open("x0.html", "r")
    html = file.read()
    file.close()
    file = open("../menu.html", "r")
    menu = file.read()
    file.close
    html = html.replace("<!--#menu-->", menu)
    html = html.replace("<!--cells-->", html_cells)
    print(html)

def str_set_elem(str, index, new_elem):
    return str[:index] + new_elem + str[(index+1):]

file = open("x0.txt", "r")
str = file.read()
file.close()

a = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

r = range(0, 3)

for str_num in r:
    for col_num in r:
        a[str_num][col_num] = str[str_num*3 + col_num]

import sys

#data = "cell_00=-"
data = sys.stdin.read()
if(data == ""):
    display(a, [])
    sys.exit(0)

str_num = int(data[5])
col_num = int(data[6])
player = str[9]


if a[str_num][col_num]=="-":
    a[str_num][col_num]=player
    index = str_num*3 + col_num
  #  str[index] = player
    str = str_set_elem(str, index, player)
    if(player == "X"):
        player = "0"
    else:
        player = "X"
    str = str_set_elem(str, 9, player)
    file = open("x0.txt", "w")
    file.write(str)
    file.close()

    highlight_cells = []

    if((a[0][0] == a[0][1]) & (a[0][1] == a[0][2]) & (a[0][0] != "-")):
        highlight_cells = [[0, 0], [0, 1], [0, 2]]

    if((a[1][0] == a[1][1]) & (a[1][1] == a[1][2]) & (a[1][0] != "-")):
        highlight_cells = [[1, 0], [1, 1], [1, 2]]

    if((a[2][0] == a[2][1]) & (a[2][1] == a[2][2]) & (a[2][0] != "-")):
        highlight_cells = [[2, 0], [2, 1], [2, 2]]

    if((a[0][0] == a[1][1]) & (a[0][0] == a[2][2]) & (a[0][0] != "-")):
        highlight_cells = [[0, 0], [1, 1], [2, 2]]

    if((a[0][2] == a[1][1]) & (a[0][2] == a[2][0]) & (a[0][2] != "-")):
        highlight_cells = [[0, 2], [1, 1], [2, 0]]

    if((a[0][0] == a[1][0]) & (a[1][0] == a[2][0]) & (a[0][0] != "-")):
        highlight_cells = [[0, 0], [1, 0], [2, 0]]

    if((a[0][1] == a[1][1]) & (a[1][1] == a[2][1]) & (a[0][1] != "-")):
        highlight_cells = [[0, 1], [1, 1], [2, 1]]

    if((a[0][2] == a[1][2]) & (a[1][2] == a[2][2]) & (a[0][2] != "-")):
        highlight_cells = [[0, 2], [1, 2], [2, 2]]
 
display(a, highlight_cells)