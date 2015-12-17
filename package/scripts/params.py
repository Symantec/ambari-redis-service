#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

from resource_management import *
import json

# server configurations
config = Script.get_config()

conf_dir = "/etc/"
redis_user = "root"
user_group = "root"
redis_slave = False

# redis configuration
daemonize = config['configurations']['redis']['daemonize']
port = config['configurations']['redis']['port']
bind = config['configurations']['redis']['bind']
timeout = config['configurations']['redis']['timeout']
pidfile = "/var/run/redis/redis.pid"

loglevel = config['configurations']['redis']['loglevel']
logfile = config['configurations']['redis']['logfile']
databases = config['configurations']['redis']['databases']
rdbcompression = config['configurations']['redis']['rdbcompression']
dbfilename = config['configurations']['redis']['dbfilename']
dbdir = config['configurations']['redis']['dbdir']
slave_serve_stale_data = config['configurations']['redis']['slave_serve_stale_data']
maxclients = config['configurations']['redis']['maxclients']
appendfsync = config['configurations']['redis']['appendfsync']
appendonly = config['configurations']['redis']['appendonly']
no_appendfsync_on_rewrite = config['configurations']['redis']['no_appendfsync_on_rewrite']
auto_aof_rewrite_percentage = config['configurations']['redis']['auto_aof_rewrite_percentage']
auto_aof_rewrite_min_size = config['configurations']['redis']['auto_aof_rewrite_min_size']
slowlog_log_slower_than = config['configurations']['redis']['slowlog_log_slower_than']
slowlog_max_len = config['configurations']['redis']['slowlog_max_len']

# Sentinel configuration
sentinel_port = config['configurations']['redis-sentinel']['sentinel_port']
sentinel_logfile = config['configurations']['redis-sentinel']['sentinel_logfile']
sentinel_log_dir = config['configurations']['redis-sentinel']['sentinel_log_dir']
master_name = config['configurations']['redis-sentinel']['master_name']
master_ip = config['configurations']['redis-sentinel']['master_ip']
quorum = config['configurations']['redis-sentinel']['quorum']
master_name = config['configurations']['redis-sentinel']['master_name']
blacklist_threshold = config['configurations']['redis-sentinel']['blacklist_threshold']
numslaves = config['configurations']['redis-sentinel']['numslaves']
sentinel_pidfile = "/var/run/redis/sentinel.pid"
known_slave = config['configurations']['redis-sentinel']['known_slave']
known_sentinel_1 = config['configurations']['redis-sentinel']['known_sentinel_1']
known_sentinel_2 = config['configurations']['redis-sentinel']['known_sentinel_2']

if 'ganglia_server_host' in config['clusterHostInfo'] and \
    len(config['clusterHostInfo']['ganglia_server_host'])>0:
  ganglia_installed = True
  ganglia_server = config['clusterHostInfo']['ganglia_server_host'][0]
  ganglia_report_interval = 60
else:
  ganglia_installed = False