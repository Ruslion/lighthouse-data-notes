#!/usr/bin/env python
# coding: utf-8

# In[33]:


import twitter
import json
import os
import requests as req
import datetime
# ADD OTHER PACKAGES WE WILL NEED
# <HERE>


# **Task:** Load the values of access tokens and keys from environmental variables to python variables

# In[34]:


consumer_key = os.environ["TWITTER_KEY"]
consumer_secret = os.environ["TWITTER_SECRET"]
access_token = os.environ["TWITTER_TOKEN_ACCESS"]
access_token_secret = os.environ["TWITTER_TOKEN_SECRET"]


# In[35]:


api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                 access_token_key=access_token,
                 access_token_secret=access_token_secret)


# In[36]:


# Checking the type of api object
print(type(api))


# In[46]:


## FOLLOWING FUNCTION WILL COLLECT REAL-TIME TWEETS IN OUR COMPUTER

# data returned will be for any tweet mentioning strings in the list FILTER
#FILTER = ['#datascience']

# Languages to filter tweets by is a list. This will be joined by Twitter
# to return data mentioning tweets only in the english language.
#LANGUAGES = ['en']


def main():
    date_now=datetime.datetime.now()
    date_now = date_now.strftime("%Y-%m-%d %Hh%Mm%Ss")
    with open(input("Please select folder to store the data: ") + "\output " + str(date_now) + ".txt", 'a') as f:
        # api.GetStreamFilter will return a generator that yields one status
        # message (i.e., Tweet) at a time as a JSON dictionary.
        count=0
        filter_str= input("Please input filter (use ',' as a delimiter): ")
        list_filter=filter_str.split(",")
        lang_str=input("Please input languages (use ',' as a delimiter): ")
        list_lang = lang_str.split(",")
        for line in api.GetStreamFilter(track=list_filter, languages=list_lang):
            f.write(json.dumps(line))
            f.write('\n')
            count+=1
            if count > 200: #This is implemeted to limit the number of tweets
                f.close()
                break
        return


# In[47]:


# Execute function
main()


# **Task:** Edit function `main` so it can store tweets anywhere (location specified as parameter). The FILTER and LANGUAGES should be parameters as well. Test it with different values and languages.

# **Task:** Create File `stream_tweets.py` that can be executed from the Terminal

# **Task:** Start storing tweets with either happy smiley (`:)`) or sad smiley (`:(`). We will use this dataset during the NLP section.

# In[ ]:




