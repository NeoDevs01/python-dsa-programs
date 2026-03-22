def selectionsort(a):
    n = len(a)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]

x = [34, 46, 43, 27, 57, 41, 45, 21, 70]
print("Before sorting:", x)
selectionsort(x)
print("After sorting:", x)
# End of P6.PY