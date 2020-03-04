-- script that lists all shows, and all genres linked to that show, from the database
SELECT sh.title, gr.name
       FROM tv_shows sh
       LEFT OUTER JOIN tv_show_genres sh_gr
       ON sh.id = sh_gr.show_id
       LEFT OUTER JOIN tv_genres gr
       ON sh_gr.genre_id = gr.id
       ORDER BY sh.title, gr.name;
