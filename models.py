from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, nullable=False, server_default='True')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

# NEW TABLES BELOW HERE // these are not created on the server yet.

class Genre(Base):
    __tablename__ = "genres"

    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    name = Column(String, nullable=False)
    isChild = Column(Boolean, nullable=False, server_default='False')

class Subgenre(Base):
    __tablename__ = "subgenres"

    id = Column(Integer, primary_key=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    name = Column(String, nullable=False)
    isChild = Column(Boolean, nullable=False, server_default='False')
    isYoungAdult = Column(Boolean, nullable=False, server_default='False')
    isMiddleGrade = Column(Boolean, nullable=False, server_default='False')
    isExplicit = Column(Boolean, nullable=False, server_default='False')

    genre_id = Column (Integer, ForeignKey("genres.id", ondelete="CASCADE", nullable=False))

class World(Base):
    __tablename__ = "worlds"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    isPrivate = Column(Boolean, nullable=False, server_default='True')
    isFriends = Column(Boolean, nullable=False, server_default='False')
    isPublic = Column(Boolean, nullable=False, server_default='False')

    owner_id = Column (Integer, ForeignKey("users.id", ondelete="CASCADE", nullable=False))
    
    owner = relationship("User")

class BookGroup(Base):
    __tablename__ = "bookgroups"
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    isPrivate = Column(Boolean, nullable=False, server_default='True')
    isFriends = Column(Boolean, nullable=False, server_default='False')
    isPublic = Column(Boolean, nullable=False, server_default='False')

    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE", nullable=False))
    world_id = Column(Integer, ForeignKey("worlds.id", ondelete="CASCADE", nullable=False))
    
    owner = relationship("User")

class Story(Base):
    __tablename__ = "stories"
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    premise = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    isPrivate = Column(Boolean, nullable=False, server_default='True')
    isFriends = Column(Boolean, nullable=False, server_default='False')
    isPublic = Column(Boolean, nullable=False, server_default='False')

    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE", nullable=False))
    world_id = Column(Integer, ForeignKey("worlds.id", ondelete="CASCADE", nullable=False))
    
    owner = relationship("User")

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    description = Column(String, nullable=False)
    story_role = Column(String, nullable=False)
    occupation = Column(String, nullable=False)
    story_goal = Column(String, nullable=False)
    physical_description = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    isPrivate = Column(Boolean, nullable=False, server_default='True')
    isFriends = Column(Boolean, nullable=False, server_default='False')
    isPublic = Column(Boolean, nullable=False, server_default='False')

    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE", nullable=False))
    world_id = Column(Integer, ForeignKey("worlds.id", ondelete="CASCADE", nullable=False))
    group_id = Column(Integer, ForeignKey("bookgroups.id", ondelete="CASCADE", nullable=False))
    first_appearance = Column(Integer, ForeignKey("stories.id", ondelete="CASCADE", nullable=False))
    
    owner = relationship("User")