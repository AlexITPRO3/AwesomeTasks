from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Sample data for tasks
tasks = [
    {
        'id': 1,
        'title': 'Complete project proposal',
        'description': 'Write a detailed proposal for the new project',
        'status': 'Pending'
    },
    {
        'id': 2,
        'title': 'Update website content',
        'description': 'Add new blog posts and update product information',
        'status': 'In Progress'
    },
    {
        'id': 3,
        'title': 'Prepare presentation slides',
        'description': 'Create a presentation for the upcoming conference',
        'status': 'Completed'
    }
]

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/task/<int:task_id>')
def view_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    return render_template('task.html', task=task)

@app.route('/task/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_task = {
            'id': len(tasks) + 1,
            'title': request.form['title'],
            'description': request.form['description'],
            'status': 'Pending'
        }
        tasks.append(new_task)
        return redirect('/')
    return render_template('add_task.html')

if __name__ == '__main__':
    app.run(debug=True)
