def insertion_sort( list_to_sort ):
    n = len(list_to_sort)
    i = 1
    while i < n:
        number = list_to_sort[i]
        j = i
        while j >= 0:
            if list_to_sort[j] > number:
                list_to_sort[j+1] = list_to_sort[j]
                j -=1
            else:
                list_to_sort[j] = number
                break
            
        
        i += 1
