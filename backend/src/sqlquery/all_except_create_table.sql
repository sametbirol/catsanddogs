INSERT INTO pets (id, name, species, owner_id)
VALUES (1, 'Buddy', 'Dog', 1);
INSERT INTO pets (id, name, species, owner_id)
VALUES (2, 'Luna', 'Cat', 2);
INSERT INTO pets (id, name, species, owner_id)
VALUES (3, 'Maxy', 'Dog', 1);
INSERT INTO pets (id, name, species, owner_id)
VALUES (6, 'Buddy', 'Dog', 2);
INSERT INTO pets (id, name, species, owner_id)
VALUES (7, 'Luna', 'Cat', 1);
INSERT INTO pets (id, name, species, owner_id)
VALUES (8, 'Max', 'Cat', 2);


INSERT INTO posts (id, reference, text, owner_id, pet_id, timestamp)
VALUES 
    (1, 'pets/1_1_1649638021743', 'My furry friend(Buddy) enjoying the sunshine!', 1, 1, '1649638021743'),
    (2, 'pets/2_6_1649638052931', 'Buddy loves playing fetch!', 2, 6, '1649638052931'),
    (3, 'pets/1_3_1649638090547', 'Maxy always makes me smile 😊', 1, 3, '1649638090547'),
    (4, 'pets/1_7_1649638121297', 'Luna is the queen of the house 👑', 1, 7, '1649638121297'),
    (5, 'pets/2_8_1649638164763', 'Max loves his treats!', 2, 8, '1649638164763');


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
	
INSERT INTO follows (user_id, pet_id)
SELECT DISTINCT
    u.id,
    p.id
FROM
    users u
    CROSS JOIN pets p
WHERE
    p.owner_id <> u.id;
	
INSERT INTO comments (comment_id, user_id, post_id, comment)
VALUES 
    (1, 1, 1, 'Aww, My Buddy looks so happy!'),
    (2, 2, 1, 'What a cute dog!'),
    (3, 2, 2, 'It is clear that my Buddy is having the blast here!'),
    (4, 1, 3, 'My Maxy is adorable!'),
    (5, 2, 3, 'Agreed! Maxy always puts a smile on my face.'),
    (6, 1, 4, 'My Luna is the queen indeed!'),
    (7, 1, 4, 'She looks like royalty.I wish I had that cat :/'),
    (8, 2, 5, 'My Max is so cute when he eats his treats!'),
    (9, 1, 5, 'I love spoiling your pets with treats!');


