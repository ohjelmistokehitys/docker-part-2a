import sys
from tests import check, line

result = sys.stdin.read()
print(result)

line()

check("You configured your ports correctly" in result, "Make sure you copied the message correctly")

print("Success!")
