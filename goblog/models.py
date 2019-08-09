from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from goblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship("Post", backref="author", lazy=True)

    def upvote_post(self, post):
        if not self.has_upvoted_post(post):
            upvote = PostUpvote(user_id=self.id, post_id=post.id)
            db.session.add(upvote)
            post.upvotes_count = post.upvotes_count + 1
            if self.has_downvoted_post(post):
                downvote = PostDownvote.get_post_downvote(
                    user_id=self.id, post_id=post.id
                )
                db.session.delete(downvote)
            db.session.commit()

    def has_upvoted_post(self, post):
        return PostUpvote.query.filter_by(user_id=self.id, post_id=post.id).count() > 0

    def downvote_post(self, post):
        if not self.has_downvoted_post(post):
            downvote = PostDownvote(user_id=self.id, post_id=post.id)
            db.session.add(downvote)
            post.upvotes_count = post.upvotes_count - 1
            if self.has_upvoted_post(post):
                upvote = PostUpvote.get_post_upvote(user_id=self.id, post_id=post.id)
                db.session.delete(upvote)
            db.session.commit()

    def has_downvoted_post(self, post):
        return (
            PostDownvote.query.filter_by(user_id=self.id, post_id=post.id).count() > 0
        )

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config["SECRET_KEY"], expires_sec)
        return s.dumps({"user_id": self.id}).decode("utf-8")

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token)["user_id"]
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    upvotes_count = db.Column(db.Integer, nullable=False, default=0)
    upvotes = db.relationship("PostUpvote", backref="post", lazy=True)
    downvotes = db.relationship("PostDownvote", backref="post", lazy=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class PostUpvote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    @staticmethod
    def get_post_upvote(user_id, post_id):
        return PostUpvote.query.filter_by(user_id=user_id, post_id=post_id).first()

    def __repr__(self):
        return f"Post_id('{self.post_id}') User_id('{self.user_id}')"


class PostDownvote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    @staticmethod
    def get_post_downvote(user_id, post_id):
        return PostDownvote.query.filter_by(user_id=user_id, post_id=post_id).first()

    def __repr__(self):
        return f"Post_id('{self.post_id}') User_id('{self.user_id}')"
