import matplotlib.pyplot as plt
from datetime import datetime

def read_sales_data(file_path):
    with open(file_path, 'r') as data:
        content = data.readlines()
    data = []
    keys = ['product_name', 'quantity', 'price', 'date'] 
    for content in content:
        if content.strip():
            parts = content.strip().split(', ')
            row = tuple(parts)
            data.append(row)
    result = dict(zip(keys, zip(*data)))
    return result

def total_sales_per_product(sales_data):
    product_name = list(sales_data['product_name'])
    quantitys = list(map(int, sales_data['quantity']))
    prices = list(map(int, sales_data['price']))
    sales_summury = {}
    for i in range(len(product_name)):
        product = product_name[i]
        quantity = quantitys[i]
        price = prices[i]
        total_sales = quantity * price       
        if product in sales_summury:
            sales_summury[product] += total_sales
        else:
            sales_summury[product] = total_sales       
    return sales_summury

def sales_over_time(sales_data):
    dates = list(sales_data['date'])
    quantitys = list(map(int, sales_data['quantity']))
    prices = list(map(int, sales_data['price']))
    sales_summury = {}
    for i in range (len(dates)):
        date = dates[i]
        quantity = quantitys[i]
        price = prices[i]
        total_sales = quantity * price
        if date in sales_summury:
            sales_summury[date] += total_sales
        else:
            sales_summury[date] = total_sales
    return sales_summury   

def show_bar_product(data):
    products = list(data.keys())
    total_price = list(data.values())
    plt.figure(figsize=(10, 10))
    plt.xlabel('Продукт')
    plt.ylabel('Сумма продаж')
    plt.xticks(rotation=45, ha='right')
    plt.bar(products, total_price)
    plt.show() 
    
def show_bar_date(data):
    products = list(data.keys())
    total_price = list(data.values())
    plt.figure(figsize=(10, 10))
    plt.xlabel('Продукт')
    plt.ylabel('Сумма продаж')
    plt.xticks(rotation=45, ha='right')
    plt.bar(products, total_price)
    plt.show()
    
path = input('Введите путь к файлу или его название: ')

sales_data = read_sales_data(path)
sales_per_product = total_sales_per_product(sales_data)
sales_time = sales_over_time(sales_data)

most_sales_product = max(sales_per_product, key=sales_per_product.get)
most_sales_date = max(sales_time, key=sales_time.get)

#Cортировка по значению словаря
product_sorted = dict(sorted(sales_per_product.items(), key=lambda item: item[1], reverse=True))
date_sorted = dict(sorted(sales_time.items(), key=lambda item: item[1], reverse=True))

print(f'Наибольшую выручку принёс продукт: {most_sales_product}')
print(f'Наибольшая сумма продаж была: {most_sales_date}')

show_bar_product(product_sorted)
show_bar_date(date_sorted)