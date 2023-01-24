#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats

cat1 = Cat('billy', 5)
cat2 = Cat('susan', 6)
cat3 = Cat('Snickers', 1)

# 2 Create a function that finds the oldest cat

def getOldestCat(cats):
    oldest_age = 0
    for cat in cats:
        if cat.age > oldest_age:
            oldest = cat
            oldest_age = cat.age

    return oldest


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

print(f'The oldest cat is {getOldestCat([cat1, cat2, cat3]).age} years old.')