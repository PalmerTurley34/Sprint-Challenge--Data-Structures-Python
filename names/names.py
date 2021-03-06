import time

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
from binary_search_tree import BSTNode
bst = BSTNode(names_1[0])
for name_1 in names_1[1:]:
    bst.insert(name_1)
for n2 in names_2:
    if bst.contains(n2):
        duplicates.append(n2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
set1 = set(names_1)
set2 = set(names_2)

duplicates2 = set1.intersection(set2)
second_end_time = time.time()
print (f"{len(duplicates2)} duplicates:\n\n{', '.join(duplicates2)}\n\n")
print (f"runtime: {second_end_time - end_time} seconds")