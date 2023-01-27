from ..extensions import db


class Answer(db.Model):
    # This is the model for the answers table
    __tablename__ = "answers"
    # This is the primary key for the answers table
    id = db.Column(db.Integer, primary_key=True)
    # This is the answer column for the answers table
    answer = db.Column(db.String(10), nullable=False)
    # This is the is_correct column for the answers table
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)

    # This is the representation of the answers table
    def __repr__(self):
        # This returns the answer
        return f"{self.answer}"
