import tabulate

list_no = [3,4,5,1,2,8,9,6,5,3,2,1,6,4,7,8,1,1,5,5,2,3,4,5,7,8,3,4,2,5,1,9,4,5,6,7,8,9,2,1,5,4,3,4,5,6,1,4,4,8]

#sort the list
list_no.sort()
list_elements = list(set(list_no))

print("List elements: ", list_elements)

counts = []

for element in list_elements:
    print("Element: ", element, "Count: ", list_no.count(element))
    counts.append([element, list_no.count(element)])

# Use tabulate to draw table of counts
print(tabulate.tabulate(counts, headers=['Element', 'Count'], tablefmt='pretty'))
