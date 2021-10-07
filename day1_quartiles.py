
def median(data):
	if len(data) % 2 != 0:
		median = data[len(data)//2]
	else:
		median = (data[(len(data)//2)] + data[((len(data)-1)//2)])/2
	return median

def quartiles(arr):
	arr = sorted(arr)
	r_arr = []
	q1 = "{:.0f}".format(median(arr[:len(arr)//2]))
	q2 = "{:.0f}".format(median(arr))
	r_arr.append(q1)
	r_arr.append(q2)
	if len(arr) % 2 == 0:
		q3 = "{:.0f}".format(median(arr[(len(arr)//2):]))
		r_arr.append(q3)		
	else:
		q3 = "{:.0f}".format(median(arr[len(arr)//2+1:]))
		r_arr.append(q3)
	return r_arr


test_case1 = [3, 7, 8, 5, 12, 14, 21, 13,18] #['6', '12', '16']
test_case2 = [3 ,7 ,8, 5 ,12 ,14 ,21 ,15 ,18 ,14] #7 13 15
test_case3 = [4 ,17 ,7 ,14 ,18, 12 ,3, 16 ,10 ,4 ,4 ,12] #4 11 15
quartiles(test_case1)
quartiles(test_case2)
quartiles(test_case3)
