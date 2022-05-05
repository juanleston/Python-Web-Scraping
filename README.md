# Python-Web-Scraping
*How to use Scrapy to build your own dataset?*

Wouldn't it be great if we could always find ready to use ready to use datasets anywhere around the web? After being in the Data Analytics field for some time, I have realized that plug and play scenarios are not the norm. Sometimes, you have to roll up your sleeves and build your own data sources.

Web scraping is the process of gathering large batches of unstructured data from a website and then organizing it into an analytics-ready format. To illustrate how this can be done using Scrapy, World Postal Code data will be extracted from [here](https://worldpostalcode.com/). In this opportunity the country of interest is Vietnam, however, the concepts covered in this project can be applied to obtain data from any other country in this site or even adjusted to use on other websites.

## 1. Repository Contents

  - Sitemap.csv: contains the associated url sitemap of the website mentioned above.
  - SitemapFormattingVietnam.py: python script developed to clean and filter Vietnam's url's from the 'Sitemap.csv' file.
  - address1.py: spider built to scrape address data from the website.
  - address2.py: spider built to scrape address data from the website.
  - ScrappyOutputFormatting_Vietnam.py: python script developed to clean and format the JSON files obtained by the spiders.

## 2. Installation

The installation pre-requisites to reproduce this project locally are:

  ### 2.1 Install Anaconda:
  
  To install anaconda select your operating system and follow the steps outlined in the following link: [Anaconda Installation](https://docs.anaconda.com/anaconda/install/index.html)
    
  ### 2.2 Install Scrapy:

  Scrapy is included as part of the Anaconda installation. However, if it has not been installed you can install using the Command Line/Terminal of your device by running the following code:
  
  > conda install -c conda-forge scrapy

## 3.Usage

The steps below demonstrate in detail how to use the contents of the repository:

  ### 3.1 Create a new Scrapy Project:
  
  To create a new Scrapy Project, navigate to the desired location and open the Command Line/Terminal. Once there, run the following code:
  
  > scrapy startproject yourprojectname

  Doing so will generate your project's directory with these contents:
  
    yourprojectname/
      scrapy.cfg            deploy configuration file
      yourprojecname
        __initn__.py        project's python module
        items.py            project items definition file
        pipelines.py        project pipelines file
        settings.py         project settings file
        spiders/            directory where you have to save your spiders
  

  ### 3.2 Create a list of Start URL's:
  
  The Start URL's are a list of website addresses that the spider will crawl to extract certain data points. In this case, each element in the list holds data from a specific city in Vietnam. For example:
  
  The first URL in the list is: https://worldpostalcode.com/vietnam/bac-trung-bo/ha-tinh/cam-xuyen. Which contains the following data of interest:
  
  ![image](https://user-images.githubusercontent.com/60116541/162849840-8a6eb19d-d909-4513-93fb-97b8cb1a1f0d.png)
  
  Now, to obtain the full list of URL's to scrape we are going to use the website's site map. A site map is a list of all the pages of a web site within a domain. It is often possible to access it by writing "/sitemap.xml" at the end of the website's home address:
  
  > https://worldpostalcode.com/sitemap.xml

  This URL will open something similar to:
  
  ![image](https://user-images.githubusercontent.com/60116541/162851173-7ce054a5-81d1-4f9f-8bdb-67fc7adf28e3.png)

  Once there, select all the text and save it as a csv file.
  
  ### 3.3 Create Spider:
  
  Before creating the spider we need to determine where the specific data we want to scrape lives inside the website. To do so, we are going to use Scrapy Shell which is an interactive environment that allows you to debug your scraping code without having to run the spider.
  
  In that sense, to access the Scrapy Shell open Command Line/Terminal and run the following code:
  
  Mac/Linux:
  > scrapy shell 'url'
  
  Windows:
  > scrapy shell "url"

  The "url" corresponds to the website you want to scrape. In our case, we can use the first start url discussed above:
  
  > scrapy shell 'https://worldpostalcode.com/vietnam/bac-trung-bo/ha-tinh/cam-xuyen'

  To confirm that the Shell has been opened you can run the following code:
  
  > view(response)

  Running the code above should redirect you to the same website you have provided when you opened the Shell. At this point, we will use Xpaths to comb through portions of the website's HTML code that contain the data of interest.
  
  The first step is to inspect the website's HTML elements to see where the data is. To open the inspection pane, right-click anywhere on the screen and select inspect:
  
  ![image](https://user-images.githubusercontent.com/60116541/163074698-c815c8ab-ae5d-4611-b629-31e8715827e1.png)

  Doing so should open a similar pane on the right side of the screen:
  
  ![image](https://user-images.githubusercontent.com/60116541/163074851-f5b2d4d0-49c3-4a9c-9691-ef29d16dcd8b.png)

  Once there, you can highlight the parts of the website that hold the data that you are interested in and that should subsequently highlight certain lines of the HTML code. For example:
  
  Each address in this website contains a navigation path at the top of the screen:
  
  ![image](https://user-images.githubusercontent.com/60116541/166153132-083118c2-e3f0-4aaa-a0f7-c33a8fa5bfe1.png)
  
  By inspecting that section of the website, you can see that it hold valuable data:

  ![image](https://user-images.githubusercontent.com/60116541/166155829-92af2033-d384-47e7-ac05-a6063029e476.png)
  
  Next, we can open the Scrapy shell of Vietnam's first location by running the following code in the Command Line/Terminal:
  
  ![image](https://user-images.githubusercontent.com/60116541/166153857-c739fbad-b9f3-4d8c-b390-c2c7586ad2d3.png)
  
  In that sense, to gather the data points mentioned above we can test the following Xpaths inside Scrapy's shell to make sure we are accessing the expected content:
  
  - Country:

  ![image](https://user-images.githubusercontent.com/60116541/166153898-bd3b71c8-8863-4ace-b221-2786faae8c6a.png)

  - Region:

  ![image](https://user-images.githubusercontent.com/60116541/166153963-e20ca399-073f-494e-8bf0-b08eb67a909b.png)

  - Province:

  ![image](https://user-images.githubusercontent.com/60116541/166154012-a5dc3c79-0580-42a8-9d3d-3951cb0d0264.png)

  - District:
  
  ![image](https://user-images.githubusercontent.com/60116541/166154060-d5b5e182-50dc-4197-bedc-7877830818b8.png)
  
 At this point the only missing data points are the name of the city/town and its respective postal code. However, these pieces of information live in another section of the website:
 
 ![image](https://user-images.githubusercontent.com/60116541/166154944-d8fe9dbf-c14c-47f9-a35e-b2688590be32.png)
 
 If we inspect that section, we can see the data stored as follows:

 ![Screen Shot 2022-05-01 at 12 23 53 PM](https://user-images.githubusercontent.com/60116541/166155189-d576f281-6907-4205-b110-05d2b58daa40.png)

 The Xpath I used to extract these data points is:

  ![image](https://user-images.githubusercontent.com/60116541/166155441-3d4eb8de-9841-48b4-aaa9-dd9c94b48bc5.png)

 As you can see the code above pull the contents of the city-postal code section as a whole. The reason I chose to do it this way is that there are times where a city has multiple postal codes and the website shows that as follows:
 
 ![image](https://user-images.githubusercontent.com/60116541/166155533-8b1372a0-baea-4fee-a843-75c0c825bad7.png)
<br />(Example from cities of Taiwan)
  
  So, because the website uses a one (city) to many (postal codes) relationship I considered simpler to extract the whole container so that data point relationships are preserved.
  
  Once the Xpath scripts to extract the different data points of interest have been designed, it is time to put it all together in the Spider. In that sense, the image below shows how it is structured:
  
  ![image](https://user-images.githubusercontent.com/60116541/166604773-6e025542-8d1f-42b5-b275-fac4247cb7ca.png)

  ### 3.4 Run the Spider:
  
  To run the spider, navigate to the directory and open Command Line/Terminal. Then, run the following code:
  
  > scrapy crawl my_scraper_name -o name_of_output_file.extension

  In this case I ran it as:
  
  > scrapy crawl address -o vietnam_data.json

  Note that the "my_scraper_name" portion of the code has to match the name you give to the spider. Also, you are not limited to JSON file extensions for the spider output.
  
  Running the spider should return a file with the following structure:
  
  ![image](https://user-images.githubusercontent.com/60116541/166844928-7bab781d-beb3-4a3c-9129-f7024ef458c0.png)

  ### 3.5 Format the output data:
 
 After extracting the data from the website, we need to perform some data wrangling to reshape the output into a tabular format that can be used for analytics purposes.
 
 To see more of the step taking in this project check the file named "ScrappyOutputFormatting_Vietnam.py".
 
## 5. Conclusion

In my opinion Web Scraping is one of those skills where the amount of effort required to build a custom solution is high, however I believe learning it is worth pursuing because oh the increased time efficiency in collecting the data. I consider that this skill is often overlooked by professionals in the area but it can be of utmost importance in non-ideal situations where the data is not readily available.

## 6. Credits

Resources used to build this repository include:

  - https://towardsdatascience.com/using-scrapy-to-build-your-own-dataset-64ea2d7d4673

## 7. License

![image](https://user-images.githubusercontent.com/60116541/142733137-9ed23afb-0ee8-468e-b0f0-f90f60e70f3c.png)

This work is licensed under a Creative Commons Attribution 3.0 International License
