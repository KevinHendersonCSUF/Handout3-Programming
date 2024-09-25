#-------------------------------------------------------------------------------------------------------------
# Group names: Gonong, Theo and Henderson, Kevin and Le, Anthony
# Assignment : No.3
# Due date : 9/24/24
#Purpose: This program reads the user's input and determines if it is accepted or rejected according to CFG
#-------------------------------------------------------------------------------------------------------------

while True:
	w = input("Please provide string: ")
	current = "S"
	for sym in w:
		if sym != 'a' and sym != 'b' and sym != 'c' and sym != '$':
			print("String contains character not in alphabet!, Alphabet is {a, b, c}")
			break
		match current:
			case "S":
				if sym == 'b' or sym == 'c' or sym == '$':
					if sym == 'b':
						current = "B"
					if sym == 'c':
						current = "C"
					if sym == '$':
						print("String is rejected!")
						break
			case "B":
				if sym == 'a' or sym == 'b' or sym == 'c' or sym == '$':
					if sym == 'b':
						current = "B"
					if sym == 'a':
						current = "C"
					if sym == 'c':
						print("String is rejected!")
						break
					if sym == '$':
						current = '$'
						print("String is accepted!")
						break
			case "C":
				if sym == 'a' or sym == 'b' or sym == 'c' or sym == '$':
					if sym == 'b':
						print("String is rejected!")
						break
					if sym == 'a':
						current = "S"
					if sym == 'c':
						print("String is rejected!")
						break
					if sym == '$':
						current = '$'
						print("String is accepted!")
						break
			case _:
				print("String is accepted!")
				break
	choice = input("Input another string?")
	if choice == 'n':
		break
	if choice != 'y' and choice != 'n':
		print("Invalid option, terminating program")
		break
