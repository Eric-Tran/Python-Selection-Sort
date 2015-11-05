import random
arr = random.sample(xrange(1,100),10)

def selectionsort(a):
	for i in range(0, len(a)):
		min = i
		for x in range (i+1, len(a)):
			if a[x] < a[min]:
				min = x
		a[min], a[i] = a[i], a[min]
	print a

selectionsort(arr)





		





