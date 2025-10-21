#!/usr/bin/env python3

# Fibonacci Sequence Exercise with functions
# TODO: (Read detailed instructions in the Readme file)

# Prompt user for number of terms and validate input.
# Returns a positice integer.
def get_user_input():
  while True :
    try:
      num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
      if num_terms <= 0:
        print("Please enter a postitive integer.")
      else:
        return num_terms
  except InputError:
    print("Invalid input. Please enter a valid integer.")

# Generate fibonacci sequence up to n terms.
# Returns the sequence.
def generate_fiboncacci(n):
  sequence = []
  a, b = 0, 1
  for  _ in range (n):
    sequence .append(a)
    a, b = b, a + b
  return sequence

#Print the Fibonaccie sequence in a readable format.
def print_sequence(seq):
  print("Fibonacci sequence: ")
  for num in seq:
    print(num, end=" ")
  print()

# Main program
def main():
  terms = get_user_input()
  fib_sequence = generate_fibonacci(terms)
  print_sequence(fib_sequence)

# Run program
if if __name__ == "__main__"
  main()
