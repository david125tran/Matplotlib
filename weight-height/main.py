"""
    This example uses Python's csv library to read a csv file,
    "weight-height.csv", which contains imaginary height and weight data of
    males and females.

    The Matplotlib library is then used to create a scatter plot of the males
    against the females for data visualization.

"""
# -------------------------------- REQUIREMENTS --------------------------------
# pip install matplotlib

# -------------------------------- IMPORTS --------------------------------
import matplotlib.pyplot as plt
import csv

# -------------------------------- OPEN THE CSV FILE --------------------------------
# Create Empty Dictionaries
male_dict = {
    'height': [],
    'weight': []
}

female_dict = {
    'height': [],
    'weight': []
}

with open('weight-height.csv', mode='r') as file:
    # Reading the CSV file
    csvFile = csv.reader(file)
    # Separate and append the contents to either male_dict or female_dict
    for row in csvFile:
        if row[0] == 'Male':
            male_dict['height'].append(int(float(row[1])))
            male_dict['weight'].append(int(float(row[2])))
        elif row[0] == 'Female':
            female_dict['height'].append(int(float(row[1])))
            female_dict['weight'].append(int(float(row[2])))
        else:
            pass    # In case a gender entry does not match exactly

# -------------------------------- DATA VISUALIZATION WITH Matplotlib --------------------------------
# Create a Plot Figure
plt.figure(figsize=(14, 8))

# Create X and Y Labels
plt.title('Weight and Height of Doctor Office Visits: In December of 2019')
plt.xlabel('weight (lbs)')
plt.ylabel('height (inches)')

# Plot the Data
plt.scatter(male_dict['weight'], male_dict['height'], color='blue', label='male')
plt.scatter(female_dict['weight'], female_dict['height'], color='pink', label='female')

# Add Male and Female Labels
plt.legend()

# Show the Plot
plt.show()

