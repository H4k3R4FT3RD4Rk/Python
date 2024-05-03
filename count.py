count = 0
number = input("Enter number: ")
end = int(input("Enter the end of the range: "))
for num in range(1, end):
    count += str(num).count(number)

print(count)
