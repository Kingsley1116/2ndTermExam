#　定義函數判別a和b的大小，輸出ab之中的最小值

def compare(a, b):
    if a > b:
        return b
    else:
        return a

min = compare(int(input("請輸入整數: ")), int(input("請輸入整數: ")))
print(f"最小值為: {min}")