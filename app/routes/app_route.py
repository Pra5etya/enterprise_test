from flask import Blueprint, render_template
from config.logger import setup_logger

# 
app_bp = Blueprint('main', __name__)
logger = setup_logger()


@app_bp.route("/")
def index():
    logger.info("Memasuki halaman utama")

    return render_template("index.html")


@app_bp.route("/forbidden")
def forbidden():
    logger.warning("Akses ditolak: user tidak punya izin")
    
    return render_template("forbidden.html"), 403


@app_bp.route("/unsupported")
def unsupported():
    logger.warning("Memasuki halaman unsupported")
    
    return render_template("unsupported.html"), 406