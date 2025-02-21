import flask from Flask
import flask_sqlalchemy from SQLAlchemy
import flask_cors from CORS

app = Flask(__name__)
CORS(app)

# Configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///mycrud.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

