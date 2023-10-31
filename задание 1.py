def find_index(list_of_products, product):  # Функция поиска товара
    for index_product in range(0, len(list_of_products) + 1):  # Перебор элементов списка
        if product in list_of_products:  # Сопоставление товара и элементов списка
            return list_of_products.index(product)  # Возвращение значения индекса продукта


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index(items_list, find_item)
    # Приём аргументов функции : списка товаров items_list и товара find_item
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
