def asteroidCollision(asteroids):
    stk = []
    i = 0
    while i < len(asteroids):
        sto = asteroids[i]
        # if there is an asteroids going in positive and coming one is negative
        # hence can collide
        if len(stk) > 0 and stk[-1] > 0 and sto < 0:
            if abs(sto) > stk[-1]:
                stk.pop() 
            elif abs(sto) == stk[-1]:
                stk.pop() 
                i += 1
            else:
                i += 1
        else:
            stk.append(sto)
            i += 1
        
    return stk

asteroids = [5,10,-5]
print(asteroidCollision(asteroids))


