-- script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT gr.name AS genre, COUNT(sh.show_id) AS number_of_shows
FROM tv_genres gr INNER JOIN  tv_show_genres sh
    ON gr.id = sh.genre_id
    GROUP BY genre
    ORDER BY number_of_shows DESC;
