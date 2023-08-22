import time
from multiprocessing import Pool, cpu_count

def factorize(*numbers):
    result = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        result.append(factors)
    return result

def factorize_sync(*numbers):
    start_time = time.time()
    result = factorize(*numbers)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def factorize_parallel(*numbers):
    start_time = time.time()
    pool = Pool(processes=cpu_count())
    result = pool.map(factorize, numbers)
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

if __name__ == '__main__':
    numbers = [128, 255, 99999, 10651060]

    result_sync, execution_time_sync = factorize_sync(*numbers)
    print("Synchronous Execution Time:", execution_time_sync)
    print("Result (Synchronous):", result_sync)

    a, b, c, d = result_sync

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


    result_parallel, execution_time_parallel = factorize_parallel(*numbers)
    print("Parallel Execution Time:", execution_time_parallel)
    print("Result (Parallel):", result_parallel)

    a, b, c, d = result_parallel

    assert a[0] == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b[0]== [1, 3, 5, 15, 17, 51, 85, 255]
    assert c[0]== [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d[0] == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


    print("Все вийшло")