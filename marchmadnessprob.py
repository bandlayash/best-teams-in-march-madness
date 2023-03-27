import requests
from bs4 import BeautifulSoup
import pandas as pd

# URLs for KenPom and Simple Rating Score

srs_url = 'https://www.sports-reference.com/cbb/seasons/men/2023-advanced-school-stats.html'



# Scrape KenPom data
with open(r"2023 Pomeroy College Basketball Ratings.html") as file:
    html = file.read()
kp_soup = BeautifulSoup(html, 'html.parser')


kp_table = kp_soup.find("table", {"id": "ratings-table"})
kp_headers = [header.text.strip() for header in kp_table.find_all("th")]

kp_data = []

for row in kp_table.find_all("tr")[1:]:
    kp_team = [cell.text.strip() for cell in row.find_all("td")]
    if kp_team:
        school_name = kp_team[1].strip()
        defense_rank = int(kp_team[0].strip())

        res = ''.join([i for i in school_name if not i.isdigit()])
        kp_data.append({"School": res , "Defense Rank": defense_rank})



# Scrape Simple Rating Score data
srs_response = requests.get(srs_url)
srs_soup = BeautifulSoup(srs_response.content, 'html.parser')

srs_data = []
pointDiff = []

srs_table = srs_soup.find('table', {"id": "adv_school_stats"})
srs_headers = [header.text.strip() for header in srs_table.find_all("th")]


for row in srs_table.find_all('tr')[1:]:
    srs_team = [cell.text.strip() for cell in row.find_all('td')]
    if srs_team:
        team = srs_team[0].strip()
        srs = float(srs_team[5].strip())
        point_diff = (float(srs_team[17]) - float(srs_team[18]))

        
        srs_data.append(srs)
        pointDiff.append(point_diff)
        

kp_df = pd.DataFrame(kp_data)
kp_df.insert(2, "SRS", srs_data)
kp_df.insert(3, "Point Differential", pointDiff)
kp_df_sorted = kp_df.sort_values('School')

pd.set_option('display.max_rows', None)
 

# Calculate probability of winning March Madness
prob_data = []

    
school = kp_df_sorted["School"]
simpleratingscore = kp_df['SRS']
def_rank = kp_df_sorted['Defense Rank']
point_diff = kp_df["Point Differential"]
prob = 0.5 + (srs - def_rank) / 50
prob_data.append({"School": school, "Defense Rank": def_rank, "SRS": simpleratingscore, "Point Differential": point_diff, "Prob": round(prob*100, 4)})

prob_df = pd.DataFrame(prob_data)
#prob_df_sorted = prob_df.sort_values(by = "Prob", ascending = False)
prob_df.to_csv("prob_data.csv", index=False)

# Output data
print(prob_df)
