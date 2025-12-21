-- Comedy genre
SELECT DISTINCT s.title AS title 
FROM tv_show_genres AS sg
INNER JOIN tv_shows AS s
ON s.id = sg.show_id
INNER JOIN tv_genres AS g
ON g.id = sg.genre_id
WHERE g.name = "Comedy"
ORDER BY s.title ASC;
