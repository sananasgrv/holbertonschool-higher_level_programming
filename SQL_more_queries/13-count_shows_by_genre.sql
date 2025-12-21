-- Listing
SELECT g.name AS genre , count(*) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
GROUP BY g.id
ORDER BY COUNT(*) DESC;
