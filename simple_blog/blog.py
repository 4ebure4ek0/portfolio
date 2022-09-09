#!C:\Users\white\AppData\Local\Programs\Python\Python310\python.exe
coding = "utf-8"
print("Content-type: text/html; charset={}\r\n".format(coding))

import encodings
import json
import sys
from token import ENCODING
from urllib.parse import parse_qs

sys.stdout.reconfigure(encoding=coding)

file = open("./blog.html", "r")
html = file.read()
file.close()

file = open("../menu.html", "r")
menu = file.read()
file.close()
html = html.replace("<!--#menu-->", menu)

file = open("./posts.json", "r")
all_posts_json = file.read()
file.close()

all_posts = json.loads(all_posts_json)

def display(html, all_posts):
    posts_html = ""
    file = open("./post_pattern.html", "r")
    post_pattern = file.read()
    file.close()
    for cur_post in all_posts:
        post_html = post_pattern
        post_html = post_html.replace("<!--#name-->", cur_post["name"])
        post_html = post_html.replace("<!--#title-->", cur_post["title"])
        post_html = post_html.replace("<!--#content-->", cur_post["content"])
        posts_html = posts_html + post_html + "\r\n"

    html = html.replace("<!--#posts-->", posts_html)
    print(html)

data = sys.stdin.read()

#data = "name=Liza&title=Text&content=%D0%BF%D1%80%D0%B8%D0%B2%D0%B5%D1%82"
#data = ""
if data == "":
    display(html, all_posts)
else:
    parts = parse_qs(data, encoding=coding)
    name = parts["name"][0]
    title = parts["title"][0]
    content = parts["content"][0]

    post = {}
    post["name"] = name
    post["title"] = title
    post["content"] = content

    all_posts = [post] + all_posts
    display(html, all_posts)

    all_posts_json = json.dumps(all_posts, ensure_ascii=False, indent=4)

    file = open("./posts.json", "w")
    file.write(all_posts_json)
    file.close()