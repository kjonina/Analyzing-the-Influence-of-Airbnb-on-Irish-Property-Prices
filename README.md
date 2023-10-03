# Impact of Airbnb on Property Market in Greater Dublin Area
Created as part of Master of Science in Data Science in South East Technological University, Ireland.

### SKILLS GAINED
Data Cleaning | Data Analysis| Exploratory Data Analysis | Data Visualization | Statistical Analysis | Machine Learning | Data Mining | Feature Engineering | Time Series Analysis

## Table of Contents
- [ABSTRACT](#ABSTRACT)
- [Introduction](#Introduction)
- [Problem Statement](#Problem-Statement)
- [Methodology Summary](#Methodology-Summary)
- [Findings](#Findings)

### ABSTRACT
Housing crisis is one of the most talked about social issues in Ireland.  Entire properties, as well as private rooms, available on Airbnb in highly touristic areas such as Dublin, contributes to a demand on the rental market for long term tenants and property markets for first-time buyers. Unaffordability in the property market has coincided with the increase of private short-term rentals (STRs) such as Airbnb in many cities around the world, including Dublin. In this study, we evaluated the impact of Airbnb on property prices since July 2021 in the Greater Dublin Area, where roughly 1.9 million people live, using linear regression and other machine learning algorithms. Findings suggests that the number of Airbnb listings has returned to the pre-pandemic high, while ML results were inconclusive due to the dataset chosen for this research and no recommendations could be made in relation to Airbnb.

### Introduction
The housing crisis in Ireland has become a pressing issue, affecting both renters and potential homebuyers due to the unaffordability of properties in both the rental and property markets. This crisis has been exacerbated by the presence of Airbnb, a platform where individuals offer their homes or private rooms for short-term rentals to tourists. This practice has reduced the availability of long-term rental properties, leading to increased rents in high-demand areas like London, Denver, and Sydney. This study aims to investigate the impact of Airbnb on property prices in Ireland by analyzing property sales data from the Residential Property Price Register and Airbnb listings data in specific areas.

### Problem Statement
#### Housing Crisis
The housing crisis in Ireland is characterized by a shortage of affordable accommodations for rent or purchase. While the government has attempted to address this crisis with affordable and social housing plans, critics argue that these efforts have been insufficient and lack innovation. The study focuses on the rental market, which provides long-term accommodation, and the property market, which involves property sales, excluding commercial or industrial properties.
After the 2007-2008 Great Financial Crisis, Irish property prices hit their lowest point but rebounded by 24.1% the following year. The property market continued to recover until late 2019, with prices rising by as much as 9% in 2022. Meanwhile, the median household income for first-time buyers increased from €71,000 in 2019 to €77,000 in 2021. Although the housing stock in Ireland grew by an average of 6% between 2016 and 2022, it failed to outpace population growth, leading to a shortage of available properties for both the rental and property markets.

#### Airbnb 
Airbnb has been criticized for contributing to the shortage of long-term rentals by converting properties into short-term rentals for tourists. In 2019, there were over 30,000 Airbnb listings in Ireland, with around half being private rooms, and over 10,000 entire homes available year-round. The Irish government has considered legislation to restrict Airbnb listings to increase the supply of long-term rentals, but this could potentially raise prices for tourists.
During the start of the COVID-19 pandemic, the number of long-term rentals in Dublin increased significantly, similar to trends observed in Sydney. However, the impact of Airbnb on the property market remains largely unexplored.
Greater Dublin Area as a Case Study: Greater Dublin, with its inflated housing market and high tourist demand, presents an intriguing case study to examine Airbnb's effects. Over 9 million overseas tourists visited Ireland in 2017, with the majority spending time in Dublin. The high demand for tourist accommodations has led to a proliferation of Airbnb listings in the capital.

Dublin has consistently ranked among the top 20 most expensive European cities due to the cost of living, factoring in both rental and property markets. A 2022 report revealed that there were more rentals available on Airbnb than long-term rentals in all 26 Irish counties. This has forced tenants to seek housing outside Greater Dublin to find affordable options.

While Airbnb's impact on the rental market has been empirically documented, its influence on the property market remains unexplored in the Greater Dublin Area.

#### Influence of Airbnb on the Rental and Property Markets
Empirical studies have shown that Airbnb disrupts rental markets in major cities worldwide. In the Greater Dublin Area, a three-year period saw rent prices and the number of Airbnb listings rise significantly, indicating a correlation between more Airbnb listings and fewer long-term rentals. Regulation of home-sharing websites like Airbnb has been suggested to ease rental market pressures.
While research on Airbnb's impact on property markets is emerging, no studies have been conducted in the Greater Dublin Area. Previous research in Sydney found a relationship between the number of Airbnb listings and property prices, with factors like distance to commercial zones and amenities playing a role.

#### Hypothesis
Building on the findings from a Sydney study, this research examines the influence of Airbnb listings on Irish property prices in the Greater Dublin Area. The region was chosen due to its housing affordability challenges and a substantial number of Airbnb listings, which, if unregulated, could drive up property sale prices.
The study will test the following hypotheses:
1.	H0: The number of Airbnb listings has no significant effect on property prices in the Greater Dublin Area.
2.	H1: The number of Airbnb listings has a significant effect on property prices in the Greater Dublin Area.
This study aims to provide insights into how Airbnb impacts property prices in Ireland, particularly in the Greater Dublin Area, and whether regulatory measures are needed to address these effects on housing affordability.


![image](https://github.com/kjonina/Analyzing-the-Influence-of-Airbnb-on-Irish-Property-Prices/assets/48295461/1ec32972-cdd5-4d55-b37d-4300530afd70)

The counties in GDA. Created in Tableau Dashboard.

# Methodology Summary
#### Data Sources
- Residential Property Price Register (PPR) – Information about property sales in Ireland.
- Inside Airbnb – Data on Airbnb listings in Ireland.
- Central Statistics Office (CSO) – Shapefiles for areas and Small Area Population Statistics (SAPS).

#### Data Cleaning and Selection:
- Property sales data collected from PPR since January 1, 2010, and last updated on July 12, 2022.
- Selection of properties sold between July 1, 2021, and June 30, 2022, in Greater Dublin Area (GDA): County Dublin, County Wicklow, County Kildare, County Meath, and County Louth.
- Cleaning address column: Standardized word cases to uppercase, corrected spellings, replaced abbreviations (e.g., 'RD' to 'ROAD'), replaced Irish spellings with English equivalents.
- Identified and dropped duplicates (101 cases).
- Removed the Euro symbol from price values and converted to numeric.
- Examined VAT exclusion column (values: 'Yes', 'No') but decided not to recalculate prices due to data accuracy concerns.
- Dropped the 'Not Full Market Price' column due to lack of explanation.
- Examined the distribution of prices and decided to drop properties priced over €1 million due to data limitations.
- Examined Eircode availability and attempted to extract missing Eircodes from addresses.
- Addressed Irish translations in various columns (e.g., description) and translated them to English but dropped irrelevant information.
- Created a new formatted address column combining address, county, and Eircode for better compatibility with Google Maps APIs.

#### Google Maps API
The use of the Google Maps API facilitated the acquisition of geocoded coordinates for properties, enabling further spatial analysis and integration with the PPR dataset. The methodology also highlighted the hierarchical administrative divisions within Ireland.
- Used Google Maps APIs to obtain GPS coordinates for properties in the filtered PPR dataset.
- Performed geocoding in Python with a free Google MAPS API key.
- Split the formatted address column into 2,500 segments to manage API fees and processed them daily.
- Dropped addresses geocoded outside Ireland and those outside the chosen counties (Dublin, Wicklow, Kildare, Meath, Louth).
- Translated Irish place names to English where necessary.

#### PPR Geodataframe:
- Merged geocoded information with the PPR dataset.
- Converted data to a pandas geodataframe for spatial analysis.

#### Country Divide:
-  Explained the various administrative divisions in Ireland, including counties, county councils, local electoral areas (LEAs), and electoral divisions (EDs).

![image](https://github.com/kjonina/Analyzing-the-Influence-of-Airbnb-on-Irish-Property-Prices/assets/48295461/4d718307-f961-4b7d-bc0b-55f479a2e456)

South East Inner City LEA is shown on the left, while the EDs compiling the South East Inner City LEA are shown on the right. 

![image](https://github.com/kjonina/Analyzing-the-Influence-of-Airbnb-on-Irish-Property-Prices/assets/48295461/28099aba-1049-4c3a-b94a-8420fc126b2c)
Pembroke East A ED is shown on the left, while the SAs compiling the Pembroke East A ED are shown on the right. 

#### Eircodes:
- Ireland has 139 Eircode routing keys.
- Eircode shapefiles are available but may not always accurately map properties.
- An Post assigns routing keys, and errors can occur.

#### Shapefiles:
- Shapefiles store geometric data and attributes.
- Used shapefiles from the Central Statistics Office (CSO) for Local Electoral Area (LEA), Electoral Division (ED), and Small Area (SA).
- Calculated area in square kilometers for each geographical area.
- Eircode shapefiles were obtained from Autoaddress.ie.

#### Census Data
The methodology incorporated geographic data and Census information to enrich the analysis of geolocated properties and their relationship with various housing attributes.
- Used 2016 Census Summary Data for dwellings due to the unavailability of 2022 data.
- Utilized Small Area Population Statistics (SAPS) from CSO, focusing on housing-related information.
- Extracted data on accommodation type, year built, and number of rooms.
- Created a new shapefile containing geolocations and SAPS data.
- Merged SAPS data with the Small Area shapefile using a unique identification number (GUID).

#### Calculations

Total number of properties was provided by SAPS. New columns were developed to examine the number of properties in each category in percentages from the total number of properties (Table 9).

| Category          | # of Properties | % of Properties |
|-------------------|-----------------|-----------------|
| 1 Room            | 0               | 0.00%           |
| 2 Rooms           | 1               | 0.82%           |
| 3 Rooms           | 6               | 4.92%           |
| 4 Rooms           | 2               | 1.64%           |
| 5 Rooms           | 32              | 26.23%          |
| 6 Rooms           | 51              | 41.80%          |
| 7 Rooms           | 20              | 16.39%          |
| 8 or More Rooms   | 7               | 5.74%           |
| Number of rooms not stated | 3     | 2.46%           |
| Total             | 122             | 100%            |

 #### Crime Data
- Crime statistics dataset for 2021 from [CSO](https://data.cso.ie/product/RC) was used, aggregated by garda stations.
- Garda sub-divisions shapefile was obtained to match garda stations in the crime statistics dataset.
- Merging crime data with sub-divisions revealed discrepancies due to spelling variations and Irish translations.
- Stations containing '[SS]' referred to sub-stations, which are no longer applicable.
- Some stations lacked crime statistics.
- A new shapefile was created to contain geolocations of garda sub-divisions and total crime statistics.
- Coordinate Reference Systems (CRS) were adjusted to ensure accurate mapping of geolocated properties.

#### Missing Crime Statistics
- 317 geolocated properties in County Dublin and 5 in County Wicklow lacked crime statistics data.
- The mean crime total for each county in 2021 was calculated and used for properties missing crime statistics data (Table 9).

#### Open Street Map
- QGIS 3.22.8 and the 'Quick OSM' plugin were used to collect points of interest from Open Street Map.
- A sub-section of the PPR dataset with geolocated properties was saved as a shapefile.
- Unique row IDs were created for the geolocated properties.
- CRS in QGIS was adjusted to match the program's CRS.
- Relevant neighborhood facilities and amenities for the Greater Dublin Area (GDA) and Louth were determined, including Dart and railway stations, Luas stops, bus stops, M50 junctions, motorway junctions, industrial zones, offices, retail shops, supermarkets, and universities/colleges.
- Euclidean distance was calculated from geolocated properties to these important facilities using Open Street Map data.
- Some locations were initially mapped as polygons, which were converted to points using centroids.
- The calculated distances were exported and merged with the geolocated dataset.

![image](https://github.com/kjonina/Analyzing-the-Influence-of-Airbnb-on-Irish-Property-Prices/assets/48295461/2a56e263-a7b7-4a86-96be-61463746b735)

Euclidian distance (purple lines) was taken from the geolocated properties (purple dots) to the nearest commercial zone (black dots). 

### Airbnb
Airbnb data was obtained from Inside Airbnb, encompassing all listings in Ireland from 27th June 2021. Efforts to acquire additional data through applications did not yield responses. Two sets of datasets were downloaded from each quarter and combined to ensure completeness. The data includes listings, calendar data, and room types (entire property, private room, shared room, hotel rooms). Outliers were observed in Airbnb prices; one listing with an extremely high price was dropped. Calendar data provides information on availability for each listing. Data for analysis was selected for the period from 1st July 2021 to 30th June 2022. Graphs were used to visualize the number of listings over time. Some gaps in data collection were observed, but efforts were made to minimize data loss.

![image](https://github.com/kjonina/Analyzing-the-Influence-of-Airbnb-on-Irish-Property-Prices/assets/48295461/2147390e-29df-4c29-b461-18ee11a5f993)
Combining the best of all three calendar files to ensure continuation.  

#### Airbnb Pandas Geodataframe
The Airbnb data included latitude and longitude for each listing, allowing it to be converted into a pandas geodataframe. Additionally, each Airbnb listing was mapped onto shapefiles for LEAs, Eircodes, EDs, and SAs to extract corresponding values for increased accuracy.

#### Number of Airbnb Listings
Airbnb listings available from 1st July for the next 365 days were grouped by month within each LEA. Similar grouping was done for SAs, EDs, and Eircodes. The table shows an example of Airbnb listings in Blanchardstown-Mulhuddart (LEA) grouped by month.

### Tableau and Storytelling

Tableau was used to visualize Airbnb and PPR data, focusing on data storytelling. Shapefiles for LEAs, SAs, EDs, and Eircodes were imported into Tableau to facilitate data visualization. Median property prices (MPP) were used instead of mean prices to prevent skewing due to outliers. Tableau worksheets were created to display graphs, while Tableau Dashboards allowed interactivity and filtration. Tableau Story combined multiple dashboards to create a data narrative.

#### Audience
The target audience includes individuals interested in residing in Ireland and buying property for residential purposes. The user is expected to have familiarity with Irish counties but limited knowledge of LEAs, EDs, and SAs.

Various questions were posed to explore PPR data:
- Examining MPP for each county and year.
- Comparing MPP and property sales between Greater Dublin Area (GDA) and Non-GDA counties.
Focused questions explored selected counties:
- Identifying high-crime sub-divisions and common crimes.
- Identifying electoral divisions with vacant dwellings.
- Analyzing electoral divisions with numerous Airbnb listings, including MPP by month, vacancy rate, and property sales.
- Examining the breakdown of accommodation types, year built, and number of rooms in each SA.
Data outside the selected counties was filtered as it was not relevant to the research's scope.

#### GPR and Final Dataset
- The PPR dataset did not contain personal identifying information, and no data required anonymization. Addresses, though private, were mixed to ensure anonymity. Data files related to the project were kept private.
- Airbnb data, obtained from a third-party website, did not include personal details like names or contact information. Airbnb listings' locations were generalized within a 150-meter radius for security.
- SAPS data is aggregated by SA, with no identifiable information, and CSO shapefiles lack identifiable details.

#### Final Dataset
After filtering data (July 1, 2021, to June 30, 2022), selecting Greater Dublin Area (Dublin, Meath, Kildare, Wicklow) and Louth, and removing houses priced above €1 million, the final dataset contained 22,173 rows.

#### Feature Selection
The dataset was split into two sets: one containing LEAs and Airbnb listings, the other containing EDs and Airbnb listings.

#### Descriptive Statistics of Features
Histograms, boxplots, and correlations were used to examine feature distributions. Some features, like vacancy rate and the percentage of houses in SAs, were heavily skewed.

#### Multicollinearity of Features
High multicollinearity was observed between variables, such as accommodation type, year built, and number of rooms. Variance Inflation Factor (VIF) was used to analyze multicollinearity, and steps were taken to reduce it.

#### Descriptive Statistics of Target Variable
The target variable, property price, was examined for outliers using Z-scores, boxplots, and the interquartile range (IQR). Outliers beyond the IQR were removed.

#### Logged Numeric Data
Some variables, like crime rate, distance to commercial zones, and the percentage of pre-1991 properties, were right-skewed and required log transformation to achieve normality.

#### Dummy Variables
Categorical variables were converted into dummy variables, creating separate columns for each category.

#### Training and Test Set
The dataset was split into training and test sets, using various splits (70:30, 80:20, 90:10) to find the best models. The number of rows in each split varied accordingly.

### Findings - Summary

#### Exploratory Descriptive Analysis
Property prices in Ireland saw a steady decline from 2010 until 2013, after which they started increasing. In Dublin, for example, the median property price (MPP) hit a low of €202,643 in 2012 but rose to €385,000 in 2022.

#### Crime Rates
In 2021, the top 10 garda sub-divisions with the highest crime rates were all in County Dublin, with Store Street having the highest crime total.

#### Vacancies
Mansion House B in Dublin City had the highest vacancy rate at nearly 20%. Other Dublin City electoral divisions with high vacancy rates included Merchants Quay and Pembroke West.
Electoral divisions outside Dublin City, like Killeagh in County Meath and Ballinguille in County Wicklow, also had high vacancy rates at 17.2% and 18.3%, respectively.

![image](https://github.com/kjonina/Analyzing-the-Influence-of-Airbnb-on-Irish-Property-Prices/assets/48295461/ec23507b-d9f8-4c5e-8e03-b0e0a5991e9d)

Vacancy rate in Dublin City Centre is high in the city centre. No vacancy figures were given for Portobello ED.

#### Eircodes
In the selected counties, there were a total of 57 Eircodes, with areas ranging from 3.22 km sq. to 1509.91 km sq. Dublin had the most Eircodes (37), followed by Kildare with 10, Meath with 14, Wicklow with 8, and Louth with 2 Eircodes.

Some Eircodes extended beyond the selected counties and into neighboring counties like Carlow, Wexford, Westmeath, and Offaly. This extension occurred because Eircodes are used for postal routing rather than strict geographical delineation.

Initially, there was a consideration to use Eircodes to measure the number of Airbnb listings, but this approach was abandoned due to the potential inclusion of Airbnb listings from outside the selected counties, which could skew the results.

(Note: The summary provides information about the number and distribution of Eircodes in the selected counties and the decision not to use Eircodes for measuring Airbnb listings.)

![image](https://github.com/kjonina/Analyzing-the-Influence-of-Airbnb-on-Irish-Property-Prices/assets/48295461/206507a7-a739-409f-bcd4-41c8f2beb68f)

Eircodes that are in, or partially in, County Dublin. Created in Tableau from Eircode shapefile.


#### Local Electoral Areas
In the selected counties, there were 56 Local Electoral Areas (LEAs) with varying areas, ranging from 4.63 km sq. to 916.21 km sq.

Dublin had the most LEAs (31), followed by Kildare with 8 LEAs, Louth with 5 LEAs, Meath with 6 LEAs, and Wicklow with 6 LEAs.

The Stillorgan LEA had the highest Median Property Price (MPP) at €511,507, while the Dundrum LEA had the second-highest MPP at €500,000. In contrast, Athy LEA in County Kildare had the lowest MPP at €194,000.

The North Inner City LEA in Dublin had the highest number of Airbnb listings, with 811 listings, of which 46.24% were entire houses or apartments. The MPP in this LEA was €325,000. South-East Inner City LEA had 557 Airbnb listings, with over 70% being entire houses or apartments, and a MPP of €428,571.

![image](https://github.com/kjonina/Analyzing-the-Influence-of-Airbnb-on-Irish-Property-Prices/assets/48295461/83396c42-1f0e-4ce6-a700-8fb574e1f534)
LEAs coloured by the number of Airbnb Listings in each LEA. The darker the colour the more Airbnb listings are available. 

Outside of Dublin, Naas LEA in County Kildare had the most property sales, with 619 sales and a MPP of €338,000, along with 54 Airbnb listings. Ladytown-Bettystown LEA in Meath and Maynooth LEA in County Kildare had 548 and 526 property sales, respectively, with MPPs of €275,000 and €348,017. Bray West LEA had the fewest property sales, with 142, and a MPP of €422,250.

In Dublin, the LEAs with the highest number of properties sold were North Inner City LEA and Clontarf LEA, with 732 and 661 properties sold, respectively. North Inner City LEA also had 811 Airbnb listings, while Clontarf LEA had 138. The MPP in Clontarf LEA was €425,000, higher than the MPP in North Inner City LEA, which was €320,000.

(Note: The summary provides insights into the distribution of LEAs, property prices, and Airbnb listings in the selected counties, highlighting specific LEAs with high property sales and Airbnb listings.)

#### Electoral Divisions
In the selected counties, there were 598 Electoral Divisions (EDs) with varying areas, ranging from 0.14 km sq. to 76.35 km sq.

Dublin had the most EDs (322), followed by Meath with 82 EDs, Kildare with 80 EDs, Wicklow with 72 EDs, and Louth with 43 EDs.

Lucan North ED had the highest Median Property Price (MPP) at €711,543, followed by Ladytown in County Kildare with an MPP of €700,000. However, there were concerns about the validity of the €30,000 MPP in Barronstown ED in County Louth, as it may have been an error.

In Dublin, Blanchardstown-Blakestown ED had the most properties sold, with 463 properties sold, along with 32 Airbnb listings. The MPP in this ED varied from €270,000 to €380,000. Glencullen ED had the second-highest number of property sales, with 239 houses and 44 Airbnb listings, with MPP ranging from €387,500 to €603,524.

Outside of Dublin, Naas Urban ED in County Kildare had the highest number of properties sold, with 432 properties sold and 21 Airbnb listings. Navan Rural ED in County Meath had the second-highest number of property sales, with 333 properties sold and 21 Airbnb listings.

In Dublin, South Dock ED had the highest number of Airbnb listings, with over 70% being entire houses or apartments and an MPP of half a million euros. The percentage of entire houses or apartments in EDs with the highest Airbnb listings ranged from 29.41% to 72.60%, with MPP varying from €295,500 to €500,000.

![image](https://github.com/kjonina/Analyzing-the-Influence-of-Airbnb-on-Irish-Property-Prices/assets/48295461/9bb9b645-bb39-4b47-86a0-db7451775a55)
Figure shows the areas with high number of Airbnb listings in the date range selected. The darker the colour the more Airbnb listings are available.

Outside of Dublin, the top three EDs with the highest number of Airbnb listings were Carlingford ED in County Louth (65 listings), Wicklow Urban ED (27 listings), and St. Mary’s ED in County Meath, and Bray No.2 ED in County Wicklow (26 listings each). Carlingford ED had 34 properties sold with an MPP of €255,000, while St. Mary’s ED had over 288 properties sold with an MPP of €277,533. Wicklow Urban ED had 91 property sales with an MPP of €299,500, and Bray No.2 ED had 66 properties sold with an MPP of €440,529.

(Note: The summary provides insights into the distribution of Electoral Divisions, property prices, and Airbnb listings in the selected counties, highlighting specific EDs with high property sales and Airbnb listings.)

#### Small Areas (SAs)
In the selected counties, there were a total of 5,910 Small Areas (SAs) with varying areas, ranging from 0.01 km sq. to 61.91 km sq. The mean area of SAs was 0.87 km sq., with a standard deviation of 2.79.

SAs are defined as areas of population consisting of between 80 and 120 dwellings, designed as the lowest level of geographical area for compiling statistics.

The SAPS data revealed that several SAs had exceeded the maximum number of properties in the defined range of 80 to 120 dwellings. This discrepancy was attributed to a possible error in the Central Statistics Office (CSO) data.

Each of the selected counties had varying numbers of SAs, with Dublin having the highest at 3,964 SAs, followed by Kildare (622), Meath (526), Wicklow (418), and Louth (380).

When mapping Airbnb listings onto the SAs and grouping them by month, it was observed that not every SA had active Airbnb listings throughout the year or even had any Airbnb listings at all. Therefore, it was decided not to use Airbnb listings at the SA level due to the limited number of listings, which could make the analysis impractical.

(Note: This section provides information about the distribution and characteristics of Small Areas in the selected counties, along with the decision to exclude Airbnb listings at this geographical level due to limited data.)
