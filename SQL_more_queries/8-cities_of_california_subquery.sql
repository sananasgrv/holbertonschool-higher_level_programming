-- Listing California
SELECT id, name
FROM cities
WHERE cities.id=(
	SELECT id
	FROM state
	WHERE name='California')
ORDER BY cities.id
