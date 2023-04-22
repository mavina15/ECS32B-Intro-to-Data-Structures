# Mel Avina-Beltran
# 4/20/23
# H2 P5
# Goal: optimize quicksort function

def insertionSort(lyst, left, right): 
  i = left + 1
  while i <= right:
    itemToInsert = lyst[i] 
    j=i-1
    while j >= 0:
      if itemToInsert < lyst[j]: 
        lyst[j + 1] = lyst[j]
        j -= 1
      else: 
        break
  lyst[j + 1] = itemToInsert 
  i += 1

def quicksort(lyst): 
  quicksortHelper(lyst, 0, len(lyst) - 1)
  
def quicksortHelper(lyst, left, right):
  # insertionSort runs when list length <= 50
  if right - left <= 50:
    insertionSort(lyst, left, right) 
  else:
    pivotLocation = partition(lyst, left, right) 
    quicksortHelper(lyst, left, pivotLocation - 1) 
    quicksortHelper(lyst, pivotLocation + 1, right)

def partition(lyst, left, right):
  # finds and exchanges pivot w/ last element in list
  pivot = lyst[middle]
  lyst[middle] = lyst[right]
  lyst[right] = pivot
  # first position is boundary and items are moved if they are less than pivot
  boundary = left
  for index in range(left, right):
    if lyst[index] < pivot: 
      swap(lyst, index, boundary) 
      boundary += 1
  # pivot and boundary elements are exchanged
  swap (lyst, right, boundary)
  return boundary

def swap(lyst, i, j):
  # exchanges elements at positions i and j
  lyst[i], lyst[j] = lyst[j], lyst[i]

import random

def main(size = 1000, sort = quicksort): 
  lyst = []
  for count in range(size): 
    lyst.append(random.randint(1, size + 1))
  print(lyst) 
  sort(lyst) 
  print(lyst)

if __name__ == "__main__": main()
