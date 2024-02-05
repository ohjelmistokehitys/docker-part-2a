import sys
from tests import check, line

result = sys.stdin.read()
print(result)

line()

check("FROM" in result.upper(), "Make sure to write a valid Dockerfile")
check("install" in result, "See the README about how to install the app")
check("serve" in result, "Make sure you use the `serve` command")

print("Success!")
