import sys
from tests import check, line

result = sys.stdin.read()
print(result)

line()

check("name" in result, "The compose file must be valid")
check("redis" in result, "You need to add a redis service in your Docker compose file")
check("REDIS_HOST" in result, "Make sure the backend has the required environment variable for connecting to redis")
check('published: "6379"' not in result, "You should not publish the Redis port to Redis to the outside world")

print("Success!")
