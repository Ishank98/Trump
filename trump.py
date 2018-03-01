import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
from pprint import pprint
import datadotworld
from collections import Counter
data1= json.load(open('/home/ishank/Downloads/2017-11-01.json'))
data2= json.load(open('/home/ishank/Downloads/2017-11-02.json'))
data3= json.load(open('/home/ishank/Downloads/2017-11-03.json'))
# Joining all the dataset from 2017-11-01 to 2017-11-03 and storing them to result
result = data1 + data2 + data3
result1 = result.copy()


# Defining a function to solve questions:
def search(result):
    # to add all the accounts tweeting about donald trump
    a = 0
    # total number of accounts
    c = 0
    # creating a list of screen_name's of accounts tweeting about donald trump
    df = []
    # dataset which contains data of only trump related tweets
    trump = []
    for element in result:
        c += 1
        if "trump" in element['text'].lower():
            a += 1
            df.append(element['screen_name'])
            trump.append(element)
        elif "donald" in element['text'].lower():
            a += 1
            df.append(element['screen_name'])
            trump.append(element)
        elif "potus" in element['text'].lower():
            a += 1
            df.append(element['screen_name'])
            trump.append(element)
    print("Reference to all tweets about Donald Trump:")
    pprint(trump)
    print(" ")
    print(" ")
    print(" ")
    print("The number of accounts tweeting about Donald Trump are:")
    print(a)
    print("Hence,the % of accounts tweeting about Donald Trump is:")
    print(a * 100 / c)
    print("Order of accounts by the frequency of tweets about Trump")
    y=Counter(df)
    sortedlist=sorted(y, key=y.get, reverse=True)
    for value in sortedlist:
        for cv in trump:
            if value in cv['screen_name']:
                pprint(cv)
                break




    print(" ")
    print("")
    print("Solution of the Bonus Question:")

    # to add all the positive twwets about donald trump
    i = 0
    # creating a list of positive tweeter
    df1 = []
    for element in trump:
        if "good" in element['text'].lower():
            i += 1
            df1.append(element['screen_name'])
        elif "very good" in element['text'].lower():
            i += 1
            df1.append(element['screen_name'])
        elif "nice" in element['text'].lower():
            i += 1
            df1.append(element['screen_name'])

    print("The number of accounts which are positive about Donald Trump is:")
    print(i)
    print("Hence,the % of accounts which are positive about Donald Trump is:")
    print(i * 100 / a)
    print("Number of accounts with more than 50% positive tweets about Donald Trump:")

    # total number tweets about donald trump by positive tweeters
    w = []
    for key in Counter(df1):
        q = 0
        for element in trump:
            if element['screen_name'] == key:
                q += 1
        w.append(q)
    # print(w)
    # print(Counter(df1).values())
    t = np.array(list(Counter(df1).values())) / np.array(w)
    # print(t)
    g = 0
    for v in t:
        if v > 0.5:
            g += 1

    print(g)
    print("Hence, the % is:")
    print(g * 100 / a)


search(result)
