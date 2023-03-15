# 登入帳號且增加改密碼選項（第四題進階版）

# 設置默認用戶名和密碼
defaultUserName = "admin"
defaultPassword = "1234"
# 設置登入狀態的變量，預設為False，表示未登入
loggedIn = False

# 進入主循環
while True:
    print("----------")
    print("1. 登入")
    print("2. 修改密碼")
    print("3. 退出系統")
    choice = int(input())  # 輸入用戶選擇的操作

    if choice == 1:  # 如果用戶選擇登入
        i = 0  # 設置計數器，用於計算輸入用戶名和密碼的次數
        while i < 3:  # 設置while循環
            if i < 3:  # 如果輸入錯誤的次數小於3
                inputUserName = input("請輸入用戶名: ")
                inputPassword = input("請輸入密碼: ")

                if inputUserName == defaultUserName:  # 如果輸入的用戶名正確
                    if inputPassword == defaultPassword:  # 如果輸入的密碼正確
                        print("登入成功!")
                        loggedIn = True  # 登入狀態設為True
                        break  # 跳出while循環
                    else:
                        print(f"密碼錯誤，剩下 {2 - i} 次機會!")
                        i = i + 1  # 輸入錯誤，計數器+1
                else:
                    print(f"用戶名錯誤，剩下 {2 - i} 次機會!")
                    i = i + 1  # 輸入錯誤，計數器+1
            else:
                print("3次機會已用盡!")  # 如果輸入錯誤的次數大於等於3，提示用戶已用盡機會

    elif choice == 2:  # 如果用戶選擇修改密碼
        if loggedIn:  # 如果已經登入
            oldPassword = input("請輸入舊密碼: ")
            newPassword = input("請輸入新密碼: ")
            confirmPassword = input("請再次輸入新密碼: ")

            if oldPassword == defaultPassword:  # 如果輸入的舊密碼正確
                if newPassword == confirmPassword:  # 如果輸入的新密碼和確認新密碼一致
                    defaultPassword = newPassword  # 將默認密碼設置為新密碼
                    print("密碼修改成功!")
                else:
                    print("確認新密碼錯誤!")
            else:
                print("舊密碼錯誤!") # 如果輸入的舊密碼不正確，顯示錯誤訊息
        else:
            print("請先登入!") # 如果未登入，提示用戶需要先登入

    elif choice == 3: # 選擇退出系統
        exit("再見!") # 退出程式，顯示再見訊息