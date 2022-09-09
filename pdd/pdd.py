#!C:\Users\white\AppData\Local\Programs\Python\Python310\python.exe
print("Content-type: text/html; charset=utf-8\r\n")

import json

file = open("./variants/var1.json", "r")
data = file.read()
file.close()
tasks = json.loads(data)

def display(tasks, html, ans_data_arr):
    file = open("pattern.html", "r")
    task_pattern = file.read()
    file.close()

    tasks_html = ""

    lenght = len(tasks)
    
    tasks_range = range(0, lenght)
    for task_num in tasks_range:
        task = tasks[task_num]
        task_html = task_pattern
        task_html = task_html.replace("<!--question-->", task["question"])
        
        img_html = ""
        img = task["img"]
        for cur_img in img:
             img_html = img_html + '<img src="{}" />\n'.format(cur_img)
        task_html = task_html.replace("<!--img-->", img_html)

        answers_html = ""
        answers = task["answers"]
        answers_range = range(0, len(answers))
        if(len(ans_data_arr) == 0):
            ans_data = [0, ""]
        else:
            ans_data = ans_data_arr[task_num]

        for ans_num in answers_range:
        #begin
            value = ans_num+1
            if(value == ans_data[0]):
                answer_pattern = '<div class="{}"><input type="radio" name="answer{}" value="<!--value-->"/><!--answer--><br /></div>\n'.format(ans_data[1], task_num)
            else:
                answer_pattern = '<div><input type="radio" name="answer{}" value="<!--value-->"/><!--answer--><br /></div>\n'.format(task_num)
            answer_html = answer_pattern.replace("<!--value-->",  str(value)) 
            answer_html = answer_html.replace("<!--answer-->",  answers[ans_num]) 
            answers_html = answers_html + answer_html
        #end
        task_html = task_html.replace("<!--answers-->", answers_html)
        tasks_html = tasks_html + task_html
        #print(task_html)

    html = html.replace("<!--tasks-->", tasks_html)
    print(html)

    
import os
import sys

file = open("pdd.html", "r")
html = file.read()
file.close()
file = open("../menu.html", "r")
menu = file.read()
file.close
html = html.replace("<!--#menu-->", menu)

ans_data_arr = []
#query_string = ""
#query_string = "answer0=1&answer1=3&answer2=2&answer3=3"
query_string=os.getenv("QUERY_STRING")
if(query_string == ""):
    display(tasks, html, ans_data_arr)
    sys.exit(0)

params = query_string.split("&")

task_num = 0

for param in params:
    
    parts=param.split("=")
    user_answer = parts[1]
    user_answer = int(user_answer)

    if(user_answer==tasks[task_num]["right_answ"]):
        ans_data = [user_answer, "right_answer"]
    else:
        ans_data = [user_answer, "wrong_answer"]
    ans_data_arr = ans_data_arr + [ans_data]
    task_num = task_num + 1

display(tasks, html, ans_data_arr)