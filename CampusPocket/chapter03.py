# 第3章：用两个列表保存5笔消费
items = ["食堂午餐", "校园公交", "打印资料", "奶茶", "社团聚餐"]
amounts = [18.5, 2.0, 12.0, 8.0, 25.0]

print("=== CampusPocket 消费记录 ===")
print("全部项目：", items)
print("全部金额：", amounts)

# [-3:]表示取出最后3个元素，原来的顺序不变
print("最近3笔项目：", items[-3:])
print("最近3笔金额：", amounts[-3:])
print("----------------------------------")

# len求笔数，sum求总额
count = len(amounts)
total = sum(amounts)
average = total / count
print("消费笔数：", count)
print(f"消费总额： {total:.2f}")
print(f"平均每笔： {average:.2f}")
print("----------------------------------")

# reverse=True表示从大到小排序，[:3]取前三个
sorted_amounts = sorted(amounts, reverse=True)
print("金额前三名：", sorted_amounts[:3])

# index找到金额的位置，再到items中取对应的项目名
largest = max(amounts)
smallest = min(amounts)
print(f"最大一笔： {largest:.2f}", items[amounts.index(largest)])
print(f"最小一笔： {smallest:.2f}", items[amounts.index(smallest)])
print("----------------------------------")

# 每满2元画一个方块，ljust(6)在项目名右侧补空格
# 还没有学循环，所以先按顺序写5行
print(items[0].ljust(6), "█" * int(amounts[0] // 2), f"{amounts[0]:.2f}")
print(items[1].ljust(6), "█" * int(amounts[1] // 2), f"{amounts[1]:.2f}")
print(items[2].ljust(6), "█" * int(amounts[2] // 2), f"{amounts[2]:.2f}")
print(items[3].ljust(6), "█" * int(amounts[3] // 2), f"{amounts[3]:.2f}")
print(items[4].ljust(6), "█" * int(amounts[4] // 2), f"{amounts[4]:.2f}")
