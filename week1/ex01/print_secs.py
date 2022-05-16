import sys

if len(sys.argv) != 4:
	print("Usage: python3 print_secs.py [Hours] [Minutes] [Seconds]")
else:
	hours = int(sys.argv[1]) * 60 * 60
	minutes = int(sys.argv[2]) * 60
	seconds = int(sys.argv[3])
	print(hours + minutes + seconds)