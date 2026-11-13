# day1_basics.py —— Python 第一天

# 1. 输出
print("你好，欢迎学习 AI 应用开发！")

# 2. 变量
name = input("请输入你的名字：")
age = input("请输入你的年龄：")

print(f"你好，{name}！你今年 {age} 岁。")

# 3. 数据类型
price = 99.5           # 浮点数
is_student = True      # 布尔值
skills = ["Python", "Excel", "AI"]  # 列表

print(f"技能列表：{skills}")
print(f"第一个技能：{skills[0]}")

# 4. 列表操作
skills.append("机器学习")
skills.remove("Excel")
print(f"更新后的技能：{skills}")

# 5. 简单判断
score = 85
if score >= 90:
    print("等级：优秀")
elif score >= 80:
    print("等级：良好")
else:
    print("等级：继续努力")

# 6. 循环
print("\n你的技能清单：")
for skill in skills:
    print("- " + skill)

# 7. 函数
def greet(name):
    return f"欢迎，{name}！祝你学习愉快。"

print(greet(name))