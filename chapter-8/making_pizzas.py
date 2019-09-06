# 第一种导入方式
import pizza_module
# 第二种导入方式
from pizza_module import make_size_pizza

# 给导入的函数起别名as
from pizza_module import make_pizza as mp

# 给模块其别名 as
import pizza_module as p

# 导入引入模块的所有的函数
from pizza_module import *

pizza_module.make_pizza('mushrooms')

pizza_module.make_size_pizza(16, 'mushrooms', 'green pepper')

make_size_pizza(9, 'mushrooms', 'green pepper')

mp('mushrooms')

p.make_pizza('mushrooms')
