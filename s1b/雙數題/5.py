# 登入帳號且增加改密碼選項（第四題進階版）

defaultUserName = "admin"
defaultPassword = "1234"

def main():
    print("----------")
    print("1. 登入")
    print("2. 退出系統")
    choice = int(input())

    if choice == 1:
        system()
    else:
        exit("bye 9 bye!")

def system():
    global defaultPassword
    for i in range(3):

        inputUserName = input("請輸入用戶名: ")
        inputPassword = input("請輸入密碼: ")

        if inputUserName == defaultUserName:
            if inputPassword == defaultPassword:
                print("登入成功!")

                while True:
                    print("----------")
                    print("1. 登出")
                    print("2. 修改密碼")

                    choice = int(input())

                    if choice == 1:
                        print("bye 9 bye!")
                        main()

                    elif choice == 2:
                       changePassword() 
            else:
                print(f"密碼錯誤，剩下 {2 - i} 次機會!")
        else:
            print(f"用戶名錯誤，剩下 {2 - i} 次機會!")
    print("3次機會已用盡!")

def changePassword():
    global defaultPassword
    oldPassword = input("請輸入舊密碼: ")
    newPassword = input("請輸入新密碼: ")
    confirmPassword = input("請再次輸入新密碼: ")

    if oldPassword == defaultPassword:
        if newPassword == confirmPassword:
            defaultPassword = newPassword
            print("密碼修改成功!")
        else:
            print("確認新密碼錯誤!")
    else:
        print("舊密碼錯誤!")

if __name__ == "__main__":
    main()