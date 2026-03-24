from datetime import datetime
import pytz

# Set timezone
a = pytz.timezone("Asia/Tokyo")

# Current time in Tokyo
b = datetime.now(a)

print("Tokyo Time:", b)
