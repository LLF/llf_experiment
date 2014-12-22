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

data_dic = {}
for name in REDIS_DATABASES.keys():
    client = get_client(
            name=name,
            setting=REDIS_DATABASES
            )
    key_list = client.client.keys("PlayerData:*")
    player_dic = {}
    for key in key_list:
        event_point = client.client.hget(key, 'event_point')
        if event_point and int(event_point) != 0:
            player_dic[key] = event_point
    data_dic[name] = player_dic

data_str = ''
for data_key in data_dic.keys():
    for player_key in data_dic[data_key].keys():
        data_str = data_str + str(data_key) + '!' + str(player_key) + '!' + str(data_dic[data_key][player_key]) + '\n'
myfile = open('data2.txt','w')
myfile.write(data_str)
