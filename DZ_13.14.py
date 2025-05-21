purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

#1. total_revenue(purchases): Рассчитайте и верните общую выручку (цена * количество для всех записей).
def total_revenue(purchases):
    res = sum(sl['price']*sl['quantity'] for sl in purchases)
    return f'Общая выручка: {res}'
print(total_revenue(purchases))

#2. items_by_category(purchases): Верните словарь, где ключ — категория, а значение — список уникальных товаров в этой категории.
def items_by_category(purchases):
    res = {}
    for sl in purchases:
        res[sl['category']] = res.get(sl['category'], []) + [sl['item']] 
    return f'Товары по категориям: {res}'
print(items_by_category(purchases))

#3. expensive_purchases(purchases, min_price): Выведите все покупки, где цена товара больше или равна min_price.
def expensive_purchases(purchases, min_price:int) -> str:
    res = [sl for sl in purchases if sl['price']>=min_price]
    return f'Покупки дороже {min_price}: {res}'
print(expensive_purchases(purchases, 1.0))

#4. average_price_by_category(purchases): Рассчитайте среднюю цену товаров по каждой категории.
def average_price_by_category(purchases):
    res = {}
    for sl in purchases:
        res[sl['category']] = res.get(sl['category'], []) + [[sl['item'], sl['quantity']]]
    r = {}
    for k, v in res.items():
        if len(v)==1:
            r[k] = v[0][1]
        else:
            r[k] = sum(i[1] for i in v)/(len(v))
    return f'Средняя цена по категориям: {r}'
print(average_price_by_category(purchases))

#5. most_frequent_category(purchases): Найдите и верните категорию, в которой куплено больше всего единиц товаров (учитывайте поле quantity).
def most_frequent_category(purchases):
    res = {}
    for sl in purchases:
        res[sl['category']] = res.get(sl['category'], []) + [sl['quantity']]
    res = {k:sum(v) for k, v in res.items()}
    r = [k for k, v in res.items() if v==max(res.values())]
    return 'Категория с наибольшим количеством проданных товаров:', *r
print(*most_frequent_category(purchases))