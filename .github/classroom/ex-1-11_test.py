import sys
from tests import check, line

result = sys.stdin.read()
print(result)

line()

check("FROM" in result.upper(), "Make sure to write a valid Dockerfile")
check("/mvnw package" in result, "See the README about how to package the app")
check(".jar" in result, "Make sure that the packaged app is executed when the container starts")

print("Success!")
