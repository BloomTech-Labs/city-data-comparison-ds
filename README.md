# 1️⃣ Citrics

You can find the project [Here](https://master.d1td9ufw3xylcx.amplifyapp.com/).

## 5️⃣ Contributors


|                                    [Scott Maxwell](https://github.com/scottwmwork)                                   |                                          [Matthew Sessions](https://github.com/matthew-sessions)                                         |                                 [Luke Townsend](https://github.com/ldtownsend)                                 |
|:--------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------:|
| [<img src="https://avatars0.githubusercontent.com/u/33496996?s=400&u=454aad7eb839b42caa4cfca9357bae07c7a3325c&v=4" width = "200" />](https://github.com/) |              [<img src="https://avatars1.githubusercontent.com/u/53715422?s=400&v=4" width = "200" />](https://github.com/)              | [<img src="https://avatars1.githubusercontent.com/u/53023268?s=400&v=4" width = "200" />](https://github.com/) |
|                     [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/scottwmwork)                    |                          [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/matthew-sessions)                          |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/ldtownsend)            |
|     [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](www.linkedin.com/in/scott-w-maxwell)    | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/matthew-sessions/) |  [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/luke-townsend-caia-95312610a/) |

## Project Overview


1️⃣ [Trello Board](https://trello.com/b/VXbaBrSL/labs-19-citydatacomparison)

1️⃣ [Product Canvas](https://www.notion.so/City-Data-Comparison-bc94a2f56b05482e9c42a12748a0ed0a)

Citrics provides statistics on 28,924 different cities in the United States that are available for viewing. This was created with a team of web developers and data engineers. These statistics include information about housing prices, employment, lifestyle and much more.


1️⃣ [Deployed Front End](https://master.d1td9ufw3xylcx.amplifyapp.com/)

### Tech Stack

- Python
- Jupyter Notebooks
- Pandas Python Library
- Plotly Python Library
- Mongo DB
- AWS


### 2️⃣ Predictions


#### The following models are using a K-Nearest Neighbors algorithm from the Scikit-Learn Python Library

### [Housing Model](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/Housing_model.ipynb): 
- Features & Metrics Used: 

 - Median Rent
 - Occupants per room
 - Housing by bedrooms
 - Vacancy Rate
 - Rent Pricing
 - Historical Property Value

### [Industry Model](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/industry_knn_model.ipynb):

- Features & Metrics Used:
 - Industry Types
 - Health insurance
 - Salary
 - Commute & travel time
 - Retirement
 - Unemployment
 
### [Culture Model](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/Notebooks/culture_knn_model.ipynb):

- Features & Metrics used:
 - Education
 - Language
 - Ethnicity
 - Birth Rate
 - Population

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

#### Features
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

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](https://github.com/Lambda-School-Labs/city-data-comparison-ds/blob/master/code_of_conduct.md). Please follow it in all your interactions with the project.

### Issue/Bug Request

 **If you are having an issue with the existing project code, please submit a bug report under the following guidelines:**
 - Check first to see if your issue has already been reported.
 - Check to see if the issue has recently been fixed by attempting to reproduce the issue using the latest master branch in the repository.
 - Create a live example of the problem.
 - Submit a detailed bug report including your environment & browser, steps to reproduce the issue, actual and expected outcomes,  where you believe the issue is originating from, and any potential solutions you have considered.

### Feature Requests

We would love to hear from you about new features which would improve this app and further the aims of our project. Please provide as much detail and information as possible to show us why you think your new feature should be implemented.

### Pull Requests

If you have developed a patch, bug fix, or new feature that would improve this app, please submit a pull request. It is best to communicate your ideas with the developers first before investing a great deal of time into a pull request to ensure that it will mesh smoothly with the project.

Remember that this project is licensed under the MIT license, and by submitting a pull request, you agree that your work will be, too.

#### Pull Request Guidelines

- Ensure any install or build dependencies are removed before the end of the layer when doing a build.
- Update the README.md with details of changes to the interface, including new plist variables, exposed ports, useful file locations and container parameters.
- Ensure that your code conforms to our existing code conventions and test coverage.
- Include the relevant issue number, if applicable.
- You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.

### Attribution

These contribution guidelines have been adapted from [this good-Contributing.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426).

## Documentation

See [Backend Documentation](_link to your backend readme here_) for details on the backend of our project.

See [Front End Documentation](_link to your front end readme here_) for details on the front end of our project.

