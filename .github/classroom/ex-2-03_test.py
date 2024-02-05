import sys
from tests import check, line

result = sys.stdin.read()
print(result)

line()

check("name" in result, "The compose file must be valid")
check("8080" in result, "You need to bind a local port to the port 8080 of the backend container")
check("5000" in result, "You need to bind a local port to the port 5000 of the frontend container")

print("Success!")
