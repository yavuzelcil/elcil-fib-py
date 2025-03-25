import argparse

from elcil_fib_py.fib_calcs.fib_number import recurring_fibonacci_number

def fib_numb():
    parser = argparse.ArgumentParser(description='Calculate the nth Fibonacci number.')
    parser.add_argument('--number', action='store', type=int, required=True, help='Fibonacci number to calculate.')
    args = parser.parse_args()
    print(f"Your Fibonacci number is: {recurring_fibonacci_number(number=args.number)}")