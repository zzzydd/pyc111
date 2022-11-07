def check_prime(n):
	is_prime = True
	for i in range(2, int(n/2)+1):
		if n/i == int(n/i):
			is_prime = False
			break
	return is_prime

for x in range(100, 201):
	if check_prime(x):
		print(x, " ", end="")