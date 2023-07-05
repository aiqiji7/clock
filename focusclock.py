import time

def focus_timer():
    cycles = 4 # 设置循环次数
    focus_time = 25 * 60 # 设置专注时间（25分钟）
    rest_time = 5 * 60 # 设置休息时间（5分钟）

    for i in range(cycles):
        print("开始专注，持续25分钟...")
        time.sleep(focus_time) # 等待25分钟

        print("休息5分钟...")
        time.sleep(rest_time) # 等待5分钟

    print("专注时钟完成！")

if __name__ == "__main__":
    focus_timer()
