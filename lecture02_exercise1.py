lst_number_1= [934, 9348, 39, 59, 32, 904, 575, 9458, 39, 32]
print("***current list values***")
print(lst_number_1)
print("count of items: " + str(len(lst_number_1)))
#appending the list
print("***appending list***")
lst_number_1.append(45)
print(lst_number_1)
print("count of items: " + str(len(lst_number_1)))
#sorting the list
lst_number_1.sort()
print("sorting the list: " + str(lst_number_1))
#reversing the list
lst_number_1.reverse()
print("reversing the list: " + str(lst_number_1))
# counting the occurence of 32 in the list
print("# of 32 occuring in the list: " + str(lst_number_1.count(32)))
