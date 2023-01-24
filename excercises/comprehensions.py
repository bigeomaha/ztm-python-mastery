some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# REMOVE DUPLICATES, DO NOT USE A SET
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)


# Simplify using comprehensions
duplicates = list(set([
    val for val in some_list
        if some_list.count(val) > 1
]))

print(duplicates)


