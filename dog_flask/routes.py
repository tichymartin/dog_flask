from flask import Blueprint, render_template, redirect, url_for

from dog_flask.extensions import db
from dog_flask.forms import PostForm
from dog_flask.models import Post

main = Blueprint("main", __name__)


@main.route("/")
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()

    return render_template("index.html", posts=posts)


@main.route("/about")
def about():
    return render_template("about.html")


@main.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get(post_id)
    return render_template("post.html", post=post)


@main.route("/contact")
def contact():
    return render_template("contact.html")


@main.route("/add_post", methods=["GET", "POST"])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, subtitle=form.subtitle.data, content=form.content.data,
                        author=form.author.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("add_post.html", form=form)
