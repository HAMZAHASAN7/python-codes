Q1.)
file_name = 'file1.txt'

with open(file_name, 'r') as file:
    file_contents = file.read()

reversed_contents = file_contents[::-1]

with open(file_name, 'w') as file:
    file.write(reversed_contents)

print(f"Contents of {file_name} have been reversed.")



Q3.)

filename = 'f1.txt'
data_dict = {}

with open(filename, 'r') as file:
    for line in file:
        key, value = map(str.strip, line.split(','))  
        data_dict[key] = value

print(data_dict)
