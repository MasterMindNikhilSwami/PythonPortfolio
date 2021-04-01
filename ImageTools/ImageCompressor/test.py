import multiprocessing
def worker1(v):
    # with v.get_lock():
    v.value += 1

def worker2(v):
    with v.get_lock():
        v.value += 2


if __name__ == '__main__':
	POOL=multiprocessing.Pool(4)
	ctypes_int = multiprocessing.Manager().Value("i", 0)
	print (ctypes_int.value)

	POOL.apply(worker1,(ctypes_int,))
	# process1 = multiprocessing.Process(
	#     target=worker1, args=[ctypes_int])
	# process2 = multiprocessing.Process(
	#     target=worker2, args=[ctypes_int])

	# process1.start()
	# process2.start()
	# process1.join()
	# process2.join()

	print (ctypes_int.value)