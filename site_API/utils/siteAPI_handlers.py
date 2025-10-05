from typing import Dict

import requests


def _search(method: str, url, headers: Dict, params: Dict, success=200):
    response = requests.request(
        method,
        url,
        headers=headers,
        params=params,

    )
    status_code = response.status_code
    if status_code == success:
        return response

    return status_code


def _get_search_result(method, url, headers: Dict, params: Dict, func=_search):
    url = '{}/{}'.format(url, params)
    response = func(method, url, headers=headers, params=params)

    return response


class SiteApiInterface():
    @staticmethod
    def find_film():
        return _get_search_result


def pars_film_data(moviee_data):
    movies = []

    for movie_data in moviee_data:
        movie = {
            'movie_name': movie_data.get('name', 'Неизвестно'),
            'description': movie_data.get('description'),
            'rating': movie_data.get('rating', {}).get('kp'),
            'year': movie_data.get('year', 0),
            'genres': [genre.get('name', '') for genre in movie_data.get('genres', [])],
            'age_rating': movie_data.get('ageRating'),
            'poster_url': movie_data.get('poster', {}).get('url')
        }
        movies.append(movie)
    return movies


if __name__ == 'main':
    _search()
    _get_search_result()
    pars_film_data()

    SiteApiInterface()
