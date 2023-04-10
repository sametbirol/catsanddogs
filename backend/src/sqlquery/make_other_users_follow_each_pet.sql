INSERT INTO follows (user_id, pet_id)
SELECT DISTINCT
    u.id,
    p.id
FROM
    users u
    CROSS JOIN pets p
WHERE
    p.owner_id <> u.id;
