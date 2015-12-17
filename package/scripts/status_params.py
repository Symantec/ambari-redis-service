#!/usr/bin/env python
"""
Redis service params

"""

from resource_management import *

config = Script.get_config()

redis_pid_file = format("/var/run/redis/redis.pid")
sentinel_pid_file = format("/var/run/redis/sentinel.pid")