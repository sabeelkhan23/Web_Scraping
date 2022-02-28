# Web_Scraping
## Information Extraction from a Website with a Collection of Webpages:

Information extraction from a Website with a collection of webpages, below is the link to the webpage that was extracted and web scraped on;
https://www.infoplease.com/primary-sources/government/presidential-speeches/state-union-addresses
Scripting lang : Python 3.8, IDE : vscode, Database: MSSM
The Method 2 has been used : Webpages as Unstructured Data with Parsing
I performed this LAB1 using simple steps which are:
1. I used the inspect element to inspect the HTML structure of the webpage using the developer tools.
2. Looked closely in analyzing the DOM tree of the URL which had the information needed to be extracted.
3. Scraped through the webpage and HTML content using the python script and used libraries such as requests.
4. Later parsed the HTML content using a library called BeautifulSoup which helps in parsing through structured data.
5. This step involves writing data such as Name, Date and Link to the csv file.
6. I have also written the code to connect to server and created a database to display the table for Name, Date, Link.
Libraries Imported for this LAB:

![image](https://user-images.githubusercontent.com/89702819/156047582-9b5f211c-b5a5-4953-9bfc-1eb01900a750.png)

### Data stored in CSV format:

![image](https://user-images.githubusercontent.com/89702819/156048063-01096fb3-5d84-418b-9bb5-142ccf260247.png)

### Database table in MSSQL for the Name, Date and Link of the Presidents:

![image](https://user-images.githubusercontent.com/89702819/156048108-788f3c6e-226e-4a06-9782-42800e13c577.png)
