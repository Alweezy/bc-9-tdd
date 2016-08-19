def super_sum(*args):
	if args !=():
		#intialize the sum to empty list
		my_sum =[]
		# loop through the items
		for item in args:
			#check if the items are integers or a list.
			if isinstance(item,int):
				my_sum.append(item)

			if isinstance(item,list):
				my_sum=my_sum + item
		try:
			total=sum(my_sum)

		except TypeError:

			return "Invalid type"

		return total
	else:
		return "You must pass an argument"