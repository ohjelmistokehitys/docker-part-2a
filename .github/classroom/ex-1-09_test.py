import sys
from tests import check, line

result = sys.stdin.read()
print(result)

line()

check("-v" in result, "Make sure to use -v or --volume")
check("/usr/src/app" in result, "Mount the text file under /usr/src/app")

print("Success!")
