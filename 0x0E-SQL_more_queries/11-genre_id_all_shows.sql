-- Import the database dump of hbtn_0d_tvshows to your MySQL server
-- script that lists all shows contained in the database hbtn_0d_tvshow
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
