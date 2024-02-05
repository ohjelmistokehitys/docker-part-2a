import sys
from tests import check, line

result = sys.stdin.read()
print(result)

line()

check("name" in result, "The compose file must be valid")
check("devopsdockeruh/simple-web-service" in result, "You must use the devopsdockeruh/simple-web-service container image in this exercise")
check("8080" in result, "You need to bind a local port to the port 8080 inside the container")
check("command" in result, "You need to provide a command for the container to start the server")

print("Success!")
