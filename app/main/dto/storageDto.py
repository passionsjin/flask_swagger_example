from . import *


class StorageDto:
    api = Namespace('storage', description='메모 저장')

    storage = api.model('storage', {
        'memo': fields.String,
        'create_at': fields.String
    })
