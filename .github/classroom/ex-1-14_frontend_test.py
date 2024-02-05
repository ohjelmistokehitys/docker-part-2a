import sys
from tests import check, line

result = sys.stdin.read()
print(result)

line()

check("FROM" in result.upper(), "Make sure to write a valid Dockerfile")
check("REACT_APP_BACKEND_URL" in result, "Make sure to define the REACT_APP_BACKEND_URL environment variable in the Dockerfile")

print("Success!")
