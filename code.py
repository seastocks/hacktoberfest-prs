from time import sleep
'''
we are given two lists and we have to find out if these two lists are
made of same elements.

Algorithm1:
len(d1) = n1
len(d2) = n2

assume n1 always < n2

n1*log(n1) + n2*log(n1)

Algorithm2:
We'll use array as a hashmap
array has two things, index and value
we can store something at a given index

'''
def algorithm1(d1, d2):
    if(len(d1) > len(d2)):
        d1,d2 = d2,d1
    d1.sort()
    for item in d2:
        if not isPresent(item, d1):
            return False
    return True

def isPresent(item, nums):
    low = 0
    high = len(nums) - 1
    while(low <= high):
        mid = low + (high-low)//2
        if nums[mid] == item:
            return True
        elif item < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

def algorithm2(d1, d2):
    n1 = max(max(d1), max(d2)) + 10
    _counts = [-1]*n1
    for item in d1:
        _counts[item] += 1
    for item in d2:
        if _counts[item] == -1:
            return False
    return True




def _main_():
    d1 = [3,3,2,1,2,4]
    d2 = [1,2,3,4]
    print(algorithm2(d1, d2))

_main_()