#!/usr/bin/python3

def canGetExactChange(targetMoney, somme, denominations):
  # Write your code here

  if somme == targetMoney:
    return True
  elif len(denominations) == 0 and somme != targetMoney:
    return False

  if len(denominations) != 0:
    change = denominations.pop()
    if targetMoney%change == 0:
      return True
    while change <= targetMoney - somme:
      somme += change
      print(change, somme, targetMoney, denominations) 
    return canGetExactChange(targetMoney, somme, denominations)
  

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
  target_1 = 94
  arr_1 = [5, 10, 25, 100, 200]
  expected_1 = False
  output_1 = canGetExactChange(target_1, 0, arr_1)
  check(expected_1, output_1)

  target_2 = 75
  arr_2 = [4, 5, 17, 29]
  expected_2 = True
  output_2 = canGetExactChange(target_2, 0, arr_2)
  check(expected_2, output_2)
