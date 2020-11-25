# Web Scraper
## About Application
Web Scraper is console based application which can be used for scraping web pages and counting the number of img and leaf p tags
 
 ## Installation
 - Application can be installed using following command from console:
 sh
  git clone https://github.com/jeka-01/web_scaper.git
 
 - To install all the required packages:
  sh
  pip install requirements.txt
 
 
 ## Usage
  - First you open two console window one for server, another for client.
  
  For server:
   sh
  python3 web_scraper.py server -p <port_number>
   
   For client:
   sh
  python3 web_scraper.py client --host <ip_address> -p <port_number> --webpage <url>
   
