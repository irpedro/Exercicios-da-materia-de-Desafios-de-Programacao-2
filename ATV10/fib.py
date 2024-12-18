def max_fib(max):
    fibs = [1, 2]
    while True:
        next_fib = fibs[-1] + fibs[-2]
        if next_fib > max:
            break
        fibs.append(next_fib)
    return fibs

def quant_fib(a, b, fibs):
    from bisect import bisect_left, bisect_right
    start = bisect_left(fibs, a)
    end = bisect_right(fibs, b) - 1
    return max(0, end - start + 1)

max = 10**100
fibs = max_fib(max)

while True:
    inp = input().strip()
    if inp == "0 0":
        break
    first, last = map(int, inp.split())
    result = quant_fib(first, last, fibs)
    print(result)