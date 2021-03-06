from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms import IntegerField
from wtforms import SelectField
from wtforms import StringField
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import NumberRange


class QuestionForm(FlaskForm):
    question = TextAreaField("Question",
                             validators=[DataRequired(),
                                         Length(min=2)])
    mark = IntegerField(
        "Mark",
        validators=[
            DataRequired(),
            NumberRange(1, 101, "Not in a valid mark range")
        ],
    )
    difficulty = SelectField(
        "Difficulty Level",
        choices=[("Easy", "Easy"), ("Medium", "Medium"), ("Hard", "Hard")],
    )
    cognitive_level = SelectField(
        "Cognitive Level",
        choices=[
            ("Application", "Application"),
            ("Comprehension", "Comprehension"),
            ("Knowledge", "Knowledge"),
        ],
    )
    imp = BooleanField("Mark As IMP")
    submit = SubmitField("submit")


class MCQQuestionForm(QuestionForm):
    option1 = StringField("Option1", validators=[DataRequired()])
    option2 = StringField("Option2", validators=[DataRequired()])
    option3 = StringField("Option3", validators=[DataRequired()])
    option4 = StringField("Option4", validators=[DataRequired()])
