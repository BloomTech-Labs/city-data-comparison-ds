# 1️⃣ Citrics

You can find the project [Here](https://citrics.io/).
The API Docs for the DS app  can be found [Here](https://api.citrics.io/docs)


#### High level overview presentation [Here](https://docs.google.com/presentation/d/1d7sk8eKj25dVvFoWsu9aERXwdkw6JH33FIgaYkq3bt4/edit?usp=sharing).

#### Deep dive into cleaning the data [Here](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/Citrics_Documentation.ipynb).

## 5️⃣ Contributors


|                                    [Scott Maxwell](https://github.com/scottwmwork)                                   |                                          [Matthew Sessions](https://github.com/matthew-sessions)                                         |                                 [Luke Townsend](https://github.com/ldtownsend)                                 |
|:--------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| [<img src="https://avatars0.githubusercontent.com/u/33496996?s=400&u=454aad7eb839b42caa4cfca9357bae07c7a3325c&v=4" width = "200" />](https://github.com/) |              [<img src="https://avatars1.githubusercontent.com/u/53715422?s=400&v=4" width = "200" />](https://github.com/)              | [<img src="https://avatars1.githubusercontent.com/u/53023268?s=400&v=4" width = "200" />](https://github.com/) |
|                     [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/scottwmwork)                    |                          [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/matthew-sessions)                          |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/ldtownsend)            |
|     [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](www.linkedin.com/in/scott-w-maxwell)    | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/matthew-sessions/) |  [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/luke-townsend-caia-95312610a/) |

## Project Overview


1️⃣ [Trello Board](https://trello.com/b/VXbaBrSL/labs-19-citydatacomparison)

1️⃣ [Product Canvas](https://www.notion.so/City-Data-Comparison-bc94a2f56b05482e9c42a12748a0ed0a)

Citrics provides statistics on 28,924 different locations in the United States that are available for viewing. This was created with a team of web developers and data engineers. These statistics include information about housing prices, employment, lifestyle and much more.


1️⃣ [Deployed Front End](https://citrics.io/)

### Tech Stack

- Python
- Flask
- Docker
- Jupyter Notebooks
- Mongo DB
- AWS Elastic Beanstalk
- AWS PostreSQL


### 2️⃣ Predictions


#### The following models are using a K-Nearest Neighbors KD-Tree algorithm from the Scikit-Learn Python Library

### [Housing Model](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Model_Scripts/housing.py): 
- Features & Metrics Used: 

 - Median Rent
 - Occupants per room
 - Housing by bedrooms
 - Vacancy Rate
 - Rent Pricing
 - Historical Property Value
 - Historical Property Value Growth by %

### [Industry Model](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Model_Scripts/industry.py):

- Features & Metrics Used:
 - Industry Types
 - Health insurance
 - Salary
 - Commute & travel time
 - Retirement
 - Unemployment
 
### [Culture Model](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Model_Scripts/culture.py):

- Features & Metrics used:
 - Education
 - Language
 - Ethnicity
 - Birth Rate
 - Population
 
#### Note: AWS EB has a hard time runing Numpy and Scipy. These libraries power Sklearn. Also, the joblib library had a hard time running models that were trained on different operating systems. Once we found models that worked, we exported the code to a python script and ran it on a Linux based machines runing python 3.6. We then used Docker to contain and ship our flask app. These steps allowed us to seamlessly deploy predictive models.

### 2️⃣ Explanatory Variables

-   Explanatory Variable 1
-   Explanatory Variable 2
-   Explanatory Variable 3
-   Explanatory Variable 4
-   Explanatory Variable 5

### Data Sources

<img src = 'https://raw.githubusercontent.com/Lambda-School-Labs/city-data-comparison-ds/master/images/data%20source%20map.PNG'>

-   [Census Bureau](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/City_Naming.ipynb)
-   [Zillow Housing](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/zillowData_clean.ipynb)
-   [Longitude & Latitude](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/Get_Lat_Lng.ipynb)
-   [Population Growth](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/PopulationGrowth.ipynb)
-   [Weather Data](https://www.ncdc.noaa.gov/cdo-web/webservices/v2)

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

##### Housing Data
- [Cleaning Zillow Data](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/zillowData_clean.ipynb)
- [Price Checking](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/zillow_price_check.ipynb)
- [Mapping Lat & Long to zillow](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/zillowzip.ipynb)

#### Models (for suggesting similar cities):

- [Housing KNN Model](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/Housing_model.ipynb)
- [Industry KNN Model](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/industry_knn_model.ipynb)
- [Culture KNN Model](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/culture_knn_model.ipynb)

### 3️⃣ How to connect to the data API

You can find documentation for the API [here](https://api.citrics.io/docs)


