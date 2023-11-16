from sqlalchemy import Column, DateTime, func


class TimestampedModel(object):
    created_date = Column(DateTime, nullable=True,
                          default=func.now())
    updated_date = Column(DateTime, nullable=True,
                          default=func.now(), onupdate=func.now())
    deleted_date = Column(DateTime, nullable=True
                          )

    @staticmethod
    def sa_attributes():
        return [
            Column('created_date', DateTime,
                   nullable=True, default=func.now()),
            Column('updated_date', DateTime, nullable=True,
                   default=func.now(), onupdate=func.now()),
            Column('deleted_date', DateTime, nullable=True),
        ]
