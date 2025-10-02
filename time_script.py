from datetime import datetime, timezone, timedelta

# 日本時間 (UTC+9)
JST = timezone(timedelta(hours=9))
now_jst = datetime.now(JST)
time_str = now_jst.strftime("%Y-%m-%d %H:%M:%S")

with open("now_time.txt", "w", encoding="utf-8") as f:
    f.write(time_str)

print("現在の日本時刻を now_time.txt に出力:", time_str)
