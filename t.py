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

#поменять Дата на СейлсДата
def total_sales_per_product(data):
    product_name = list(data['product_name'])
    quantitys = list(map(int, data['quantity']))
    prices = list(map(int, data['price']))
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
path = input()
sales_data = read_sales_data(path)
sales_per_product = total_sales_per_product(sales_data)
sales_time = sales_over_time(sales_data)

most_sales_product = max(sales_per_product)
most_sales_date = max(sales_time)

print(f'Самый продаваемый товар: {most_sales_product}')
print(f'Наибольшая сумма продаж была: {most_sales_date}')


