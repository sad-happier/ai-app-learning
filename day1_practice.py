print("=== 简易 AI 助手 ===")
print("我可以帮你：.计算两个数之和  2.判断奇偶  3.退出程序")

while True:
    choice = input("请输入你的选择（1/2/3）：")

    if choice == "1":
        num1 = float(input("请输入第一个数字："))
        num2 = float(input("请输入第二个数字："))
        result = num1 + num2
        print(f"结果：{num1} + {num2} = {result}")

    elif choice == "2":
        num = int(input("请输入一个整数："))
        if num % 2 == 0:
            print(f"{num} 是偶数。")
        else:
            print(f"{num} 是奇数。")

    elif choice == "3":
        print("退出程序。再见！")
        break

    else:
        print("无效的选择，请重新输入。")

