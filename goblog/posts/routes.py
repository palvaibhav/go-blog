from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from goblog import db
from goblog.models import Post, Comment
from goblog.posts.forms import PostForm, CommentForm

posts = Blueprint("posts", __name__)


@posts.route("/post/new", methods=["GET", "POST"])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(
            title=form.title.data, content=form.content.data, author=current_user
        )
        db.session.add(post)
        db.session.commit()
        flash("Your Post has been created!", "success")
        return redirect(url_for("main.home"))
    return render_template(
        "create_post.html", title="New Post", form=form, legend="New Post"
    )


@posts.route("/post/<int:post_id>", methods=["GET", "POST"])
def post(post_id):
    form = CommentForm()
    if form.validate_on_submit():
        newComment = Comment(
            body=form.comment_body.data, user_id=current_user.id, post_id=post_id
        )
        db.session.add(newComment)
        db.session.commit()
        return redirect(url_for("posts.post", post_id=post_id))
    post = Post.query.get_or_404(post_id)
    comments = post.comments
    count_of_comments = Comment.query.filter_by(post_id=post_id).count()
    return render_template(
        "post.html",
        title=post.title,
        post=post,
        form=form,
        comments=comments,
        count_of_comments=count_of_comments,
    )


@posts.route("/post/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash("Your post has been updated!", "success")
        return redirect(url_for("posts.post", post_id=post.id))
    elif request.method == "GET":
        form.title.data = post.title
        form.content.data = post.content
    return render_template(
        "create_post.html", title="Update Post", form=form, legend="Update Post"
    )


@posts.route("/post/<int:post_id>/delete", methods=["POST"])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash("Your post has been deleted!", "success")
    return redirect(url_for("main.home"))


@posts.route("/upvote/<int:post_id>")
@login_required
def upvote(post_id):
    post = Post.query.filter_by(id=post_id).first()
    current_user.upvote_post(post)
    print(request.form)
    return redirect(url_for("main.home"))


@posts.route("/downvote/<int:post_id>")
@login_required
def downvote(post_id):
    post = Post.query.filter_by(id=post_id).first()
    current_user.downvote_post(post)
    return redirect(url_for("main.home"))

