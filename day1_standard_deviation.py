def standard_deviation(arr):
	mean = sum(arr)/len(arr)
	ans = []
	for i in arr:
		x = (i - mean)**2
		ans.append(x)
	y = sum(ans)/len(arr)
	y = (y)**(1/2)
	print("{:.1f}".format(y))


def two_sum(nums, target):
	i = 0
	j = 1
	for i in range(len(arr)):
		for j in range(i+1, len(arr)):
			if nums[i] + nums[j] == target:
				return [i ,j]
	



arr = [2,7,11,15]
target = 9

arr2 = [3,2,4]
target2 = 6

arr3 = [3,3]
target3 = 6

arr3 = [4,4]
target3 = 8

two_sum(arr, target)
# two_sum(arr2, target2)
# two_sum(arr3, target3)
# standard_deviation(arr)