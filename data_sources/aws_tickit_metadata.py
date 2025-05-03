tickit_metadata = """
数据库: sample_data_dev
模式: tickit

表: sample_data_dev.tickit.category
- catid (integer): 唯一类别ID。
- catgroup (varchar): 此类别所属的组。
- catname (varchar): 类别名称。
- catdesc (varchar): 类别描述。

表: sample_data_dev.tickit.date
- dateid (integer): 日期代理键。
- caldate (date): 日历日期。
- day (integer): 月份中的日。
- week (integer): 周数。
- month (integer): 月份数。
- qtr (integer): 季度。
- year (integer): 年份。
- holiday (boolean): 是否为假日。

表: sample_data_dev.tickit.event
- eventid (integer): 每个事件的唯一ID。
- venueid (integer): 场地的外键。
- catid (integer): 类别的外键。
- dateid (integer): 日期的外键。
- eventname (varchar): 事件名称。
- starttime (timestamp): 事件开始时间。

表: sample_data_dev.tickit.listing
- listid (integer): 唯一列表ID。
- sellerid (integer): 用户的外键。
- eventid (integer): 事件的外键。
- dateid (integer): 日期的外键。
- numtickets (integer): 可用票数。
- priceperticket (decimal): 每张票价格。
- totalprice (decimal): 总价。
- listtime (timestamp): 创建列表的时间。

表: sample_data_dev.tickit.sales
- salesid (integer): 唯一销售ID。
- listid (integer): 列表的外键。
- sellerid (integer): 卖家用户ID。
- buyerid (integer): 买家用户ID。
- eventid (integer): 事件ID。
- dateid (integer): 日期ID。
- qtysold (integer): 售出票数。
- pricepaid (decimal): 支付总价。
- commission (decimal): 收取的佣金。
- saletime (timestamp): 销售时间。

表: sample_data_dev.tickit.users
- userid (integer): 唯一用户ID。
- username (varchar): 用户全名。
- city (varchar): 用户所在城市。
- state (varchar): 用户所在州。
- email (varchar): 用户电子邮件。
- phone (varchar): 电话号码。
- likesports (boolean): 用户喜欢体育。
- liketheatre (boolean): 用户喜欢戏剧。
- likeconcerts (boolean): 用户喜欢音乐会。
- likejazz (boolean): 用户喜欢爵士乐。
- likeclassical (boolean): 用户喜欢古典音乐。
- likeopera (boolean): 用户喜欢歌剧。
- likerock (boolean): 用户喜欢摇滚乐。
- likevegas (boolean): 用户喜欢拉斯维加斯表演。
- likebroadway (boolean): 用户喜欢百老汇。
- likemusicals (boolean): 用户喜欢音乐剧。

表: sample_data_dev.tickit.venue
- venueid (integer): 唯一场地ID。
- venuename (varchar): 场地名称。
- venuecity (varchar): 城市。
- venuestate (varchar): 州。
- venueseats (integer): 座位总数。
"""
