from flask_restplus import Resource

from app.main.dto.storageDto import StorageDto
from app.main.model import storage
from app.main.service.storageService import save_storage, get_all_storage

api = StorageDto.api
_info = StorageDto.storage


@api.route('/save/<memo>')
@api.param('memo')
class MemoSave(Resource):
    @api.doc('save memo')
    @api.marshal_with(_info, code=201, description='Object created')
    def get(self, memo):
        return save_storage(memo)


@api.route('/show')
class MemoShow(Resource):
    @api.doc('get all number')
    @api.marshal_with(_info)
    def get(self):
        return get_all_storage()
