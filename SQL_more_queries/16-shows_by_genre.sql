-- comment
SELECT s.title AS title, g.name AS name
FROM tv_show_genres AS sg
RIGHT JOIN tv_shows AS s
ON s.id = sg.show_id
LEFT JOIN tv_genres AS g
ON sg.genre_id = g.id
ORDER BY s.title, g.name
