-- script that lists all Comedy shows in the database hbtn_0d_tvshows
SELECT sh.title
       FROM tv_genres gr, tv_show_genres sh_gr, tv_shows sh
       WHERE gr.name = 'Comedy'
       AND sh_gr.genre_id = gr.id
       AND sh.id = sh_gr.show_id
       ORDER BY sh.title ASC;
