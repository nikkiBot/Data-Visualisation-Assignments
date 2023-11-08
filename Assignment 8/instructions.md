# Goal: Geo-visualization of thematic data using Choropleth

## Detail:
Use Choropleth map to show the population variation among the states of India.

## Data Preparation:
Note: Geo-visualization needs geometric information about the geographical location/space. That data may or may not be available with the thematic data.
If it is not available in the data file then the it must identify the location/space by the commonly accepted identity of the geographical location/space.
The identity may be simply name, ex: Delhi, India, etc... Or an ISO code for the state, country, for ex: see https://en.wikipedia.org/wiki/ISO_3166-2:IN for ISO code of Indian States,  see https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes for ISO codes for counties.
It is the responsibility of the geo-visualization creator to acquire the geometric data from the standard sources and related the identity of the geographical location/space to the geometrical data.

You may use geometrical information of the Indian states and Union territories from https://github.com/HindustanTimesLabs/shapefiles. 

Attached is a CSV data file containing the estimated 2023 population of the Indian states and most of the Indian Union Territories. The data has been assembled from a table in https://www.findeasy.in/top-indian-states-by-population/ and guarantees a  one-to-one correspondence between the names in the data file and properties.ST_NM key of the feature dictionary of IndiaState.json file (available in the above mentioned shapefiles folder). The related information will be covered in the class.

---
## Data Visualization:

You may use `plotly.express` or `geopandas` for creating the choropleth map.
plotly.express provides two methods: 
`px.choropleth` or `px.choropleth_mapbox`  for the purpose.
Find attached two sample plots using `px.choropleth`