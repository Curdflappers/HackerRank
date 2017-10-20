#!/bin/python3

import sys

def isBalanced(s):
  if(len(s)) == 0:
    return True
  pairing = {"{": "}", "(":")", "[":"]"}
  first = s[0]
  try:
  	match = pairing[first]
  except:
    return False
  
  openings = 0;
  for i in range(1, len(s)):
    if s[i] == first:
      openings += 1
    elif s[i] == match and openings == 0:
      return isBalanced(s[1:i]) and isBalanced(s[i+1:])
    elif s[i] == match:
      openings -= 1
  
  return False


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        s = input().strip()
        result = isBalanced(s)
        if result:
            print("YES")
        else:
            print("NO")
