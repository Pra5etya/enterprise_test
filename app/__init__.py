from flask import Flask

import os


def create_app():
    # =================
    # 0. app core
    # =================

    core = Flask(__name__, 
                static_url_path = '/', 
                static_folder = 'static', 
                template_folder = 'templates')
    

    # =================
    # 1. routes
    # =================

    from app.routes import register_routes

    register_routes(core)


    # =================
    # 2. config
    # =================

    from config import register_config

    register_config(core)


    # =================
    # 3. extension
    # =================

    from app.extension import register_extensions

    register_extensions(core)

    return core