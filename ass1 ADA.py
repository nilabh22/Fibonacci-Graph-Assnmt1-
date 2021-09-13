import time
start = time.time()

def fibonacci(n):
    a = 0
    b = 1
    sum = 0
    count = 1
    print("Fibonacci Series:")
    while (count <= n):
        print(sum, end=" ")
        count += 1
        a = b
        b = sum
        sum = a + b
print(fibonacci(10))
end = time.time()
runtime = end-start
print(runtime)
