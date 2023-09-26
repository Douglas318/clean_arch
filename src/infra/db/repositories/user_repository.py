from typing import List
from src.infra.db.settings.connection import DBConectionHandler
from src.infra.db.entites.users import Users as UsersEntity
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users


class UsersRepository(UsersRepositoryInterface):

    @classmethod
    def insert_user(cls, first_name: str, last_name: str, age: int) -> None:
        with DBConectionHandler() as db:
            try:
                data = UsersEntity(
                    first_name=first_name,
                    last_name=last_name,
                    age=age
                )
                db.session.add(data)
                db.session.commit()
            except Exception as error:
                db.session.rollback()
                raise error

    @classmethod
    def select_user(cls, first_name: str) -> List[Users]:
        with DBConectionHandler() as db:
            try:
                result = (
                    db.session
                        .query(UsersEntity)
                        .filter(UsersEntity.first_name == first_name)
                        .all()
                )
                return result
            except Exception as error:
                db.session.rollback()
                raise error
