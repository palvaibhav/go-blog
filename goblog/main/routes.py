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


@main.route("/upvote/<int:post_id>")
@login_required
def upvote(post_id):
    post = Post.query.filter_by(id=post_id).first()
    current_user.upvote_post(post)
    return redirect(url_for("main.home"))


@main.route("/downvote/<int:post_id>")
@login_required
def downvote(post_id):
    post = Post.query.filter_by(id=post_id).first()
    current_user.downvote_post(post)
    return redirect(url_for("main.home"))

