item_all = []
cost_sum = 0

while True:

    # 選擇功能
    print('--- 消費紀錄統計系統 ---')
    print('1. 新增消費')
    print('2. 顯示消費明細')
    print('3. 顯示統計')
    print('4. 退出系統')
    print('------------------------')
    choice = input("請選擇功能: ")

    # 新增消費
    if choice == '1':
        name = input('請輸入消費項目: ')

        while True:
            cost = input('請輸入金額: ').strip()
            if cost.replace(".", "", 1).isascii() and cost.replace(".", "", 1).isdigit():
                if float(cost) > 0:
                    item_all.append({"項目":name, "金額":float(cost)})
                    cost_sum += float(cost)
                    break
                else:
                    print('請輸入大於 0 的有效金額。')

            else:
                print('請輸入大於 0 的數字，可包含小數點。')

        print('新增成功。')
        print()

    # 顯示消費明細
    elif choice == '2':
        if len(item_all) >= 1:
            print()
            print('--- 消費明細 ---')
            print('編號  項目          金額')
            print('------------------------')
            for i, item in enumerate(item_all):
                print(f'{i+1:>4}{item["項目"]:>4}{item["金額"]:14.2f}')
        else:
            print('目前沒有消費紀錄。')
        print()

    # 顯示統計
    elif choice == '3':
        if len(item_all) >= 1:
            print()
            print('--- 消費統計 ---')
            print(f'消費筆數: {len(item_all)}')
            print(f'總金額: {cost_sum:.2f} 元')
            print(f'平均每筆金額: {cost_sum/len(item_all):.2f} 元')
            print('消費提醒: ', end='')

            if cost_sum >= 500:
                print('已達提醒門檻')
            elif cost_sum >= 300:
                print('注意控制消費')
            else:
                print('消費不多')
        else:
            print('目前沒有消費紀錄。')
        print()

    # 退出系統
    elif choice == '4':
        print('系統已退出。')
        break
    else:
        print('選項錯誤，請重新選擇。')
        print()