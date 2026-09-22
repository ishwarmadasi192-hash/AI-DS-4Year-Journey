#1. What is a Set?
#A set is a collection of unique values.
numbers={1,2,3,4}
#numbers={1,2,2,3,3,4}
#becomes{1,2,3,4}  Duplicates are automatically removed.
#2.why are sets usefu?
numbers={10,20,20,30,30,30,40}

#3. Adding elements to a set
numbers={10,20,30}
numbers.add(40)
#Remove from a set
numbers.remove(20)
#5.set vs list
#A set is unordered, meaning that the items do not have a defined order.
# This is important.
# List	                     Set
# Allows duplicates	         Stores unique values
# Ordered/indexable          Not index-based
# [1,2,2,3]	                 {1,2,3}
# numbers[0] works           numbers[0] doesn't work
# So don't try:
#             numbers[0]
# on a set.