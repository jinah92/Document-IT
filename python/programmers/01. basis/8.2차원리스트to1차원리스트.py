import itertools

def solution(mylist):
    return list(itertools.chain(*mylist))