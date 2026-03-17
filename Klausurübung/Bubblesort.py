def bubble_sort(A):

    n = len(A)

    for n in range(n, 1, -1):      # äußere Schleife
        for i in range(0, n - 1):  # innere Schleife

            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]   

    return A



zahlen = [5, 2, 8, 1, 4]

print("Vorher:", zahlen)
bubble_sort(zahlen)
print("Nachher:", zahlen)