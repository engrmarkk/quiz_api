from ..extensions import db


# This is the model for the questions table
class Question(db.Model):
    # This is the table name for the questions table
    __tablename__ = "questions"
    # This is the primary key for the questions table
    id = db.Column(db.Integer, primary_key=True)
    # This is the question column for the questions table
    question = db.Column(db.Text, nullable=False)
    # This is the relationship between the questions table and the options table
    options = db.relationship(
        "Options", backref="question", lazy=True, foreign_keys="Options.question_id"
    )
    # This is the relationship between the questions table and the answers table
    answer = db.relationship(
        "Answer", backref="q_to_ans", lazy=True, foreign_keys="Answer.question_id"
    )

    # This is the representation of the questions table
    def __repr__(self):
        # This returns the question
        return f"{self.question}"