#[JumboJobs](leo.adberg.com)

####PURPOSE:
Use the US Census data to create a predictive model to project salaries. Use these
predictions to create a service that would be beneficial to a user who recently graduated
college and is looking for a new career. 

####AUTHORS:
Leo Adberg, Thanatcha Panpairoj, Amir Shahatit, Alex Bondarenko

####HOW TO RUN:
 - `https://github.com/leoadberg/leo.adberg.com` contains all the HTML, CSS, and ECMAScript code to display the form, as well as an `index.php` file that runs the python code and generates a table from the form submission.
 - `GetAllData.sh` runs the code to scrape *Economy-Wide Key Indicators* from the US Census website.
 - `GetAllData.py` is a CLI tool that can query this data, link the 2002 and 2012 datasets, and run analytics.
