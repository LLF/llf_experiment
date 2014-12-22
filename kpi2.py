#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys
from time import strptime

def date_to_dt_begin(date):
    return datetime.datetime(date.year, date.month, date.day, 0, 0, 0)

def date_to_dt_end(date):
    return datetime.datetime(date.year, date.month, date.day, 23, 59, 59) 

def date_time_to_date(dt):
    return dt.date()

def str_to_date(date_str):
    return date_time_to_date(datetime.datetime(*strptime(date_str, '%Y-%m-%d')[:6]))

def delete_sql(date_str, date_begin, date_end):
    return    "delete from zone_devices where create_time between '{}' and '{}';".format(date_begin, date_end) \
            + "delete from zone_device_count where date='{}';".format(date_str) \
            + "delete from platform_devices where create_time between '{}' and '{}';".format(date_begin, date_end) \
            + "delete from devices where create_time between '{}' and '{}';".format(date_begin, date_end) \
            + "delete from device_count where date='{}';".format(date_str) \
            + "delete from platform_device_count where date='{}';".format(date_str) \
            + "delete from zone_user_count where date='{}';".format(date_str) \
            + "delete from user_count where date='{}';".format(date_str) \
            + "delete from zone_platform_user_count where date='{}';".format(date_str) \
            + "delete from platform_user_count where date='{}';".format(date_str) \
            + "delete from zone_user_login where date='{}';".format(date_str) \
            + "delete from zone_platform_user_login where date='{}';".format(date_str) \
            + "delete from platform_user_login where date='{}';".format(date_str) \
            + "delete from user_login where date='{}';".format(date_str) \
            + "delete from zone_lu_asset where date='{}';".format(date_str) \
            + "delete from lu_asset where date='{}';".format(date_str) \
            + "delete from zone_lu_level where date='{}';".format(date_str) \
            + "delete from lu_level where date='{}';".format(date_str) \
            + "delete from zone_user_asset where date='{}';".format(date_str) \
            + "delete from user_asset where date='{}';".format(date_str) \
            + "delete from zone_dau where date='{}';".format(date_str) \
            + "delete from zone_platform_dau where date='{}';".format(date_str) \
            + "delete from platform_dau where date='{}';".format(date_str) \
            + "delete from dau where date='{}';".format(date_str) \
            + "delete from lc1 where date='{}';".format(date_str) \
            + "delete from lc2 where date='{}';".format(date_str) \
            + "delete from lc3 where date='{}';".format(date_str) \
            + "delete from lc4 where date='{}';".format(date_str) \
            + "delete from lc5 where date='{}';".format(date_str) \
            + "delete from lc6 where date='{}';".format(date_str) \
            + "delete from lc7 where date='{}';".format(date_str) \
            + "delete from lc14 where date='{}';".format(date_str) \
            + "delete from lc30 where date='{}';".format(date_str) \
            + "delete from lc60 where date='{}';".format(date_str) \
            + "delete from lc90 where date='{}';".format(date_str) \
            + "delete from lc120 where date='{}';".format(date_str) \
            + "delete from platform_lc1 where date='{}';".format(date_str) \
            + "delete from platform_lc2 where date='{}';".format(date_str) \
            + "delete from platform_lc3 where date='{}';".format(date_str) \
            + "delete from platform_lc4 where date='{}';".format(date_str) \
            + "delete from platform_lc5 where date='{}';".format(date_str) \
            + "delete from platform_lc6 where date='{}';".format(date_str) \
            + "delete from platform_lc7 where date='{}';".format(date_str) \
            + "delete from platform_lc14 where date='{}';".format(date_str) \
            + "delete from platform_lc30 where date='{}';".format(date_str) \
            + "delete from platform_lc60 where date='{}';".format(date_str) \
            + "delete from platform_lc90 where date='{}';".format(date_str) \
            + "delete from platform_lc120 where date='{}';".format(date_str) \
            + "delete from platform_vip_count where date='{}';".format(date_str) \
            + "delete from vip_count where date='{}';".format(date_str) \
            + "delete from zone_vip_count where date='{}';".format(date_str) \
            + "delete from platform_vip_amount where date='{}';".format(date_str) \
            + "delete from vip_amount where date='{}';".format(date_str) \
            + "delete from zone_vip_amount where date='{}';".format(date_str) \
            + "delete from platform_purchase where date='{}';".format(date_str) \
            + "delete from purchase where date='{}';".format(date_str) \
            + "delete from zone_purchase where date='{}';".format(date_str) \
            + "delete from new_platform_vip_count where date='{}';".format(date_str) \
            + "delete from new_vip_count where date='{}';".format(date_str) \
            + "delete from new_platform_vip_amount where date='{}';".format(date_str) \
            + "delete from new_vip_amount where date='{}';".format(date_str) \
            + "delete from new_platform_purchase where date='{}';".format(date_str) \
            + "delete from new_purchase where date='{}';".format(date_str) \

if len(sys.argv) == 2:
    yestoday = str_to_date(sys.argv[1])
else:
    yestoday = datetime.date.today() + datetime.timedelta(days=-1)

yestoday_begin = date_to_dt_begin(yestoday)
yestoday_end = date_to_dt_end(yestoday)

envs = {
        'seq1' : {'common' : 'wcat', 'user_attr': 'wcat_UA00', 'user_stat': 'wcat_US00', 'global': 'wcat_global', 'type':'android'},
        'seq2' : {'common' : 'wcat', 'user_attr': 'wcat_UA00', 'user_stat': 'wcat_US00', 'global': 'wcat_global', 'type':'android'},
}

sql = ['use kpi;']

# 新增设备
tmp_sql = []
for env in envs:
    dbs = envs[env]
    tmp_sql.append( """select userId, deviceId, createdAt, from {}.DeviceIdHistory where createdAt between '{}' and '{}'""".format(dbs['common'], yestoday_begin, yestoday_end) )
    sql.append( "insert ignore into zone_devices select '{}', DEVICE_ID, CREATEDATE from {}.FULL_BRV_USER_INFO where CREATEDATE between '{}' and '{}';".format(env, dbs['common'], yestoday_begin, yestoday_end) )
    sql.append( "insert ignore into zone_device_count select '{}', '{}', count(*) from zone_devices where zone='{}' and create_time between '{}' and '{}';".format(env, yestoday, env, yestoday_begin, yestoday_end) )
