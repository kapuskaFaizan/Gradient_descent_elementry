import matplotlib.pyplot as plt

next_x = 0  
gamma = 0.01  
precision = 0.00001  
max_iters = 1000  

# the derivative of function given is -6*(x-6)
def df(x):
    return -6*(x-6)

l =[]
for _i in range(max_iters):
    current_x = next_x
    next_x = current_x + gamma * df(current_x)
    
    print( next_x)
    l.append(next_x)
    step = next_x - current_x
    
    if abs(step) <= precision:
        break

print('(a) : The derivative is -6(x-6)')
print("(a) : Maximum at ", round(next_x))
print('(b) : value of eta smaller then 25 the algorithm proceeds directly to the maximum without oscillation.')
print('(c) : For values of eta greater than the value in (b), but smaller than 75 the algorithm oscillates around the maximum, but still converges to it. ')

plt.plot(l)
plt.show()
