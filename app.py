import streamlit as st
import plotly.express as px
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    redirect_uri="http://localhost:8888/callback",
    scope="user-top-read"
))

results = sp.current_user_top_tracks(limit=10, time_range='short_term')

tracks = [track['name'] for track in results['items']]
artists = [track['artists'][0]['name'] for track in results['items']]
popularity = [track['popularity'] for track in results['items']]

st.title("🎧 Your Top Spotify Tracks")
df = pd.DataFrame({'Track': tracks, 'Artist': artists, 'Popularity': popularity})
fig = px.bar(df, x='Track', y='Popularity', color='Artist')
st.plotly_chart(fig)