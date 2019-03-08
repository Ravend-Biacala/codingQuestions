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
