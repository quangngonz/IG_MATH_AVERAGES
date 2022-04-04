list_of_classes = []

for i in range(20, 25):
    list_of_classes.append(i/2)
    
frequency = [58, 24, 15, 3]

for class_number in range(len(frequency)):
    list_of_classes[class_number] = list_of_classes[class_number] + 0.25

list_of_classes = [1,4,7, 11.5]

print("Middle Value: ", list_of_classes)

estimate_total = 0

for class_number in range(len(frequency)):
    estimate_total += list_of_classes[class_number] * frequency[class_number]

print(estimate_total/sum(frequency))



