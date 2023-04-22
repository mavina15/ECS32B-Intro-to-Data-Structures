# Mel Avina-Beltran
# 4/20/23
# H2 P3
# Goal: Defines an efficient function that reverses the elements in a list

def reverse(lyst):
  # first element of list
  left = 0
  # last element of list
  right = len(lyst) - 1
  while left < right:
    swap(lyst, left, right) 
    # continues next iterations accordingly
    left += 1
    right -= 1

# swap function exchanges positions of two items in list
def swap(lyst, x, y):
  lyst[x], lyst[y] = lyst[y], lyst[x]

def main():
  # list range creates list of n numbers to reverse and print
  lyst = list(range(4)) 
  reverse(lyst)
  print(lyst)
  lyst = list(range(3)) 
  reverse(lyst)
  print(lyst)

if __name__ == "__main__": 
  main()
