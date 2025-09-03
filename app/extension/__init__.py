from .postgre import postgres, db, migrate
from .arango import arango
from .redis import redis_client
from .elastic import elastic_client

def register_extensions(app):
    """Inisialisasi semua extensions ke Flask app"""
    postgres.init_app(app)
    arango.init_app(app)
    redis_client.init_app(app)
    elastic_client.init_app(app)
