from typing import Dict, List, TypeVar

from peewee import ModelSelect

from database.common.models import ModelBase
from database.common.models import db

T = TypeVar('T')


def _store_date(db, model: T, data) -> None:
    with db.atomic():
        model.insert_many(data).execute()


def _retrieve_all_data(db: db, model: T, *columns: ModelBase) -> ModelSelect:
    with db.atomic():
        response = model.select(*columns)

    return response


def _update_data(db, model: T, updates: dict, where_condition) -> None:
    with db.atomic():
        query = model.update(**updates).where(where_condition)
        query.execute()


def _delete_data(db, model: T, where_condition) -> None:
    with db.atomic():
        query = model.delete().where(where_condition)
        query.execute()


class CRUDInterface():
    @staticmethod
    def create():
        return _store_date

    @staticmethod
    def retrieve():
        return _retrieve_all_data

    @staticmethod
    def update():
        return _update_data

    @staticmethod
    def delete():
        return _delete_data


if __name__ == 'main':
    _store_date()
    _retrieve_all_data()
    _update_data()
    _delete_data()
    CRUDInterface()
