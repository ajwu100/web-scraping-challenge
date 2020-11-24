# web-scraping-challenge
By: Ai-Jiuan Wu
UNC Data Analytics Bootcamp

"Missions_to_Mars" Directory contains the following files :

1. mission_to_mars.ipynb: Jupyter notebook with Python code written to scrape of 4 websites using Splinter and Beautiful Soup and to store all return data in a Python dictionary.  
2. scrape_mars.py: Python script associated with the 'scrape' function.  This script was generated from Jupyter notebook (described above).
3. app.py: Store all the return data into Mongo as a python dictionary and pass the resulting mars data into a HTML template to display the data.
4. index.html (stored in 'templates' folder): Take the mars data and display in the appropriate html elements.  One of the element is a "Get the Latest Update" button which will execute the scraping code (scrape_mars.py) and display the latest data on the html page.
5. style.css (stored in 'static' folder): Referenced in index.html script and supports the formating of the html page.
