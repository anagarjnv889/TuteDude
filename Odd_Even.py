# Check if a Number is Even or Odd
a=int(input("Enter a number"))
if a%2==0:
    print(a, "is an even number.")
else:
    print(a, "is an odd number.")

# Sum of Integers from 1 to 50 Using a Loop
sum=0
for i in range(1,51):
    sum+=i
print("The sum of number from 1 to 50 is:",sum)