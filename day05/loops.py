# Python Loops

# for item in my list do something
my_list = ["Apple", "Cherry", "Banana"]
for item in my_list:
    print(item)
    print(item + " pie")

# for num in range(0, 10). Gauss-> [1-10] + [10-1] = 11, so to see [0-100], then range(0,101,[step = 1])
for number in range(0, 11, 2):
    print(number) # 0, 2, 4, 6, 8, 10

# Addition of the serie is max_number/2&max_number/2 -> 100 => 5050; 1000=> 500500
total_gauss = 0
for number in range(1, 101):
    total_gauss += number
print(total_gauss)