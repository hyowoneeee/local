import streamlit as st
import folium
import pandas as pd

info_df= pd.read_excel('data.xlsx')

def create_us_map():
    us_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)
    # Add markers, layers, etc. to the map
    return us_map

def main():
    st.title("Ticker Headquarters Map")
    st.write("Displaying ticker headquarters on the map based on Federal Reserve districts.")
    st.write("Blue markers indicate known districts. Red markers indicate unknown districts.")

    us_map = create_us_map()

    # Assuming info_df and get_ticker_info functions are defined
    for index, row in info_df.iterrows():
        ticker = row['Ticker']
        name = row['Name']
        sector = row['Sector']
        market_cap = row['MarketCap']
        headquarters= row['Headquarters']
        latitude= row['Latitude']
        longitude= row['Longitude']
        district= row['District']

        if latitude is not None and longitude is not None:
            color = 'blue' if district != 'N/A' else 'red'
            popup_content = f"Ticker: {ticker}<br>Name: {name}<br>Sector: {sector}<br>Market Cap: {market_cap}<br>Headquarters: {headquarters}"

            folium.Marker(
                location=[latitude, longitude],
                popup=popup_content,
                icon=folium.Icon(color=color, icon="times")
            ).add_to(us_map)

    # Display the map using Streamlit's components.v1.html
    st.components.v1.html(us_map._repr_html_(), width=800, height=600)

if __name__ == "__main__":
    main()