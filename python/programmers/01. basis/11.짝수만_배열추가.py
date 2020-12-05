my_list = [3, 2, 6, 7]
answer = []

for item in my_list:
    if not (item%2):
        answer.append(item**2)

# fot/if 동시에
answer_2 = [ i**2 for i in my_list if i %2 == 0]

print(anwer)
print(answer_2)