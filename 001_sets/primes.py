primes=set(range(2,121))
notprimes=set()

index=0

for i in range(2, 121):
    product= i * (i + index)
    while product < 121:
	notprimes.add(product)
	index = index + 1
	product = i * (i + index)
    index = 0
primes-notprimes
