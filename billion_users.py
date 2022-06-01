#!/usr/bin/python3

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def getBillionUsersDay(growthRates):
  # Write your code here
  sum_rate = sum(growthRates)
  mean_rate = sum_rate/len(growthRates)
  #t_min = math.ceil(9.0 / math.log10(sum_rate))
  t_max = math.ceil(9.0 / math.log10(mean_rate))
  total_user = sum([g**t_max for g in growthRates])

  while total_user > 1e9:
    t_max -= 1
    total_user = sum([g**t_max for g in growthRates])
  
  return t_max+1


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
  test_1 = [1.1, 1.2, 1.3]
  expected_1 = 79
  output_1 = getBillionUsersDay(test_1)
  check(expected_1, output_1)

  test_2 = [1.01, 1.02]
  expected_2 = 1047
  output_2 = getBillionUsersDay(test_2)
  check(expected_2, output_2)
