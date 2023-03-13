# 登入帳號三次錯誤機會

defaultUserName = "admin"
defaultPassword = "1234"

for i in range(3):
    inputUserName = input("請輸入用戶名: ")
    inputPassword = input("請輸入密碼: ")

    if inputUserName == defaultUserName:
        if inputPassword == defaultPassword:
            print("登入成功!")

        else:
            print(f"密碼錯誤，剩下 {2 - i} 次機會!")
    else:
        print(f"用戶名錯誤，剩下 {2 - i} 次機會!")
print("3次機會已用盡!")