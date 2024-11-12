data = [10,20,30,30,40,50,50,60,70]
def remove_duplicates(duplist):
    non_duplist=[]

    for element in duplist:
        if element not in non_duplist:
            non_duplist.append(element)
    return non_duplist ; 
print(remove_duplicates(data))
        