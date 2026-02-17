# set is a collection of unique values.

nums = {10, 20, 30}
print(nums)

# Uses curly braces { }

# MOST IMPORTANT RULE 
#  Sets store ONLY UNIQUE values
nums = {10, 20, 10, 30, 20}
print(nums)

# Output:

# {10, 20, 30}

# Duplicates automatically removed.

# Creating Empty Set  (Classic Trap)

# Wrong:

s = {}
print(type(s))   # dict 

# Correct:

s = set()
print(type(s))   # set 
# 4Accessing Set Elements 

# NOT possible via index:

nums = {10, 20, 30}
# print(nums[0])   # ERROR 

# Because → unordered.

# Use loop:

for n in nums:
    print(n)