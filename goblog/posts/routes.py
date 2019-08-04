from flask import Blueprint

posts = Blueprint('posts', __name__)

@posts.route('/post/new')
def new_post():
    return "This page will be for making a new post"


@posts.route('/post/<int:post_id>')
def post(post_id):
    return "This page will be for viewing a particular post in detail"


@posts.route('/post/<int:post_id>/update')
def update_post(post_id):
    return "This page will be for updating a post"


@posts.route('/post/<int:post_id>/delete')
def delete_post(post_id):
    return "This page will be for deleting a post"
