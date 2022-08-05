import json
import os
import re
import sqlite3
from tkinter.messagebox import NO
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

def qucong():
    check_file()
    cnt = True
    while cnt:
        a = sqlite3.connect(f'{file_path}')
        b = a.cursor()
        b.execute('''select * from imojimix''')
        last = b.fetchone()
        next = b.fetchone()
        while next:
            if last == next:
                sql = f'delete from imojimix where number = ?'
                b.execute(sql,(f'{next[0]}',))
                print(f'删除{next[0]}')
            print(last[0])
            last = next
            next = b.fetchone()
            if next == None:
                next = b.fetchone()
            if next == '20-171':
                cnt = False
        # number = list(data.keys())[0]
        # b.execute(f'''insert into imojimix (number,name,status,img_url,url) values('{number}','{data[number]["name"]}','{data[number]["status"]}','{data[number]["img_url"]}','{data[number]["url"]}')''')
        b.close()
        a.commit()
        a.close()
    # print(data)

def c():
    a = sqlite3.connect(f'{file_path}')
    b = a.cursor()
    b.execute('''select * from imojimix''')
    last = b.fetchone()
    next = b.fetchone()
    content = {}
    while True:
        c = re.findall('\d+',last[0])[-1]
        if next == None:
            break
        d = re.findall('\d+',next[0])[-1]
        # print(int(c) - int(d))
        last = next
        if int(d) - int(c) == 1:
            pass
        else:
            e,f = tuple(re.findall('\d+',last[0]))
            if e != f:
                print(last)
                data = {last[0]:[e,f]}
                content.update(data)
        next = b.fetchone()
    print(content)
    b.close()
    a.commit()
    a.close()
# print(data)

def delet():
    a = sqlite3.connect(f'{file_path}')
    b = a.cursor()
    c = '59-122'
    d = 'https://www.gstatic.com/android/keyboard/emojikitchen/20201001/u1f927/u1f927_u1f336-ufe0f.png'
    b.execute(f"delete from imojimix where number='{c}' and img_url='{d}'")
    b.close()
    a.commit()
    a.close()


if __name__ == '__main__':
    delet()