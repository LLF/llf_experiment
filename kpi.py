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
            + "delete from channel_devices where create_time between '{}' and '{}';".format(date_begin, date_end) \
            + "delete from devices where create_time between '{}' and '{}';".format(date_begin, date_end) \
            + "delete from device_count where date='{}';".format(date_str) \
            + "delete from platform_device_count where date='{}';".format(date_str) \
            + "delete from channel_device_count where date='{}';".format(date_str) \
            + "delete from zone_user_count where date='{}';".format(date_str) \
            + "delete from user_count where date='{}';".format(date_str) \
            + "delete from zone_platform_user_count where date='{}';".format(date_str) \
            + "delete from zone_channel_user_count where date='{}';".format(date_str) \
            + "delete from platform_user_count where date='{}';".format(date_str) \
            + "delete from channel_user_count where date='{}';".format(date_str) \
            + "delete from zone_user_login where date='{}';".format(date_str) \
            + "delete from zone_platform_user_login where date='{}';".format(date_str) \
            + "delete from zone_channel_user_login where date='{}';".format(date_str) \
            + "delete from platform_user_login where date='{}';".format(date_str) \
            + "delete from channel_user_login where date='{}';".format(date_str) \
            + "delete from user_login where date='{}';".format(date_str) \
            + "delete from zone_lu_asset where date='{}';".format(date_str) \
            + "delete from lu_asset where date='{}';".format(date_str) \
            + "delete from zone_lu_level where date='{}';".format(date_str) \
            + "delete from lu_level where date='{}';".format(date_str) \
            + "delete from zone_user_asset where date='{}';".format(date_str) \
            + "delete from user_asset where date='{}';".format(date_str) \
            + "delete from zone_dau where date='{}';".format(date_str) \
            + "delete from zone_platform_dau where date='{}';".format(date_str) \
            + "delete from zone_channel_dau where date='{}';".format(date_str) \
            + "delete from platform_dau where date='{}';".format(date_str) \
            + "delete from channel_dau where date='{}';".format(date_str) \
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
            + "delete from channel_lc1 where date='{}';".format(date_str) \
            + "delete from channel_lc2 where date='{}';".format(date_str) \
            + "delete from channel_lc3 where date='{}';".format(date_str) \
            + "delete from channel_lc4 where date='{}';".format(date_str) \
            + "delete from channel_lc5 where date='{}';".format(date_str) \
            + "delete from channel_lc6 where date='{}';".format(date_str) \
            + "delete from channel_lc7 where date='{}';".format(date_str) \
            + "delete from channel_lc14 where date='{}';".format(date_str) \
            + "delete from channel_lc30 where date='{}';".format(date_str) \
            + "delete from channel_lc60 where date='{}';".format(date_str) \
            + "delete from channel_lc90 where date='{}';".format(date_str) \
            + "delete from channel_lc120 where date='{}';".format(date_str) \
            + "delete from platform_vip_count where date='{}';".format(date_str) \
            + "delete from channel_vip_count where date='{}';".format(date_str) \
            + "delete from vip_count where date='{}';".format(date_str) \
            + "delete from zone_vip_count where date='{}';".format(date_str) \
            + "delete from platform_vip_amount where date='{}';".format(date_str) \
            + "delete from channel_vip_amount where date='{}';".format(date_str) \
            + "delete from vip_amount where date='{}';".format(date_str) \
            + "delete from zone_vip_amount where date='{}';".format(date_str) \
            + "delete from platform_purchase where date='{}';".format(date_str) \
            + "delete from channel_purchase where date='{}';".format(date_str) \
            + "delete from purchase where date='{}';".format(date_str) \
            + "delete from zone_purchase where date='{}';".format(date_str) \
            + "delete from new_platform_vip_count where date='{}';".format(date_str) \
            + "delete from new_channel_vip_count where date='{}';".format(date_str) \
            + "delete from new_vip_count where date='{}';".format(date_str) \
            + "delete from new_platform_vip_amount where date='{}';".format(date_str) \
            + "delete from new_channel_vip_amount where date='{}';".format(date_str) \
            + "delete from new_vip_amount where date='{}';".format(date_str) \
            + "delete from new_platform_purchase where date='{}';".format(date_str) \
            + "delete from new_channel_purchase where date='{}';".format(date_str) \
            + "delete from new_purchase where date='{}';".format(date_str) \
            + "delete from payment_level where date='{}';".format(date_str) \
            + "delete from zel_inc where date='{}';".format(date_str) \
            + "delete from zel_dec where date='{}';".format(date_str) \
            + "delete from dia_inc where date='{}';".format(date_str) \
            + "delete from dia_dec where date='{}';".format(date_str) \
            + "delete from karma_inc where date='{}';".format(date_str) \
            + "delete from karma_dec where date='{}';".format(date_str) \
            + "delete from top_vip where date='{}';".format(date_str) \
            + "delete from top_dia where date='{}';".format(date_str) \
            + "delete from top_zel where date='{}';".format(date_str) \
            + "delete from top_karma where date='{}';".format(date_str) \
            + "delete from new_user_level where date='{}';".format(date_str) \
            + "delete from arena_challenge where date='{}';".format(date_str) \
            + "delete from dungeon_key where date='{}';".format(date_str) \
            + "delete from unit_evo where date='{}';".format(date_str) \
            + "delete from unit_mix where date='{}';".format(date_str) \
            + "delete from unit_sell where date='{}';".format(date_str) \
            + "delete from facility_lvup where date='{}';".format(date_str) \
            + "delete from location_lvup where date='{}';".format(date_str) \
            + "delete from bm_refresh where date='{}';".format(date_str) \
            + "delete from bm_buy where date='{}';".format(date_str) \
            + "delete from bm_goods where date='{}';".format(date_str)

if len(sys.argv) == 2:
    yestoday = str_to_date(sys.argv[1])
else:
    yestoday = datetime.date.today() + datetime.timedelta(days=-1)

yestoday_begin = date_to_dt_begin(yestoday)
yestoday_end = date_to_dt_end(yestoday)
envs = {
        #'staging': {'common':'staging_brave_cn_common', 'user':'staging_brave_cn_user_0'},
        #'dev01' : {'common' : 'dev01_brave_cn_common', 'user': 'dev01_brave_cn_user_0', 'type':'mix'}
        'pro_android_gz01' : {'common' : 'pro_android_gz01_brave_cn_common', 'user': 'pro_android_gz01_brave_cn_user_0', 'type':'android'},
        'pro_android_gz02' : {'common' : 'pro_android_gz02_brave_cn_common', 'user': 'pro_android_gz02_brave_cn_user_0', 'type':'android'},
}

sql = ['use kpi;']

sql.append(delete_sql(yestoday, yestoday_begin, yestoday_end))
# 新增设备
tmp_sql = []
for env in envs:
    dbs = envs[env]
    tmp_sql.append( """select OS,CHANNEL,DEVICE_ID, CREATEDATE from {}.FULL_BRV_USER_INFO where CREATEDATE between '{}' and '{}'""".format(dbs['common'], yestoday_begin, yestoday_end) )
    sql.append( "insert ignore into zone_devices select '{}', DEVICE_ID, CREATEDATE from {}.FULL_BRV_USER_INFO where CREATEDATE between '{}' and '{}';".format(env, dbs['common'], yestoday_begin, yestoday_end) )
    sql.append( "insert ignore into zone_device_count select '{}', '{}', count(*) from zone_devices where zone='{}' and create_time between '{}' and '{}';".format(env, yestoday, env, yestoday_begin, yestoday_end) )

sql.append( "insert ignore into channel_devices " + " union all ".join(tmp_sql) + ";" )

sql.append( "insert ignore into devices select device_id,create_time from channel_devices where create_time between '{}' and '{}';".format(yestoday_begin, yestoday_end) )
sql.append( "insert ignore into device_count select '{}', count(*) from devices where create_time between '{}' and '{}';".format(yestoday, yestoday_begin, yestoday_end) )
sql.append( "insert ignore into platform_device_count select '{}', platform, count(*) from channel_devices where create_time between '{}' and '{}' group by platform;".format(yestoday, yestoday_begin, yestoday_end) )
sql.append( "insert ignore into channel_device_count select '{}', channel_id, count(*) from channel_devices where create_time between '{}' and '{}' group by channel_id;".format(yestoday, yestoday_begin, yestoday_end) )

# 新增用户
for env in envs:
    dbs = envs[env]
    sql.append( "insert ignore into zone_user_count (select '{}', '{}', count(*) from {}.FULL_BRV_USER_INFO where CREATEDATE between '{}' and '{}');".format(env, yestoday, dbs['common'], yestoday_begin, yestoday_end) )

sql.append( "insert ignore into user_count select '{}', sum(cnt) from zone_user_count where `date`='{}';".format(yestoday, yestoday) )
for env in envs:
    dbs = envs[env]
    sql.append( "insert ignore into zone_platform_user_count select '{}', OS, '{}', count(*) from {}.FULL_BRV_USER_INFO where CREATEDATE between '{}' and '{}' group by OS;".format(env, yestoday, dbs['common'], yestoday_begin, yestoday_end) )
    sql.append( "insert ignore into zone_channel_user_count select '{}', CHANNEL, '{}', count(*) from {}.FULL_BRV_USER_INFO where CREATEDATE between '{}' and '{}' group by CHANNEL;".format(env, yestoday, dbs['common'], yestoday_begin, yestoday_end) )

sql.append( "insert ignore into platform_user_count select '{}', platform, sum(cnt) from zone_platform_user_count where `date`='{}' group by platform;".format(yestoday, yestoday) )
sql.append( "insert ignore into channel_user_count select '{}', channel_id, sum(cnt) from zone_channel_user_count where `date`='{}' group by channel_id;".format(yestoday, yestoday) )

# 登录用户
sql.append( "truncate table tmp_user_login;" )
tmp_sql = []
for env in envs:
    dbs = envs[env]
    tmp_sql.append("select '{}', b.USER_ID, b.CHANNEL, b.OS, c.LV, c.BRAVE_COIN, c.ZEL, c.KARMA from {}.BRV_USER_ACCESS_HIST_H a JOIN {}.FULL_BRV_USER_INFO b on a.user_id = b.USER_ID JOIN {}.FULL_BRV_USER_TEAM_INFO c ON a.user_id = c.USER_ID where a.CREATEDATE between '{}' and '{}'".format(env, dbs['user'], dbs['common'], dbs['common'], yestoday_begin, yestoday_end))
sql.append( "insert ignore into tmp_user_login " + " union all ".join(tmp_sql) + ";" )

sql.append( "insert ignore into zone_user_login select zone, '{}', count(*) from tmp_user_login group by zone;".format(yestoday) )
sql.append( "insert ignore into zone_platform_user_login select zone, platform, '{}', count(*) from tmp_user_login group by zone, platform;".format(yestoday) )
sql.append( "insert ignore into zone_channel_user_login select zone, channel_id, '{}', count(*) from tmp_user_login group by zone, channel_id;".format(yestoday) )
sql.append( "insert ignore into platform_user_login select '{}', platform, sum(cnt) from zone_platform_user_login where date='{}' group by platform;".format(yestoday, yestoday) )
sql.append( "insert ignore into channel_user_login select '{}', channel_id, sum(cnt) from zone_channel_user_login where date='{}' group by channel_id;".format(yestoday, yestoday) )
sql.append( "insert ignore into user_login select '{}', sum(cnt) from platform_user_login where date='{}';".format(yestoday, yestoday) )

# 活跃用户资产
sql.append( "insert ignore into zone_lu_asset select '{}', zone, sum(dia), sum(zel), sum(karma) from tmp_user_login group by zone;".format(yestoday) )
sql.append( "insert ignore into lu_asset select '{}', sum(dia), sum(zel), sum(karma) from zone_lu_asset where date='{}';".format(yestoday, yestoday) )
# 活跃用户等级分布
sql.append( "insert ignore into zone_lu_level select '{}', zone, lv, count(*) from tmp_user_login group by zone, lv;".format(yestoday) )
sql.append( "insert ignore into lu_level select '{}', lv, sum(count) from zone_lu_level where date='{}' group by lv;".format(yestoday, yestoday) )

# 全部用户资产
for env in envs:
    dbs = envs[env]
    sql.append( "insert ignore into zone_user_asset select '{}', '{}', sum(BRAVE_COIN), sum(ZEL), sum(KARMA) from {}.FULL_BRV_USER_TEAM_INFO;".format(yestoday, env, dbs['common']) )
sql.append( "insert ignore into user_asset select '{}', sum(dia), sum(zel), sum(karma) from zone_user_asset where date='{}';".format(yestoday, yestoday) )

# dau
sql.append( "truncate table tmp_dau;" )
tmp_sql = []
for env in envs:
    dbs = envs[env]
    tmp_sql.append("select '{}', b.DEVICE_ID, b.CHANNEL, b.OS from {}.BRV_USER_ACCESS_HIST_H a JOIN {}.FULL_BRV_USER_INFO b on a.user_id = b.USER_ID where a.CREATEDATE between '{}' and '{}'".format(env, dbs['user'], dbs['common'], yestoday_begin, yestoday_end))
sql.append( "insert ignore into tmp_dau " + " union all ".join(tmp_sql) + ";" )
sql.append( "insert ignore into zone_dau select zone, '{}', count(*) from tmp_dau group by zone;".format(yestoday) )
sql.append( "insert ignore into zone_platform_dau select zone, platform, '{}', count(*) from tmp_dau group by zone, platform;".format(yestoday) )
sql.append( "insert ignore into zone_channel_dau select zone, channel_id, '{}', count(*) from tmp_dau group by zone, channel_id;".format(yestoday) )
sql.append( "insert ignore into platform_dau select '{}', platform, sum(cnt) from zone_platform_dau where date='{}' group by platform;".format(yestoday, yestoday) )
sql.append( "insert ignore into channel_dau select '{}', channel_id, sum(cnt) from zone_channel_dau where date='{}' group by channel_id;".format(yestoday, yestoday) )
sql.append( "insert ignore into dau select '{}', sum(cnt) from platform_dau where date='{}';".format(yestoday, yestoday) )

# 留存
yesterday_1 = yestoday + datetime.timedelta(days=-1)
yesterday_2 = yestoday + datetime.timedelta(days=-2)
yesterday_3 = yestoday + datetime.timedelta(days=-3)
yesterday_4 = yestoday + datetime.timedelta(days=-4)
yesterday_5 = yestoday + datetime.timedelta(days=-5)
yesterday_6 = yestoday + datetime.timedelta(days=-6)
yesterday_7 = yestoday + datetime.timedelta(days=-7)
yesterday_14 = yestoday + datetime.timedelta(days=-14)
yesterday_30 = yestoday + datetime.timedelta(days=-30)
yesterday_60 = yestoday + datetime.timedelta(days=-60)
yesterday_90 = yestoday + datetime.timedelta(days=-90)
yesterday_120 = yestoday + datetime.timedelta(days=-120)
sql.append( "insert ignore into lc1 select '{}', count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}';".format(yestoday, date_to_dt_begin(yesterday_1), date_to_dt_end(yesterday_1)) )
sql.append( "insert ignore into lc2 select '{}', count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}';".format(yestoday, date_to_dt_begin(yesterday_2), date_to_dt_end(yesterday_2)) )
sql.append( "insert ignore into lc3 select '{}', count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}';".format(yestoday, date_to_dt_begin(yesterday_3), date_to_dt_end(yesterday_3)) )
sql.append( "insert ignore into lc4 select '{}', count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}';".format(yestoday, date_to_dt_begin(yesterday_4), date_to_dt_end(yesterday_4)) )
sql.append( "insert ignore into lc5 select '{}', count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}';".format(yestoday, date_to_dt_begin(yesterday_5), date_to_dt_end(yesterday_5)) )
sql.append( "insert ignore into lc6 select '{}', count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}';".format(yestoday, date_to_dt_begin(yesterday_6), date_to_dt_end(yesterday_6)) )
sql.append( "insert ignore into lc7 select '{}', count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}';".format(yestoday, date_to_dt_begin(yesterday_7), date_to_dt_end(yesterday_7)) )
sql.append( "insert ignore into lc14 select '{}', count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}';".format(yestoday, date_to_dt_begin(yesterday_14), date_to_dt_end(yesterday_14)) )
sql.append( "insert ignore into lc30 select '{}', count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}';".format(yestoday, date_to_dt_begin(yesterday_30), date_to_dt_end(yesterday_30)) )
sql.append( "insert ignore into lc60 select '{}', count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}';".format(yestoday, date_to_dt_begin(yesterday_60), date_to_dt_end(yesterday_60)) )
sql.append( "insert ignore into lc90 select '{}', count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}';".format(yestoday, date_to_dt_begin(yesterday_90), date_to_dt_end(yesterday_90)) )
sql.append( "insert ignore into lc120 select '{}', count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}';".format(yestoday, date_to_dt_begin(yesterday_120), date_to_dt_end(yesterday_120)) )

sql.append( "insert ignore into platform_lc1 select '{}', b.platform, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.platform;".format(yestoday, date_to_dt_begin(yesterday_1), date_to_dt_end(yesterday_1)) )
sql.append( "insert ignore into platform_lc2 select '{}', b.platform, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.platform;".format(yestoday, date_to_dt_begin(yesterday_2), date_to_dt_end(yesterday_2)) )
sql.append( "insert ignore into platform_lc3 select '{}', b.platform, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.platform;".format(yestoday, date_to_dt_begin(yesterday_3), date_to_dt_end(yesterday_3)) )
sql.append( "insert ignore into platform_lc4 select '{}', b.platform, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.platform;".format(yestoday, date_to_dt_begin(yesterday_4), date_to_dt_end(yesterday_4)) )
sql.append( "insert ignore into platform_lc5 select '{}', b.platform, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.platform;".format(yestoday, date_to_dt_begin(yesterday_5), date_to_dt_end(yesterday_5)) )
sql.append( "insert ignore into platform_lc6 select '{}', b.platform, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.platform;".format(yestoday, date_to_dt_begin(yesterday_6), date_to_dt_end(yesterday_6)) )
sql.append( "insert ignore into platform_lc7 select '{}', b.platform, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.platform;".format(yestoday, date_to_dt_begin(yesterday_7), date_to_dt_end(yesterday_7)) )
sql.append( "insert ignore into platform_lc14 select '{}', b.platform, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.platform;".format(yestoday, date_to_dt_begin(yesterday_14), date_to_dt_end(yesterday_14)) )
sql.append( "insert ignore into platform_lc30 select '{}', b.platform, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.platform;".format(yestoday, date_to_dt_begin(yesterday_30), date_to_dt_end(yesterday_30)) )
sql.append( "insert ignore into platform_lc60 select '{}', b.platform, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.platform;".format(yestoday, date_to_dt_begin(yesterday_60), date_to_dt_end(yesterday_60)) )
sql.append( "insert ignore into platform_lc90 select '{}', b.platform, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.platform;".format(yestoday, date_to_dt_begin(yesterday_90), date_to_dt_end(yesterday_90)) )
sql.append( "insert ignore into platform_lc120 select '{}', b.platform, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.platform;".format(yestoday, date_to_dt_begin(yesterday_120), date_to_dt_end(yesterday_120)) )

sql.append( "insert ignore into channel_lc1 select '{}', b.channel_id, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.channel_id;".format(yestoday, date_to_dt_begin(yesterday_1), date_to_dt_end(yesterday_1)) )
sql.append( "insert ignore into channel_lc2 select '{}', b.channel_id, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.channel_id;".format(yestoday, date_to_dt_begin(yesterday_2), date_to_dt_end(yesterday_2)) )
sql.append( "insert ignore into channel_lc3 select '{}', b.channel_id, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.channel_id;".format(yestoday, date_to_dt_begin(yesterday_3), date_to_dt_end(yesterday_3)) )
sql.append( "insert ignore into channel_lc4 select '{}', b.channel_id, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.channel_id;".format(yestoday, date_to_dt_begin(yesterday_4), date_to_dt_end(yesterday_4)) )
sql.append( "insert ignore into channel_lc5 select '{}', b.channel_id, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.channel_id;".format(yestoday, date_to_dt_begin(yesterday_5), date_to_dt_end(yesterday_5)) )
sql.append( "insert ignore into channel_lc6 select '{}', b.channel_id, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.channel_id;".format(yestoday, date_to_dt_begin(yesterday_6), date_to_dt_end(yesterday_6)) )
sql.append( "insert ignore into channel_lc7 select '{}', b.channel_id, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.channel_id;".format(yestoday, date_to_dt_begin(yesterday_7), date_to_dt_end(yesterday_7)) )
sql.append( "insert ignore into channel_lc14 select '{}', b.channel_id, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.channel_id;".format(yestoday, date_to_dt_begin(yesterday_14), date_to_dt_end(yesterday_14)) )
sql.append( "insert ignore into channel_lc30 select '{}', b.channel_id, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.channel_id;".format(yestoday, date_to_dt_begin(yesterday_30), date_to_dt_end(yesterday_30)) )
sql.append( "insert ignore into channel_lc60 select '{}', b.channel_id, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.channel_id;".format(yestoday, date_to_dt_begin(yesterday_60), date_to_dt_end(yesterday_60)) )
sql.append( "insert ignore into channel_lc90 select '{}', b.channel_id, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.channel_id;".format(yestoday, date_to_dt_begin(yesterday_90), date_to_dt_end(yesterday_90)) )
sql.append( "insert ignore into channel_lc120 select '{}', b.channel_id, count(*) from devices a join tmp_dau b on a.device_id=b.device_id where create_time between '{}' and '{}' group by b.channel_id;".format(yestoday, date_to_dt_begin(yesterday_120), date_to_dt_end(yesterday_120)) )

# 付费
sql.append( "truncate table tmp_vip;" )
tmp_sql = []
for env in envs:
    dbs = envs[env]
    tmp_sql.append("(select '{}', a.USER_ID, b.CHANNEL, b.OS, a.PURCHASE_STATE, a.AMOUNT, IF(b.CREATEDATE between '{}' and '{}', 1, 0), a.PURCHASE_ID from (select USER_ID,PURCHASE_STATE,AMOUNT,PURCHASE_ID from {}.BRV_USER_PURCHASE_HISTORY where CREATEDATE between '{}' and '{}' union all select USER_ID,PURCHASE_STATE,AMOUNT,PURCHASE_ID from {}.BRV_USER_PURCHASE_CHANNEL_HISTORY where CREATEDATE between '{}' and '{}') a join {}.FULL_BRV_USER_INFO b on a.USER_ID=b.USER_ID)".format(env, yestoday_begin, yestoday_end, dbs['user'], yestoday_begin, yestoday_end, dbs['user'], yestoday_begin, yestoday_end, dbs['common']))
sql.append( "insert into tmp_vip " + " union all ".join(tmp_sql) + ";" )
sql.append( "insert ignore into platform_vip_count select '{}', platform, count(distinct(concat(zone, user_id))) from tmp_vip where state=2 group by platform;".format(yestoday) )
sql.append( "insert ignore into channel_vip_count select '{}', channel_id, count(distinct(concat(zone, user_id))) from tmp_vip where state=2 group by channel_id;".format(yestoday) )
sql.append( "insert ignore into vip_count select '{}', count(distinct(concat(zone, user_id))) from tmp_vip where state=2;".format(yestoday) )
sql.append( "insert ignore into zone_vip_count select zone, '{}', count(distinct(user_id)) from tmp_vip where state=2 group by zone;" )
sql.append( "insert ignore into platform_vip_amount select '{}', platform, sum(amount) from tmp_vip where state=2 group by platform;".format(yestoday) )
sql.append( "insert ignore into channel_vip_amount select '{}', channel_id, sum(amount) from tmp_vip where state=2 group by channel_id;".format(yestoday) )
sql.append( "insert ignore into vip_amount select '{}', sum(cnt) from channel_vip_amount where `date`='{}';".format(yestoday, yestoday) )
sql.append( "insert ignore into zone_vip_amount select zone, '{}', sum(amount) from tmp_vip where state=2 group by zone;".format(yestoday) )

sql.append( "insert ignore into platform_purchase select '{}', platform, sum(state=2), sum(state!=2) from tmp_vip group by platform;".format(yestoday) )
sql.append( "insert ignore into channel_purchase select '{}', channel_id, sum(state=2), sum(state!=2) from tmp_vip group by channel_id;".format(yestoday) )
sql.append( "insert ignore into purchase select '{}', sum(suc), sum(fail) from channel_purchase where `date`='{}';".format(yestoday, yestoday) )
sql.append( "insert ignore into zone_purchase select zone, '{}', sum(state=2), sum(state!=2) from tmp_vip group by zone;".format(yestoday) )

# 新角色付费
sql.append( "insert ignore into new_platform_vip_count select '{}', platform, count(distinct(concat(zone, user_id))) from tmp_vip where state=2 and new group by platform;".format(yestoday) )
sql.append( "insert ignore into new_channel_vip_count select '{}', channel_id, count(distinct(concat(zone, user_id))) from tmp_vip where state=2 and new group by channel_id;".format(yestoday) )
sql.append( "insert ignore into new_vip_count select '{}', count(distinct(concat(zone, user_id))) from tmp_vip where state=2 and new;".format(yestoday) )
sql.append( "insert ignore into new_platform_vip_amount select '{}', platform, sum(amount) from tmp_vip where state=2 and new group by platform;".format(yestoday) )
sql.append( "insert ignore into new_channel_vip_amount select '{}', channel_id, sum(amount) from tmp_vip where state=2 and new group by channel_id;".format(yestoday) )
sql.append( "insert ignore into new_vip_amount select '{}', sum(cnt) from new_channel_vip_amount where `date`='{}';".format(yestoday, yestoday) )

sql.append( "insert ignore into new_platform_purchase select '{}', platform, sum(state=2), sum(state!=2) from tmp_vip where new group by platform;".format(yestoday) )
sql.append( "insert ignore into new_channel_purchase select '{}', channel_id, sum(state=2), sum(state!=2) from tmp_vip where new group by channel_id;".format(yestoday) )
sql.append( "insert ignore into new_purchase select '{}', sum(suc), sum(fail) from new_channel_purchase;".format(yestoday) )



# 二期开始！！

# 充值档次
sql.append("insert ignore into payment_level select '{}', platform, zone, purchase_id, count(distinct user_id), count(*), sum(amount) from tmp_vip where state=2 group by purchase_id, zone;".format(yestoday))

for env in envs:
    dbs = envs[env]
    # 金币产出+消耗
    sql.append("insert ignore into zel_inc select '{}', b.OS, '{}', a.ACTION_TYPE, count(distinct a.USER_ID), count(*), sum(a.ZEL) from {}.BRV_USER_ZEL_HISTORY a join {}.FULL_BRV_USER_INFO b on a.USER_ID=b.USER_ID where a.CREATEDATE between '{}' and '{}' and a.DO_TYPE=1 group by a.ACTION_TYPE;".format(yestoday, env, dbs['common'], dbs['common'], yestoday_begin, yestoday_end))
    sql.append("insert ignore into zel_dec select '{}', b.OS, '{}', a.ACTION_TYPE, count(distinct a.USER_ID), count(*), sum(a.ZEL) from {}.BRV_USER_ZEL_HISTORY a join {}.FULL_BRV_USER_INFO b on a.USER_ID=b.USER_ID where a.CREATEDATE between '{}' and '{}' and a.DO_TYPE=2 group by a.ACTION_TYPE;".format(yestoday, env, dbs['common'], dbs['common'], yestoday_begin, yestoday_end))

    # 钻石产出+消耗
    sql.append("insert ignore into dia_inc select '{}', b.OS, '{}', a.ACTION_TYPE, count(distinct a.USER_ID), count(*), sum(a.BRAVE_COIN) from {}.BRV_USER_COIN_HISTORY a join {}.FULL_BRV_USER_INFO b on a.USER_ID=b.USER_ID where a.CREATEDATE between '{}' and '{}' and a.DO_TYPE=1 group by a.ACTION_TYPE;".format(yestoday, env, dbs['common'], dbs['common'], yestoday_begin, yestoday_end))
    sql.append("insert ignore into dia_dec select '{}', b.OS, '{}', a.ACTION_TYPE, count(distinct a.USER_ID), count(*), sum(a.BRAVE_COIN) from {}.BRV_USER_COIN_HISTORY a join {}.FULL_BRV_USER_INFO b on a.USER_ID=b.USER_ID where a.CREATEDATE between '{}' and '{}' and a.DO_TYPE=2 and a.ACTION_TYPE not in (5102) group by a.ACTION_TYPE;".format(yestoday, env, dbs['common'], dbs['common'], yestoday_begin, yestoday_end))
    sql.append("insert ignore into dia_dec select '{}', b.OS, '{}', a.USE_TYPE, count(distinct a.USER_ID), count(*), sum(a.BRAVE_COIN) from {}.BRV_USER_SHOP_USE_HISTORY  a join {}.FULL_BRV_USER_INFO b on a.USER_ID=b.USER_ID where a.CREATEDATE between '{}' and '{}' and a.USE_TYPE not in (6) group by a.USE_TYPE;".format(yestoday, env, dbs['common'], dbs['common'], yestoday_begin, yestoday_end))

    # 魂产出+消耗
    sql.append("insert ignore into karma_inc select '{}', b.OS, '{}', a.ACTION_TYPE, count(distinct a.USER_ID), count(*), sum(a.KARMA) from {}.BRV_USER_KARMA_HISTORY a join {}.FULL_BRV_USER_INFO b on a.USER_ID=b.USER_ID where a.CREATEDATE between '{}' and '{}' and a.DO_TYPE=1 group by a.ACTION_TYPE;".format(yestoday, env, dbs['common'], dbs['common'], yestoday_begin, yestoday_end))
    sql.append("insert ignore into karma_dec select '{}', b.OS, '{}', a.ACTION_TYPE, count(distinct a.USER_ID), count(*), sum(a.KARMA) from {}.BRV_USER_KARMA_HISTORY a join {}.FULL_BRV_USER_INFO b on a.USER_ID=b.USER_ID where a.CREATEDATE between '{}' and '{}' and a.DO_TYPE=2 group by a.ACTION_TYPE;".format(yestoday, env, dbs['common'], dbs['common'], yestoday_begin, yestoday_end))


# 充值排行榜
sql.append("insert ignore into top_vip select '{}', platform, zone, user_id, channel_id, sum(amount), count(*) from tmp_vip where state=2 group by zone,user_id;".format(yestoday))

sql.append( "truncate table tmp_dia;" )
sql.append( "truncate table tmp_zel;" )
sql.append( "truncate table tmp_karma;" )
LIMIT = 100
for env in envs:
    dbs = envs[env]
    # 钻石产出消耗排行榜
    sql.append( "insert ignore into tmp_dia select b.OS, '{}', a.USER_ID, b.CHANNEL, sum(a.BRAVE_COIN), count(*), a.DO_TYPE from {}.BRV_USER_COIN_HISTORY a join {}.FULL_BRV_USER_INFO b on a.USER_ID=b.USER_ID where a.CREATEDATE between '{}' and '{}' group by a.USER_ID, a.DO_TYPE;".format(env, dbs['common'], dbs['common'], yestoday_begin, yestoday_end) )
    sql.append( "insert ignore into top_dia select '{}', tmp_dia.* from tmp_dia where do_type=1 order by amount desc limit {};".format(yestoday, LIMIT) )
    sql.append( "insert ignore into top_dia select '{}', tmp_dia.* from tmp_dia where do_type=2 order by amount desc limit {};".format(yestoday, LIMIT) )

    # 金币产出消耗排行榜
    sql.append( "insert ignore into tmp_zel select b.OS, '{}', a.USER_ID, b.CHANNEL, sum(a.ZEL), count(*), a.DO_TYPE from {}.BRV_USER_ZEL_HISTORY a join {}.FULL_BRV_USER_INFO b on a.USER_ID=b.USER_ID where a.CREATEDATE between '{}' and '{}' group by a.USER_ID, a.DO_TYPE;".format(env, dbs['common'], dbs['common'], yestoday_begin, yestoday_end) )
    sql.append( "insert ignore into top_zel select '{}', tmp_zel.* from tmp_zel where do_type=1 order by amount desc limit {};".format(yestoday, LIMIT) )
    sql.append( "insert ignore into top_zel select '{}', tmp_zel.* from tmp_zel where do_type=2 order by amount desc limit {};".format(yestoday, LIMIT) )

    # 魂产出消耗排行榜
    sql.append( "insert ignore into tmp_karma select b.OS, '{}', a.USER_ID, b.CHANNEL, sum(a.KARMA), count(*), a.DO_TYPE from {}.BRV_USER_KARMA_HISTORY a join {}.FULL_BRV_USER_INFO b on a.USER_ID=b.USER_ID where a.CREATEDATE between '{}' and '{}' group by a.USER_ID, a.DO_TYPE;".format(env, dbs['common'], dbs['common'], yestoday_begin, yestoday_end) )
    sql.append( "insert ignore into top_karma select '{}', tmp_karma.* from tmp_karma where do_type=1 order by amount desc limit {};".format(yestoday, LIMIT) )
    sql.append( "insert ignore into top_karma select '{}', tmp_karma.* from tmp_karma where do_type=2 order by amount desc limit {};".format(yestoday, LIMIT) )

# 充值流失预警
sql.append( "delete from tmp_vip7 where date <= '{}';".format(yesterday_7) )
sql.append( "insert ignore into tmp_vip7 select '{}', zone, user_id, channel_id, platform, sum(amount) from tmp_vip where state=2 group by zone, user_id;".format(yestoday) )
sql.append( "truncate table vip7;" )
sql.append( "insert into vip7 select zone, user_id, channel_id, platform, sum(amount), sum(IF(date > '{}', amount, 0)) from tmp_vip7 group by zone, user_id;".format(yesterday_3) )


# 行为数据 !!
for env in envs:
    dbs = envs[env]
    # 当日创角等级分布 
    sql.append("insert ignore into new_user_level select '{}', '{}', LV, count(*) from {}.BRV_USER_TEAM_INFO where CREATEDATE between '{}' and '{}' group by LV;".format(yestoday, env, dbs['common'], yestoday_begin, yestoday_end))

    # 竞技场挑战
    sql.append("insert ignore into arena_challenge select '{}', '{}', BATTLE_RESULT, count(distinct USER_ID), count(*), sum(GET_RANK_POINT), sum(KARMA) from {}.BRV_USER_ARENA_BATTLE_HISTORY where CREATEDATE between '{}' and '{}' group by BATTLE_RESULT;".format(yestoday, env, dbs['user'], yestoday_begin, yestoday_end))

    # 钥匙
    sql.append("insert ignore into dungeon_key select '{}', '{}', DO_TYPE, DUNGEON_KEY_ID, count(distinct USER_ID), count(*), sum(AFTER_CNT-BEFORE_CNT) from {}.BRV_USER_DUNGEON_KEY_HISTORY where CREATEDATE between '{}' and '{}' group by DO_TYPE, DUNGEON_KEY_ID;".format(yestoday, env, dbs['common'], yestoday_begin, yestoday_end))

    # 进化
    sql.append("insert ignore into unit_evo select '{}', '{}', count(distinct USER_ID), count(*) from {}.BRV_USER_UNIT_EVO_HISTORY where CREATEDATE between '{}' and '{}';".format(yestoday, env, dbs['common'], yestoday_begin, yestoday_end))

    # 强化
    sql.append("insert ignore into unit_mix select '{}', '{}', count(distinct USER_ID), count(*) from {}.BRV_USER_UNIT_MIX_HISTORY where CREATEDATE between '{}' and '{}';".format(yestoday, env, dbs['common'], yestoday_begin, yestoday_end))

    # 出售
    sql.append("insert ignore into unit_sell select '{}', '{}', count(distinct USER_ID), count(*) from {}.BRV_USER_UNIT_SELL_HISTORY where CREATEDATE between '{}' and '{}';".format(yestoday, env, dbs['common'], yestoday_begin, yestoday_end))

    # 建筑升级
    sql.append("insert ignore into facility_lvup select '{}', '{}', facility_id, count(distinct USER_ID), count(*) from {}.BRV_FACILITY_LVUP_LOG where update_time between '{}' and '{}' group by facility_id;".format(yestoday, env, dbs['common'], yestoday_begin, yestoday_end))

    # 资源升级
    sql.append("insert ignore into location_lvup select '{}', '{}', location_id, count(distinct USER_ID), count(*) from {}.BRV_LOCATION_LVUP_LOG where update_time between '{}' and '{}' group by location_id;".format(yestoday, env, dbs['common'], yestoday_begin, yestoday_end))

    # 黑市刷新
    sql.append("insert ignore into bm_refresh select '{}', '{}', money_type, sum(money_num), count(distinct user_id), count(*) from {}.BRV_BLACK_MARKET_REFRESH_LOG where update_time between '{}' and '{}' group by money_type;".format(yestoday, env, dbs['common'], yestoday_begin, yestoday_end))

    # 黑市购买
    sql.append("insert ignore into bm_buy select '{}', '{}', money_type, sum(money_num), count(distinct user_id), count(*) from {}.BRV_BLACK_MARKET_BUY_LOG where update_time between '{}' and '{}' group by money_type;".format(yestoday, env, dbs['common'], yestoday_begin, yestoday_end))

    # 黑市物品购买
    sql.append("insert ignore into bm_goods select '{}', '{}', item_type, item_id, count(distinct user_id), count(*), sum(money_num) from {}.BRV_BLACK_MARKET_BUY_LOG where update_time between '{}' and '{}' group by item_type, item_id;".format(yestoday, env, dbs['common'], yestoday_begin, yestoday_end))

print '\n'.join(sql)
