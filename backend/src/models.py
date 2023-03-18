from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import relationship
from database import Base


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True)
    username = Column(String(50), unique=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=False)
    side = Column(String)

    posts = relationship("Posts", back_populates="owner")
    pets = relationship("Pets", back_populates="owner")
    followed_pets = relationship("Pets", secondary="follows", back_populates="followers")
    comments = relationship("Comments", back_populates="user")


class Pets(Base):
    __tablename__ = 'pets'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    species = Column(String(50))
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("Users", back_populates="pets")
    likes = relationship("Likes", back_populates="pet")
    postslist = relationship("Posts", back_populates="pet")
    followers = relationship("Users", secondary="follows",back_populates="followed_pets")


class Posts(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    text = Column(String)
    images = Column(LargeBinary)
    owner_id = Column(Integer, ForeignKey("users.id"))
    pet_id = Column(Integer, ForeignKey("pets.id"))
    timestamp = Column(DateTime)

    owner = relationship("Users", back_populates="posts")
    pet = relationship("Pets", back_populates="postslist")
    likes = relationship("Likes", back_populates="post")


class Likes(Base):
    __tablename__ = 'likes'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    pet_id = Column(Integer, ForeignKey('pets.id'))

    post = relationship("Posts", back_populates="likes")
    pet = relationship("Pets", back_populates="likes")


class Follows(Base):
    __tablename__ = 'follows'

    user_id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    pet_id = Column(Integer, ForeignKey('pets.id'), primary_key=True)

    # user = relationship("Users", backref="followed_pets")
    # pet = relationship("Pets", backref="followers")


class Comments(Base):
    __tablename__ = 'comments'

    comment_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    comment = Column(String)

    user = relationship("Users", back_populates="comments")
