import streamlit as st
from meta_ai_api import MetaAI

# Initialize MetaAI
llm = MetaAI()

# Set page config
st.set_page_config(
    page_title="Weather Information",
    page_icon="🌤️",
    layout="centered"
)

# Add title and description
st.title("🌍 Global Weather Information")
st.markdown("Enter a country name to get detailed weather information.")

# Create input field
user_input = st.text_input("Enter the country name:", placeholder="e.g. France")

# Create button
if st.button("Get Weather Info"):
    if user_input:
        # Show loading spinner while getting response
        with st.spinner("Fetching weather information..."):
            prompt = f""" You are custom gpt you have to tell about the weather of any country user asked
                       user asked for {user_input} 
                       You have to tell the weather of the country in the following format:
                       - Temperature: 20 degree celsius
                       - Humidity: 50%
                       - Wind Speed: 10 km/h
                       - Weather Description: sunny
                       - Weather Icon: 1234567890
                       - Weather Condition: clear
                       - Weather Visibility: 10 km
                       - Weather Pressure: 1000 hPa
                       - Weather Wind Direction: 10 km/h
                       - Weather Wind Speed: 10 km/h
                       - Weather Wind Gust: 10 km/h
                       - Weather Precipitation: 10 mm
                       - Weather Cloud Cover: 10%
                       - Weather UV Index: 10
                       - Weather Sunrise: 06:00
                       - Weather Sunset: 18:00
                       - Weather Moon Phase: full moon
                       - Weather Moon Age: 10 days

                       and if the user asked something else then you have to tell that you are not able capable of that 
                       """
            response = llm.prompt(prompt)
            st.markdown(response["message"])
    else:
        st.warning("Please enter a country name.")

# Add footer
st.markdown("---")

