
values = [6, 12, 8, 10, 20, 16]
freqs = [5, 4, 3, 2, 1, 5]

def median(data):
	if len(data) % 2 != 0:
		median = data[len(data)//2]
	else:
		median = (data[(len(data)//2)] + data[((len(data)-1)//2)])/2
	return median

def quartiles(arr):
	arr = sorted(arr)
	r_arr = []
	q1 = float("{:.1f}".format(median(arr[:len(arr)//2])))
	q2 = float("{:.1f}".format(median(arr)))
	r_arr.append(q1)
	r_arr.append(q2)
	if len(arr) % 2 == 0:
		q3 = float("{:.1f}".format(median(arr[(len(arr)//2):])))
		r_arr.append(q3)		
	else:
		q3 = float("{:.1f}".format(median(arr[len(arr)//2+1:])))
		r_arr.append(q3)
	return r_arr

def floaterQuartile(values, freqs):
	x = []
	for index, i in enumerate(freqs):
		x .extend([values[index]]*i)
	q1, q2, q3 = quartiles(x)
	print(q3-q1) 



	


floaterQuartile(values, freqs)