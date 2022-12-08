set_countries = {'col', 'mex', 'bol'}

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

# add() agregar un elemento al set
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)

# update() Añade cualquier tipo de objeto iterable como listas o tuplas.
# es decir, para agregar más de un elemento, necesito esta función.
set_countries.update({'ar', 'ec', 'pe'})
print(set_countries)

# remove() Elimina un elemento y si no existe, levanta un error "KeyError".
set_countries.remove('ec')
print(set_countries)

set_countries.remove('ar')
print(set_countries)

# discard() si el argumento no se encuentra en el set no lanza la excepción.
set_countries.discard('arg')
set_countries.add('arg')
print(set_countries)

# clear() borra todos los elementos en el set.
set_countries.clear()
print(set_countries)