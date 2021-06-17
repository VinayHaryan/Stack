
def calPoints(s):
    p = []
    for i in s:
    	if i == 'C': p.pop()
    	elif i == 'D': p.append(2*p[-1])
    	elif i == '+': p.append(p[-1]+p[-2])
    	else: p.append(int(i))
    return sum(p)


ops = ["5","-2","4","C","D","9","+","+"]
print(calPoints(ops))

