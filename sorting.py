# Bubble sort
# Test case: [6, 5, 3, 1, 8, 7, 2, 4]

def bubbleSort(arr):
	n = len(arr)
	for i in range(n):
		swapped = False
		for j in range(n-1-i):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
		if swapped == False:
			break 
	return arr

# test = [6, 5, 3, 1, 8, 7, 2, 4]
# sorted_test = bubbleSort(test)

def selectionSort(arr):
	n = len(arr)
	for i in range(n):
		mn_idx = i
		for j in range(i+1, n):
			if arr[j] < arr[mn_idx]:
				mn_idx = j

		if mn_idx != i:
			arr[i], arr[mn_idx] = arr[mn_idx], arr[i]
	return arr 


def insertionSort(arr):
	n = len(arr)
	for i in range(1, n):
		temp = arr[i]
		idx = i
		while idx > 0 and temp < arr[idx-1]:
			arr[idx] = arr[idx-1]
			idx -= 1
		arr[idx] = temp
	return arr


#Merge Sort Algorithm
def mergeSort(arr):
	n = len(arr)
	if n > 1:
		mid = n//2
		left = arr[:mid]
		right = arr[mid:]
		mergeSort(left)
		mergeSort(right)
		i, j, k = 0, 0, 0
		while i<len(left) and j<len(right):
			if left[i] <= right[j]:
				arr[k] = left[i]
				i += 1
			else:
				arr[k] = right[j]
				j += 1
			k += 1

		while i<len(left):
			arr[k] = left[i]
			i += 1
			k += 1

		while j<len(right):
			arr[k] = right[j]
			k += 1
			j += 1
	return arr
# test = [6, 5, 3, 1, 8, 7, 2, 4]
test = [5, 3, 1, 8, 7, 2, 4]
myList = [54,26,93,17,77,31,44,55,20]

# test = [6]
# sorted_test = bubbleSort(test)
# sorted_test = selectionSort(test)
# sorted_test = insertionSort(test)
sorted_test = mergeSort(myList)
print(sorted_test)