import time
import logging
from arango import ArangoClient
from arango.exceptions import ServerConnectionError, DatabaseCreateError

logger = logging.getLogger(__name__)

class ArangoDB:
    def __init__(self):
        self.client = None
        self.db = None

    def init_app(self, app):
        self.client = ArangoClient()

        # Konfigurasi dasar
        username = app.config.get("ARANGO_USER", "root")
        password = app.config.get("ARANGO_PASS", "")
        db_name  = app.config.get("ARANGO_DB", "test")
        max_retries = app.config.get("ARANGO_MAX_RETRIES", 10)
        retry_delay = app.config.get("ARANGO_RETRY_DELAY", 3)

        # Coba koneksi ke _system DB dengan retry
        sys_db = None
        for attempt in range(max_retries):
            try:
                sys_db = self.client.db(
                    "_system",
                    username=username,
                    password=password
                )
                # ping sederhana
                sys_db.version()
                logger.info("✅ Connected to ArangoDB (_system)")
                break
            except ServerConnectionError:
                logger.warning(f"ArangoDB not ready (attempt {attempt+1}/{max_retries}), retrying...")
                time.sleep(retry_delay)
        else:
            raise ConnectionError("❌ Could not connect to ArangoDB after retries")

        # Buat DB kalau belum ada
        try:
            if not sys_db.has_database(db_name):
                sys_db.create_database(db_name)
                logger.info(f"📦 Created database: {db_name}")
        except DatabaseCreateError as e:
            logger.error(f"❌ Failed to create database {db_name}: {e}")
            raise

        # Simpan koneksi DB utama
        self.db = self.client.db(
            db_name,
            username=username,
            password=password
        )
        logger.info(f"✅ Using database: {db_name}")

    def get_db(self):
        if not self.db:
            raise RuntimeError("ArangoDB has not been initialized. Call init_app() first.")
        return self.db


# Singleton
arango = ArangoDB()
