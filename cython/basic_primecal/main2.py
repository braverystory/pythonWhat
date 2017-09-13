
def test(prime_fn):
    primes = []
    for i in range(1000):
        primes.append(prime_fn(i))
    return primes

if __name__ == '__main__':
	import timeit
	print(timeit.timeit("test(prime_python.prime3)", number=1000, setup="from __main__ import test; import prime_python"))
