# 登入帳號三次錯誤機會

# 設定預設帳號名稱和密碼
defaultUserName = "admin"
defaultPassword = "1234"
i = 0

# 迭代三次，表示最多輸入三次
while i < 3:
    # 讓用戶輸入帳號名稱和密碼
    inputUserName = input("請輸入用戶名: ")
    inputPassword = input("請輸入密碼: ")

    # 判斷用戶輸入的帳號名稱和密碼是否與預設值相符
    if inputUserName == defaultUserName:
        if inputPassword == defaultPassword:
            # 登入成功
            print("登入成功!")
            break
        else:
            # 密碼錯誤
            print(f"密碼錯誤，剩下 {2 - i} 次機會!")
            i += 1
    else:
        # 帳號名稱錯誤
        print(f"用戶名錯誤，剩下 {2 - i} 次機會!")
        i += 1
    if i >= 3:
        # 迭代三次之後，如果還是無法成功登入，則輸出錯誤訊息
        print("3次機會已用盡!")
        break
