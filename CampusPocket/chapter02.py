# 第二版：第2章校园账本，非法金额处理留到第9章。
# 假定消费不小于0、预算大于0，金额最多两位小数。
print("=== CampusPocket 校园账本 ===")

# 输入一笔消费和月度预算，预算要大于0
expense = float(input("请输入消费金额："))
budget = float(input("请输入月度预算："))

# 计算余额和已用百分比
remaining = budget - expense
percent = expense / budget * 100

# .2f表示保留两位小数，.1f表示保留一位小数
print(f"剩余金额：{remaining:.2f}元")
print(f"已用比例：{percent:.1f}%")

# 根据百分比给出提醒
if percent < 80:
    print("预算充足")
elif percent <= 100:
    print("接近或已用完预算，请节约开支")
else:
    print("已经超出预算")

# 除以1的余数为0，说明是整数元
if expense % 1 == 0:
    print("这笔消费是整数元")
else:
    print("这笔消费不是整数元")

# 计算还能支付几笔相同的消费
if expense == 0:
    print("消费为0元，不计算还能消费的笔数")
elif remaining < 0:
    print("还能再花0笔这样的消费")
else:
    # 换算成整数分，再用整除计算笔数，避免小数误差
    remaining_fen = round(remaining * 100)
    expense_fen = round(expense * 100)
    count = remaining_fen // expense_fen
    print("还能再花", count, "笔这样的消费")

