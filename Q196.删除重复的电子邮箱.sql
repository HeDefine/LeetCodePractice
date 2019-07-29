-- https://leetcode-cn.com/problems/delete-duplicate-emails
-- 编写一个 SQL 查询，来删除 Person 表中所有重复的电子邮箱，重复的邮箱里只保留 Id 最小 的那个。
--
-- +----+------------------+
-- | Id | Email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- | 3  | john@example.com |
-- +----+------------------+
-- Id 是这个表的主键。
-- 例如，在运行你的查询语句之后，上面的 Person 表应返回以下几行:
--
-- +----+------------------+
-- | Id | Email            |
-- +----+------------------+
-- | 1  | john@example.com |
-- | 2  | bob@example.com  |
-- +----+------------------+


DELETE FROM Person
WHERE Id NOT IN (   -- 删除不在查询结果中的值
    SELECT id FROM
   (
       SELECT MIN(Id) AS Id -- 排除Email相同时中Id较大的行
       FROM Person
       GROUP BY Email
   ) AS temp    -- 此处需使用临时表，否则会发生报错
)

