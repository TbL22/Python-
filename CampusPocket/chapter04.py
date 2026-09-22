# 第4章：用字典保存完整的消费记录
record1 = {
    "date": "2026-09-01",
    "category": "餐饮",
    "amount": 18.5,
    "note": "食堂午餐"
}

record2 = {
    "date": "2026-09-01",
    "category": "交通",
    "amount": 2.0,
    "note": "校园公交"
}

record3 = {
    "date": "2026-09-02",
    "category": "餐饮",
    "amount": 8.0,
    "note": "奶茶"
}

record4 = {
    "date": "2026-09-02",
    "category": "学习",
    "amount": 12.0,
    "note": "打印资料"
}

# 用列表保存4条记录
records = [record1, record2, record3, record4]

# 用集合保存不重复的类别
categories = {
    record1["category"],
    record2["category"],
    record3["category"],
    record4["category"]
}

# 用get按类别汇总，本章还没学循环，所以写4行
totals = {}
totals[record1["category"]] = totals.get(record1["category"], 0) + record1["amount"]
totals[record2["category"]] = totals.get(record2["category"], 0) + record2["amount"]
totals[record3["category"]] = totals.get(record3["category"], 0) + record3["amount"]
totals[record4["category"]] = totals.get(record4["category"], 0) + record4["amount"]

# 计算合计和各类占比
total_amount = record1["amount"] + record2["amount"] + record3["amount"] + record4["amount"]
totals_sum = totals["餐饮"] + totals["交通"] + totals["学习"]
food_percent = totals["餐饮"] / total_amount * 100
transport_percent = totals["交通"] / total_amount * 100
study_percent = totals["学习"] / total_amount * 100

print("=== CampusPocket 分类统计 ===")
print("第一笔记录：", records[0])
print("第一笔金额：", records[0]["amount"])
print("记录总数：", len(records))
print("消费类别（已去重）：", categories)
print("----------------------------------")
print("按类别汇总：", totals)
print("汇总合计：", totals_sum, "／ 总额：", total_amount)
print("----------------------------------")
print(f"餐饮占比： {food_percent:.1f} %")
print(f"交通占比： {transport_percent:.1f} %")
print(f"学习占比： {study_percent:.1f} %")

# 还没学循环，用if找出金额最多的类别
largest_category = "餐饮"
largest_amount = totals["餐饮"]

if totals["交通"] > largest_amount:
    largest_category = "交通"
    largest_amount = totals["交通"]

if totals["学习"] > largest_amount:
    largest_category = "学习"
    largest_amount = totals["学习"]

largest_percent = largest_amount / total_amount * 100
print(f"你花得最多的是「{largest_category}」，占 {largest_percent:.1f}%。")

# 验证各类别汇总之和是否等于总额
check_result = totals_sum == total_amount
