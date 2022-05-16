def find_states(capital):
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	if capital in states:
		return capital_cities[states[capital]]
	else:
		return "Unknown state"

import sys

if len(sys.argv) == 2:
	print(find_states(sys.argv[1]))