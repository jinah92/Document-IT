def isSquare(n):
    if n == 1:
        return False
    return int(n ** 0.5) ** 2 == n

numbers = [int(input()) for _ in range(5)]
result = ''

for item in numbers:
    if (isSquare(item)):
        result = 'found'
        break
    result = 'not found'
    
print(result)