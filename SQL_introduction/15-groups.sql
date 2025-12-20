-- Number of records
SELECT score, COUNT(score)
FROM second_table
GROUP BY score
ORDER BY COUNT(score) DESC;
