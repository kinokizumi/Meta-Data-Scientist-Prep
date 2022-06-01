#!/usr/bin/python3

open_list = '([{'
close_list = ')]}'

def isBalanced(s):
  # Write your code here
  stack = []
  for elem in s:
    if elem in open_list:
      stack.append(elem)
    elif elem in close_list:
      pos = close_list.index(elem)
      if len(stack)>0 and open_list[pos] == stack[-1]:
        stack.pop()
        
  if len(stack) == 0:
    return True
  else:
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
  s1 = "{[(])}"
  expected_1 = False
  output_1 = isBalanced(s1)
  check(expected_1, output_1)

  s2 = "{{[[(())]]}}"
  expected_2 = True
  output_2 = isBalanced(s2)
  check(expected_2, output_2)

