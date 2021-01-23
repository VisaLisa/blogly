import datetime
from flask_sqlalchemy import SQLAlchemy
"""Models for Blogly."""

db = SQLAlchemy()
# IMG_URL = "PLACE HOLDER FOR DEFAULT IMG URLsour"

IMG_URL = "https://semantic-ui.com/images/wireframe/image.png"

class User(db.Model):
    """Class of User"""

    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.Text,nullable=False)
    last_name = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=IMG_URL)

    posts = db.relationship("Post", backref="user", cascade="all, delete-orphan")


    @property
    def full_name(self):
        """Return user's full name"""

        return f"{self.first_name} {self.last_name}"

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    @property
    def friendly_date(self):
        """Return nicely-formatted date."""

        return self.created_at.strftime("%a %b %-d  %Y, %-I:%M %p")

class PostTag(db.Model):
    """Tags on post""" 
    __tablename__ = 'posts_tags'

    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tag.id'), primary_key=True)

class Tag(db.Model):
    """List of Tags"""

    __tablename__ = 'tags'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)

    post = db.relationship(
        'Post',
        secondary='posts_tags',
        backref='tags',
    )

def connect_db(app):
    """Connect database to app"""

    db.app = app
    db.init_app(app)