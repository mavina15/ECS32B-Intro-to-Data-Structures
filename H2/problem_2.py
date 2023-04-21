# Mel Avina-Beltran
# 4/20/23
# H2 P2
# Goal: Modified version of sequential search for sorted lists

def seqSearch(target, lyst):
  i = 0
  # completes n searches of position and length of lyst
  # as position is less than the length of list 
  while i < len(lyst):
  # if the target is equal to the list position, returns the position
    if target == lyst[i]: 
      return i
  # if the target is less than the list position, returns the position - 1 
    elif target < lyst[i]:
      return -1
  # else returns the position + 1 to satrt search over again
    i += 1 
  return -1

# prints sorted list
def main():
  print(seqSearch(3, [0, 1, 2, 3, 4])) 
  print(seqSearch(3, [0, 1, 2]))
  print(seqSearch(3, [0, 4, 5, 6]))

if __name__ == "__main__": main()
