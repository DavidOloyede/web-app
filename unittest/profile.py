

def fullname(n):
	# if value is integer then false
	if type(n)==int:
		print("false")
		return False
	# if the string value is integer then false
	elif str(n).isdigit()==True: 
		print("false")
		return False
	#Value n must be a string of letters so it is a name
	else:
		print("true")
		return True



def address(n):
	if type(n)==int or n.isdigit():
		return False
	
	
	if all(x.isalpha() or x.isspace() for x in n):
		return False
	elif (' ' in n)==False:
		return False
	else:
		return True



def city(n):
	if type(n)==int:
		print("false")
		return False
	else:
		return False if any(char.isdigit() for char in n) else True

def zipcode(n):
	if len(str(n)) != 5:
		return False
	else: 
	  try:
		  int(str(n))
		  return True
	  except ValueError:
		  return False























# def fibonacci(n):
#     if n <= 1:
#         return 1
#     else:
#         return fibonacci(n-2)+fibonacci(n-1)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)

# fibonacci(1)
# fibonacci(10)

# factorial(0)
# factorial(1)