import requests
import streamlit as st


# Url
url = f"https://api.nasa.gov/planetary/apod?api_key={st.secrets.api_key}"

# Get data from url
response = requests.get(url)
content = response.json()

# Get title and explanation
title = content["title"]
explanation = content["explanation"]

# Get image
image_response = requests.get(content["hdurl"])
image_content = image_response.content
with open("images/image.jpg", "wb") as file:
    file.write(image_content)

# Display all the elements
st.header(title)
st.image("images/image.jpg")
st.write(explanation)
