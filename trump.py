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
result=data1+data2+data3
result1=result.copy()

def search(result):
    #to add all the accounts tweeting about donald trump
    a=0
    #total number of accounts
    c=0
    #creating a list of screen_name's of accounts tweeting about donald trump
    df=[]
    #dataset which contains data of only trump related tweets
    trump=[]
    for element in result:
        c+=1
        if "trump" in element['text'].lower():
            a+=1
            df.append(element['screen_name'])
            trump.append(element)
        elif "donald" in element['text'].lower():
            a+=1
            df.append(element['screen_name'])
            trump.append(element)
    print("Reference to all tweets about Donald Trump:")
    pprint(trump)
    print("The number of accounts tweeting about Donald Trump are:")
    print(a)
    print("Hence,the % of accounts tweeting about Donald Trump is:")
    print(a*100/c)
    print("Order of accounts by the frequency of tweets about Trump")
    pprint(Counter(df))
    print(" ")
    print("")
    print("Solution of the Bonus Question:")


    i=0
    df1=[]
    for element in trump:
        if "good" in element['text'].lower():
            i+=1
            df1.append(element['screen_name'])
        elif "very good" in element['text'].lower():
            i+=1
            df1.append(element['screen_name'])
        elif "nice" in element['text'].lower():
            i+=1
            df1.append(element['screen_name'])


    print("The number of accounts which are positive about Donald Trump is:")
    print(i)
    print("Hence,the % of accounts which are positive about Donald Trump is:")
    print(i*100/a)
    print("Number of accounts with more than 50% positive tweets about Donald Trump:")

    w=[]
    for key in Counter(df1):
        q=0
        for element in trump:
            if element['screen_name']==key:
                q+=1
        w.append(q)
    print(w)
    print(Counter(df1).values())
    t=np.array(list(Counter(df1).values()))/np.array(w)
    print(t)
    g=0
    for v in t:
        if v>0.5:
            g+=1

    print(g)
    print("Hence, the % is:")
    print(g*100/a)
search(result)


