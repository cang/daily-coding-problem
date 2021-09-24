'''
def get_step_combos(num_steps, step_sizes):
    combos = list()
    
    if num_steps < min(step_sizes):
        return combos
    
    for step_size in step_sizes:
        if num_steps == step_size:
            combos.append([step_size])
        elif num_steps > step_size:
            child_combos = get_step_combos(num_steps - step_size, step_sizes)
            for child_combo in child_combos:
                combos.append([step_size] + child_combo)
    return combos


assert get_step_combos(4, [1, 2]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2]]
assert get_step_combos(4, [1, 2, 3]) == \
    [[1, 1, 1, 1], [1, 1, 2], [1, 2, 1], [1, 3], [2, 1, 1], [2, 2], [3, 1]]


def goStairCase(n,stepsize):
	if n<=1:
		return 1
	ret=0
	for i in range(1,stepsize+1):
		ret+=goStairCase(n-i,stepsize if stepsize<=n-i else n-i)
	return ret

'''

import time

def goStairCase(n,m):
    if n<=1:
        return 1
    ret=0
    for j in range(1,m+1):
        if j<=n:
            ret+=goStairCase(n-j,m)
    return ret

#Dynamic Programming
def goStairCaseDp(n,m):
    f=[1,1]
    for i in range(2,n+1):
        ret=0
        for j in range(1,m+1):
            if j<=i:
                ret+= f[i-j]
        f.append(ret)
    return f[n]

#keep only m last element 
def goStairCaseDpOptimize(n,m):
    f = [0]*m
    f[-1]=f[-2]=1
    for i in range(2,n+1):
        ret=sum(f) #dupliate here need optimize 2
        for j in range(1,m):
            f[j-1]=f[j]
        f[m-1]=ret
        #print(f)
    return f[-1]
   
#best update
def goStairCaseDpOptimize2(n, m):
    temp = 0
    res = [1]
    for i in range(n):
        s = i - m
        #print(i,s,end=' ')
        if (s >= 0):
            temp -= res[s]
        temp += res[i]
        res.append(temp)
        #print(res)
    
    return res[n]
 
# Driver Code
n = 5
m = 3

start = time.time()
print(goStairCase(n,m),time.time() - start)

start = time.time()
print(goStairCaseDp(n,m),time.time() - start)

start = time.time()
print(goStairCaseDpOptimize(n,m),time.time() - start)

start = time.time()
print(goStairCaseDpOptimize2(n, m),time.time() - start) 
