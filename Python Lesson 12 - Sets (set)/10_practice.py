# Find elements present in one list but not other
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
set1 = set(list1)
set2 = set(list2)
unique_to_list1 = set1 - set2
unique_to_list2 = set2 - set1
print("Elements unique to list1:", unique_to_list1)
print("Elements unique to list2:", unique_to_list2)