# 列表的切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])
# 如果没有指定起始索引，默认从列表开头开始
print(players[:4])
# 如果没有截止索引，默认从列表的结尾结束
print(players[1:])


print(players[-3:])

print("Here are the first three players on my team:")
for player in players[2:]:
    print(player.title())