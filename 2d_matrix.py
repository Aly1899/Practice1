x = input("Please enter the first number: ")
y = input("Please enter the second number: ")

# setting the variable as empty lists
i_array = []
j_array = []

for i in range(int(x)):
    for j in range(int(y)):
        j_array.append(i*j)
    i_array.append(j_array)
    j_array = []
print(i_array)
