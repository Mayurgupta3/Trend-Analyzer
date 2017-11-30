import requests, urllib
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np


APP_ACCESS_TOKEN = '1946858049.0a70fa9.f8593965a37a472e9d9ed564dc32b7a5'

BASE_URL = 'https://api.instagram.com/v1/'

name =[]
a=[]
b=[]

def tag_name():
    #n=int(raw_input("How many category you want"))
    for i in range(4):
        names = raw_input("Enter the hashtag you want to search")
        name.append(names)
        request_url = (BASE_URL + "tags/%s?access_token=%s") % (names, APP_ACCESS_TOKEN)
        print "GET request url : %s" % (request_url)
        tag_list = requests.get(request_url).json()
        if tag_list['meta']['code'] == 200:
            if len(tag_list['data']):
                a= tag_list['data']['media_count']
                b.append(a)


                print b
                print name
            else:
                print 'There is no recent post of that category'
                exit()
        else:
            print 'Status code other than 200 received'
            exit()
        x=np.arange(4)


        def plot(x, pos):
            return '%100.0f' % (x * le-1)


        formatter = FuncFormatter(plot)

        fig, ax = plt.subplots()
        ax.yaxis.set_major_formatter(formatter)
        plt.bar(x,b)
        plt.xticks(x,name)
        plt.show()



plt.show()

tag_name()