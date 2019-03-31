

def rawDataToList(rawData, lineBreaker):
    list = rawData.split(lineBreaker)
    return list


def getContent(TrainingSample):
    tire = TrainingSample.split("content: ")[1]
    #and
    depression = tire.split("\nfollowing: ")[0]
    return str(depression)  # I know it's bad, but i'm too tired to rewrite the data collector.


def getPopularity(TrainingSample):
    depressed = TrainingSample.split("popularity: ")[1]
    #and
    lonely = depressed.split("\nhashtags: ")[0]
    return int(lonely)  # I know it's bad, but i'm too tired to rewrite the data collector.


def getFollowers(TrainingSample):
    intense = TrainingSample.split("following: ")[1]
    pain = intense.split("\nMinutes old: ")[0]
    return int(pain)  # I know it's bad, but i'm too tired to rewrite the data collector.


def parseTrainingSampleToJson(TrainingSample):
    content = getContent(TrainingSample)
    followers = getFollowers(TrainingSample)
    popularity = getPopularity(TrainingSample)
    json = {
        "input": {
            "content": content,
            "following": followers
        },
        "output": {
            "popularity": popularity
        }
    }
    return json

def parseListToJsonList(list):
    i = 0
    jsonlist = []
    amount = len(list)
    print("parsing " + str(amount))
    while(i < amount):
        json = parseTrainingSampleToJson(list[i])
        jsonlist.insert(i, json)
        print(i)
        i = i + 1
    return jsonlist
