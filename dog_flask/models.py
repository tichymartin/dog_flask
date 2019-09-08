from datetime import datetime

from dog_flask.extensions import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(50))
    main_img = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.id}, {self.title}, {self.subtitle}, {self.author}, {self.content}"
