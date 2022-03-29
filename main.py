#find mean of the list
def mean(list_no):
    sum = 0
    for i in list_no:
        sum += i
    return sum / len(list_no)

#find median of the list
def median(list_no):
    list_no.sort()
    if len(list_no) % 2 == 0:
        return (list_no[int(len(list_no)/2)] + list_no[int(len(list_no)/2)-1])/2
    else:
        return list_no[int(len(list_no)/2)]

# find range of the list
def range_list(list_no):
    list_no.sort()
    return list_no[len(list_no)-1] - list_no[0]

# find mode of the list
def mode(list_no):
    dict_no = {}
    for i in list_no:
        if i in dict_no:
            dict_no[i] += 1
        else:
            dict_no[i] = 1
    max_value = max(dict_no.values())
    for key in dict_no:
        if dict_no[key] == max_value:
            return key

list_no = input("Enter the list of numbers: ").split(",")

#convert list no to float
for i in range(len(list_no)):
    list_no[i] = float(list_no[i])

print("Mean:", mean(list_no))
print("Mode: ", mode(list_no))
print("Median:", median(list_no))
print("Range:", range_list(list_no))
