def bubble_sort( list_to_sort ):
    n = len(list_to_sort)
    for i in range(1,n):
        for j in range(0,n-i):
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
