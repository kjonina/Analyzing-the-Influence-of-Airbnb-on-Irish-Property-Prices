# Impact of Airbnb on Property Market in Greater Dublin Area
Created as part of Master of Science in Data Science in South East Technological University, Ireland.

### The Goal:
The goal of my thesis was to analyze the influence of Airbnb on the Irish property market within the Greater Dublin Area (GDA). The objective was to uncover patterns, correlations, and potential impacts of Airbnb listings on property prices. The study aimed to contribute valuable insights into the intricate relationship between short-term rentals and the real estate market, particularly in selected counties such as Dublin, Meath, Kildare, Wicklow, and Louth. Understanding these dynamics was crucial for policymakers, researchers, and stakeholders in the housing sector.

### Solution:
To achieve this goal, I employed a multifaceted approach. The research involved the utilization of various datasets, including the Price Property Register, Airbnb listings data, Small Areas data, Local Electoral Areas data, and Electoral Divisions data. Statistical analysis, data visualization, and geospatial mapping techniques were applied to uncover trends and patterns. Python programming and Tableau were employed to process and visualize the data effectively. The research also addressed challenges related to data quality and limitations in available datasets, ensuring a rigorous and comprehensive analysis.

The study incorporated a comparison of Airbnb listings with property prices, examining different geographical divisions such as Local Electoral Areas and Electoral Divisions. The approach included a meticulous exploration of potential correlations between Airbnb activity and property sales, considering factors like median property prices, Airbnb listing types, and property sales volumes.

### Outcomes:
The outcomes of the thesis study provided valuable insights into the complex dynamics between Airbnb activity and property prices in the GDA. Although all effort was made to remove challenges in data quality and limitations in certain datasets, the research failed to successfully contributed to the understanding of regional variations and hotspots where Airbnb may have a more pronounced impact. The geospatial visualizations and statistical findings offered a nuanced perspective on how short-term rentals relate to property markets at different geographic levels.

### Limitations and Future Research:
The study's outcomes also highlighted the need for improved data quality in property registers, especially concerning the completeness of information and standardized formats. Recommendations for future studies and data enhancements were proposed, acknowledging the evolving nature of short-term rental markets and the importance of accurate, comprehensive datasets.
Other studies should scrape the data directly from website such as Daft.ie to gather more accurate data on the house being sold. This would eliminate the need for overreliance on SAPS data. However, it is vital to remember that the methods used to address the issues are also used by Irish Residential Property Price Index.


### Challenges Faced:
- **Incomplete Property Data:** Dealing with property sales records that lacked crucial information like the number of bedrooms, bathrooms, property size, and accommodation type, making it challenging to perform comprehensive analyses.
- **Data Quality Issues:** Struggling with data quality issues such as anomalies, inconsistencies, and inaccuracies in the Price Property Register (PPR), which raised concerns about the reliability of the dataset. Addressing the discrepancy between the stamp duty date recorded in the PPR and the actual sale date of properties, which required assumptions and could impact time series analysis.
- **Lack of Airbnb Data Updates:** Relying on outdated Airbnb data for the study, as data updates from InsideAirbnb were not available, potentially leading to inaccuracies in assessing the impact of Airbnb on the property market.
- **Address Formatting Challenges:** Dealing with non-standardized property address formats in the PPR, which included Irish and English language mix, unknown characters, and inconsistencies, making data processing difficult.
- **Missing Eircodes:** Handling a significant number of missing Eircodes in the dataset, which affected geolocation accuracy and required further data cleaning.
- **Duplication of Data:** Identifying and managing cases of duplicated property records, which required interpretation to determine whether they represented separate transactions or data entry errors.
- **Outdated SAPS Data:** Working with outdated Small Area Population Statistics (SAPS) data, which may not reflect recent property changes and renovations, impacting the accuracy of the analysis.
- **Lack of Property Details:** Grappling with the absence of property details, such as size and amenities, which limited the ability to create a comprehensive machine learning model.
- **Inflation Rate Unaccounted:** Failing to control for inflation in property prices, which could affect the interpretation of price trends and market dynamics.
- **Limited Crime Data:** Working with crime data available for only one year (2021) and not by month, which made it impossible to analyze seasonal crime patterns' effects on property prices.
- **Vacant Property Data:** Analyzing vacant property data that was only available from Census 2022 and aggregated by Electoral Division (ED), rather than Small Area (SA), potentially leading to double-counting of properties and overlooking Airbnb properties.
- **Geocoding Challenges:** Addressing geocoding issues, especially when addresses contained only the name of an area without property-specific details, leading to general location estimates.
- **Shapefile Limitations:** Dealing with shapefiles that lacked data dictionaries, had inconsistent location names, and underwent unannounced changes in URL links.
- **Lack of Airbnb Updates:** Working with Airbnb data that was not updated during the study period, resulting in outdated information that may not accurately reflect recent Airbnb activity.
- **Property Location Coordinates:** Considering that Airbnb listings are often geolocated approximately 150 meters away from the actual property, which could lead to inaccuracies in assessing their impact on the property market.

- ### Skills Gained:
- **Data Management Skills:** Acquired advanced skills in data management, including cleaning, preprocessing, and handling large datasets. Dealing with incomplete and inconsistent data enhanced my ability to work with real-world datasets effectively.
- **Research Resilience:** My research journey taught me how to adapt to unexpected challenges and overcome various obstacles in the data collection and analysis process. I learned to stay persistent and resourceful in solving complex problems.
- **Data Analysis Expertise:** developed expertise in analyzing datasets using statistical methods and machine learning techniques. This allowed me to uncover patterns, trends, and correlations within the data.
- **Critical Thinking:** Conducting research in the face of data limitations required me to think critically, make informed assumptions, and assess the potential impact of data discrepancies on my findings.
- **Problem-Solving Abilities:** Honed my problem-solving skills by identifying and addressing issues related to data quality, data sources, and research methodologies.
- **Presentation Skills:**  I enhanced my presentation skills by creating Tableau dashboard.
