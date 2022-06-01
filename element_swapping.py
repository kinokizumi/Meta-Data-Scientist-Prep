#!/usr/bin/python3

def countSmaller(arr_a, arr_b):
  i = 0
  count = 0
  while arr_a[i] < arr_b[i] and i < len(arr_a):
    count += 1
    i += 1
  return count

def findMinArray(arr, k):
  # Write your code here
  queue = [[3, 0, arr]]
  visited = [arr]
  max_pairs = 0
  output = arr
  
  while queue and k > 0:
    k, count, curr = queue.pop(0)
      
    for i in range(len(curr)-1):
      swap = curr[:i] + curr[i+1:i+2] + curr[i:i+1] + curr[i+2:]
      if swap not in visited:
        visited.append(swap)
        count = countSmaller(swap, arr)      
        queue.append([k-1, count, swap])
        if count > max_pairs:
          max_pairs = count
          output = swap

  return output


# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 3
  arr_1 = [5, 3, 1]
  k_1 = 2 
  expected_1 = [3, 1, 5]
  output_1 = findMinArray(arr_1,k_1)
  check(expected_1, output_1)

  n_2 = 5
  arr_2 = [8, 9, 11, 2, 1]
  k_2 = 3
  expected_2 = [2, 8, 9, 11, 1]
  output_2 = findMinArray(arr_2,k_2)
  check(expected_2, output_2)
