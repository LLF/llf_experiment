#-*- coding: utf-8 -*-
import redis
DEFAULT_PORT = 6379
DEFAULT_DB = 0
MAX_CONNECTIONS = 1000
BLOCK_TIMEOUT = 2

CONNECTION_POOL={}
def get_connection(setting):
    s = setting
    opts = {
            'host' : s['HOST'],
            'port' : int(s.get('PORT', DEFAULT_PORT)),
            'db'   : s.get('DB', DEFAULT_DB),
            }
    return RedisConnection(**opts)

class RedisConnection(object):
    def __init__(self, host='127.0.0.1', port=DEFAULT_PORT, db=DEFAULT_DB):
        self.host = host
        self.port = port
        self.db = db

        self.con = redis.BlockingConnectionPool(max_connections=MAX_CONNECTIONS,
                timeout=BLOCK_TIMEOUT,
                host=self.host,
                port=self.port,
                db=self.db,
                )

class RedisClient(object):
    def __init__(self, setting, connection=None):
        self.setting = setting
        self.connection = connection if connection else get_connection(setting)
        self.client = redis.Redis(connection_pool=self.connection.con)


        def get_client(name="default", setting=None):
            if name not in CONNECTION_POOL:
                CONNECTION_POOL[name] = get_connection(setting[name])
                connection = CONNECTION_POOL[name]

                return RedisClient(setting[name], connection=connection)

REDIS_DATABASES = {
      'shard0': {
          'HOST': 'localhost',
          'PORT': '6379',
          },
      'shard1': {
          'HOST': 'localhost',
          'PORT': '6380',
          },
      'shard2': {
          'HOST': 'localhost',
          'PORT': '6381',
          },
      'shard3': {
          'HOST': 'localhost',
          'PORT': '6382',
          },
      }

myfile = open('data.txt','r')
data_dic = {'shard0':[], 'shard1':[], 'shard2':, [], 'shard3':[]}
for line in myfile.readlines():
    line = line.strip()
    shard, player_key, point = line.split('!')
    data_dic[shard].append((player_key, point))

for name in data_dic.keys():
    client = get_client(
            name=name,
            setting=REDIS_DATABASES
            )
    for player_key, point in data_dic[name]:
        client.clinet.hset(player_key, 'event_point', point)
