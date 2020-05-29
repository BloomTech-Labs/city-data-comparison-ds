#  Citrics

You can find the project [Here](https://citrics.io/).
The API Docs for the DS portion can be found here [Here](https://api.citrics.io/docs)


#### High level overview [presentation](https://docs.google.com/presentation/d/1d7sk8eKj25dVvFoWsu9aERXwdkw6JH33FIgaYkq3bt4/edit?usp=sharing).

#### [Deep dive](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/Citrics_Documentation.ipynb) into cleaning the data.

#### [Datasets used](https://drive.google.com/open?id=1MdnKnqFQRhMPvxeloIAPuhl-qwhhCSbi)

## Contributors:


|                                    [Scott Maxwell](https://github.com/scottwmwork)                                   |                                          [Matthew Sessions](https://github.com/matthew-sessions)                                         |                                 [Luke Townsend](https://github.com/ldtownsend)                                 |[jimmy 'Zeb' Smith](https://www.github.com/zebfred)| [Eric Ramon](https://github.com/nephylum)| [Chris Shields](https://github.com/cshields143)| [Steven Reiss](https://github.com/steve122192)| [Stephanie Miller](https://github.com/shmilyface)| [Amy NLe](https://github.com/hyamynl619)| [Robert Tom](https://github.com/RCTom168)
|:--------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| [<img src="https://avatars0.githubusercontent.com/u/33496996?s=400&u=454aad7eb839b42caa4cfca9357bae07c7a3325c&v=4" width = "200" />](https://github.com/) |              [<img src="https://avatars1.githubusercontent.com/u/53715422?s=400&v=4" width = "200" />](https://github.com/)              | [<img src="https://avatars1.githubusercontent.com/u/53023268?s=400&v=4" width = "200" />](https://github.com/) | [<img src="https://ca.slack-edge.com/ESZCHB482-W012H6HFWLD-697fe1c1ba2d-512" width="200" />](https://github.com) | [<img src="https://avatars1.githubusercontent.com/u/49967847?s=460&v=4" width="200" />](https://github.com) | [<img src="https://ca.slack-edge.com/ESZCHB482-W012BRR0Y7Q-884e2fa6a19d-512" width="200" />](https://github.com) | [<img src="https://ca.slack-edge.com/ESZCHB482-W012X6XC8AV-51551ad57fce-512" width="200" />](https://github.com) | [<img src="https://ca.slack-edge.com/ESZCHB482-W012BRRJ8B0-fbb6b94d63ab-512" width="200" />](https://github.com)

## Project Overview

Citrics provides statistics on 28,925 different locations in the United States that are available for viewing. This was created with a team of web developers and data engineers. These statistics include information about housing prices, employment, industry, lifestyle and much more, sources are listed below. 

#### Links to team documents:

 [Trello Board](https://trello.com/b/VXbaBrSL/labs-19-citydatacomparison)

 [Product Canvas](https://www.notion.so/City-Data-Comparison-bc94a2f56b05482e9c42a12748a0ed0a)
 
 [Live Front End/URL](https://citrics.io/)


### Tech Stack

- Python
- Flask
- Docker
- Jupyter Notebooks
- Mongo DB
- AWS Elastic Beanstalk/Amplify/S3/Route 53
- AWS PostgreSQL


## Predictions


#### The following models are using a K-Nearest Neighbors KD-Tree algorithm from the Scikit-Learn Python Library

_Clicking on the links for each model will take you to the .py file for that model within this repo_

### [Housing Model](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Model_Scripts/housing.py): 

Features & Metrics Used: 

 - Median Rent
 - Occupants per room
 - Housing by bedrooms
 - Vacancy Rate
 - Rent Pricing
 - Historical Property Value
 - Historical Property Value Growth by %

### [Industry Model](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Model_Scripts/industry.py):

Features & Metrics Used:

 - Industry Types
 - Health insurance
 - Salary
 - Commute & travel time
 - Retirement
 - Unemployment
 
### [Culture Model](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Model_Scripts/culture.py):

Features & Metrics used:

 - Education
 - Language
 - Ethnicity
 - Birth Rate
 - Population
 - 
 
### [Reverse User](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Model_Scripts/housing.py): 
_A recommendation questionnaire that supplies the user with a recommended city_
Features & Metrics used:
 - Population
 - Income
 - Monthly Housing
 - Temperature Preference
 - Industry* 
 
 _*Note that Industry is optional on the website, due to lack of adequate data for all cities within the database._ 

### [Time series-housing](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Model_Scripts/housing.py): 

Features & Metrics used:

 - Education
 - Language
 - Ethnicity
 - Birth Rate
 - Population

### [Time series-Industry](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Model_Scripts/housing.py): 

Features & Metrics used:

 - Education
 - Language
 - Ethnicity
 - Birth Rate
 - Population
 
 
_**Note for Library Conflicts:**_ 
* AWS' Elastic Beanstalk has a hard time runing Numpy and Scipy. These libraries power Sklearn. 
Also, the joblib library had a hard time running models that were trained on different operating systems. Once we found models that worked, we exported the code to a python script and ran it on a Linux based machines running **Python 3.6**. We then used Docker/Dockerhub to contain and ship our flask app, and then connected it to AWS to test in Elastic Beanstalk. These steps allowed us to seamlessly deploy predictive models.


### Data Sources

<img src = 'https://raw.githubusercontent.com/Lambda-School-Labs/city-data-comparison-ds/master/images/data%20source%20map.PNG'>

-   [Census Bureau](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/City_Naming.ipynb)
-   [Zillow Housing](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/zillowData_clean.ipynb)
-   [Longitude & Latitude](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/Get_Lat_Lng.ipynb)
-   [Population Growth](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/PopulationGrowth.ipynb)
-   [Weather Data](https://www.ncdc.noaa.gov/cdo-web/webservices/v2)
-   Bureau of Labor and Statistics

_**Notes:**_
[How we pushed our data to MongoDB](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/to_datebase.py)



### Python Notebooks

[Documation Notebook](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/Citrics_Documentation.ipynb)

#### Fixing City Names:
- [Fixing City Names_1](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/fixnames.ipynb)
- [Fixing City Names_2](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/City_Naming.ipynb)

#### Different types of data and sources
- [Longitude & Latitude](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/Get_Lat_Lng.ipynb)
- [Population Growth](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/PopulationGrowth.ipynb)
- [Weather Data](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/Weather_Data.ipynb)

#### Housing Data
- [Cleaning Zillow Data](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/zillowData_clean.ipynb)
- [Price Checking](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/zillow_price_check.ipynb)
- [Mapping Lat & Long to Zillow](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/zillowzip.ipynb)

#### Models (for suggesting similar cities):

- [Housing KNN Model](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/Housing_model.ipynb)
- [Industry KNN Model](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/industry_knn_model.ipynb)
- [Culture KNN Model](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/culture_knn_model.ipynb)
#### Models (Time series):

- [Housing Forecasting](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/Housing_model.ipynb)
- [Industry Forecasting](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/industry_knn_model.ipynb)


#### Model (Questionnaire):
-[KNN Unclassified](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/industry_knn_model.ipynb)

### How to connect to the data API

You can find documentation for the API [here](https://api.citrics.io/docs)
