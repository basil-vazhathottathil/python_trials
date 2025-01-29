def add_new_item(inventory):
    name = input('Enter the product name: ')
    product_id = input('Enter the product id: ')
    category = input('Enter the product category: ')
    stock = int(input('Enter the stock: '))
    price = float(input('Enter the price: '))
    discount = float(input('Enter the discount: '))
    print('\n\n\n')
    inventory[name] = [product_id, stock, price, discount]

def display_item(name, inventory):
    if name in inventory:
        product_info = inventory[name]
        print(f'Product ID: {product_info[0]}')
        print(f'Stock: {product_info[1]}')
        print(f'Price: {product_info[2]}')
        print(f'Discount: {product_info[3]}')
        
    else:
        print('Product not found in inventory.')
    
    print('\n\n')

def update_info(name, inventory):
    if name in inventory:
        product_info = inventory[name]
        print('You cannot update the product id, name, category')
        product_info[1] = int(input('Enter the updated stock: '))
        product_info[2] = float(input('Enter the updated price: '))
        product_info[3] = float(input('Enter the updated discount: '))
    else:
        print('Product not found in inventory.')

    print('\n\n')

def main():
    inventory = {}
    
    ask1 = input('Do you want to add another item (y or n): ')
    count = int(input('How many items do you need to add: '))
    for i in range(count):
        if ask1.lower() == 'y':
            add_new_item(inventory)
    
    ask2 = input('Do you want to update a product info (y or n): ')
    if ask2.lower() == 'y':
        name = input('Enter the product name: ')
        if name in inventory:
            update_info(name, inventory)
        else:
            print('Product not found in inventory.')

    ask3 = input('Do you want to view item details (y or n): ')
    if ask3.lower() == 'y':
        name = input('Enter the product name: ')
        display_item(name, inventory)


main()