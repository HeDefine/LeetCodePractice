-- https://leetcode-cn.com/problems/classes-more-than-5-students/
-- SQL架构
-- 有一个courses 表 ，有: student (学生) 和 class (课程)。
-- 请列出所有超过或等于5名学生的课。
--
-- 例如,表:
-- +---------+------------+
-- | student | class      |
-- +---------+------------+
-- | A       | Math       |
-- | B       | English    |
-- | C       | Math       |
-- | D       | Biology    |
-- | E       | Math       |
-- | F       | Computer   |
-- | G       | Math       |
-- | H       | Math       |
-- | I       | Math       |
-- +---------+------------+
--
-- 应该输出:
-- +---------+
-- | class   |
-- +---------+
-- | Math    |
-- +---------+
--
-- Note:
-- 学生在每个课中不应被重复计算。


SELECT class
FROM courses
GROUP BY class
HAVING count(DISTINCT(student))>=5