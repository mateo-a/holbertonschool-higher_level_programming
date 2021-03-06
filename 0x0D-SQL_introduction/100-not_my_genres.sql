-- script that uses the hbtn_0d_tvshows database to list all genres
-- not linked to the show Dexter
SELECT tv_genres.name AS name FROM tv_shows
       INNER JOIN tv_show_genres ON tv_shows.id = tv.show_genres.show_id
       AND tv_shows.tittle = "Dexter"
       RIGHT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
       WHERE genre_id IS NULL ORDER BY name
