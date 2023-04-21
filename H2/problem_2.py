# Mel Avina-Beltran
# 4/20/23
# H2 P2
# Goal: Optimizes linear search for sorted lists

def linearSearch(target, lyst):
  position = 0
  while position < len(lyst):
    if target == lyst[position]: 
      return position
    elif target < lyst[position]:
      return -1
    position += 1 
  return -1

def main():
  print(linearSearch(3, [0, 1, 2, 3, 4])) 
  print(linearSearch(3, [0, 1, 2]))
  print(linearSearch(3, [0, 4, 5, 6]))

if __name__ == "__main__": main()

