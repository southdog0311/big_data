
def checks(word):
    d = dict()
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1
    return d 
