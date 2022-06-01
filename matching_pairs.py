#!/usr/bin/python3

def matching_pairs(s, t):
  # Write your code here
  if s == t:
    return len(s) - 2
  
  queue = [t]
  visited = [t]
  count = []

  while queue:
    curr = queue.pop(0)
  
    for i in range(len(curr)-1):
      for j in range(i+1, len(curr)):
        swap = curr[:i] + curr[j] + curr[i+1:j] + curr[i] + curr[j+1:]
        if swap not in visited:
          count.append(sum([s[i]==swap[i] for i in range(0, len(s))]))
          visited.append(swap)
          queue.append(swap)

  return max(count)


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
  s_1, t_1 = "abcfe", "adcbe"
  expected_1 = 4
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)
