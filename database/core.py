from database.utils.CRUD import CRUDInterface
from database.common.models import db, SearchHistory

db.connect()
db.create_tables([SearchHistory])

crud = CRUDInterface()

if __name__ == 'main':
    crud()