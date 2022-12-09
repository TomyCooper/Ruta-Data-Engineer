items = [
  {
    'product': 'camisa',
    'price': 100,
  },
  {
    'product': 'pantalones',
    'price': 300
  },
  {
    'product': 'pantalones 2',
    'price': 200
  }
]

def add_taxes(item):
  new_item = item.copy() #OJO! AL UTILIZAR COPY, SE CREA UNA NUEVA REFERENCIA EN MEMORIA QUE PERMITE MODIFICAR SOLO EL ARRAY NUEVO.
  new_item['taxes'] = new_item['price'] * .19
  return new_item

new_items = list(map(add_taxes, items))
print('New list')
print(new_items)
print('Old list')
print(items)