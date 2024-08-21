from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import ForeignKey, String, BIGINT, TIMESTAMP, DateTime, BOOLEAN, FLOAT




class Base(DeclarativeBase):
    pass


    
class Users(Base):
    __tablename__ = 'users'
    user_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str] = mapped_column(String(255), nullable=True)
    username: Mapped[str] = mapped_column(String(255), nullable=True)
    joined_at: Mapped[DateTime] = mapped_column(TIMESTAMP)
    is_admin: Mapped[bool] = mapped_column(BOOLEAN)
    phone_number: Mapped[str] = mapped_column(String(255), nullable=True)
    latitude: Mapped[float] = mapped_column(FLOAT, nullable=True)
    longitude: Mapped[float] = mapped_column(FLOAT, nullable=True)
    
    
    
    
class First_layer(Base):
    __tablename__ = 'first_layer'
    first_layer_id: Mapped[int] = mapped_column(BIGINT, primary_key=True,autoincrement=True)  # noqa: E501
    user_id: Mapped[int] = mapped_column(BIGINT, ForeignKey('users.user_id'), autoincrement=True)  # noqa: E501
    click_time: Mapped[DateTime] = mapped_column(TIMESTAMP)
    callback: Mapped[str] = mapped_column(String(255))
    
    
class Success_clicks(Base):
    __tablename__ = 'success_clicks'
    success_click_id: Mapped[int] = mapped_column(BIGINT, primary_key=True, autoincrement=True)  # noqa: E501
    user_id: Mapped[int] = mapped_column(BIGINT, ForeignKey('users.user_id'), autoincrement=True)  # noqa: E501
    click_time: Mapped[DateTime] = mapped_column(TIMESTAMP)
    
    
    

    
    


    
    
    
    