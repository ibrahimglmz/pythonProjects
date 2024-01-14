
import requests


api_key = "f5d1c882fd5b8366bea70fbf222f7a89"
base_url = "https://api.themoviedb.org/3"

def film_ara(query):
    aranacak_url = f"{base_url}/search/movie"
    params = {
        "api_key": api_key,
        'query': query
    }

    response = requests.get(aranacak_url, params=params)
    data = response.json()

    if 'results' in data:
        movies = data['results']
        for movie in movies:
            print(f"Title: {movie['title']},Release Date: {movie['release_date']}")

movi_query = input("Film Adı Giriniz: ")

film_ara(movi_query)