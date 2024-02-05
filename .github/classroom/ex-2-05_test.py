import sys
from tests import check, line

result = sys.stdin.read()
print(result)

line()

check("docker" in result, "The command must start with docker")
check("compose" in result, "The command must contain 'compose'")
check("scale" in result, "Make sure to *scale* the compute service in your command")
check("compute" in result, "Make sure to scale the *compute* service in your command")

print("Success!")
