"""Task - 11.1. Город, страна
    Task - 11.2. Население"""


def country_city(country: str, city: str, population: int = None) -> str:
    """Возвращает Страну + Имя города + население в формате:
        :return <<Country, City - population number>>
    """
    country, city = (_.capitalize() for _ in (country, city))
    if population:
        return f'<<{country}, {city} - population {population}>>'
    return f'<<{country}, {city}>>'
