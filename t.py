# def read_sales_data(file_path):
#     data = open(file_path, 'r')
#     content = data.readlines()
#     keys = ['product_name', 'quantity', 'price', 'date']
    
#     dictionary = dict(zip(keys, content))
#     return content[0]

# path = input()
# print(read_sales_data(path))

def read_sales_data(file_path):
    data = open(file_path, 'r')
    content = data.readlines()
    return content

path = input()
print(read_sales_data(path))

    



 



