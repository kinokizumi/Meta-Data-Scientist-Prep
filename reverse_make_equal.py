#!/usr/bin/python3

def are_they_equal(array_a, array_b):
  # Write your code here
  queue = [array_b]
  visited = [array_b]
  
  while queue:
    curr = queue.pop(0)
    if curr == array_a:
      return True
    
    for i in range(len(curr)-1):
      for j in range(i+1, len(curr)):
        solution = curr[:i] + list(reversed(curr[i:j+1])) + curr[j+1:]
        if solution not in visited:
          visited.append(solution)
          queue.append(solution)

  return False

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.
def printString(string):
  print('[\"', string, '\"]', sep='', end='')

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
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 4
  a_1 = [1, 2, 3, 4]
  b_1 = [1, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 4, 3, 2]
  b_2 = [1, 2, 3, 5]  
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)

  n_3 = 4
  a_3 = [1, 4, 3, 2]
  b_3 = [1, 3, 2, 4]  
  expected_3 = True
  output_3 = are_they_equal(a_3, b_3)
  check(expected_3, output_3)
