# SQLite database table using SQLAlchemy
# This file defines the SQLite table structure for storing five-year weather statistics.

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.orm import declarative_base

# Base class for SQLAlchemy ORM models
Base = declarative_base()


# ORM model representing the weather_data table in SQLite
class WeatherRecord(Base):
    __tablename__ = "weather_data"

    # Primary key
    id = Column(Integer, primary_key=True)

    # Location + date fields
    latitude = Column(Float)
    longitude = Column(Float)
    month = Column(Integer)
    day = Column(Integer)
    year = Column(Integer)

    # Five-year temperature stats (F)
    avg_temp = Column(Float)
    min_temp = Column(Float)
    max_temp = Column(Float)

    # Five-year wind stats (mph)
    avg_wind = Column(Float)
    min_wind = Column(Float)
    max_wind = Column(Float)

    # Five-year precipitation stats (inches)
    sum_precip = Column(Float)
    min_precip = Column(Float)
    max_precip = Column(Float)

# Create the SQLite database file and table if they do not already exist
engine = create_engine("sqlite:///weather.db")

# Create a session factory (used to insert/query)
SessionLocal = sessionmaker(bind=engine)


Base.metadata.create_all(engine)

# Insert one WeatherData object into the database
def insert_weather_record(weather:"WeatherData") -> None:
    session = SessionLocal()
    try:
        record = WeatherRecord(
            latitude=weather.latitude,
            longitude=weather.longitude,
            month=weather.month,
            day=weather.day,
            year=weather.year,
            avg_temp=weather.avg_temp,
            min_temp=weather.min_temp,
            max_temp=weather.max_temp,
            avg_wind=weather.avg_wind,
            min_wind=weather.min_wind,
            max_wind=weather.max_wind,
            sum_precip=weather.sum_precip,
            min_precip=weather.min_precip,
            max_precip=weather.max_precip,
    )
        session.add(record)
        session.commit()
    finally:
        session.close()

# Query the most recent record and return it
def get_latest_weather_record():
    session = SessionLocal()
    try:
        return session.query(WeatherRecord).order_by(WeatherRecord.id.desc()).first()
    finally:
        session.close()