def factorial(a):
	f = 1
	for i in range(1, a + 1):
		f *= i
	return f

def power(a):
	return a ** a

print(power(5))
print(factorial(5))

print("Hello")
