from flask import Flask


def create_app():
    app = Flask(__name__)

    from goblog.users.routes import users
    from goblog.posts.routes import posts
    from goblog.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    
    return app

