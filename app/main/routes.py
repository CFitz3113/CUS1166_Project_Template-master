from flask import render_template,  redirect, url_for
from app.main import bp
from app import db
from app.main.forms import TaskForm
from app.models import Task


# Main route of the applicaitons.
@bp.route('/', methods=['GET','POST'])
def index():
    return render_template("main/index.html")


#
#  Route for viewing and adding new tasks.
@bp.route('/todolist', methods=['GET','POST'])
def todolist():
    form = TaskForm()

    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.
        new_task = Task()
        new_task.task_desc =  form.task_desc.data
        new_task.task_status = form.task_status_completed.data
        new_task.task_start = form.task_start.data
        new_task.task_end = form.task_start.data
        new_task.task_customer = form.task_customer.data
        new_task.task_location = form.task_location.data
        db.session.add(new_task)
        db.session.commit()

        # Redirect to this handler - but without form submitted - gets a clear form.
        return redirect(url_for('main.todolist'))

    todo_list = db.session.query(Task).all()

    return render_template("main/todolist.html",todo_list = todo_list,form= form)


#
# Route for removing a task
@bp.route('/todolist/remove/<int:task_id>', methods=['GET','POST'])
def remove_task(task_id):

    # Query database, remove items
    Task.query.filter(Task.task_id == task_id).delete()
    db.session.commit()

    return redirect(url_for('main.todolist'))


#
# Route for editing a task

@bp.route('/todolist/edit/<int:task_id>', methods=['GET','POST'])
def edit_task(task_id):
    form = TaskForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        # Get the data from the form, and add it to the database.

        current_task = Task.query.filter_by(task_id=task_id).first_or_404()
        current_task.task_desc =  form.task_desc.data
        current_task.task_status = form.task_status_completed.data
        current_task.task_start = form.task_start.data
        current_task.task_end = form.task_start.data
        current_task.task_customer = form.task_customer.data
        current_task.task_location = form.task_location.data

        db.session.add(current_task)
        db.session.commit()
        # After editing, redirect to the view page.
        return redirect(url_for('main.todolist'))

    # get task for the database.
    current_task = Task.query.filter_by(task_id=task_id).first_or_404()

    # update the form model in order to populate the html form.
    form.task_desc.data =     current_task.task_desc
    form.task_status_completed.data = current_task.task_status

    return render_template("main/todolist_edit_view.html",form=form, task_id = task_id)

#route sorting tasks
@bp.route('/todolist/<int:sort>/', methods=['GET','POST'])
def sort_task(sort):
    form = TaskForm()
    if TaskForm.is_submitted():
        if sort == 1:
            task = Task.query.order_by(Task.task_status)
        elif sort == 2:
            task = Task.query.order_by(Task.task_start)
        elif sort == 3:
            task = Task.query.order_by(Task.task_end)
        elif sort == 4:
            task = Task.query.order_by(Task.task_customer)

