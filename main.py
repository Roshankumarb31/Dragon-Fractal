# import the turtle module to use turtle graphics
import turtle

# make variables for the right and left containing 'r' and 'l'
r = 'r'
l = 'l'

# assign our first iteration a right so we can build off of it
old = r
new = old

# for inputs
iteration = int(input('Enter iteration:'))
length = int(input('Enter length of each segment:'))
pencolor = input('Enter pen color:')
bgcolor = input('Enter background color:')

# set the number of times we have been creating
# the next iteration as the first
cycle = 1

# keep on generating the next iteration until desired iteration is reached
while cycle<iteration:
	# add a right to the end of the old iteration and save it to the new
	new = (old) + (r)
	# flip the old iteration around(as in the first character becomes last)
	old = old[::-1]
	# cycling through each character in the flipped old iteration:
	for char in range(0, len(old)):
		# if the character is a right:
		if old[char] == r:
			# change it to a left
			old = (old[:char])+ (l) + (old[char + 1:])
		# otherwise, if it's a left:
		elif old[char] == l:
			#change it to a right
			old = (old[:char]) + (r) + (old[char + 1:])
	# add the modified old to the new iteration
	new = (new) + (old)

	# save the new iteration to old as well for use next cycle
	old = new

	# advance cycle variable to keep track of the number of times it's been done
	cycle = cycle + 1


ans = input('Display r/l form?(y/n):')
if ans =='y':
	print(new)
	
# for not show the turtle icon when drawing
turtle.ht()
turtle.speed(0)
turtle.color(pencolor)
turtle.bgcolor(bgcolor)
turtle.forward(length)

# cycling through all the characters in the iteration
for char in range(0, len(new)):
	# if the character is a right:
	if new[char] == (r):
		turtle.right(90)
		turtle.forward(length)
	# otherwise, if the character is a left:
	elif new[char] == (l):	
		turtle.left(90)
		turtle.forward(length)
