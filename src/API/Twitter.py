from _ctypes import Array

import twitter
import json
import io

twAPI = twitter.api.Api(consumer_key='eHBEWz1pxz0kGiNLX5k5R9wtn',
                        consumer_secret='ixGGmExOptTC8bSiwMqjipBYq4JE1CiO6vju5Uea09RbOdnr8E',
                        access_token_key='1110228799445041160-NPf6ez5OmNolxzxPxQAICuaRkMq3zj',
                        access_token_secret='FPZdxqCiM7sdX5UMNkruHl4nG4V0jwMoN2s1PySvAfOGz')


def getRandomSample():
    #statuses = twAPI.GetStreamFilter(locations='-179.9,-89.9,179.9,89.9',
    #                                 languages="en")
    statuses = twAPI.GetStreamSample()
    return statuses


def getFollowers(screen_name=None, user_id=None):
    user = getUser(screen_name=screen_name, user_id=user_id)
    return user.followers_count


def getUser(screen_name=None, user_id=None):
    user = twAPI.GetUser(screen_name=screen_name, user_id=user_id)
    return user


def getScreenName(user_id=None):
    user = getUser(user_id=user_id)
    return user.screen_name


def getStatusStats(status_id=None):
    status = twAPI.GetStatus(status_id=status_id)
    return status


def getRetweets(status_id=None):
    status = twAPI.GetRetweets(status_id)
    return status