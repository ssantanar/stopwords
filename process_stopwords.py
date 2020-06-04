def acentos(word):
    # this fuction replace special-characters in words
    import re
    word = re.sub('á','a', word)
    word = re.sub('é','e', word)
    word = re.sub('í','i', word)
    word = re.sub('ó','o', word)
    word = re.sub('ú','u', word)
    word = re.sub('ñ','n', word)
    word = re.sub('[^a-z]',' ', word)
    word = re.compile(r'\W*\b\w{1,1}\b').sub('', word)
    word = re.sub(r'\s+',' ',word)
    return word

# read stopwords
f = open("stopwords_spanish.txt", 'r')
x = f.readlines()
f.close()
# delete \n
stopwords = [line.rstrip('\n') for line in x]
stopwords = [acentos(stopword) for stopword in stopwords]

# export
with open('stopwords_spanish.txt', 'w') as f:
    for item in stopwords:
        # write words 
        if item != '':
            f.write("%s\n" % item)
        else:
            pass
