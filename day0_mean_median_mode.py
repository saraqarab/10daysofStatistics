from testcase3_day0_mean_median_mode import x
import json


def get_stats(data):
    data = [int(i) for i in data.split(" ")]
    x=sum(data)
    print(x/len(data))
    median(data)
    mode(data)
   
   
def median(data): 
    if len(data)%2 != 0:
        median = data[len(data)//2]
        print("{:.1f}".format(median))
    else:
        d = sorted(data)
        n = len(data)
        m = n - 1
        data = sorted(data)
        median = data[(n//2)] + data[(m//2)]
        print("{:.1f}".format(median/2))

def mode(data):
    freq = 0
    mode = 0
    dictionary = dict()
    for num in data:
        if num not in dictionary:
            dictionary[num] = 1
        else:
            dictionary[num] = dictionary[num] + 1

    for val, count in dictionary.items():
        if count > freq:
            mode = val
            freq = count
            
        elif count == freq and val < mode:
            mode = val
    print(mode)



get_stats(x)
