"""Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?"""


lst = [1,2,3,4,5]
lst2 = [3,2,1]

newlst = []

for i in lst:

	total = 1
	for j in lst:
		if i != j:
			total *= j

	newlst.append(total)


print(newlst)
