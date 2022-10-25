file = open ("data.txt", 'r', encoding='UTF-8')
s = file.readlines()
numbers = [int(x) for x in s]
print(min(numbers))
print(max(numbers))
print(min(numbers)+max(numbers))
index = numbers.index(max(numbers))
print('максимальный индекс равен:', index)
