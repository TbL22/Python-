# 第6章：把菜单功能拆成函数

def format_money(value):
    return f"¥{value:.2f}"


def calculate_total(expenses):
    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    return total


def add_expense(expenses):
    date = input("日期：")
    category = input("类别：")
    amount = float(input("金额："))
    note = input("备注：")
    expense = {"date": date, "category": category,
               "amount": amount, "note": note}
    expenses.append(expense)
    print(f"添加成功，当前共 {len(expenses)} 笔。")


def show_expenses(expenses, category=None):
    number = 1
    count = 0
    for expense in expenses:
        if category is None or expense["category"] == category:
            print(number, expense["date"], expense["category"],
                  expense["note"], format_money(expense["amount"]))
            count = count + 1
        number = number + 1
    if category is not None:
        print(f"共 {count} 笔。")
    elif count == 0:
        print("暂无消费记录。")


def get_amount(expense):
    return expense["amount"]


def top_n(expenses, n=3):
    sorted_expenses = sorted(expenses, key=get_amount, reverse=True)
    return sorted_expenses[:n]


def show_statistics(expenses, category=None):
    selected = []
    for expense in expenses:
        if category is None or expense["category"] == category:
            selected.append(expense)
    if len(selected) == 0:
        print("暂无消费记录。")
        return
    total = calculate_total(selected)
    totals = {}
    for expense in selected:
        name = expense["category"]
        totals[name] = totals.get(name, 0) + expense["amount"]
    for name in totals:
        percent = 0
        if total != 0:
            percent = totals[name] / total * 100
        print(f"{name} {format_money(totals[name])} 占 {percent:.1f}%")
    print("金额前三名：")
    for expense in top_n(selected):
        print("    " + expense["note"], format_money(expense["amount"]))


def show_budget(expenses, budget):
    used = calculate_total(expenses)
    remaining = budget - used
    percent = used / budget * 100
    print(f"月度预算 {format_money(budget)} ／已用 {format_money(used)}"
          f" ／剩余 {format_money(remaining)}")
    print(f"已用比例 {percent:.1f}%")
    if percent < 80:
        print("预算状态良好。")
    elif percent <= 100:
        print("预算快要用完了。")
    else:
        print("预算已经超支了。")


def filter_expenses(expenses):
    category = input("要看哪个类别：")
    show_expenses(expenses, category)


def delete_expense(expenses):
    if len(expenses) == 0:
        print("暂无消费记录，不能删除。")
        return
    number = int(input("删除第几笔："))
    if 1 <= number <= len(expenses):
        removed = expenses.pop(number - 1)
        print("已删除：", removed["note"])
    else:
        print("序号无效，请重新选择。")


def show_menu():
    print("1.添加  2.查看  3.分类统计  4.预算状态  5.按类别查看  0.退出")
    print("6.删除第 n 笔")


expenses = []
monthly_budget = 1500
while True:
    show_menu()
    choice = input("请选择：")
    if choice == "1":
        add_expense(expenses)
    elif choice == "2":
        show_expenses(expenses)
    elif choice == "3":
        show_statistics(expenses)
    elif choice == "4":
        show_budget(expenses, monthly_budget)
    elif choice == "5":
        filter_expenses(expenses)
    elif choice == "6":
        delete_expense(expenses)
    elif choice == "0":
        print("再见！")
        break
    else:
        print("无效选项，请重新选择。")
