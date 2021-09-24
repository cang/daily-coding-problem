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

# Python3 program to count the number
# of ways to reach n'th stair when
# user climb 1 .. m stairs at a time.
 
# Function to count number of ways
# to reach s'th stair
def countWays(n, m):
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
 
print(countWays(n, m))
print(goStairCase(n,m))
