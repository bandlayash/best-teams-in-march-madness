# best-teams-in-march-madness
2023 Men's NCAA Basketball Simple Rating Score Calculator

THIS IS NOT AN ACCURATE PREDICTION.

-------------------------------------------------------------------------------------------------------------------------------
UPDATE:

marchmadnessprob.py uses methods from previous files and adds a new data source from kenpom.com. Due to kenpom.com blocking requests, I downloaded the page as an html file. You will need to do so in order to run the program properly. Due to adding KenPom defense rank in the calculation, it is slightly more accurate in it's predictions. The formula to find the probability is 0.5 + srs - (defense rank) / 50. This was a general probability formula.


datascraper.py uses BeautifulSoup to scrape data from sports-reference.com and outputs the data as a csv file called "reg_season_data.csv"

srscalc.py uses pandas to read from this csv file and calculates the SRS, simple rating score, of each team

-------------------------------------------------------------------------------------------------------------------------------

The outputting csv file shows every school instead of just schools that have made the tournament. 
