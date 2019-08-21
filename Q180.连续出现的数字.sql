-- https://leetcode-cn.com/problems/consecutive-numbers/
-- SQL架构
-- 编写一个 SQL 查询，查找所有至少连续出现三次的数字。
--
-- +----+-----+
-- | Id | Num |
-- +----+-----+
-- | 1  |  1  |
-- | 2  |  1  |
-- | 3  |  1  |
-- | 4  |  2  |
-- | 5  |  1  |
-- | 6  |  2  |
-- | 7  |  2  |
-- +----+-----+
-- 例如，给定上面的 Logs 表， 1 是唯一连续出现至少三次的数字。
--
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+

SELECT DISTINCT a.Num AS ConsecutiveNums
FROM Logs a, Logs b, Logs c
WHERE
a.Id = b.Id - 1
AND
b.Id = c.Id - 1
AND
a.Num = b.Num
AND
b.Num = c.Num