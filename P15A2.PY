def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

n = int(input("Enter the range: "))
print("The fibonacci value is:", fib(n))
# End of P15A2.PY