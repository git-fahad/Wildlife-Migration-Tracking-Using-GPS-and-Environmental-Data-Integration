import pandas as pd

def clean_gps_data(input_file, output_file):
    df = pd.read_csv(input_file)
    df = df.dropna()  # Drop rows with missing values
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    clean_gps_data("data/raw/gps_data.csv", "data/processed/cleaned_gps_data.csv")
