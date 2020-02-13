import matplotlib.pyplot as plt

next_x = 0  # We start the search at x=0 and y=0
gamma = 0.01  # Step size multiplier
precision = 0.00001  # Desired precision of result
max_iters = 1000  # Maximum number of iterations

# the derivative of function given is -6*(x-6)
def df(x,y):
    return -2*(x-2)+(-6*(x-6))


l =[]
for _i in range(max_iters):

    current_x = next_x
    next_x = current_x + gamma * df(current_x,current_x)
    
    print( next_x)
    l.append(next_x)
    step = next_x - current_x
    
    if abs(step) <= precision:
        break

print('(a) : The derivative is -2*(x-2)+(-6*(x-6))')
print("(a) : Maximum at ", round(next_x))
print('(b) : value of eta smaller then 20 the algorithm proceeds directly to the maximum without oscillation.')
print('(c) : For values of eta greater than the value in (b), but smaller than 50 the algorithm oscillates around the maximum, but still converges to it. ')

plt.plot(l)
plt.show()
