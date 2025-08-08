import pandas as pd

def create_sample_data():
    data = {
        "area": [1000, 1200, 1500, 1800, 900],
        "rooms": [2, 3, 3, 4, 2],
        "location": ["Hyderabad", "Mumbai", "Bangalore", "Chennai", "Delhi"],
        "price": [45, 60, 70, 85, 40]  # Price in lakhs
    }
    return pd.DataFrame(data)

if __name__ == "__main__":
    df = create_sample_data()
    print(df)
