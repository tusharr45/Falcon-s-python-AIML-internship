



n = int (input("Enter the number for which the factorial needs to be calculated:"))

factorial = 1

if n < 0:

              print ("Factorial cannot be calculated, non-integer input")

elif n == 0:

              print ("Factorial of the number is 1")

else:

              for i in range (1, n+1):

                             factorial = factorial *i

              print ("Factorial of the given number is: ", factorial)