from datetime import datetime
from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = 'f591403d35539b3579144c08c938df0d'
db = SQLAlchemy(app)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    subtitle = db.Column(db.String(50))
    content = db.Column(db.Text)
    author = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.id}, {self.title}, {self.subtitle}, {self.author}, {self.content}"


class PostForm(FlaskForm):
    title = StringField("Titulek", validators=[DataRequired(), Length(min=5, max=50)])
    subtitle = StringField("Podtitulek")
    # content = TextAreaField("Obsah", validators=[DataRequired()])
    content = TextAreaField("Obsah")
    author = StringField("Autor")
    submit = SubmitField("Uložit")


@app.route("/")
def index():
    posts = Post.query.order_by(Post.date_posted.desc()).all()

    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get(post_id)
    return render_template("post.html", post=post)


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/add_post", methods=["GET", "POST"])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        new_post = Post(title=form.title.data, subtitle=form.subtitle.data, content=form.content.data,
                        author=form.author.data)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("add_post.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)
