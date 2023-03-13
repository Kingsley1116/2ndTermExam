# 利用所學知識“for”迴圈進行計算1-自變量n的各偶數之和之值

n = int(input("請輸入整數: "))
total = 0

for i in range(1, n + 1):
    # 偶數
    if i % 2 == 0:
        total += i
print(f"偶數之和之值為: {total}")