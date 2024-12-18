#Set is collection of unordered items 
#Each elemet in the set must be unique and immutable

collection = {1,2,3,4,4,4,4,"Dilasha"}#ignores multiple values #unordered


print(collection)
print(len(collection))#5 cause doesn't count multiple duplicate values

# collection = set() <--Empty set
#Set is mutable elements in set is Immutable

collection.add(6)
collection.add(9)
collection.remove(2)
collection.add((2,4,6))
collection.add("Shraya")
# print(collection.clear()) #clears all the set
print(collection.pop())
print(collection)