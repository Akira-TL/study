import json
import os
import re
import sqlite3
import requests
from selenium import webdriver
import time
file_path = 'study/pa_chong/database.db'
def writef(data:dict):
    check_file()
    a = sqlite3.connect(f'{file_path}')
    b = a.cursor()
    number = list(data.keys())[0]
    b.execute(f'''insert into imojimix (number,name,status,img_url,url) values('{number}','{data[number]["name"]}','{data[number]["status"]}','{data[number]["img_url"]}','{data[number]["url"]}')''')
    b.close()
    a.commit()
    a.close()
    print(data)

def check_file():
    try:
        with open(f'{file_path}','r') as f:
            pass
    except FileNotFoundError:
        try:
            os.mkdir('data')
        except:
            pass
        a = sqlite3.connect(f'{file_path}')
        b = a.cursor()
        b.execute('''create table imojimix(number text,name text,status integer,img_url text,url text)''')
        b.close()
        a.commit()
        a.close()


if __name__ == '__main__':
    with open(f'study/pa_chong/database.json','r') as f:
        content:dict = json.load(f)
    for key in content:
        content[key]['status'] = int(content[key]['status'])
        writef({key:content[key]})