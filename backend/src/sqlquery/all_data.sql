INSERT INTO users (email, username, first_name, last_name, hashed_password, is_active,side)
VALUES ('string@gmail.com','string','string','string','$2b$12$hXRtXp2QotdXKLOE9DrjreKUDlTU/8n8Br0bmdZ8RXxlXsDxvXJcC',true,'Cat');
-- password:String123*
INSERT INTO users (email, username, first_name, last_name, hashed_password, is_active,side)
VALUES ('string1@gmail.com','string1','string1','string1','$2b$12$tIZHYQF.NpIvbfwjJZNMQet7PDpec14eWz0RTiSrHj9WXTyk3RRNW',true,'Cat');
-- password:String123*
INSERT INTO users (email, username, first_name, last_name, hashed_password, is_active,side)
VALUES ('string2@gmail.com','string2','string2','string2','$2b$12$ZL1Q8k5pY3LjQy8tnxwMp.K9mYIHjnCvk8BEOWGVJ43i5IUKQqjQW',true,'Dog');
-- password:String123*
INSERT INTO users (email, username, first_name, last_name, hashed_password, is_active,side)
VALUES ('string3@gmail.com','string3','string3','string3','$2b$12$I5inUiXcljL4qiTYpNZq0OtiqZJz5qckbudi3dyeL3rpvWbQh7se2',true,'Dog');
-- password:String123*


-- Insert pets for user 1
INSERT INTO pets (name, species, owner_id)
VALUES ('Buddy', 'Dog', 1),
       ('Luna', 'Cat', 1);

-- Insert pets for user 2
INSERT INTO pets (name, species, owner_id)
VALUES ('Max', 'Cat', 2);

-- Insert pets for user 3
INSERT INTO pets (name, species, owner_id)
VALUES ('Maxy', 'Dog', 3);

-- Insert pets for user 4
INSERT INTO pets (name, species, owner_id)
VALUES ('Charlie', 'Dog', 4),
       ('Tiger', 'Cat', 4);

-- For bigger pet data
-- Insert pets for user 1
INSERT INTO pets (name, species, owner_id)
VALUES ('Fluffy', 'Cat', 1),
       ( 'Rocky', 'Dog', 1);

-- Insert pets for user 2
INSERT INTO pets (name, species, owner_id)
VALUES ('Simba', 'Cat', 2),
       ('Daisy', 'Dog', 2),
       ('Misty', 'Cat', 2);

-- Insert pets for user 3
INSERT INTO pets (name, species, owner_id)
VALUES ('Bruno', 'Dog', 3),
       ('Lucky', 'Dog', 3),
       ('Milo', 'Cat', 3);

-- Insert pets for user 4
INSERT INTO pets (name, species, owner_id)
VALUES ('Ziggy', 'Dog', 4),
       ('Sassy', 'Cat', 4),
       ('Oscar', 'Dog', 4);


INSERT INTO posts (reference, text, owner_id, pet_id, timestamp) 
VALUES 
('pets/1_7_1681525571792', 'Businessman late for work!', 1, 7, '1681525571792'),
('pets/1_9_1681525854234', 'Wakey wakey, sun is set.', 1, 9, '1681525854234'),
('pets/1_1_1681525937192', 'My good buddy!', 1, 1, '1681525937192'),
('pets/1_10_1681526103642', 'He might not look tough but he has a good spirit', 1, 10, '1681526103642'),
('pets/2_11_1681526191326', 'Go simba!', 2, 11, '1681526191326'),
('pets/2_13_1681526220961', 'Misty but smiley', 2, 13, '1681526220961'),
('pets/2_8_1681526298157', 'Pay respect to his majesty !!!', 2, 8, '1681526298157'),
('pets/2_12_1681526407213', 'Yey', 2, 12, '1681526407213');
--For bigger post data
INSERT INTO posts (reference, text, owner_id, pet_id, timestamp) 
VALUES 
('pets/3_15_1681526447073', 'She looks like a cloud right??', 3, 15, '1681526447073'),
('pets/3_14_1681526577441', 'Bruno happy birthday to you!', 3, 14, '1681526577441'),
('pets/3_3_1681526622474', 'Maxy looks like a toy. My lovely puppy :)', 3, 3, '1681526622474'),
('pets/3_16_1681526650343', 'Milo is found sleeping in the market', 3, 16, '1681526650343'),
('pets/4_4_1681526838079', 'Charlieeeeee!', 4, 4, '1681526838079'),
('pets/4_17_1681526982183', 'He woke us up by farting and he tryna act surprised , naah', 4, 17, '1681526982183'),
('pets/4_5_1681527219870', 'find 5 difference haha!', 4, 5, '1681527219870');


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
	
INSERT INTO comments (user_id, post_id, comment)
VALUES
    (4, 1, 'That dog looks like it means business.'),
    (2, 2, 'Beautiful sunset!'),
    (2, 3, 'Aww, such a cute dog.'),
    (3, 4, 'Looks can be deceiving, right?'),
    (1, 5, 'Simba is the king of the jungle!'),
    (1, 6, 'Love the misty atmosphere.'),
    (3, 7, 'What a majestic cat!'),
    (4, 8, 'Yay!'),
    (2, 9, 'She definitely looks like a cloud.'),
    (2, 10, 'Happy birthday, Bruno!'),
    (4, 11, 'Maxy is adorable!'),
    (1, 12, 'Milo looks so comfy.'),
    (3, 13, 'Sassy indeed!'),
    (1, 14, 'Charlie is such a charmer.'),
    (2, 15, 'Oscar is a natural in front of the camera.');

INSERT INTO comments (user_id, post_id, comment)
VALUES 
    (1, 7, 'Wow, what a majestic cat! I love seeing posts of Max!'),
    (3, 5, 'Simba is such a beautiful cat, love his fur pattern!'),
    (2, 12, 'Milo is so cute, I can see why he fell asleep in the market'),
    (4, 2, 'I love the sunset in the background, it really sets the mood!'),
    (1, 10, 'Happy birthday Bruno, you deserve all the treats and belly rubs!'),
    (4, 6, 'Misty is such a happy cat, I love seeing her smile!'),
    (4, 4, 'I agree, even though he looks small, he has a big heart!');


