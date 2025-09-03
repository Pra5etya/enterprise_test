def register_routes(app):
    from .app_route import app_bp
    from .user_route import user_bp
    from .transaction_route import tx_bp
    from .graph_route import graph_bp
    from .search_route import search_bp

    # 
    app.register_blueprint(app_bp)      # App Routes
    app.register_blueprint(user_bp)     # User Routes
    app.register_blueprint(tx_bp)       # Transaction Routes
    app.register_blueprint(graph_bp)    # Graph Routes
    app.register_blueprint(search_bp)   # Search Routes