"""Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?"""


lst = [10,15,3,7]
k = 17

i = 0
while i < len(lst):
	j = 0
	while j < len(lst):
		if lst[i] == k - lst[j]:
			print("true")
			print(lst[i])
			print(lst[j])
		j += 1
	#print("hello")
	i += 1
