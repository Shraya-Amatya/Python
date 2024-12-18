list = [1,2,3,2,1]
copy_list = list.copy()
list.reverse()
print(list)
if copy_list == list:
    print("This list is a palindrome")
else:
    print("This list is not a palindrome")