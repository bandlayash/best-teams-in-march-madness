import pandas as pd

# Load the CSV file
data = pd.read_csv("reg_season_data.csv")

# Calculate the Simple Rating Score (SRS) for each team
data['SRS'] = data['SOS'] + data['Point Diff']

# Sort the teams by their SRS in descending order
sorted_data = data.sort_values('SRS', ascending=False)

# Print the sorted data
print(sorted_data)

# Export to csv
sorted_data.to_csv("sorted_data.csv", index=False)
