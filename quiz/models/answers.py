from ..extensions import db
from enum import Enum


class Answer_enum(Enum):
    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'
    E = 'e'


class Answer(db.Model):
    # This is the model for the answers table
    __tablename__ = "answers"
    # This is the primary key for the answers table
    id = db.Column(db.Integer, primary_key=True)
    # This is the answer column for the answers table
    answer = db.Column(db.Enum(Answer_enum))
    # This is the is_correct column for the answers table
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"),
                            nullable=False, unique=True)

    # This is the representation of the answers table
    def __repr__(self):
        # This returns the answer
        return f"{self.answer}"
