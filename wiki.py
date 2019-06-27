import wikipedia

def search():
    topic = raw_input("Search Wikipedia: ")
    a = wikipedia.page(topic)
    b = a.url
    print wikipedia.summary(topic, sentences = 10)
    print ('''
    For more information click: 
    ''') + b

search()