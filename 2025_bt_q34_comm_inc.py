import matplotlib.pyplot as plt
import os

# Display the given equations
print("Given equations:")
print("2x + 3y = 6")
print("4x + 6y = 3k")
print()

# Display the augmented matrix
print("Augmented Matrix:")
print("[ 2   3 | 6  ]")
print("[ 4   6 | 3k ]")
print()

# Display the row operation
print("After R2 -> R2 - 2R1:")
print("[ 2   3 | 6       ]")
print("[ 0   0 | 3k - 12 ]")
print()

# Calculate k
k = 12 / 3

print("For at least one solution:")
print("3k - 12 = 0")
print("3k = 12")
print("k =", int(k))


# Create x-values for the graph
x = [i / 10 for i in range(-20, 51)]

# Calculate y-values for the first equation
y1 = [(6 - 2*i) / 3 for i in x]

# Calculate y-values for the second equation when k = 4
y2 = [(12 - 4*i) / 6 for i in x]

# Create the graph
plt.figure(figsize=(8, 6))

# Plot the first equation
plt.plot(x, y1, label="2x + 3y = 6")

# Plot the second equation
plt.plot(x, y2, "--", label="4x + 6y = 12 (k = 4)")

# Draw x-axis and y-axis
plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)

# Label the axes
plt.xlabel("x")
plt.ylabel("y")

# Add title
plt.title("Q34: Same Line → Infinitely Many Solutions")

# Add grid and legend
plt.grid(True)
plt.legend()

# Save the graph
plt.savefig("q34.png")

# Automatically open the graph in Termux
os.system("termux-open q34.png")
