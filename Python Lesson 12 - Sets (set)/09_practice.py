# Check if two lists share elements
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
set1 = set(list1)
set2 = set(list2)
shared_elements = set1 & set2
if shared_elements:
    print("Lists share elements:", shared_elements)
else:
    print("Lists do not share any elements")