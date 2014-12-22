create database if not exists kpi;
use kpi;
drop table if exists devices;
create table devices (
    device_id varchar(255) primary key,
    create_time datetime,
    index create_time_idx (create_time)
);

drop table if exists channel_devices;
create table channel_devices (
    platform tinyint(10),
    channel_id varchar(20),
    device_id varchar(255),
    create_time datetime,
    primary key(platform, channel_id, device_id),
    index create_time_idx (create_time)
);

/* 区服设备 */
drop table if exists zone_devices;
create table zone_devices (
    zone varchar(32),
    device_id varchar(255),
    create_time datetime,
    primary key(zone, device_id),
    index create_time_idx (create_time),
    index zone_create_time_idx (zone, create_time)
);

drop table if exists zone_device_count;
create table zone_device_count (
    zone varchar(32),
    `date` varchar(32),
    `cnt` int,
    primary key(zone, date)
);

/* 区服登陆用户 */
drop table if exists zone_user_login;
create table zone_user_login (
    zone varchar(32),
    `date` varchar(32),
    `cnt` int,
    primary key(zone, date)
);

/* 区服dau */
drop table if exists zone_dau;
create table zone_dau (
    zone varchar(32),
    `date` varchar(32),
    `cnt` int,
    primary key(zone, date)
);

/* 区服付费 */
drop table if exists zone_vip_count;
create table zone_vip_count (
    zone varchar(32),
    `date` varchar(32),
    `cnt` int,
    primary key(zone, date)
);

drop table if exists zone_vip_amount;
create table zone_vip_amount (
    zone varchar(32),
    `date` varchar(32),
    `cnt` int,
    primary key(zone, date)
);

drop table if exists zone_purchase;
create table zone_purchase (
    zone varchar(32),
    `date` varchar(32),
    `suc` int(11) DEFAULT NULL,
    `fail` int(11) DEFAULT NULL,
    primary key(zone, date)
);



/* 每日新增设备数 */
drop table if exists device_count;
create table device_count (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 每日平台新增设备数 */
drop table if exists platform_device_count;
create table platform_device_count (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 每日渠道新增设备数 */
drop table if exists channel_device_count;
create table channel_device_count (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
/* 每日新增用户数 */
drop table if exists user_count;
create table user_count (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 每日平台新增用户数 */
drop table if exists platform_user_count;
create table platform_user_count (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 每日渠道新增用户数 */
drop table if exists channel_user_count;
create table channel_user_count (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
drop table if exists zone_user_count;
create table zone_user_count (
    zone varchar(32),
    `date` varchar(32),
    `cnt` int,
    primary key(`date`, zone)
);
drop table if exists zone_platform_user_count;
create table zone_platform_user_count (
    zone varchar(32),
    platform tinyint(10),
    `date` varchar(32),
    `cnt` int,
    primary key(`date`, zone, platform)
);
drop table if exists zone_channel_user_count;
create table zone_channel_user_count (
    zone varchar(32),
    `channel_id` varchar(20),
    `date` varchar(32),
    `cnt` int,
    primary key(`date`, zone, channel_id)
);

/* 每日登录用户数 */
drop table if exists user_login;
create table user_login (
    `date` varchar(32),
    `cnt` int,
    primary key(`date`)
);
/* 每日平台登录用户数 */
drop table if exists platform_user_login;
create table platform_user_login (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 每日渠道登录用户数 */
drop table if exists channel_user_login;
create table channel_user_login (
    `date` varchar(32),
    channel_id varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
drop table if exists zone_channel_user_login;
create table zone_channel_user_login (
    zone varchar(32),
    channel_id varchar(20),
    `date` varchar(32),
    `cnt` int,
    primary key(`date`, zone, channel_id)
);
drop table if exists zone_platform_user_login;
create table zone_platform_user_login (
    zone varchar(32),
    platform tinyint(10),
    `date` varchar(32),
    `cnt` int,
    primary key(`date`, zone, platform)
);
drop table if exists tmp_user_login;
create table tmp_user_login (
    zone varchar(32),
    user_id varchar(32),
    channel_id varchar(20),
    platform tinyint(10),
    lv int(10),
    dia int(10),
    zel int(10),
    karma int(10),
    primary key(zone, user_id)
);

/* 所有用户资产 */
drop table if exists user_asset;
create table user_asset (
    `date` varchar(32),
    dia bigint(20),
    zel bigint(20),
    karma bigint(20),
    primary key(`date`)
);
drop table if exists zone_user_asset;
create table zone_user_asset (
    `date` varchar(32),
    zone varchar(32),
    dia bigint(20),
    zel bigint(20),
    karma bigint(20),
    primary key(`date`, zone)
);

/* 活跃用户资产 */
drop table if exists lu_asset;
create table lu_asset (
    `date` varchar(32),
    dia bigint(20),
    zel bigint(20),
    karma bigint(20),
    primary key(`date`)
);
drop table if exists zone_lu_asset;
create table zone_lu_asset (
    `date` varchar(32),
    zone varchar(32),
    dia bigint(20),
    zel bigint(20),
    karma bigint(20),
    primary key(`date`, zone)
);
/* 活跃用户等级分布 */
drop table if exists zone_lu_level;
create table zone_lu_level (
    `date` varchar(32),
    zone varchar(32),
    lv int(11),
    count int(11),
    primary key(`date`, zone, lv)
);
drop table if exists lu_level;
create table lu_level (
    `date` varchar(32),
    lv int(11),
    count int(11),
    primary key(`date`, lv)
);



/* 每日登录设备数 */
drop table if exists dau;
create table dau (
    `date` varchar(32),
    `cnt` int,
    primary key(`date`)
);
/* 每日平台登录设备数 */
drop table if exists platform_dau;
create table platform_dau (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 每日渠道登录设备数 */
drop table if exists channel_dau;
create table channel_dau (
    `date` varchar(32),
    channel_id varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
drop table if exists zone_channel_dau;
create table zone_channel_dau (
    zone varchar(32),
    channel_id varchar(20),
    `date` varchar(32),
    `cnt` int,
    primary key(`date`, zone, channel_id)
);
drop table if exists zone_platform_dau;
create table zone_platform_dau (
    zone varchar(32),
    platform tinyint(10),
    `date` varchar(32),
    `cnt` int,
    primary key(`date`, zone, platform)
);
drop table if exists tmp_dau;
create table tmp_dau (
    zone varchar(32),
    device_id varchar(255),
    channel_id varchar(20),
    platform tinyint(10),
    primary key(zone, device_id)
);

/* 次日留存 */
drop table if exists lc1;
create table lc1 (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 平台次日留存 */
drop table if exists platform_lc1;
create table platform_lc1 (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 渠道次日留存 */
drop table if exists channel_lc1;
create table channel_lc1 (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
/* 2日留存 */
drop table if exists lc2;
create table lc2 (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 平台2日留存 */
drop table if exists platform_lc2;
create table platform_lc2 (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 渠道2日留存 */
drop table if exists channel_lc2;
create table channel_lc2 (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);

/* 3日留存 */
drop table if exists lc3;
create table lc3 (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 平台3日留存 */
drop table if exists platform_lc3;
create table platform_lc3 (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 渠道次日留存 */
drop table if exists channel_lc3;
create table channel_lc3 (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
/* 4日留存 */
drop table if exists lc4;
create table lc4 (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 平台4日留存 */
drop table if exists platform_lc4;
create table platform_lc4 (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 渠道4日留存 */
drop table if exists channel_lc4;
create table channel_lc4 (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
/* 5日留存 */
drop table if exists lc5;
create table lc5 (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 平台5日留存 */
drop table if exists platform_lc5;
create table platform_lc5 (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 渠道5日留存 */
drop table if exists channel_lc5;
create table channel_lc5 (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
/* 6日留存 */
drop table if exists lc6;
create table lc6 (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 平台6日留存 */
drop table if exists platform_lc6;
create table platform_lc6 (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 渠道6日留存 */
drop table if exists channel_lc6;
create table channel_lc6 (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);


/* 7日留存 */
drop table if exists lc7;
create table lc7 (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 平台7日留存 */
drop table if exists platform_lc7;
create table platform_lc7 (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 渠道7日留存 */
drop table if exists channel_lc7;
create table channel_lc7 (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
/* 14日留存 */
drop table if exists lc14;
create table lc14 (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 平台14日留存 */
drop table if exists platform_lc14;
create table platform_lc14 (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 渠道14日留存 */
drop table if exists channel_lc14;
create table channel_lc14 (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
/* 30日留存 */
drop table if exists lc30;
create table lc30 (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 平台30日留存 */
drop table if exists platform_lc30;
create table platform_lc30 (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 渠道30日留存 */
drop table if exists channel_lc30;
create table channel_lc30 (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
/* 60日留存 */
drop table if exists lc60;
create table lc60 (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 平台60日留存 */
drop table if exists platform_lc60;
create table platform_lc60 (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 渠道60日留存 */
drop table if exists channel_lc60;
create table channel_lc60 (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
/* 90日留存 */
drop table if exists lc90;
create table lc90 (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 平台90日留存 */
drop table if exists platform_lc90;
create table platform_lc90 (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 渠道90日留存 */
drop table if exists channel_lc90;
create table channel_lc90 (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
/* 120日留存 */
drop table if exists lc120;
create table lc120 (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 平台120日留存 */
drop table if exists platform_lc120;
create table platform_lc120 (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 渠道120日留存 */
drop table if exists channel_lc120;
create table channel_lc120 (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);

/* 每日付费角色数 */
drop table if exists vip_count;
create table vip_count (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 每日平台付费角色数 */
drop table if exists platform_vip_count;
create table platform_vip_count (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 每日渠道付费角色数 */
drop table if exists channel_vip_count;
create table channel_vip_count (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
/* 每日付费金额 */
drop table if exists vip_amount;
create table vip_amount (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 每日平台付费金额 */
drop table if exists platform_vip_amount;
create table platform_vip_amount (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 每日渠道付费金额 */
drop table if exists channel_vip_amount;
create table channel_vip_amount (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
/* 每日订单成功失败数 */
drop table if exists purchase;
create table purchase (
    `date` varchar(32) primary key,
    `suc` int,
    `fail` int
);
/* 每日平台订单成功失败数 */
drop table if exists platform_purchase;
create table platform_purchase (
    `date` varchar(32),
    platform tinyint(10),
    `suc` int,
    `fail` int,
    primary key(`date`, `platform`)
);
/* 每日渠道订单成功失败数 */
drop table if exists channel_purchase;
create table channel_purchase (
    `date` varchar(32),
    `channel_id` varchar(20),
    `suc` int,
    `fail` int,
    primary key(`date`, `channel_id`)
);

drop table if exists tmp_vip;
create table tmp_vip (
    zone varchar(32),
    user_id varchar(32),
    channel_id varchar(20),
    platform tinyint(10),
    state tinyint(4),
    amount int(11),
    new tinyint(1),
    purchase_id int(11),
    `device_id` varchar(255) NOT NULL,
    new_device tinyint(1),
    old_device_1st tinyint(1)
);

drop table if exists device_first_payment;
create table device_first_payment (
    `device_id` varchar(255) NOT NULL,
    `date` varchar(32),
    PRIMARY KEY (`device_id`)
);

drop table if exists device_payment;
create table device_payment (
    `date` varchar(32),
    kind tinyint(2),
    count int(11),
    sum int(11),
    PRIMARY KEY (`date`, kind)
);

drop table if exists zone_device_payment;
create table zone_device_payment (
    zone varchar(32),
    `date` varchar(32),
    kind tinyint(2),
    count int(11),
    sum int(11),
    PRIMARY KEY (zone, `date`, kind)
);

drop table if exists zone_vip10;
create table zone_vip10 (
    zone varchar(32),
    `date` varchar(32),
    count int(11),
    PRIMARY KEY (`date`, zone)
);
drop table if exists vip10;
create table vip10 (
    `date` varchar(32),
    count int(11),
    PRIMARY KEY (`date`)
);

drop table if exists zone_l5gacha;
create table zone_l5gacha (
    `date` varchar(32),
    zone varchar(32),
    gacha_type tinyint(2),
    dia bigint(20),
    times bigint(20),
    user_count bigint(20),
    PRIMARY KEY (`date`, zone)
);


drop table if exists l5gacha;
create table l5gacha (
    `date` varchar(32),
    gacha_type tinyint(2),
    dia bigint(20),
    times bigint(20),
    user_count bigint(20),
    PRIMARY KEY (`date`)
);

drop table if exists tmp_charge_user;
drop table if exists tmp_gacha_user;
drop table if exists tmp_charge_and_gacha_user;
create table tmp_charge_user (
    user_id varchar(32) primary key
);
create table tmp_gacha_user (
    user_id varchar(32) primary key
);
create table tmp_charge_and_gacha_user (
    user_id varchar(32) primary key
);


/* 每日新角色付费角色数 */
drop table if exists new_vip_count;
create table new_vip_count (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 每日平台新角色付费角色数 */
drop table if exists new_platform_vip_count;
create table new_platform_vip_count (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 每日渠道新角色付费角色数 */
drop table if exists new_channel_vip_count;
create table new_channel_vip_count (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
/* 每日新角色付费金额 */
drop table if exists new_vip_amount;
create table new_vip_amount (
    `date` varchar(32) primary key,
    `cnt` int
);
/* 每日平台新角色付费金额 */
drop table if exists new_platform_vip_amount;
create table new_platform_vip_amount (
    `date` varchar(32),
    platform tinyint(10),
    `cnt` int,
    primary key(`date`, platform)
);
/* 每日渠道新角色付费金额 */
drop table if exists new_channel_vip_amount;
create table new_channel_vip_amount (
    `date` varchar(32),
    `channel_id` varchar(20),
    `cnt` int,
    primary key(`date`, channel_id)
);
/* 每日新角色订单成功失败数 */
drop table if exists new_purchase;
create table new_purchase (
    `date` varchar(32) primary key,
    `suc` int,
    `fail` int
);
/* 每日平台新角色订单成功失败数 */
drop table if exists new_platform_purchase;
create table new_platform_purchase (
    `date` varchar(32),
    platform tinyint(10),
    `suc` int,
    `fail` int,
    primary key(`date`, `platform`)
);
/* 每日渠道新角色订单成功失败数 */
drop table if exists new_channel_purchase;
create table new_channel_purchase (
    `date` varchar(32),
    `channel_id` varchar(20),
    `suc` int,
    `fail` int,
    primary key(`date`, `channel_id`)
);

