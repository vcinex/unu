#!/usr/bin/ python3

import requests

def user_choice(*choice):
    user_input = 0
    while not 1 <= user_input <= len(choice):
        for n in range(len(choice)):
            print("%d. %s" %(n+1, choice[n]))
        user_input = int(input ("Please Make a choice (only need to input the number): "))
    return choice[user_input-1]

def unu(url="https://vcinex.com", action="shorturl", format="simple",keyword=""):
    if action != "shorturl":
        action = user_choice("shorturl")
    if format != "simple":
        format = user_choice("simple","xml","json")
    unu_url="https://u.nu/api.php"
    data={"action":action,"format":format,"url":url,"keyword":keyword}
    r = requests.get(unu_url,params = data)
    return r.text
