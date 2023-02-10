from ..extensions import db


# This is the model for the is_answered table
class Is_answered(db.Model):
    # This is the table name for the is_answered table
    __tablename__ = "is_answered"
    # This is the primary key for the is_answered table
    id = db.Column(db.Integer, primary_key=True)
    # This is the user_id column for the is_answered table
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    # This is the relationship between the is_answered table and the questions table
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"), nullable=False)

    # This is the representation of the is_answered table
    def __repr__(self):
        # This returns the user_id
        return {"user_id": self.user_id}
