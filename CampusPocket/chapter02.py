"""第 2 章：输入一笔消费，计算余额并给出预算提醒。"""

print("=== CampusPocket 校园账本 ===")

# 本章假定输入合法：消费不小于 0，预算大于 0，金额最多两位小数。
# 非法金额的处理按照题目要求留到第 9 章。
expense = float(input("请输入一笔消费金额（元）："))
budget = float(input("请输入月度预算（元）："))

# 金额换算成整数分，避免小数误差影响还能消费的笔数。
expense_cents = round(expense * 100)
budget_cents = round(budget * 100)
remaining_cents = budget_cents - expense_cents
used_percent = expense_cents / budget_cents * 100

print(f"本次消费：{expense_cents / 100:.2f} 元")
print(f"月度预算：{budget_cents / 100:.2f} 元")
print(f"剩余金额：{remaining_cents / 100:.2f} 元")
print(f"已用比例：{used_percent:.1f}%")

# 80% 和 100% 都属于中间档；判断使用真实金额，不使用舍入后的显示值。
if expense_cents * 100 < budget_cents * 80:
    print("预算提醒：低于 80%，预算充足。")
elif expense_cents <= budget_cents:
    print("预算提醒：80%—100%，接近或已用完预算，请节约开支。")
else:
    print("预算提醒：超过 100%，已经超出预算！")

# 选做：判断整数元。
if expense_cents % 100 == 0:
    print("这笔消费是整数元。")
else:
    print("这笔消费不是整数元。")

# 选做：算出剩余预算还能支付几笔同额消费。
if expense_cents == 0:
    print("本次消费为 0 元，无法计算有限的同额消费笔数。")
elif remaining_cents < 0:
    print("还能再花 0 笔这样的消费（已经超出预算）。")
else:
    more_count = remaining_cents // expense_cents
    print(f"还能再花 {more_count} 笔这样的消费。")
