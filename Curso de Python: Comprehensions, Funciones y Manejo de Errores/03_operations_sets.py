set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# UNION
set_c = set_a.union(set_b)
print(set_c)
print(set_a | set_b)

# INTERSECTION
set_c = set_a.intersection(set_b)
print(set_c)
print(set_a & set_b)

# DIFFERENCE: OJO! Va a mantener los elementos de A y le quita los elementos de B.
set_c = set_a.difference(set_b)
print(set_c)
print(set_a - set_b)

# SYMMETRIC_DIFFERENCE: OJO! Es lo mismo que una UNION y luego quitar los elementos en la intersección
set_c = set_a.symmetric_difference(set_b)
print(set_c)
print(set_a ^ set_b)