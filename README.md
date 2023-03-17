# best-teams-in-march-madness
2023 Men's NCAA Basketball Simple Rating Score Calculator

This is not as accurate as other website's simple rating score because it includes all games (non D1 games).

-------------------------------------------------------------------------------------------------------------------------------

datascraper.py uses BeautifulSoup to scrape data from sports-reference.com and outputs the data as a csv file called "reg_season_data.csv"

srscalc.py uses pandas to read from this csv file and calculates the SRS, simple rating score, of each team

-------------------------------------------------------------------------------------------------------------------------------

The higher the SRS, the higher the chance of the team winning the tournament. This is not an accurate measurement of determining the winner as you would need more data
in order to accurately determine the winner.
