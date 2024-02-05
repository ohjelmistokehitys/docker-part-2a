import sys
from tests import check, line

result = sys.stdin.read()
print(result)

line()

check("Success!" in result, "Make sure you copied the message correctly")
check("Great job!" in result, "Make sure you copied the message correctly")

print("Success!")
