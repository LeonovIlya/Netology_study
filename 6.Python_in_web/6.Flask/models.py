from sqlalchemy import Column, Integer, String, DateTime, func
from settings import Base, engine


class AdvModel(Base):
    __tablename__ = 'advertisements'
    id = Column(Integer, primary_key=True)
    header = Column(String, index=True)
    owner = Column(String, index=True)
    description = Column(String, index=True)
    registration_time = Column(DateTime, server_default=func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'header': self.header,
            'owner': self.owner,
            'description': self.description,
            'registration_time': self.registration_time.isoformat()
        }


Base.metadata.create_all(engine)
