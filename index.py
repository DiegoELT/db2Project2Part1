from fileToStructure import *
import math
tweetIds = jsonToDict("idTerminos.json")
df = jsonToDict("documentFrequency.json")

def weightTweet(id, token):
    if token in  tweetIds[id]:
        tf = 1
    else:
        tf = 0
    if token in df.keys():
        n = len(tweetIds.keys())
        b = math.log(n/df[token], 10)
    else:
        b = 0
    return tf * b

def weightQuery(query):
    tf = {}
    for token in query:
        if token in tf.keys():
            tf[token] = tf[token] + 1
        else:
            tf[token] = 0
    n = len(tweetIds.keys())
    for token in tf.keys():
        tf[token] = math.log(tf[token] + 1, 10)
        tf[token] = tf[token] * math.log(n/df[token], 10)
    return tf


def queryWeightPerDoc(tokens):
    tokens
    result = {}
    for id in tweetIds.keys():
        sum1 = 0
        sum2 = 0
        sum3 = 0
        qs = weightQuery(tokens)
        for i in tokens:
            qi = qs[i]
            di = weightTweet(id, i)
            sum1 = sum1 + (qi * di)
            sum2 = sum2 + (qi * qi)
            sum3 = sum3 + (di * di)
        b = (math.sqrt(sum2)) * (math.sqrt(sum3))
        if b == 0:
            cos = 0
        else :
            cos = float(sum1) / float(b)
        result[id] = cos
    
    return result

