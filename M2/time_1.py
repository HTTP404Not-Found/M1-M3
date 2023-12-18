# 引入 time 模組
import time

# 開始測量
start = time.time()

# 要測量的程式碼
un1 = 4
un1 += 3
print(un1)

# 結束測量
end = time.time()

# 輸出結果
print("執行時間：%f 秒" % (end - start))