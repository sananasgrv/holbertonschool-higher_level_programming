-- List the shows
SELECT DISTINCT g.name
FROM tv_show_genres AS sg
INNER JOIN tv_shows AS s
ON s.id = sg.show_id
INNER JOIN tv_genres AS g
ON sg.genre_id = g.id
WHERE s.title = "Dexter"
ORDER BY g.name ASC;
