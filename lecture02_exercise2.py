lst_prices = [10, 20, 60, 10, 30, 10, 20]
# adding 160 to the list
print("***appending list***")
lst_prices.append(160)
print("appended list: " + str(lst_prices))
# counting the times of 160 in the list
print("# of 160 in the list: " + str(lst_prices.count(160)))
# finding the least value in the list
print("The least value in the list is: " + str(min(lst_prices)))
# finding the index of 10
print("Index of the least value is: " + str(lst_prices.index(min(lst_prices))))
# removing 10 from the list
print("***removing 10 from list***")
lst_prices.remove(min(lst_prices))
print("Updated list: " + str(lst_prices))
# sorting the list
lst_prices.sort()
print("Sorted list: " + str(lst_prices))