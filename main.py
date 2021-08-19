# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import datetime
import subprocess

import requests
import json

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':

    # d1 = datetime.datetime.strptime('2021-04-01', '%Y-%m-%d')
    # delta = d1 + datetime.timedelta(hours=25)
    # print(d1)
    # print(delta)
    # print((delta - d1).days * 24 + (delta - d1).seconds/3600)

    # subprocess.Popen('pip list', shell=True)

    # tes()

    print("dasdas")
    # url = "https://livescore6.p.rapidapi.com/matches/v2/list-live"
    url = "https://prod-public-api.livescore.com/v1/api/react/date/soccer/20210818/5.00?MD=1"

    querystring = None#{"Category": "soccer"}

    headers = {
        # 'path': "/v1/api/react/date/soccer/20210818/5.00?MD=1",
        # 'x-rapidapi-host': "livescore6.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    con = (response.json())
    l = list(dict(con)['Stages'])


    # print(response.content)
    # print(l)
    print(len(l))
    # print(dict(l[0]))
    # print(dict(l[4]))
    print(list(dict(l[0])['Events'])[0])

    print("asdasda")
