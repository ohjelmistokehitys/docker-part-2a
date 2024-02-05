import sys
from tests import check, line

result = sys.stdin.read()
print(result)

line()

check("FROM" in result.upper(), "Make sure to write a valid Dockerfile")
check("build" in result, "See the README about how to build the app")
check("server" in result, "Make sure you use the right command to start the server")

print("Success!")
