from ..extensions import db


# This is the model for the options table
class Options(db.Model):
    # This is the table name for the options table
    __tablename__ = "options"
    # This is the primary key for the options table
    id = db.Column(db.Integer, primary_key=True)
    # This is the first option column for the options table
    a = db.Column(db.Text, nullable=False)
    # This is the second option column for the options table
    b = db.Column(db.Text, nullable=False)
    # This is the third option column for the options table
    c = db.Column(db.Text, nullable=False)
    # This is the fourth option column for the options table
    d = db.Column(db.Text, nullable=False)
    # This is the fifth option column for the options table
    e = db.Column(db.Text, nullable=False)
    # This is the relationship between the options table and the questions table
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)

    # This is the representation of the options table
    def __repr__(self):
        # This returns the option
        return f"{self.question_id}"
