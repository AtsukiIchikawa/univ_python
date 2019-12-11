import time

# 処理開始時間
start = time.time()

for i in range(0, 11):
    print("a")

# 処理終了時間
end = time.time()


# 経過時間
proc_time = end - start

print(proc_time)
