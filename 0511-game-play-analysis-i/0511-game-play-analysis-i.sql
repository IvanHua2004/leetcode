# Write your MySQL query statement below
SELECT A1.player_id, MIN(A1.event_date) AS first_login
FROM Activity AS A1
JOIN Activity AS A2 ON A1.player_id = A2.player_id
GROUP BY A1.player_id