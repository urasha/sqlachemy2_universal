from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    description = StringField('Описание', validators=[DataRequired()])
    work_size = StringField('Объём работы (часы)', validators=[DataRequired()])
    team_leader = StringField('Team leader id', validators=[DataRequired()])
    collaborators = StringField('Участники', validators=[DataRequired()])
    is_finished = BooleanField('Закончена?')
    submit = SubmitField('Применить')
