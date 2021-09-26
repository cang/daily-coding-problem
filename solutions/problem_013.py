'''
def get_longest_sub_with_k_dist(s, k):
    if not s:
        return ""
    elif len(s) <= k:
        return s
    elif k == 1:
        return s[0]

    distinct_char_count = 0
    seen_chars = set()
    candidate = None
    remaining_string = None

    # to keep track of where the second character occurred
    first_char = s[0]
    second_char_index = 0
    while s[second_char_index] == first_char:
        second_char_index += 1

    candidate = s
    for index, char in enumerate(s):
        if char not in seen_chars:
            seen_chars.add(char)
            distinct_char_count += 1

        if distinct_char_count > k:
            candidate = s[:index]
            remaining_string = s[second_char_index:]
            break
            
    longest_remaining = get_longest_sub_with_k_dist(remaining_string, k)
    
    longest_substring = None
    if len(candidate) < len(longest_remaining):
        longest_substring = longest_remaining
    else:
        longest_substring = candidate
    return longest_substring


assert get_longest_sub_with_k_dist("abcba", 2) == "bcb"
assert get_longest_sub_with_k_dist("abccbba", 2) == "bccbb"
assert get_longest_sub_with_k_dist("abcbbbabbcbbadd", 2) == "bbbabb"
assert get_longest_sub_with_k_dist("abcbbbaaaaaaaaaabbcbbadd", 1) == "a"
assert get_longest_sub_with_k_dist("abccbba", 3) == "abccbba"
'''

import time 

#original
def longest_k_substring(s,k):
    n=len(s)
    maxlen=0
    reti=retj=0
    for i in range(n):
        kset=set()
        j=i
        while j<n:
            kset.add(s[j])
            if len(kset)>k:
                break #end sequence
            j+=1

        if j-i>maxlen:
            maxlen=j-i #+1-1=0
            reti=i
            retj=j
    return s[reti:retj]

def longest_k_substring_one_loop(s,k):
    n=len(s)
    maxlen=0
    i=j=reti=retj=0
    kset=set()
    while j<n:
        kset.add(s[j])
        if len(kset)>k:
            c=s[i]
            while i<j and c==s[i]:
                i+=1
            kset.discard(c)
        
        if j-i>maxlen:
            maxlen=j-i
            reti=i
            retj=j
        
        #print(i,j,reti,retj,s[j],kset)
        
        j+=1
    
    return s[reti:retj+1]


#print(ord('z')-ord('a'))
s=''
n=1000
for i in range(n):
    s+= chr(ord('a')+i%25)
print(s)

start = time.time()
print(longest_k_substring(s,10))
print(time.time() - start)

start = time.time()
print(longest_k_substring_one_loop(s,10))
print(time.time() - start)
