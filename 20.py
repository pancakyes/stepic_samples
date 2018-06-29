def f(x):
    return x ** 2

number_of_inputs = int(input())
all_values = {}

for step in range(number_of_inputs):
    next_number = int(input())
    if next_number not in all_values:
        all_values[next_number] = f(next_number)
    print(all_values[next_number])

print(all_values)
