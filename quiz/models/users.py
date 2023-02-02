from ..extensions import db


# This is the model for the users table
class Users(db.Model):
    # This is the table name for the users table
    __tablename__ = "users"
    # This is the primary key for the users table
    id = db.Column(db.Integer, primary_key=True)
    # This is the first_name column for the users table
    first_name = db.Column(db.String(50), nullable=False)
    # This is the last_name column for the users table
    last_name = db.Column(db.String(50), nullable=False)
    # This is the email column for the users table
    email = db.Column(db.String(100), nullable=False, unique=True)
    # This is the username column for the users table
    username = db.Column(db.String(50), nullable=False, unique=True)
    # This is the scores column for the users table
    scores = db.Column(db.Integer, nullable=False, default=0)
    # This is the taken column for the users table
    taken = db.Column(db.Boolean, nullable=False, default=False)
    # This is the password column for the users table
    password = db.Column(db.Text, nullable=False)
    # This is the is_admin column for the users table
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    # This is the representation of the users table
    def __repr__(self):
        # This returns the username
        return f"{self.username}"

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    def save(self):
        db.session.add(self)
        db.session.commit()
