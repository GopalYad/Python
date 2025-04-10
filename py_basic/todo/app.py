from flask import Flask,jsonify,request,render_template

app=Flask(__name__)

tasks=[]

#function to find a task by id
def find_task(task_id):
    return next((task for task in tasks if task['id']==task_id),None)

@app.route('/')
def home():
    return render_template('index.html')

#add a new task
@app.route('/api/tasks',methods=['POST'])
def addTask():
    data=request.get_json()
    task={
        'id':len(tasks)+1,
        'title':data.get('title'),
        'description':data.get('description'),
        'completed':False
    }
    
    tasks.append(task)
    return jsonify(task),201

if __name__ == '__main__':
    app.run(debug=True)