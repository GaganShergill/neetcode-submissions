-- Write your query below
WITH user_friends AS (
    SELECT user2_id AS friend_id FROM friendship WHERE user1_id = 1
    UNION
    SELECT user1_id AS friend_id FROM friendship WHERE user2_id = 1
),
friends_liked_pages AS (
    SELECT DISTINCT page_id 
    FROM likes 
    WHERE user_id IN (SELECT friend_id FROM user_friends)
)
SELECT page_id AS recommended_page
FROM friends_liked_pages
WHERE page_id NOT IN (
    SELECT page_id 
    FROM likes 
    WHERE user_id = 1
);