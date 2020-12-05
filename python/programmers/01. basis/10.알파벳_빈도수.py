import collections

my_str = input().strip()

counter = collections.Counter(my_str).most_common()

answer = ''

for i in range(len(counter)):
    if counter[i][1] == counter[0][1]:
        answer += counter[i][0]

return 