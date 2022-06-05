import urllib.parse
import webbrowser
import time
import random

with open("shopping_list.txt", "r") as f:
    shopping_list = f.readlines()


urls = []
for item in shopping_list:
	item = item.strip()
	url = "https://www.tesco.com/groceries/en-GB/search?query=" + urllib.parse.quote(item)

	webbrowser.open(url, new=2)

	time.sleep(5 + random.random())
