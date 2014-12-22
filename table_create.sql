create database if not exists kpi;
use kpi;

drop table if exists user_info;
create table user_info(
    platformId tinyint(4) unsigned NOT NULL,
    gamezoneSeq int(10) NOT NULL,
    deviceId varchar(255) NOT NULL,
    userId int(11) NOT NULL,
    idfa varchar(255),
    idfv varchar(255),
    mac varchar(255),
    createdAt datetime,
    primary key(platformId, deviceId, userId),
    index createdAtIdx (createdAt)
);

drop table if exists devices;
create table devices (
    deviceId varchar(255) primary key,
    createdAt datetime,
    index createdAtIdx (createdAt)
);

drop table if exists platform_devices;
create table platform_devices (
    platformId tinyint(10),
    deviceId varchar(255),
    createdAt datetime,
    primary key(platformId, channel_id, deviceId),
    index createdAtIdx(createdAt)
);

/* 区服设备 */
drop table if exists zone_devices;
create table zone_devices (
    gamezoneSeq varchar(32),
    deviceId varchar(255),
    createdAt datetime,
    primary key(gamezoneSeq, deviceId),
    index createdAtIdx (createdAt),
    index gamezoneSeq_createdAtIdx (zone, createdAt)
);

drop table if exists zone_device_count;
create table zone_device_count (
    gamezoneSeq varchar(32),
    `date` varchar(32),
    `cnt` int,
    primary key(gamezoneSeq, date)
);

/* 区服登陆用户 */
drop table if exists zone_user_login;
create table zone_user_login (
    gamezoneSeq varchar(32),
    `date` varchar(32),
    `cnt` int,
    primary key(gamezoneSeq, date)
);

/* 区服dau */
drop table if exists zone_dau;
create table zone_dau (
    gamezoneSeq varchar(32),
    `date` varchar(32),
    `cnt` int,
    primary key(gamezoneSeq, date)
);

/* 区服付费 */
drop table if exists zone_vip_count;
create table zone_vip_count (
    gamezoneSeq varchar(32),
    `date` varchar(32),
    `cnt` int,
    primary key(gamezoneSeq, date)
);

drop table if exists zone_vip_amount;
create table zone_vip_amount (
    gamezoneSeq varchar(32),
    `date` varchar(32),
    `cnt` int,
    primary key(gamezoneSeq, date)
);

drop table if exists zone_purchase;
create table zone_purchase (
    gamezoneSeq varchar(32),
    `date` varchar(32),
    `suc` int(11) DEFAULT NULL,
    `fail` int(11) DEFAULT NULL,
    primary key(gamezoneSeq, date)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
);
drop table if exists zone_user_count;
create table zone_user_count (
    gamezoneSeq varchar(32),
    `date` varchar(32),
    `cnt` int,
    primary key(`date`, gamezoneSeq)
);
drop table if exists zone_platform_user_count;
create table zone_platform_user_count (
    gamezoneSeq varchar(32),
    platformId tinyint(10),
    `date` varchar(32),
    `cnt` int,
    primary key(`date`, gamezoneSeq, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
);
drop table if exists zone_platform_user_login;
create table zone_platform_user_login (
    gamezoneSeq varchar(32),
    platform tinyint(10),
    `date` varchar(32),
    `cnt` int,
    primary key(`date`, gamezoneSeq, platform)
);
drop table if exists tmp_user_login;
create table tmp_user_login (
    gamezoneSeq varchar(32),
    user_id varchar(32),
    channel_id varchar(20),
    platform tinyint(10),
    lv int(10),
    dia int(10),
    zel int(10),
    karma int(10),
    primary key(gamezoneSeq, user_id)
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
    gamezoneSeq varchar(32),
    dia bigint(20),
    zel bigint(20),
    karma bigint(20),
    primary key(`date`, gamezoneSeq)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
);
drop table if exists zone_channel_dau;
create table zone_channel_dau (
    gamezoneSeq varchar(32),
    channel_id varchar(20),
    `date` varchar(32),
    `cnt` int,
    primary key(`date`, gamezoneSeq, channel_id)
);
drop table if exists zone_platform_dau;
create table zone_platform_dau (
    gamezoneSeq varchar(32),
    platformId tinyint(10),
    `date` varchar(32),
    `cnt` int,
    primary key(`date`, gamezoneSeq, platformId)
);
drop table if exists tmp_dau;
create table tmp_dau (
    gamezoneSeq varchar(32),
    deviceId varchar(255),
    channel_id varchar(20),
    platformId tinyint(10),
    primary key(gamezoneSeq, deviceId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `suc` int,
    `fail` int,
    primary key(`date`, `platformId`)
);
drop table if exists tmp_vip;
create table tmp_vip (
    gamezoneSeq varchar(32),
    user_id varchar(32),
    channel_id varchar(20),
    platformId tinyint(10),
    state tinyint(4),
    amount int(11),
    new tinyint(1),
    purchase_id int(11),
    `deviceId` varchar(255) NOT NULL,
    new_device tinyint(1),
    old_device_1st tinyint(1)
);

drop table if exists device_first_payment;
create table device_first_payment (
    `deviceId` varchar(255) NOT NULL,
    `date` varchar(32),
    PRIMARY KEY (`deviceId`)
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
    gamezoneSeq varchar(32),
    `date` varchar(32),
    kind tinyint(2),
    count int(11),
    sum int(11),
    PRIMARY KEY (gamezoneSeq, `date`, kind)
);

drop table if exists zone_vip10;
create table zone_vip10 (
    gamezoneSeq varchar(32),
    `date` varchar(32),
    count int(11),
    PRIMARY KEY (`date`, gamezoneSeq)
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
    gamezoneSeq varchar(32),
    gacha_type tinyint(2),
    dia bigint(20),
    times bigint(20),
    user_count bigint(20),
    PRIMARY KEY (`date`, gamezoneSeq)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `cnt` int,
    primary key(`date`, platformId)
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
    platformId tinyint(10),
    `suc` int,
    `fail` int,
    primary key(`date`, `platformId`)
);

