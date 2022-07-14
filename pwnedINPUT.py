#!/usr/bin/env python
import requests
import hashlib

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

def main():
    password = input("Enter passsword: ")
    occurences = lookup(password)
    if occurences:
        print(f"{password} was found {occurences} times.")
    else:
        print(f"{password} was not found")

if __name__ == "__main__":
    main()
