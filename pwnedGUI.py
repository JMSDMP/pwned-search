#!/usr/bin/env python
import requests
import hashlib
from tkinter import *
from tkinter import ttk

def lookup(pwd):
    sha1pwd = hashlib.sha1(pwd.encode("utf-8")).hexdigest().upper()
    head, tail = sha1pwd[:5], sha1pwd[5:]
    url = "https://api.pwnedpasswords.com/range/" + head
    response = requests.get(url)
    response.text
    data = response.text.splitlines()
    for item in data:
        item = item.split(":")
        t, occurences = item[0], item[1]
        if t == tail:
            return occurences

def main(entry, lable):
    password = entry.get()
    print(password)
    occurences = lookup(password)
    if occurences:
        lable.configure(text = f"{password} was found {occurences} times.")
    else:
        lable.configure(f"{password} was not found")

def gui():
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    lable = ttk.Label(frm, text="Enter Password").grid(column=0, row=0)
    entry = Entry(frm).grid(column=0, row=1)
    e = entry.get()
    ttk.Button(frm, text="Search", command=lambda: main(e, lable)).grid(column=1, row=1)
    root.mainloop()

if __name__ == "__main__":
    gui()