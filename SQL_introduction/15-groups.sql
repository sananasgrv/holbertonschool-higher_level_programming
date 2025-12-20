-- Number of records
SELECT score, COUNT(score)
FROM second_table
ORDER BY COUNT(score) DESC
