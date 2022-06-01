#!/usr/bin/python3

def rotateCharacter(character, rotation_factor):
  if character.isupper():
    output_char = chr((ord(character)-ord("A")+rotation_factor)%26 + ord("A"))
  elif character.islower():
    output_char = chr((ord(character)-ord("a")+rotation_factor)%26 + ord("a"))
  elif character.isnumeric():
    output_char = f"{(int(character)+rotation_factor)%10}"
  else:
    output_char = character
  return output_char


def rotationalCipher(input, rotation_factor):
  # Write your code here
  output = ""
  for character in input:
    output = output + rotateCharacter(character, rotation_factor)
  return output


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
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)
