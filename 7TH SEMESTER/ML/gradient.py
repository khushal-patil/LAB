def gradient_descent(deri, initial_x, n, itr):
   x = initial_x
   for i in range(itr):
       grad = deri(x)
       x = x - n * grad
       print(f"Iteration {i+1}: x = {x:.6f}, gradient = {grad:.6f}")
   return x


def derivative(x):
   return 2 * (x -1)


try:
   initial_x = float(input("Enter initial x value: "))
   n = float(input("Enter learning rate: "))
   itr = int(input("Enter number of iterations: "))
except ValueError:
   print("Invalid input. Please enter numeric values.")
   exit(1)

# Run gradient descent
min_x = gradient_descent(derivative, initial_x, n, itr)
print(f"\nLocal minimum occurs at x = {min_x:.6f}")
 

 

 

def gradient_descent(deri, initial_x, n, itr):
   x = initial_x
   for i in range(itr):
       grad = deri(x)
       x = x - n * grad
       print(f"Iteration {i+1}: x = {x:.6f}, gradient = {grad:.6f}")
   return x


def derivative(x):
   return 2 * (x + 3)


try:
   initial_x = float(input("Enter initial x value: "))
   n = float(input("Enter learning rate: "))
   itr = int(input("Enter number of iterations: "))
except ValueError:
   print("Invalid input. Please enter numeric values.")
   exit(1)

# Run gradient descent
min_x = gradient_descent(derivative, initial_x, n, itr)
print(f"\nLocal minimum occurs at x = {min_x:.6f}")