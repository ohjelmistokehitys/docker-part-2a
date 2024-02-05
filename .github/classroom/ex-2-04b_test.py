import sys
from tests import check, line

result = sys.stdin.read()
print(result)

line()

check("exercise is complete" in result, "The message shown in the browser was not found in the file.")

print("Success!")
