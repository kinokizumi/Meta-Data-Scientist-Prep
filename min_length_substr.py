#!/usr/bin/python3

def min_length_substring(s, t):

  char_list = set(t)
  for char in char_list:
    if t.count(char) > s.count(char):
      return -1

  length = len(s)

  for i in range(len(s)-len(t)):
    for j in range(i+len(t), len(s)):
      subarr = s[i:j]
      boolean = 0
      for char in char_list:
        if char in subarr and t.count(char) <= s.count(char):
          boolean += 0
        else:
          boolean += 1
      
      if boolean == 0 and len(subarr) < length:
        length = len(subarr)

  return length 

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
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  s3 = "dcbjkefjkfledfbce"
  t3 = "fed"
  expected_3 = 3
  output_3 = min_length_substring(s3, t3)
  check(expected_3, output_3)
