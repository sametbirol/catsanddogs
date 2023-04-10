INSERT INTO likes (id, user_id, post_id, pet_id)
SELECT 
    ROW_NUMBER() OVER () as id,
    u1.id as user_id,
    p.id as post_id,
    p.pet_id as pet_id
FROM 
    users u1
    JOIN posts p ON u1.id <> p.owner_id
    JOIN users u2 ON u2.id = p.owner_id
WHERE 
    u1.id <> u2.id;
