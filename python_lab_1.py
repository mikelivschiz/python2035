#python lab 1

current_age = 0
while current_age < 1 or current_age > 100:
	current_age = int(input("how old are you?\n"))
	if current_age > 0 and current_age <= 100:
		future_age = current_age + 17
	else:
		print("please input a number from 1 to 100")
print "your age in 2035 will be %d" % (future_age)
