from elasticsearch import Elasticsearch

class ElasticClient:
    def __init__(self):
        self.client = None

    def init_app(self, app):
        self.client = Elasticsearch(
            hosts=[{"host": app.config["ELASTIC_HOST"], "port": app.config["ELASTIC_PORT"]}],
        )
        app.elastic = self.client

elastic_client = ElasticClient()
