import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 

file = input("Enter the file name: ")
data = pd.read_csv(file)

print("\nFirst 5 rows of the dataset:")
print(data.head())

print("Columns in datasets:", list(data.columns))

print("\nChoose a plot type:")
print("1. Line Plot")
print("2. Bar Plot")
print("3. Scatter Plot")
print("4. Histogram")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    x_col = input("Enter the column name for x-axis: ")
    y_col = input("Enter the column name for y-axis: ")
    sns.lineplot(data=data, x=x_col, y=y_col)
    plt.title(f"Line Plot of {y_col} vs {x_col}")
    plt.show()
elif choice == 2:
    x_col = input("Enter the column name for x-axis: ")
    y_col = input("Enter the column name for y-axis: ")
    sns.barplot(data=data, x=x_col, y=y_col)
    plt.title(f"Bar Plot of {y_col} vs {x_col}")
    plt.show()
elif choice == 3:
    x_col = input("Enter the column name for x-axis: ")
    y_col = input("Enter the column name for y-axis: ")
    sns.scatterplot(data=data, x=x_col, y=y_col)
    plt.title(f"Scatter Plot of {y_col} vs {x_col}")
    plt.show()
elif choice == 4:
    col = input("Enter the column name for histogram: ")
    sns.histplot(data=data, x=col, kde=True)
    plt.title(f"Histogram of {col}")
    plt.show()
else:
    print("Invalid choice. Please select a number between 1 and 4.")