def insertionsort(a):
    n = len(a)

    for i in range(1, n-1):
        v = a[i]



        j = i-1
        while j>=0 and a[j]>v:
            a[j+1]=j
            j=j-1
            a[j+1]=v
            x=[20,40,50,30,20,10,50]

            print("before sorting:",x)
            insertionsort(x)
            print("Aftersorting:",x)

            # End of P7.PY