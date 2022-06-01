#!/usr/bin/python3

from collections import deque
# Add any extra import statements you may need here


# Add any helper functions you may need here


def minOverallAwkwardness(arr):
  # Write your code here
  arr = sorted(arr)
  seats = deque()
  max_awkward = 0
  
  while arr:
    min_arr_l = arr.pop(0)
    seats.appendleft(min_arr_l)
    if arr:
      min_arr_r = arr.pop(0)
      seats.append(min_arr_r)      
    
    awkward = max([abs(min_arr_l - seats[1]), abs(min_arr_r - seats[-2])])
    if max_awkward < awkward:
      max_awkward = awkward
    
  return max_awkward

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [5, 10, 6, 8]
  expected_1 = 4
  output_1 = minOverallAwkwardness(arr_1)
  check(expected_1, output_1)

  arr_2 = [1, 2, 5, 3, 7]
  expected_2 = 4
  output_2 = minOverallAwkwardness(arr_2)
  check(expected_2, output_2)
  
  arr_3 = [1, 8, 3, 7, 12, 14]
  expected_3 = 6
  output_3 = minOverallAwkwardness(arr_3)
  check(expected_3, output_3)
