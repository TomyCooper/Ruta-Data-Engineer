from pkg.mod_1 import func_1, func_2
from pkg.mod_2 import func_3, func_4

print(func_1())
print(func_2())
print(func_3())
print(func_4())

import pkg

print(pkg.URL)

# Esta línea genera error si y solo si no se hace la importación explícita
# como en las líneas 1 y 2.
# 
# Para solucionar dicho error, se puede agregar esas importaciones explícitas
# en el __init__.py
print(pkg.mod_1.func_1()) 