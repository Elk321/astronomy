import requests
import streamlit as st
from pytube import YouTube

st.set_page_config(page_title="Astronomy Image", page_icon="telescope.png")

hide_st_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                header {visibility: hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Url
url = f"https://api.nasa.gov/planetary/apod?api_key={st.secrets.api_key}"

# Get data from url
response = requests.get(url)
content = response.json()

# Get title and explanation
title = content["title"]
explanation = content["explanation"]

if content["media_type"] == "video":
    # Get video
    # Youtube video
    if "youtube" in content["url"]:
        yt = YouTube(content["url"])
        video = yt.streams.get_highest_resolution()
        video.download("videos/", "video.mp4",
                       skip_existing=False)
    else:
        video_response = requests.get(content["url"])
        video_data = video_response.content
        with open("videos/video.mp4", "wb") as file:
            file.write(video_data)
    # Display video
    st.title(title)
    st.video("videos/video.mp4")
    st.write(explanation)
else:
    # Get image
    image_response = requests.get(content["hdurl"])
    image_content = image_response.content
    with open("images/image.jpg", "wb") as file:
        file.write(image_content)

    # Display image
    st.title(title)
    st.image("images/image.jpg")
    st.write(explanation)