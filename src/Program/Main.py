from io import StringIO

from API import Twitter
import time
import json

io = StringIO()

statuses = Twitter.getRandomSample()

def fileprint(val):
    with open("sample.txt", 'a') as out:
        out.write(str(val))
        out.write("\n")
        #time.sleep(0.05)
    print(val)

while(True):
    tweet = statuses.__next__()
    #fileprint(tweet)
    time.sleep(0.05)


    while(tweet.get("delete") != None):
        tweet = statuses.__next__()
        #fileprint(tweet)
        time.sleep(0.05)


    fileprint("username: @" +tweet.get("user").get("screen_name"))
    fileprint("content: " + tweet.get("text"))
    fileprint("following: " + str(tweet.get("user").get("followers_count")))
    fileprint("Minutes old: " + str(int(tweet.get("timestamp_ms")) / 60000))

    #rt = Twitter.getRetweets(tweet.get("id"))

    #popularity = str(rt).__sizeof__() #  Honestly, I've been working on this for 12 hours strait now, I just don't give a shit
    # Edit: oh shit it ate all the bandwidth


    #I REALLY dont give a shit anymore
    ENDME = str(tweet).split("\'retweet_count\': ",)[1]
    ENDME = ENDME.split(", \'favorite_count\'")[0]

    fileprint("popularity: " + str(ENDME))
    fileprint("hashtags: " + str([s.get("text") for s in tweet.get('entities').get("hashtags")]))
    fileprint("\n eatshit \n")




#for val in statuses:
#    fileprint(val)




statuses.close()
