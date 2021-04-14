#Time complexity:
#Worst-case performance - O(n2)
#best-case performance - O(n log n) (simple partition) or O(n) (three-way partition and equal keys)
#Average performance - O(n log n)
#Worst-case space complexity -	O(n) auxiliary (naive) and O(log n) auxiliary

def partition(arr, low, high): 
	i = (low-1)		 # index of smaller element 
	pivot = arr[high]	 # pivot 

	for j in range(low, high): 
		if arr[j] <= pivot: 
			# increment index of smaller element 
			i = i+1
			arr[i], arr[j] = arr[j], arr[i] 

	arr[i+1], arr[high] = arr[high], arr[i+1] 
	return (i+1) 

def quickSort(arr, low, high): 
	if len(arr) == 1: 
		return arr 
	if low < high: 
		pi = partition(arr, low, high) 
		quickSort(arr, low, pi-1) 
		quickSort(arr, pi+1, high) 

#taking user input for sorting
arr = [] 
n = int(input("Enter the number of elements to be sorted : "))
for i in range(0,n):
    element = int(input())
    arr.append(element) 
n = len(arr) 
quickSort(arr, 0, n-1) 
print("Sorted array is:") 
for i in range(n): 
	print("%d" % arr[i]), 


