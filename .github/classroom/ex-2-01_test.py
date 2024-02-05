import sys
from tests import check, line

result = sys.stdin.read()
print(result)

line()

check("name" in result, "The compose file must be valid")
check("devopsdockeruh/simple-web-service" in result, "You must use the devopsdockeruh/simple-web-service container image in this exercise")
check("/usr/src/app" in result, "You need to mount the text file under /usr/src/app into local filesystem")

print("Success!")
