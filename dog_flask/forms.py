from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField("Titulek", validators=[DataRequired(), Length(min=5, max=50)])
    subtitle = StringField("Podtitulek")
    content = TextAreaField("Obsah")
    author = StringField("Autor")

    submit = SubmitField("Uložit")
