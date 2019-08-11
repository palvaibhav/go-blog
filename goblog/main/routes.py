from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import login_required, current_user
from goblog.models import Post, PostUpvote

main = Blueprint("main", __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)

