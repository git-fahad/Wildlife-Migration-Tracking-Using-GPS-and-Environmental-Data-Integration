import pandas as pd
import geopandas as gpd

def integrate_data(gps_file, environmental_file, output_file):
    gps_df = pd.read_csv(gps_file)
    env_df = gpd.read_file(environmental_file)

    # Merge datasets based on location and time
    integrated_df = pd.merge_asof(
        gps_df.sort_values('timestamp'),
        env_df.sort_values('timestamp'),
        on='timestamp',
        direction='nearest'
    )

    integrated_df.to_csv(output_file, index=False)
    print(f"Integrated data saved to {output_file}")

if __name__ == "__main__":
    integrate_data(
        "data/processed/cleaned_gps_data.csv",
        "data/raw/environmental_data.geojson",
        "data/processed/integrated_data.csv"
    )
