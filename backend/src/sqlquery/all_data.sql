
INSERT INTO users (id, email, username, first_name, last_name, hashed_password, is_active,side)
VALUES (1,'string@gmail.com','string','string','string','$2b$12$hXRtXp2QotdXKLOE9DrjreKUDlTU/8n8Br0bmdZ8RXxlXsDxvXJcC',true,'Cat');
-- password:String123*

INSERT INTO users (id, email, username, first_name, last_name, hashed_password, is_active,side)
VALUES (2,'string1@gmail.com','string1','string1','string1','$2b$12$tIZHYQF.NpIvbfwjJZNMQet7PDpec14eWz0RTiSrHj9WXTyk3RRNW',true,'Cat');
-- password:String123*
INSERT INTO users (id, email, username, first_name, last_name, hashed_password, is_active,side)
VALUES (3,'string2@gmail.com','string2','string2','string2','$2b$12$ZL1Q8k5pY3LjQy8tnxwMp.K9mYIHjnCvk8BEOWGVJ43i5IUKQqjQW',true,'Dog');
-- password:String123*
INSERT INTO users (id, email, username, first_name, last_name, hashed_password, is_active,side)
VALUES (4,'string3@gmail.com','string3','string3','string3','$2b$12$I5inUiXcljL4qiTYpNZq0OtiqZJz5qckbudi3dyeL3rpvWbQh7se2',true,'Dog');
-- password:String123*


-- Insert pets for user 1
INSERT INTO pets (id, name, species, owner_id)
VALUES (1, 'Buddy', 'Dog', 1),
       (7, 'Luna', 'Cat', 1);

-- Insert pets for user 2
INSERT INTO pets (id, name, species, owner_id)
VALUES (8, 'Max', 'Cat', 2);

-- Insert pets for user 3
INSERT INTO pets (id, name, species, owner_id)
VALUES (3, 'Maxy', 'Dog', 3);

-- Insert pets for user 4
INSERT INTO pets (id, name, species, owner_id)
VALUES (4, 'Charlie', 'Dog', 4),
       (5, 'Tiger', 'Cat', 4);

-- For bigger pet data
-- Insert pets for user 1
INSERT INTO pets (id, name, species, owner_id)
VALUES (9, 'Fluffy', 'Cat', 1),
       (10, 'Rocky', 'Dog', 1);

-- Insert pets for user 2
INSERT INTO pets (id, name, species, owner_id)
VALUES (11, 'Simba', 'Cat', 2),
       (12, 'Daisy', 'Dog', 2),
       (13, 'Misty', 'Cat', 2);

-- Insert pets for user 3
INSERT INTO pets (id, name, species, owner_id)
VALUES (14, 'Bruno', 'Dog', 3),
       (15, 'Lucky', 'Dog', 3),
       (16, 'Milo', 'Cat', 3);

-- Insert pets for user 4
INSERT INTO pets (id, name, species, owner_id)
VALUES (17, 'Ziggy', 'Dog', 4),
       (18, 'Sassy', 'Cat', 4),
       (19, 'Oscar', 'Dog', 4);


INSERT INTO posts (id, reference, text, owner_id, pet_id, timestamp) 
VALUES 
(1, 'pets/1_7_1681525571792', 'Businessman late for work!', 1, 7, '1681525571792'),
(2, 'pets/1_9_1681525854234', 'Wakey wakey, sun is set.', 1, 9, '1681525854234'),
(3, 'pets/1_1_1681525937192', 'My good buddy!', 1, 1, '1681525937192'),
(4, 'pets/1_10_1681526103642', 'He might not look tough but he has a good spirit', 1, 10, '1681526103642'),
(5, 'pets/2_11_1681526191326', 'Go simba!', 2, 11, '1681526191326'),
(6, 'pets/2_13_1681526220961', 'Misty but smiley', 2, 13, '1681526220961'),
(7, 'pets/2_8_1681526298157', 'Pay respect to his majesty !!!', 2, 8, '1681526298157'),
(8, 'pets/2_12_1681526407213', 'Yey', 2, 12, '1681526407213');
--For bigger post data
INSERT INTO posts (id, reference, text, owner_id, pet_id, timestamp) 
VALUES 
(9, 'pets/3_15_1681526447073', 'She looks like a cloud right??', 3, 15, '1681526447073'),
(10, 'pets/3_14_1681526577441', 'Bruno happy birthday to you!', 3, 14, '1681526577441'),
(11, 'pets/3_3_1681526622474', 'Maxy looks like a toy. My lovely puppy :)', 3, 3, '1681526622474'),
(12, 'pets/3_16_1681526650343', 'Milo is found sleeping in the market', 3, 16, '1681526650343'),
(13, 'pets/4_18_1681526682631', 'sassy', 4, 18, '1681526682631'),
(14, 'pets/4_4_1681526838079', 'Charlieeeeee!', 4, 4, '1681526838079'),
(15, 'pets/4_19_1681526871823', 'Oscar is soo photogenic', 4, 19, '1681526871823'),
(16, 'pets/4_17_1681526982183', 'He woke us up by farting and he tryna act surprised , naah', 4, 17, '1681526982183'),
(17, 'pets/4_5_1681527219870', 'find 5 difference haha!', 4, 5, '1681527219870');



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
    (1, 4, 1, 'That dog looks like it means business.'),
    (2, 2, 2, 'Beautiful sunset!'),
    (3, 2, 3, 'Aww, such a cute dog.'),
    (4, 3, 4, 'Looks can be deceiving, right?'),
    (5, 1, 5, 'Simba is the king of the jungle!'),
    (6, 1, 6, 'Love the misty atmosphere.'),
    (7, 3, 7, 'What a majestic cat!'),
    (8, 4, 8, 'Yay!'),
    (9, 2, 9, 'She definitely looks like a cloud.'),
    (10, 2, 10, 'Happy birthday, Bruno!'),
    (11, 4, 11, 'Maxy is adorable!'),
    (12, 1, 12, 'Milo looks so comfy.'),
    (13, 3, 13, 'Sassy indeed!'),
    (14, 1, 14, 'Charlie is such a charmer.'),
    (15, 2, 15, 'Oscar is a natural in front of the camera.'),
    (16, 3, 16, 'Haha, the joys of pet ownership.'),
    (17, 3, 17, 'Love the find the difference challenge!');
--For bigger comment data
INSERT INTO comments (comment_id, user_id, post_id, comment)
VALUES 
    (18, 1, 7, 'Wow, what a majestic cat! I love seeing posts of Max!'),
    (19, 3, 5, 'Simba is such a beautiful cat, love his fur pattern!'),
    (20, 2, 12, 'Milo is so cute, I can see why he fell asleep in the market'),
    (21, 4, 2, 'I love the sunset in the background, it really sets the mood!'),
    (22, 1, 10, 'Happy birthday Bruno, you deserve all the treats and belly rubs!'),
    (23, 4, 6, 'Misty is such a happy cat, I love seeing her smile!'),
    (24, 4, 4, 'I agree, even though he looks small, he has a big heart!');


--Everyone follows other than their pets, and likes posts other than their pets posts
--No one commented on their own pets posts
--17 posts for 17 pets, 1 for each

