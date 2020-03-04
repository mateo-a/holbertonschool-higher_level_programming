-- script that uses the hbtn_0d_tvshows database to lists all genres of the show
-- Dexter
SELECT gr.name
       FROM tv_genres gr, tv_show_genres sh_gr, tv_shows sh
       WHERE sh.title = 'Dexter'
       AND sh_gr.show_id = sh.id
       AND gr.id = sh_gr.genre_id
       ORDER BY gr.name;
