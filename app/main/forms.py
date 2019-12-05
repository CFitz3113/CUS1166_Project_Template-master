from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, IntegerField, FloatField
from wtforms import RadioField,SelectField
from wtforms.validators import DataRequired




class TaskForm(FlaskForm):
    task_desc = StringField('task_desc', validators=[DataRequired()])
    task_status_completed = SelectField('Status', choices=[('todo','Todo'),('doing','Doing'),('done','Done')])
    task_date = ""
    task_customer = StringField('task_customer', validators =[DataRequired()])
    task_location = StringField('task_location', validators =[DataRequired()])
    submit = SubmitField('submit')
