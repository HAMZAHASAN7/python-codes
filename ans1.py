Q1.) result = []
     for num in range(2000, 3201):

     	if num % 7 == 0 and num % 5 != 0:
        	result.append(num)

      	print(','.join(map(str, result)))



Q2.)def factorial(n):
    	if n == 0 or n == 1:
            return 1
    	else:
            return n * factorial(n-1)
    numbers = [5, 8, 10, 3, 6]

    factorials = [factorial(num) for num in numbers]
    print(','.join(map(str, factorials)))


Q3.)
def generate_squared_dict(n):
    if not isinstance(n, int) or n < 0:
        print("Please provide a non-negative integer.")
        return

    squared_dict = {i: i*i for i in range(1, n+1)}

    print(squared_dict)

generate_squared_dict(5)

Q4.)

input_numbers = input("Enter a sequence of comma-separated numbers: ")


number_list = input_numbers.split(',')

number_tuple = tuple(number_list)

print(number_list)
print(number_tuple)


