use kpi;
/* 充值档次 */
drop table if exists payment_level;
create table payment_level (
    `date` varchar(32),
    platform tinyint(10),
    zone varchar(32),
    purchase_id int(11),
    user_count int(10),
    times_count int(10),
    amount int(10),
    primary key(`date`, zone, purchase_id)
);

/* 金币产出 */
drop table if exists zel_inc;
create table zel_inc (
    `date` varchar(32),
    platform tinyint(10),
    zone varchar(32),
    `channel_id` int(11),
    user_count int(10),
    times_count int(10),
    amount int(10),
    primary key(`date`, zone, channel_id)
);

/* 金币消耗 */
drop table if exists zel_dec;
create table zel_dec (
    `date` varchar(32),
    platform tinyint(10),
    zone varchar(32),
    `channel_id` int(11),
    user_count int(10),
    times_count int(10),
    amount int(10),
    primary key(`date`, zone, channel_id)
);

/* 钻石产出 */
drop table if exists dia_inc;
create table dia_inc (
    `date` varchar(32),
    platform tinyint(10),
    zone varchar(32),
    `channel_id` int(11),
    user_count int(10),
    times_count int(10),
    amount int(10),
    primary key(`date`, zone, channel_id)
);

/* 钻石消耗 */
drop table if exists dia_dec;
create table dia_dec (
    `date` varchar(32),
    platform tinyint(10),
    zone varchar(32),
    `channel_id` int(11),
    user_count int(10),
    times_count int(10),
    amount int(10),
    primary key(`date`, zone, channel_id)
);

/* 魂产出 */
drop table if exists karma_inc;
create table karma_inc (
    `date` varchar(32),
    platform tinyint(10),
    zone varchar(32),
    `channel_id` int(11),
    user_count int(10),
    times_count int(10),
    amount int(10),
    primary key(`date`, zone, channel_id)
);

/* 魂消耗 */
drop table if exists karma_dec;
create table karma_dec (
    `date` varchar(32),
    platform tinyint(10),
    zone varchar(32),
    `channel_id` int(11),
    user_count int(10),
    times_count int(10),
    amount int(10),
    primary key(`date`, zone, channel_id)
);

/* 当日充值榜 */
drop table if exists top_vip;
create table top_vip (
    `date` varchar(32),
    platform tinyint(10),
    zone varchar(32),
    user_id varchar(32),
    `channel_id` int(11),
    amount int(10),
    times int(10),
    primary key(`date`, zone, user_id)
);

drop table if exists tmp_dia;
create table tmp_dia (
    platform tinyint(10),
    zone varchar(32),
    user_id varchar(32),
    `channel_id` int(11),
    amount int(10),
    times int(10),
    do_type int(11),
    index amount_index(do_type, amount)
);

/* 钻石榜 */
drop table if exists top_dia;
create table top_dia (
    `date` varchar(32),
    platform tinyint(10),
    zone varchar(32),
    user_id varchar(32),
    `channel_id` int(11),
    amount int(10),
    times int(10),
    do_type int(11),
    primary key(`date`, zone, user_id, do_type)
);

drop table if exists tmp_zel;
create table tmp_zel (
    platform tinyint(10),
    zone varchar(32),
    user_id varchar(32),
    `channel_id` int(11),
    amount int(10),
    times int(10),
    do_type int(11)
);

/* 金币榜 */
drop table if exists top_zel;
create table top_zel (
    `date` varchar(32),
    platform tinyint(10),
    zone varchar(32),
    user_id varchar(32),
    `channel_id` int(11),
    amount int(10),
    times int(10),
    do_type int(11),
    primary key(`date`, zone, user_id, do_type)
);

drop table if exists tmp_karma;
create table tmp_karma (
    platform tinyint(10),
    zone varchar(32),
    user_id varchar(32),
    `channel_id` int(11),
    amount int(10),
    times int(10),
    do_type int(11)
);

/* 魂榜 */
drop table if exists top_karma;
create table top_karma (
    `date` varchar(32),
    platform tinyint(10),
    zone varchar(32),
    user_id varchar(32),
    `channel_id` int(11),
    amount int(10),
    times int(10),
    do_type int(11),
    primary key(`date`, zone, user_id, do_type)
);

drop table if exists tmp_vip7;
create table tmp_vip7 (
    `date` varchar(32),
    zone varchar(32),
    user_id varchar(32),
    channel_id varchar(20),
    platform tinyint(10),
    amount int(11),
    primary key(`date`, zone, user_id)
);

/* 充值预警榜 */
drop table if exists vip7;
create table vip7 (
    zone varchar(32),
    user_id varchar(32),
    channel_id varchar(20),
    platform tinyint(10),
    amount7 int(11),
    amount3 int(11),
    index amount7_idx (amount7)
);

/* 行为数据 */

/* 当日创角等级分布 */
drop table if exists new_user_level;
create table new_user_level (
    `date` varchar(32),
    zone varchar(32),
    lv int(11),
    count int(11),
    primary key(`date`, zone, lv)
);

/* 竞技场挑战 */
drop table if exists arena_challenge;
create table arena_challenge (
    `date` varchar(32),
    zone varchar(32),
    result int(11),
    user_count int(11),
    times_count int(11),
    point_count int(11),
    karma_count int(11),
    primary key (`date`, zone, result)
);

/* 钥匙 */
drop table if exists dungeon_key;
create table dungeon_key (
    `date` varchar(32),
    zone varchar(32),
    do_type int(11),
    key_id int(11),
    user_count int(11),
    times_count int(11),
    key_count int(11),
    primary key(`date`, zone, do_type, key_id)
);

/* 进化 */
drop table if exists unit_evo;
create table unit_evo (
    `date` varchar(32),
    zone varchar(32),
    user_count int(11),
    times_count int(11),
    primary key(`date`, zone)
);

/* 强化 */
drop table if exists unit_mix;
create table unit_mix (
    `date` varchar(32),
    zone varchar(32),
    user_count int(11),
    times_count int(11),
    primary key(`date`, zone)
);

/* 出售 */
drop table if exists unit_sell;
create table unit_sell (
    `date` varchar(32),
    zone varchar(32),
    user_count int(11),
    times_count int(11),
    primary key(`date`, zone)
);

/* 建筑升级 */
drop table if exists facility_lvup;
create table facility_lvup (
    `date` varchar(32),
    zone varchar(32),
    facility_id int(11),
    user_count int(11),
    times_count int(11),
    primary key(`date`, zone, facility_id)
);

/* 资源升级 */
drop table if exists location_lvup;
create table location_lvup (
    `date` varchar(32),
    zone varchar(32),
    location_id int(11),
    user_count int(11),
    times_count int(11),
    primary key(`date`, zone, location_id)
);

/* 黑市刷新 */
drop table if exists bm_refresh;
create table bm_refresh (
    `date` varchar(32),
    zone varchar(32),
    money_type int(11),
    amount int(11),
    user_count int(11),
    times_count int(11),
    primary key(`date`, zone, money_type)
);

/* 黑市购买 */
drop table if exists bm_buy;
create table bm_buy (
    `date` varchar(32),
    zone varchar(32),
    money_type int(11),
    amount int(11),
    user_count int(11),
    times_count int(11),
    primary key(`date`, zone, money_type)
);

/* 黑市物品购买 */
drop table if exists bm_goods;
create table bm_goods (
    `date` varchar(32),
    zone varchar(32),
    item_type int(11),
    item_id int(11),
    user_count int(11),
    times_count int(11),
    amount int(11),
    primary key(`date`, zone, item_type, item_id)
);
