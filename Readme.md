# Wildlife Migration Tracking and Environmental Data Integration  

## Overview  
This project develops a data pipeline to analyze wildlife migration patterns by integrating GPS tracking data with environmental data (e.g., vegetation indices, temperature, and precipitation). The project leverages big data technologies to process large datasets, perform geospatial analysis, and visualize results for ecological insights and conservation planning.

## Features  
- **Data Ingestion:** Fetch GPS data and environmental datasets from APIs and open data repositories.  
- **Data Processing:** Use Apache Spark for large-scale transformations and geospatial analysis.  
- **Integration:** Combine GPS data with environmental metrics for comprehensive insights.  
- **Visualization:** Interactive dashboards showing migration routes overlaid on environmental maps.  

## Tech Stack  
- **Languages:** Python, SQL  
- **Tools & Frameworks:** Apache Spark, PySpark, Pandas, Rasterio, Matplotlib, Folium  
- **Storage:** AWS S3 (or local), PostgreSQL  
- **Visualization:** Tableau or Folium for geospatial mapping  

## Data Sources  
1. **GPS Tracking Data:** Open datasets such as [Movebank](https://www.movebank.org/)  
2. **Environmental Data:**  
   - [MODIS Vegetation Indices](https://modis.gsfc.nasa.gov/data/)  
   - [NOAA Weather Data](https://www.noaa.gov/weather)  
   - [NASA Earthdata](https://earthdata.nasa.gov/)  

## How to Run  
1. Clone this repository:  
   ```bash  
   git clone https://github.com/your-username/wildlife-migration-tracking.git  
   cd wildlife-migration-tracking

2.	Install dependencies:
    ```bash 
    pip install -r requirements.txt

3.	Set up environment variables for API keys in a .env file:
    ```bash 
    NASA_API_KEY=your_api_key  
    NOAA_API_KEY=your_api_key  

4.	Execute the pipeline:
    ```bash 
    python main_pipeline.py
## Visualization

View the output interactive map with migration paths and environmental overlays in the visualizations/ folder.
