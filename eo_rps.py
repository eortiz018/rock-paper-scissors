print "Hi, I'm Doug the computer. Let's play Rock-Paper-Scissors! "
print "PS. (Once you get tired of playing, press q to exit)"

print "\n"

move = raw_input("Make your move (r, p, s): ")

comp = 0
user = 0


def choice(move, comp, user):
	
		from random import choice
		x = choice("rps")
	
		if move == "r" and x == "r":
			print "I play rock."
			print "We tied!"
			return comp, user
		elif move == "r" and x == "s":
			print "I play scissors!"
			print "You win!"
			return comp, user + 1
		elif move == "r" and x == "p":
			print "I play paper!"
			print "I win!"
			return comp + 1, user
#_________________
		if move == "p" and x == "p":
			print "I play paper!"
			print "We tie!"
			return comp, user
		elif move == "p" and x == "r":
			print "I play rock!"
			print "You win!"
			return comp, user + 1
		elif move == "p" and x == "s":
			print "I play scissores!"
			print "I win!"
			return comp + 1, user
#__________________
		if move == "s" and x == "s":
			print "I play scissores!"
			print "We tie!"
			return comp, user
		elif move == "s" and x == "p":
			print "I play paper!"
			print "You win!"
			return comp, user + 1
		elif move == "s" and x == "r":
			print "I play rock."
			print "I win!"
			return comp + 1, user	
#__________________
		else:
			print "I do not understand. Please use either (r) for rock, (p) for paper, or (s) for scissors."
			return comp, user	
			print "\n"


while move != "q":
	comp, user = choice(move, comp, user)
	print comp, user
	print "\n"

	move = raw_input("Make your move (r, p, s): ")
	print comp, user
	print "\n"

if move == "q":
	print "Final score is Doug: %d, You: %d" % (comp, user)





