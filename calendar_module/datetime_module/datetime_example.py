from datetime import datetime

# Input two dates
x = input("Enter first date (YYYY-MM-DD): ")
y = input("Enter second date (YYYY-MM-DD): ")

# Convert string to datetime
a1 = datetime.strptime(x, "%Y-%m-%d")
b1 = datetime.strptime(y, "%Y-%m-%d")

# Difference between dates
print("Difference:", b1 - a1)
