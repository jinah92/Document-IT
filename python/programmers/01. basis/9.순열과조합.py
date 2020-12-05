import itertools

def solution(mylist):
    mylist.sort()
    return list(map(list, itertools.permutations(mylist)))