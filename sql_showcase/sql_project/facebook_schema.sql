-- Startup Code: mysql-ctl cli

-- TABLES FOR FACEBOOK CLONE: User, Posts, Comments, Likes, User_Relationship, Tags, Post_Tags, Comment_Tags

-- CREATE DATABASE:
CREATE DATABASE fb_clone;
USE fb_clone;

-- USERNAME TABLE:
CREATE TABLE users(
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(30) UNIQUE NOT NULL,
    birthday DATE, 
    created_at TIMESTAMP DEFAULT NOW()
);

-- POSTS TABLE:
CREATE TABLE posts(
    id INT AUTO_INCREMENT PRIMARY KEY,
    post_text VARCHAR(999) NOT NULL,
    post_url VARCHAR(2048) NOT NULL,
    user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY(user_id) REFERENCES users(id)
);

-- COMMENTS TABLE:
CREATE TABLE comments(
    id INT AUTO_INCREMENT PRIMARY KEY,
    comment_text VARCHAR(255) NOT NULL,
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(post_id) REFERENCES posts(id)
);

-- LIKES TABLE: *** PRIMARY KEY(user_id, photo_id) makes it so each user can only like each photo once ***
CREATE TABLE likes(
    user_id INT NOT NULL,
    post_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(post_id) REFERENCES posts(id),
    PRIMARY KEY(user_id, post_id)
);

-- FOLLOWS TABLE: *** Best to use one table for both followers/followees, both reference user_id *** Also, can only have one of a given relationship: PRIMARY KEY(follower_id, followee_id)
CREATE TABLE user_relationships(
    related_user_id INT NOT NULL,
    relating_user_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    type VARCHAR(6),
    FOREIGN KEY(related_user_id) REFERENCES users(id),
    FOREIGN KEY(relating_user_id) REFERENCES users(id),
    PRIMARY KEY(related_user_id, relating_user_id)
);

-- TAGS TABLE:
CREATE TABLE tags(
    id INT AUTO_INCREMENT PRIMARY KEY,
    tag_name VARCHAR(255) UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- POSTS_TAGS TABLE:
CREATE TABLE post_tags(
    post_id INT NOT NULL,
    tag_id INT NOT NULL,
    FOREIGN KEY(post_id) REFERENCES posts(id),
    FOREIGN KEY(tag_id) REFERENCES tags(id)
);

-- COMMENT TAGS TABLE:
CREATE TABLE comment_tags(
    comment_id INT NOT NULL,
    tag_id INT NOT NULL,
    FOREIGN KEY(comment_id) REFERENCES comments(id),
    FOREIGN KEY(tag_id) REFERENCES tags(id)
);