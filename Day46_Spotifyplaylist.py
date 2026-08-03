import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Spotify Authentication
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
SPOTIPY_REDIRECT_URI = os.environ.get("SPOTIPY_REDIRECT_URI")

# User Input - Date
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Step 1: Scrape Billboard Hot 100
print(f"🎵 Scraping Billboard Hot 100 for {date}...")

BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date}/"

try:
    response = requests.get(BILLBOARD_URL)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all song titles
    song_titles = []
    song_elements = soup.select("li.o-chart-results-list__item h3.c-title")
    
    if not song_elements:
        print("❌ No songs found! Trying alternative selector...")
        song_elements = soup.select("div.o-chart-results-list__item h3.c-title")
    
    for element in song_elements[:100]:
        title = element.get_text().strip()
        if title:
            song_titles.append(title)
    
    # If still no songs, try the old Billboard structure
    if not song_titles:
        song_elements = soup.find_all(name="h3", class_="c-title")
        for element in song_elements:
            text = element.get_text().strip()
            if text and len(text) > 2:
                song_titles.append(text)
    
    if not song_titles:
        print("❌ Could not find any songs. The Billboard website structure might have changed.")
        print("🔍 Debug: Please check the HTML structure manually.")
        exit()
        
    print(f"✅ Found {len(song_titles)} songs!")
    
except Exception as e:
    print(f"❌ Error scraping Billboard: {e}")
    exit()

# Step 2: Authenticate with Spotify
print("🔐 Authenticating with Spotify...")

try:
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            redirect_uri=SPOTIPY_REDIRECT_URI,
            scope="playlist-modify-private",
            cache_path=".spotify_cache"
        )
    )
    
    user_id = sp.me()["id"]
    print(f"✅ Authenticated as: {sp.me()['display_name']}")
    
except Exception as e:
    print(f"❌ Spotify authentication failed: {e}")
    print("Make sure SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET are set correctly.")
    exit()

# Step 3: Search for songs on Spotify
print("🔍 Searching for songs on Spotify...")

song_uris = []
year = date.split("-")[0]

for song in song_titles:
    try:
        # Search query with year and track
        query = f"track:{song} year:{year}"
        result = sp.search(q=query, type="track", limit=1)
        
        if result["tracks"]["items"]:
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
            print(f"✅ Found: {song}")
        else:
            print(f"❌ Not found: {song}")
            
    except Exception as e:
        print(f"⚠️ Error searching for {song}: {e}")

# Step 4: Create playlist on Spotify
print("🎵 Creating playlist...")

try:
    # Create playlist
    playlist_name = f"{date} Billboard 100"
    playlist_description = f"Top 100 songs from {date} - Scraped using Python!"
    
    playlist = sp.user_playlist_create(
        user=user_id,
        name=playlist_name,
        public=False,
        description=playlist_description
    )
    
    playlist_id = playlist["id"]
    print(f"✅ Playlist created: {playlist_name}")
    
    # Add songs to playlist
    if song_uris:
        # Spotify API limit: 100 songs per request
        for i in range(0, len(song_uris), 100):
            batch = song_uris[i:i+100]
            sp.playlist_add_items(playlist_id=playlist_id, items=batch)
            print(f"✅ Added {len(batch)} songs to playlist")
    else:
        print("⚠️ No songs found to add to playlist")
        
except Exception as e:
    print(f"❌ Failed to create playlist: {e}")

print("\n🎉 Spotify Playlist Created Successfully!")
print(f"📱 Check your Spotify account: {playlist['external_urls']['spotify']}")