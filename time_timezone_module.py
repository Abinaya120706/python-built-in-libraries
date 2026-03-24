from datetime import datetime
import pytz
import time
import sys

# -------- Timezone Example --------
t = pytz.timezone("Asia/Tokyo")
t1 = datetime.now(t)
print("Current Time in Tokyo:", t1)


# -------- Digital Clock --------
h = 3
m = 25
s = 0

print("\nDigital Clock:\n")

while True:
    # Print time in same line
    sys.stdout.write("\r{:02d}:{:02d}:{:02d}".format(h, m, s))
    sys.stdout.flush()

    time.sleep(1)
    s += 1

    if s == 60:
        s = 0
        m += 1

    if m == 60:
        m = 0
        h += 1

    if h == 24:   # 24-hour format
        h = 0
