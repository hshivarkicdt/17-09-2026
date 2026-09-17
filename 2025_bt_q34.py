import matplotlib.pyplot as plt
import os

# Q34:
# 2x + 3y = 6
# 4x + 6y = 3k

print("Given equations:")
print("2x + 3y = 6")
print("4x + 6y = 3k")
print()

# Augmented matrix
print("Augmented Matrix:")
print("[ 2   3 | 6  ]")
print("[ 4   6 | 3k ]")
print()

# R2 -> R2 - 2R1
print("After R2 -> R2 - 2R1:")
print("[ 2   3 | 6       ]")
print("[ 0   0 | 3k - 12 ]")
print()

# Condition for at least one solution
k = 12 / 3

print("For at least one solution:")
print("3k - 12 = 0")
print("3k = 12")
print("k =", int(k))

# -----------------------------
# Draw the diagram
# -----------------------------

x = [i / 10 for i in range(-20, 51)]

# 2x + 3y = 6
y1 = [(6 - 2*i) / 3 for i in x]

# 4x + 6y = 12, when k = 4
y2 = [(12 - 4*i) / 6 for i in x]

plt.figure(figsize=(8, 6))

plt.plot(x, y1, label="2x + 3y = 6")
plt.plot(x, y2, "--", label="4x + 6y = 12 (k = 4)")

plt.axhline(0, linewidth=1)
plt.axvline(0, linewidth=1)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Q34: Same Line → Infinitely Many Solutions")

plt.grid(True)
plt.legend()

# Automatically save and open the image
plt.savefig("q34.png")
os.system("termux-open q34.png")
