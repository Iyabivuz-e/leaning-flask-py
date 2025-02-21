# Imports
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# My App
app = Flask(__name__)

Scss(app)

# database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///smash_tasks.db"
db = SQLAlchemy(app)

# Creating a class model for our database


class SmashTaskModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer, default=0)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow)

    # A function to print an object
    def __repr__(self) -> str:
        return f"Task {self.id}"


# The main page and routes
@app.route("/", methods=["POST", "GET"])
def index():
    # Add tasks
    if request.method == "POST":
        # capturing what the user is typing
        current_task = request.form["content"]
        print(f"{current_task}")
        # we update the content in our database
        new_task = SmashTaskModel(content=current_task)
        print(f"{new_task}")
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exemption as e:
            print(f"Error: {e}")
            return f"Error: {e}"

    # See all taks
    else:
        tasks = SmashTaskModel.query.order_by(SmashTaskModel.createdAt).all()
        print(f"My tasks {tasks}")
        return render_template("index.html", tasks=tasks)

# Deleting a task from our database
@app.route("/delete/<int:id>")
def delete_tasks(id:int):
    delete_task = SmashTaskModel.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"Error {e}"


if __name__ in "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
