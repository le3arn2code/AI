import pandas as pd
import matplotlib.pyplot as plt

# Example dataset
data = {
    'study_hours': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'pass_fail': [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}
df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# Visualize dataset
plt.scatter(df['study_hours'], df['pass_fail'], color='blue')
plt.xlabel('Study Hours')
plt.ylabel('Pass/Fail')
plt.title('Study Hours vs Pass/Fail')
plt.savefig("screenshot.png")
print("✅ Data plotted and saved as screenshot.png")
