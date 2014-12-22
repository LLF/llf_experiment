#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

sql = ['use kpi;']

sql.append("
    CREATE TABLE IF NOT EXISTS `UserAccount` (
      `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
      `userId` int(11) unsigned NOT NULL ,
      `guestId` int unsigned NOT NULL ,
      `deviceId` int unsigned NOT NULL ,
      `createdAt` datetime NOT NULL,
      PRIMARY KEY (`id`),
    ) ENGINE=InnoDB
;")
