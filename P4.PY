import time

def linearsearch(a, key):
    n = len(a)
    for i in range(n):
        if a[i] == key:
            return i
    return -1

a = [13, 23, 43, 52, 12, 45]
start = time.time()
print("The array elements are:", a)
k = int(input("Enter the element to search: "))
i = linearsearch(a, k)
if i == -1:
    print("Search unsuccessful")
else:
    print("Search successful, key found at location:", i + 1)
end = time.time()
print("Runtime of the program is", end - start)
# End of P4.PY