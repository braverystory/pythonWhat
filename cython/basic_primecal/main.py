import pyximport; pyximport.install()	# Cython
import prime_cython
import prime_python

def test(prime_fn):
    primes = []
    for i in range(1000):
        primes.append(prime_fn(i))
    #print("primes: ", primes)
    return primes

if __name__ == '__main__':
	import timeit
	print("Test cython with cython type");
	print(timeit.timeit("test(prime_cython.prime1)", number=1000, setup="from __main__ import test; import prime_cython"))
	print("Test cython with python code");
	print(timeit.timeit("test(prime_cython.prime2)", number=1000, setup="from __main__ import test; import prime_cython"))
	print("Test python");
	print(timeit.timeit("test(prime_python.prime3)", number=1000, setup="from __main__ import test; import prime_python"))

