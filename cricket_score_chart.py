import matplotlib.pyplot as plt
import numpy as np

# Overs (1 to 20)
overs = np.arange(1, 21)

# Runs scored in each over
scores = [4, 4, 5, 3, 7, 2, 10, 11, 4, 6, 7, 2, 19, 4, 2, 3, 8, 9, 10, 11]

# Bar chart
plt.bar(overs, scores)

# Title and labels
plt.title("India Score for all Overs (Bar Chart)")
plt.xlabel("Overs (1 - 20)")
plt.ylabel("Runs per Over")

# X-axis ticks
plt.xticks(overs)

# Grid
plt.grid(True, linestyle="--", alpha=0.7)

# Show graph
plt.show()
