-- 部门表 Department：

-- +---------------+---------+
-- | Column Name   | Type    |
-- +---------------+---------+
-- | id            | int     |
-- | revenue       | int     |
-- | month         | varchar |
-- +---------------+---------+
-- (id, month) 是表的联合主键。
-- 这个表格有关于每个部门每月收入的信息。
-- 月份（month）可以取下列值 ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]。
--  

-- 编写一个 SQL 查询来重新格式化表，使得新的表中有一个部门 id 列和一些对应 每个月 的收入（revenue）列。

-- 查询结果格式如下面的示例所示：

-- Department 表：
-- +------+---------+-------+
-- | id   | revenue | month |
-- +------+---------+-------+
-- | 1    | 8000    | Jan   |
-- | 2    | 9000    | Jan   |
-- | 3    | 10000   | Feb   |
-- | 1    | 7000    | Feb   |
-- | 1    | 6000    | Mar   |
-- +------+---------+-------+

-- 查询得到的结果表：
-- +------+-------------+-------------+-------------+-----+-------------+
-- | id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
-- +------+-------------+-------------+-------------+-----+-------------+
-- | 1    | 8000        | 7000        | 6000        | ... | null        |
-- | 2    | 9000        | null        | null        | ... | null        |
-- | 3    | null        | 10000       | null        | ... | null        |
-- +------+-------------+-------------+-------------+-----+-------------+

SELECT 
id,
SUM(case month WHEN 'Jan' THEN revenue END) as 'Jan_Revenue',
SUM(case month WHEN 'Feb' THEN revenue END) as 'Feb_Revenue',
SUM(case month WHEN 'Mar' THEN revenue END) as 'Mar_Revenue',
SUM(case month WHEN 'Apr' THEN revenue END) as 'Apr_Revenue',
SUM(case month WHEN 'May' THEN revenue END) as 'May_Revenue',
SUM(case month WHEN 'Jun' THEN revenue END) as 'Jun_Revenue',
SUM(case month WHEN 'Jul' THEN revenue END) as 'Jul_Revenue',
SUM(case month WHEN 'Aug' THEN revenue END) as 'Aug_Revenue',
SUM(case month WHEN 'Sep' THEN revenue END) as 'Sep_Revenue',
SUM(case month WHEN 'Oct' THEN revenue END) as 'Oct_Revenue',
SUM(case month WHEN 'Nov' THEN revenue END) as 'Nov_Revenue',
SUM(case month WHEN 'Dec' THEN revenue END) as 'Dec_Revenue'

FROM Department
GROUP BY ID
