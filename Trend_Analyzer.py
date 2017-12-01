#To import library like requests, numpy, matplotlib etc
import requests, urllib
from matplotlib.ticker import FuncFormatter
import matplotlib.pyplot as plt
import numpy as np

#This is my Access Token for access the data from Instagram
APP_ACCESS_TOKEN = '1946858049.0a70fa9.f8593965a37a472e9d9ed564dc32b7a5'

#This is the base url to access the api of the Instagram
BASE_URL = 'https://api.instagram.com/v1/'

name =[]
a=[]
b=[]


#The function to find the Trending hashag on the internet
def tag_name():
    #n=int(raw_input("How many category you want"))
    #Here you can change the number of category you want
    for i in range(4):
        names = raw_input("Enter the hashtag you want to search")
        name.append(names)
        #This is the url  to find the tags on the internet
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

        #Function to plot the graph of the trending hashtag
        def plot(x, pos):
            return '%100.0f' % (x * le-1)


        formatter = FuncFormatter(plot)

        fig, ax = plt.subplots()
        ax.yaxis.set_major_formatter(formatter)
        plt.bar(x,b)
        plt.xticks(x,name)
        plt.show()



plt.show()


#Pick up line of the project.
tag_name()