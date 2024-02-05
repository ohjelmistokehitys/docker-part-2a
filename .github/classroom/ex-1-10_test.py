import sys
from tests import check, line

result = sys.stdin.read()
print(result)

line()

check("run" in result, "Make sure you included the command to run the container")
check("8080" in result, "Make sure you bind to the port 8080 in the container")

print("Success!")
