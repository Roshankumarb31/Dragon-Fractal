import turtle	# import the turtle module to use turtle graphics

r = 'r'		#r --> right
l = 'l'		#l --> left

#basic iteration function
old = r
new = old

#input block
iteration = int(input('Enter iteration:'))
length = int(input('Enter length of each segment:'))
pencolor = input('Enter pen color:')
bgcolor = input('Enter background color:')

#a variable for keeping a count on the number of iterations
cycle = 1

#this is the main loop in the program where the path for the pointer is calculated
while cycle<iteration:
	# a right is added to the end of the previous iteration 
	new = (old) + (r)			#new path is saved
	# reverse the path
	old = old[::-1]
	# Now traverse the old path by flipping the cycle
	for char in range(0, len(old)):
		# if the character is right --> change it to left
		if old[char] == r:
			old = (old[:char])+ (l) + (old[char + 1:])
		# if the character is left  --> change it to right
		elif old[char] == l:
			old = (old[:char]) + (r) + (old[char + 1:])
	# add the altered old to the new iteration
	new = (new) + (old)

	# save the new iteration to old as well for use next cycle
	old = new

	# advance the cycle for next iteration
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

#the path calculated in the above while loop is iterated by each character for pointer position
for i in range(0, len(new)):
	# if the character is a right
	if new[i] == (r):
		turtle.right(90)
		turtle.forward(length)
	# otherwise, if the character is a left:
	elif new[i] == (l):	
		turtle.left(90)
		turtle.forward(length)
