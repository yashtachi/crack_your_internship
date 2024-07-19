def printDups(Str):

    d = {}
    for i in Str:
        d.setdefault(i,0)
        d[i]+=1
        
    for it,it2 in d.items():   
        if (it2 > 1):   
            print(str(it) + ", d = "+str(it2))
    

