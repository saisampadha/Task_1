import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:/task1/Task_1.csv")
print("Data Set\n",df)
print("No of Columns\n",df.count())
print("No of Null Values\n",df.isnull().sum())
df = df.dropna()
print("Data set after dropping null values are\n",df)
df.count()


col = df.columns
print(col)


f_data =df['Fare']
plt.boxplot(f_data)
plt.title('Figure For Fare Data')
plt.ylabel('Fare')
plt.show()


from scipy import stats
z_score = stats.zscore(f_data)
threshold = 2
df = df[z_score>threshold]
print(df)
plt.boxplot(df['Fare'])


''''import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

# Load the dataset
df = pd.read_csv("D:/data/Task_1.csv")

# Step 1: Data Exploration
print("Step 1: Data Exploration")
print("**********")

# Display the given  dataset
print("Given Dataset Overview:")
print(df.head())

# Count the number of rows and columns in the given dataset
num_rows, num_columns = df.shape
print(f"No of Rows: {num_rows}")
print(f"No of Columns: {num_columns}")

# Check for missing values in each column
missing_values = df.isnull().sum()
print("\nMissing Values per Column:")
print(missing_values)

# Step 2: Data Cleaning
print("\nStep 2: Data Cleaning")
print("**************")

# Remove rows with missing values
df= df.dropna()

# Display the cleaned dataset
print("Cleaned Dataset Overview:")
print(df.head())

# Step 3: Data Analysis
print("\nStep 3: Data Analysis")
print("************")

# Extract 'Fare' data for data analysis
f_data = df_cleaned['Fare']

# Create a box plot for 'Fare'
plt.boxplot(f_data)
plt.title('Box Plot of Fare')
plt.ylabel('Fare')
plt.show()

# Calculate Z-scores for 'Fare'
z_scores = stats.zscore(fare_data)

# Set a threshold for identifying outliers
threshold = 2

# Filter out rows with Z-scores greater than the threshold
df_no_outliers = df_cleaned[z_scores <= threshold]

# Display the dataset after removing outliers
print("Dataset After Removing Outliers:")
print(df_no_outliers.head())

# Create a box plot for 'Fare' after removing outliers
plt.boxplot(df_no_outliers['Fare'])
plt.title('Box Plot of Fare (Outliers Removed)')
plt.ylabel('Fare')
plt.show()

# Step 4: Conclusion
print("\nStep 4: Conclusion")
print("*************")

# Provide a summary or conclusion of the analysis
print("Data analysis and cleaning completed. Outliers have been removed.")
'''