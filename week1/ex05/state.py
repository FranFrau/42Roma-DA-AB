import sys

def find_capital(state):
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
	capital_key = list(capital_cities.keys())
	states_key = list(states.keys())
	i = 0
	initial = ""
	for x in capital_cities:
		if capital_cities[capital_key[i]] == state:
			initial = capital_key[i]
		i += 1
	i = 0
	for x in states:
		if states[states_key[i]] == initial:
			return (states_key[i])
		i += 1
	return "Unknown capital city"

if len(sys.argv) == 2:
	print(find_capital(sys.argv[1]))