def minOperations(logs):

    res = 0
    for val in logs:
        if(val  ==  "../"):
            if res: res-=1
        elif(val != "./" ) :  # to count for operations such as d1/ , d21/ 
            res+=1
    return res

logs = ["d1/","d2/","./","d3/","../","d31/"]
print(minOperations(logs))
