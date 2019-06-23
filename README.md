# My-scripts

Contains python scripts created by me:
1. Downloader for arrow season 6: Downloads the lastest episode for arrow season 6
2. Libgen book fetch URL : fetch book download url from libgen(To be used in app/Can be converted to a download script)
3. Libgen API : Simple REST API using flask for the libgen scripts.
4. PpoDecision: Scrape data from placement portal of IITG, and export to CSV containing company name, 
   profile, ctc, base and monthly salary. You need to get chromedriver for windows for it to work.

REQUIREMENTS:
1. Beautiful Soup
    Install by running the command `pip install beautifulsoup4` in terminal.
2. Requests module
    Install by running the command `pip install requests` in terminal.
3. Flask
    Install flask by running `pip install flask` . Flask is used to create the REST API for the libgen service.
4. Selenium (For the company salary list)
    Install by running `pip install selenium` , also download chromedriver from selenium website and add it's path to `PATH`
    environment variable.