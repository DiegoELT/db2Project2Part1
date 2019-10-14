from index import *
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords

idText = jsonToDict("idText.json")


#se agrega la función acá para que no ejecutar preprocessing solo por esta función
def preprocessing(tweet):
    sw = set(stopwords.words('spanish')) 
    tokens = word_tokenize(tweet) 
    
    words = [] 
    stemmer = PorterStemmer()

    for token in tokens:
        if token not in sw: 
            token = stemmer.stem(token)
            words.append(token) 
    return words

def query(sentence):
    tokens = preprocessing(sentence)
    result = queryWeightPerDoc(tokens)
    return result

def topTen(q):
    result = query(q)
    sortedResult = sorted(result.items(), key=lambda kv: kv[1], reverse= True)
    top = []
    for i in range(10):
        top.append(sortedResult[i][0])
    print("Query: " + q + "\n")
    for i in top:
        print(idText[i])
        print("\n")
    print("Fin de la búsqueda. \n")
    
