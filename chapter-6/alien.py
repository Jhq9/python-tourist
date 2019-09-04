# 字典 key:value
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')

# 向已存在的字典添加新的键值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 创建了一个空字典
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 4
print(alien_0)


# 修改字典中的值
alien_0['color'] = 'yellow'
print('The alien is now ' + alien_0['color'])

# del 删除字典中的key
del alien_0['color']
print(alien_0)