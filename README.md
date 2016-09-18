#JumboJobs

####PURPOSE:
Use the US Census data to create a predictive model to project salaries. Use these
predictions to create a service that would be beneficial to a user who recently graduated
college and is looking for a new career. 

####AUTHORS:
Leo Adberg, Thanatcha Panpairoj, Amir Shahatit, Alex Bondarenko

####HOW TO RUN:
 - To run the front end, a PHP server with Python 3 and numpy is needed. Once it is set up, modify `index.php` for your specific server's python implementation, which is definitely not the same as ours.
 - `GetAllData.sh` runs the code to scrape *Economy-Wide Key Indicators* from the US Census website.
 - `GetAllData.py` is a CLI tool that can query this data, link the 2002 and 2012 datasets, and run analytics.
