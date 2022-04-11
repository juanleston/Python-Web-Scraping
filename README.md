# Python-Web-Scraping
*How to use Scrapy to build your own dataset?*

Wouldn't it be great if we could always find ready to use ready to use datasets anywhere around the web? After being in the Data Analytics field for some time, I have realized that plug and play scenarios are not the norm. Sometimes, you have to roll up your sleeves and build your own data sources.

Web scraping is the process of gathering large batches of unstructured data from a website and then organizing it into an analytics-ready format. To illustrate how this can be done using Scrapy, world postal code data will be extracted from [Worl Postal Code](https://worldpostalcode.com/). In this opportunity the country of interest is Vietnam, however, the concepts covered in this project can be applied to obtain data from any other country in this site or even adjusted to use on other websites.

## 1. Repository Contents

  - Sitemap.csv: contains the associated url sitemap of the website mentioned above.
  - SitemapFormattingVietnam.py: python script developed to clean and filter Vietnam's url's from the 'Sitemap.csv' file.
  - address1.py: spider built to scrape address data from the website.
  - address2.py: spider built to scrape address data from the website.
  - ScrappyOutputFormatting_Vietnam.py: python script developed to clean and format the JSON files obtained by the spiders.

## 2. Installation

The installation steps are as follows:

  ### 2.1 Install Anaconda:
  
  To install anaconda select your operating system and follow the steps outlined in the following link: [Anaconda Installation](https://docs.anaconda.com/anaconda/install/index.html)
    
  ### 2.2 Install Scrapy:

  Scrapy is included as part of the Anaconda installation. However, if it does not for some reason you can install it in your Command Line/Terminal by running the following code:
  
  > conda install -c conda-forge scrapy

  ### 2.3 Create a new Scrapy Project:
  
  To create a new Scrapy Project, navigate to the desired location and open Command Line/Terminal. Once there, run the following code:
  
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
  

  ### 2.4 Create a list of Start URL's:
  
  ### 2.5 Create Spider:
  
  ### 2.6 Run the Spider:
  
  ### 2.7 Format the output data:

## 3. Usage

## 4. Credits

Resources used to build this repository include:

  - https://towardsdatascience.com/using-scrapy-to-build-your-own-dataset-64ea2d7d4673

## 5. License

![image](https://user-images.githubusercontent.com/60116541/142733137-9ed23afb-0ee8-468e-b0f0-f90f60e70f3c.png)

This work is licensed under a Creative Commons Attribution 3.0 International License
