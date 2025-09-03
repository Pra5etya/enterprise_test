def register_config(app): 
    from config.logger import setup_logger

    import os


    # 2.1 log setup
    # =================

    logger = setup_logger()

    # Hanya log "Restart" ketika proses utama berjalan setelah restart
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        logger.info(f"{"="  * 30} LOGGER STARTING POINT {"="  * 30} \n")
        logger.info("Flask is restarting...")
        logger.info("Log Start ... \n")

    # 2.2 Secret setup
    # =================

    app.config.update(
        SECRET_KEY = "supersecret",

        POSTGRES_USER = "appuser",
        POSTGRES_PASS = "secret",
        POSTGRES_DB = "appdb",
        POSTGRES_HOST = "postgres",
        POSTGRES_PORT = 5432,

        ARANGO_USER = "root",
        ARANGO_PASS = "openSesame",
        ARANGO_DB = "flask_db",

        REDIS_HOST = "redis",
        REDIS_PORT = 6379,

        ELASTIC_HOST = "elasticsearch",
        ELASTIC_PORT = 9200
    )

    # 2.3 Middleware setup
    # =================