import sys

if len(sys.argv) == 3:
	first = int(sys.argv[1])
	second = int(sys.argv[2])
	print(first + second)
else:
	print("Usage: python3 print_sum.py [number-1] [number-2]")