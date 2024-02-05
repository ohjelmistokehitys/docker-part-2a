import sys
from tests import check, line

result = sys.stdin.read()
print(result)

line()

check("FROM" in result.upper(), "Make sure to write a valid Dockerfile")
check("REQUEST_ORIGIN" in result, "Make sure to define the REQUEST_ORIGIN environment variable in the Dockerfile")

print("Success!")
