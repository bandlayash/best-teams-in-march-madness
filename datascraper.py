import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as py

# Send HTTP request and retrieve HTML content
url = 'https://www.sports-reference.com/cbb/seasons/men/2023-advanced-school-stats.html'
response = requests.get(url)
html_content = response.content

# Parse HTML content and extract necessary data
soup = BeautifulSoup(html_content, 'html.parser')

team_data = []

table = soup.find('table', {'id': 'adv_school_stats'})
headers = [header.text.strip() for header in table.find_all('th')]

for row in table.find_all('tr')[1:]:
    team = [cell.text.strip() for cell in row.find_all('td')]
    if team:
        # Extract necessary columns
        school_name = team[0]
        win_loss_percentage = float(team[4])
        strength_of_schedule = float(team[6])
        point_differential = float(team[17]) - float(team[18])

        if "NCAA" in row.text:
            team_data.append({"School": school_name.replace("NCAA", ""), "W-L%": win_loss_percentage, "SOS": strength_of_schedule, "Point Diff": point_differential})

# Store data in a Pandas DataFrame
df = pd.DataFrame(team_data)

#export to csv
df.to_csv("reg_season_data.csv", index=False)

# Display DataFrame
print(df)
