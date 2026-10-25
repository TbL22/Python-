# 第5章：用循环做一个可以反复使用的菜单

records = []
monthly_budget = 1500

while True:
    print("=== CampusPocket ===")
    print("1. 添加消费")
    print("2. 查看全部")
    print("3. 分类统计")
    print("4. 预算状态")
    print("5. 按类别筛选")
    print("6. 删除第 n 笔")
    print("0. 退出")

    choice = input("请选择：")

    if choice == "1":
        date = input("日期：")
        category = input("类别：")
        amount = float(input("金额："))
        note = input("备注：")

        record = {
            "date": date,
            "category": category,
            "amount": amount,
            "note": note
        }
        records.append(record)
        print(f"添加成功，当前共 {len(records)} 笔。")

    elif choice == "2":
        if len(records) == 0:
            print("暂无消费记录。")
        else:
            number = 1
            for record in records:
                print(f"{number} {record['date']} {record['category']} "
                      f"{record['note']} ¥{record['amount']:.2f}")
                number = number + 1

    elif choice == "3":
        if len(records) == 0:
            print("暂无消费记录。")
        else:
            totals = {}
            total_amount = 0

            for record in records:
                category = record["category"]
                amount = record["amount"]
                totals[category] = totals.get(category, 0) + amount
                total_amount = total_amount + amount

            for category in totals:
                percent = totals[category] / total_amount * 100
                print(f"{category} ¥{totals[category]:.2f} 占 {percent:.1f}%")

    elif choice == "4":
        used_amount = 0

        for record in records:
            used_amount = used_amount + record["amount"]

        remaining = monthly_budget - used_amount
        used_percent = used_amount / monthly_budget * 100

        print(f"月度预算 ¥{monthly_budget:.2f}，已用 ¥{used_amount:.2f}，"
              f"剩余 ¥{remaining:.2f}")
        print(f"已用比例 {used_percent:.1f}%")

        if used_percent < 80:
            print("预算状态良好。")
        elif used_percent <= 100:
            print("预算快要用完了。")
        else:
            print("预算已经超支了。")

    elif choice == "5":
        wanted_category = input("要看哪个类别：")
        count = 0

        for record in records:
            if record["category"] == wanted_category:
                print(f"{record['date']} {record['note']} "
                      f"¥{record['amount']:.2f}")
                count = count + 1

        print(f"共 {count} 笔。")

    elif choice == "6":
        if len(records) == 0:
            print("暂无消费记录，不能删除。")
        else:
            delete_number = int(input("删除第几笔："))

            if delete_number >= 1 and delete_number <= len(records):
                deleted_record = records.pop(delete_number - 1)
                print("已删除：", deleted_record["note"])
            else:
                print("序号无效，请重新选择。")

    elif choice == "0":
        print("再见！")
        break

    else:
        print("无效选项，请重新选择。")
