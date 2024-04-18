#!/usr/bin/python3
"""
Class definition of a City
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create an instance of declarative_base
Base = declarative_base()

# Define the State class
class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

# Connect to MySQL server
engine = create_engine('mysql://username:password@localhost:3306/database_name')

# Create all tables defined by Base
Base.metadata.create_all(engine)
