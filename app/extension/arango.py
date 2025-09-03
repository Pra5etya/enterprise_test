from arango import ArangoClient

class ArangoDB:
    def __init__(self):
        self.client = None
        self.db = None

    def init_app(self, app):
        self.client = ArangoClient()
        sys_db = self.client.db(
            "_system",
            username = app.config["ARANGO_USER"],
            password = app.config["ARANGO_PASS"]
        )
        if not sys_db.has_database(app.config["ARANGO_DB"]):
            sys_db.create_database(app.config["ARANGO_DB"])
        self.db = self.client.db(
            app.config["ARANGO_DB"],
            username=app.config["ARANGO_USER"],
            password=app.config["ARANGO_PASS"]
        )

    def get_db(self):
        return self.db

arango = ArangoDB()
