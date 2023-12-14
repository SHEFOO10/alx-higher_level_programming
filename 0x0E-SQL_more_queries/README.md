# 0x0E. SQL - More queries

## Learning Objectives

**At the end of this project, you are expected to be able to explain to anyone, without the help of Google:**

### General

- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are JOIN and UNION

| Task | file | Description |
|------|------|-------------|
| 0. My privileges! | [0-privileges.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/1-create_database_if_missing.sql) | lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server (in localhost). |
| 1. Root user | [1-create_user.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/1-create_user.sql) | creates the MySQL server user user_0d_1. |
| 2. Read user | [2-create_read_user.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/2-create_read_user.sql) | creates the database hbtn_0d_2 and the user user_0d_2. |
| 3. Always a name | [3-force_name.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/3-force_name.sql) | creates the table force_name on your MySQL server.|
| 4. ID can't be null | [4-never_empty.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/4-never_empty.sql) | creates the table id_not_null on your MySQL server.|
| 5. Unique ID | [5-unique_id.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/5-unique_id.sql) | creates the table unique_id on your MySQL server.|
| 6. States table | [6-states.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/6-states.sql) | creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server. |
| 7. Cities table | [7-cities.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/7-cities.sql) | creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server. |
| 8. Cities of California | [8-cities_of_california_subquery.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/8-cities_of_california_subquery.sql) | lists all the cities of California that can be found in the database hbtn_0d_usa. |
| 9. Cities by States | [9-cities_by_state_join.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/9-cities_by_state_join.sql) | lists all cities contained in the database hbtn_0d_usa. |
| 10. Genre ID by show | [10-genre_id_by_show.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/10-genre_id_by_show.sql) | lists all shows contained in hbtn_0d_tvshows that have at least one genre linked. |
| 11. Genre ID for all shows | [11-genre_id_all_shows.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/11-genre_id_all_shows.sql) | lists all shows contained in the database hbtn_0d_tvshows. |
| 12. No genre | [12-no_genre.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/12-no_genre.sql) | lists all shows contained in hbtn_0d_tvshows without a genre linked. |
| 13. Number of shows by genre | [13-count_shows_by_genre.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/13-count_shows_by_genre.sql) | lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each. |
| 14. My genres | [14-my_genres.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/14-my_genres.sql) | uses the hbtn_0d_tvshows database to lists all genres of the show Dexter. |
| 15. Only Comedy | [15-comedy_only.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/15-comedy_only.sql) | lists all Comedy shows in the database hbtn_0d_tvshows. |
| 16. List shows and genres | [16-shows_by_genre.sql](https://github.com/SHEFOO10/alx-higher_level_programming/tree/main/0x0D-SQL_introduction/16-shows_by_genre.sql) | lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows. |
