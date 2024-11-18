import folium
import pandas as pd

def generate_map(data_file, output_file):
    df = pd.read_csv(data_file)
    m = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=6)

    for _, row in df.iterrows():
        folium.Marker(
            [row['latitude'], row['longitude']],
            popup=f"Time: {row['timestamp']}\nEnv: {row['environmental_condition']}"
        ).add_to(m)

    m.save(output_file)
    print(f"Map saved to {output_file}")

if __name__ == "__main__":
    generate_map("data/processed/integrated_data.csv", "visualizations/migration_map.html")
