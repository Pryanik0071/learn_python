from chapter_9.one import Restaurant

if __name__ == '__main__':
    kfc = Restaurant('KFC', 'Европейская')
    burger_king = Restaurant('BurgerKing', 'Европейская')
    asia_food = Restaurant('Цань-Тао', 'Азиатская')

    kfc.describe_restaurant()
    burger_king.describe_restaurant()
    asia_food.describe_restaurant()
