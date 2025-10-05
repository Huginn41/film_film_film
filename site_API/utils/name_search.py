from typing import Dict

from database.common.models import SearchHistory, db
from database.core import crud

from settings import SiteSettings

from site_API.utils.siteAPI_handlers import SiteApiInterface, pars_film_data


def search_film(query: str, page: int = 1, limit: int = 1) -> Dict:
    """
    Поиск фильма по названию и сохранение результатов в историю поиска (базу данных)
    Args:
        query: Название фильма для поиска
        page: Номер страницы
        limit: Количество результатов
    :return:
        dict: Данные найденного фильма или пустой словарь
    """

    site = SiteSettings()
    url = site.site_url

    headers = {
        "accept": "application/json",
        "X-API-KEY": site.api_key
    }

    params = {
        'page': 1,
        'limit': 1,
        'query': 'Виноваты звезды'
    }

    #db_read = crud.retrieve()

    film_search = SiteApiInterface.find_film()

    try:
        response = film_search(
            'GET',
            f'{url}/search?',
            headers=headers,
            params=params
        ).json()

        data = pars_film_data(response.get('docs', []))
        if data:
            db_write = crud.create()
            db_write(db, SearchHistory, data)
            return data
        else:
            print(f"Фильм '{query}' не найден")
            return {}

    except Exception as e:
        print(f"Ошибка при поиске фильма '{query}': {e}")
        return {}

if __name__ == 'main':
    search_film()
