DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS follows;
DROP TABLE IF EXISTS likes;
DROP TABLE IF EXISTS posts;
DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id SERIAL NOT NULL,
    email VARCHAR(255) NOT NULL,
    username VARCHAR(50) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    hashed_password VARCHAR(255),
    is_active BOOLEAN DEFAULT False,
    side VARCHAR(10),
    PRIMARY KEY (id),
    UNIQUE (email),
    UNIQUE (username)
);

CREATE TABLE pets (
    id INTEGER NOT NULL,
    name VARCHAR(50),
    species VARCHAR(50),
    owner_id INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY(owner_id) REFERENCES users (id)
);

CREATE TABLE posts (
    id INTEGER NOT NULL,
    title VARCHAR(255),
    text VARCHAR,
    images BYTEA,
    owner_id INTEGER,
    pet_id INTEGER,
    timestamp TIMESTAMP,
    PRIMARY KEY (id),
    FOREIGN KEY(owner_id) REFERENCES users (id),
    FOREIGN KEY(pet_id) REFERENCES pets (id)
);

CREATE TABLE likes (
    id INTEGER NOT NULL,
    user_id INTEGER,
    post_id INTEGER,
    pet_id INTEGER,
    PRIMARY KEY (id),
    FOREIGN KEY(user_id) REFERENCES users (id),
    FOREIGN KEY(post_id) REFERENCES posts (id),
    FOREIGN KEY(pet_id) REFERENCES pets (id)
);

CREATE TABLE follows (
    user_id INTEGER NOT NULL,
    pet_id INTEGER NOT NULL,
    PRIMARY KEY (user_id, pet_id),
    FOREIGN KEY(user_id) REFERENCES users (id),
    FOREIGN KEY(pet_id) REFERENCES pets (id)
);

CREATE TABLE comments (
    comment_id INTEGER NOT NULL,
    user_id INTEGER,
    post_id INTEGER,
    comment VARCHAR,
    PRIMARY KEY (comment_id),
    FOREIGN KEY(user_id) REFERENCES users (id),
    FOREIGN KEY(post_id) REFERENCES posts (id)
);
	