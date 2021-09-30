# not use dict
def find_index(arr,l,r,x):
	if l>r:
		return -l-1
	mid=(l+r)//2
	if x==arr[mid]:
		return mid
	elif x<arr[mid]:
		return find_index(arr,l,mid-1,x)
	else:
		return find_index(arr,mid+1,r,x)

def min_classroom(arr):
	arr=sorted(arr)
	prevmax=0
	cur_lst = [arr[0][0],arr[0][1]]
	cur_roomlst = [1]

	print(0,cur_lst,cur_roomlst,prevmax)

	for i in range(1,len(arr)):
		il=find_index(cur_lst,0,len(cur_lst)-1,arr[i][0])
		if il<0:
			il=-il-1
			#out side the right of cur list
			if il>=len(cur_lst):
				prevmax=max(prevmax,max(cur_roomlst))
				cur_lst=[arr[i][0],arr[i][1]]
				break
			else:
				cur_lst= cur_lst[:il] + [arr[i][0]] + cur_lst[il:]
				cur_roomlst= cur_roomlst[:il] + [cur_roomlst[il-1]] + cur_roomlst[il:]

		for j in range(il):
			prevmax=prevmax if prevmax>cur_roomlst[j] else cur_roomlst[j]
		
		cur_lst= cur_lst[il:]
		cur_roomlst=cur_roomlst[il:]
		il=0
		
		ir=find_index(cur_lst,0,len(cur_lst)-1,arr[i][1])
		if ir<0:
			ir=-ir-1
			#out side the right of cur list
			if ir>=len(cur_lst):
				ir=len(cur_lst)-1
				cur_lst=cur_lst + [arr[i][1]]
				cur_roomlst = cur_roomlst + [1]
			else:
				cur_lst= cur_lst[:ir] + [arr[i][1]] + cur_lst[ir:]
				cur_roomlst= cur_roomlst[:ir] + [cur_roomlst[ir-1]] + cur_roomlst[ir:]

		for j in range(il,ir):
			cur_roomlst[j]+=1

		print(i,cur_lst,cur_roomlst,prevmax,il,ir)

	return max(max(cur_roomlst),prevmax)


a = [(30, 75), (0, 50), (60, 150)]
print(min_classroom(sorted(a)))





'''
def get_num_classrooms(timing_tuples):
    if not timing_tuples:
        return 0

    start_times = dict()
    end_times = dict()
    for start, end in timing_tuples:
        if start not in start_times:
            start_times[start] = 0
        start_times[start] += 1

        if end not in end_times:
            end_times[end] = 0
        end_times[end] += 1

    global_start, global_end = min(start_times), max(end_times)

    max_class_count = 0
    current_class_count = 0
    for i in range(global_start, global_end):
        if i in start_times:
            current_class_count += start_times[i]
            if current_class_count > max_class_count:
                max_class_count = current_class_count
        if i in end_times:
            current_class_count -= end_times[i]

    return max_class_count


assert get_num_classrooms([]) == 0
assert get_num_classrooms([(30, 75), (0, 50), (60, 150)]) == 2
assert get_num_classrooms([(30, 75), (0, 50), (10, 60), (60, 150)]) == 3
assert get_num_classrooms([(60, 150)]) == 1
assert get_num_classrooms([(60, 150), (150, 170)]) == 2
assert get_num_classrooms([(60, 150), (60, 150), (150, 170)]) == 3
'''

