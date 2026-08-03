import requests
from bs4 import BeautifulSoup

# Empire's 100 Greatest Movies - Archived version use karo
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")

# Movie titles find karo (h3 tags with class "title")
movies = soup.find_all(name="h3", class_="title")

movie_list = []
for movie in movies:
    text = movie.string
    if text:
        movie_list.append(text)

# Reverse karo (1 se 100 ke order mein)
movie_list.reverse()

# Text file mein save karo
with open("movies.txt", mode="w", encoding="UTF-8") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")

print(f"✅ {len(movie_list)} movies saved to movies.txt!")