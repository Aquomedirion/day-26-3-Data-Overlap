
with open("file1.txt") as file1:
    file1_list = file1.readlines()
    file1.close()

with open("file2.txt") as file2:
    file2_list = file2.readlines()
    file2.close()

stripped_file_1 = [int(stripped_file.strip("\n")) for stripped_file in file1_list]
stripped_file_2 = [int(stripped_file.strip("\n")) for stripped_file in file2_list]

print(stripped_file_1)
print(stripped_file_2)

result = [num for num in stripped_file_1 if num in stripped_file_2]


# Write your code above 👆

print(result)


