def find_states(state):
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
	if state in states:
		return capital_cities[states[state]]
	else:
		return "Unknown state"

import sys

if len(sys.argv) == 2:
	print(find_states(sys.argv[1]))