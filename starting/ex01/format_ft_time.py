from datetime import datetime
from decimal import Decimal

time = datetime.now()

seconds = time.timestamp()
sci_not = f"{Decimal(seconds):.2e}"

formatted_seconds = "{:,}".format(seconds)

print("Seconds since January 1, 1970:",
	   formatted_seconds, "or", sci_not, "in scientific notation")
print(time.strftime("%b %d %Y"))
