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
        "Options", backref="question", lazy=True, cascade="all, delete", foreign_keys="Options.question_id"
    )
    # This is the relationship between the questions table and the answers table
    answer = db.relationship(
        "Answer", backref="q_to_ans", lazy=True, cascade="all, delete", foreign_keys="Answer.question_id"
    )
    # This is the relationship between the questions table and the is_answered table
    is_answer = db.relationship(
        "Is_answered", backref="q_answered", lazy=True,
        cascade="all, delete", foreign_keys="Is_answered.question_id"
    )

    # This is the representation of the questions table
    def __repr__(self):
        # This returns the question
        return f"{self.question}"

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get_or_404(id)

    def save(self):
        db.session.add(self)
        db.session.commit()
