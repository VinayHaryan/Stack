
def decodeAtIndex(S,K):
    i=0
    count=0
    while i<len(S):
        if S[i].isnumeric():
            if (int(S[i])-1)*count>=K:
                i=0
                count=0
                continue
            else:
                K-=(int(S[i])-1)*count
                count+=(int(S[i])-1)*count
        else:
            K-=1
            count+=1
            if K==0:
                return S[i]
        i+=1


S = "leet2code3"
K = 10
print(decodeAtIndex(S,K))

