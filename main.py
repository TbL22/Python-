"""CampusPocket 校园账本：第 2 章，输入一笔消费并判断预算。"""

import math

print("=== CampusPocket 校园账本 ===")

# input 得到字符串，float 把它转换成数字。
try:
    expense = float(input("请输入一笔消费金额（元）："))
    budget = float(input("请输入月度预算（元）："))
    if not math.isfinite(expense) or not math.isfinite(budget):
        raise ValueError
    if expense < 0 or budget <= 0:
        print("输入错误：消费不能为负数，月度预算必须大于 0。")
        raise SystemExit(1)

    # 转换为整数分，避免小数运算影响整除结果；输入最多保留两位小数。
    expense_cents = round(expense * 100)
    budget_cents = round(budget * 100)
    if expense != expense_cents / 100 or budget != budget_cents / 100:
        print("输入错误：金额最多保留两位小数。")
        raise SystemExit(1)
except (ValueError, OverflowError):
    print("输入错误：请输入有效的数字金额，例如 25.50。")
    raise SystemExit(1)

# 本版只计算这一次输入的消费，不累计其他消费。
remaining_cents = budget_cents - expense_cents
used_percent = expense_cents / budget_cents * 100
print(f"本次消费：{expense_cents / 100:.2f} 元")
print(f"月度预算：{budget_cents / 100:.2f} 元")
print(f"剩余金额：{remaining_cents / 100:.2f} 元")
print(f"已用比例：{used_percent:.1f}%")

# 直接比较金额，不能用四舍五入后的显示百分比判断。
if expense_cents * 100 < budget_cents * 80:
    print("预算提醒：低于 80%，预算充足。")
elif expense_cents <= budget_cents:
    print("预算提醒：80%—100%，接近或已用完预算，请节约开支。")
else:
    print("预算提醒：超过 100%，已经超出预算！")

# 选做：判断整数元，并用整除计算还可以消费多少笔。
if expense_cents % 100 == 0:
    print("这笔消费是整数元。")
else:
    print("这笔消费不是整数元。")

if expense_cents == 0:
    print("本次消费为 0 元，无法计算有限的同额消费笔数。")
elif remaining_cents < 0:
    print("还能再花 0 笔这样的消费（已经超出预算）。")
else:
    more_count = remaining_cents // expense_cents
    print(f"还能再花 {more_count} 笔这样的消费。")
