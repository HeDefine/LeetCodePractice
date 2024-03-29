-- SQL架构
-- 编写一个 SQL 查询，查找 Person 表中所有重复的电子邮箱。
--
-- 示例：
--
-- +----+---------+
-- | Id | Email   |
-- +----+---------+
-- | 1  | a@b.com |
-- | 2  | c@d.com |
-- | 3  | a@b.com |
-- +----+---------+
-- 根据以上输入，你的查询应返回以下结果：
--
-- +---------+
-- | Email   |
-- +---------+
-- | a@b.com |
-- +---------+
-- 说明：所有电子邮箱都是小写字母。

SELECT t0.Email
From
(
    SELECT Count(*) as count, Email
    FROM Person
    Group By Email
) as t0
WHERE t0.count > 1
