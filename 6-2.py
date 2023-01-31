# 2) Дан список, вывести отдельно буквы и цифры, пользуясь filter.

# [12,'sadf',5643] ---> ['sadf'] ,[12,5643]

spisok = [12,'sadf',5643]
print(spisok)
numbers = filter(lambda x: type(x) == int, spisok)
letters = filter(lambda x: type(x) == str, spisok)

print(list(numbers), list(letters))