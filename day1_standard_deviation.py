

def standard_deviation(arr):
	mean = sum(arr)/len(arr)
	ans = []
	for i in arr:
		x = (i - mean)**2
		ans.append(x)
	y = sum(ans)/len(arr)
	y = (y)**(1/2)
	print("{:.1f}".format(y))



arr =[10, 40, 30, 50, 20]
standard_deviation(arr)