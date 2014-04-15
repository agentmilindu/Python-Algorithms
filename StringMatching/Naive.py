def naive_search( pattern, text ):
    for i in range(len(text)):
        for j in range(len(pattern)):
            #print("mathing", pattern[j], "with", text[i+j], end="")
            if pattern[j] is not text[i+j]:
                #print(" : not matched!")
                break
            else:
                pass #print(" :  matched!")
        else:
            return True
    else:
        return False
#print(naive_search("abc", "asdiueabwefwerwabcwefw"))
