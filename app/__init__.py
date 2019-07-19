from flask_restplus import Api
from flask import Blueprint

from app.main.controller.storageController import api as storage_api

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Learning controller',
          version='0.1',
          description='CONTROLLER'
          )

api.add_namespace(storage_api)
