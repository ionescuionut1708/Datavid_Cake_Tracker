from flask import Flask, request, jsonify
from datetime import datetime
from models import db, Member
from marshmallow import Schema, fields, validate, ValidationError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///members.db'
db.init_app(app)

class MemberSchema(Schema):
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    birth_date = fields.Date(required=True)
    country = fields.Str(required=True)
    city = fields.Str(required=True)

    @validates('birth_date')
    def validate_birth_date(self, value):
        age = (datetime.now().date() - value).days // 365
        if age < 18:
            raise ValidationError("Member must be at least 18 years old")

member_schema = MemberSchema()

@app.route('/')
def home():
    return "Welcome to Datavid Cake Tracker!"

@app.route('/add_member', methods=['POST'])
def add_member():
    try:
        data = member_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    member = Member.query.filter_by(first_name=data['first_name'], last_name=data['last_name'], city=data['city']).first()
    if member:
        return jsonify({"error": "Member with the same name and location already exists"}), 400

    new_member = Member(**data)
    db.session.add(new_member)
    db.session.commit()

    return jsonify({"message": "Member added successfully"}), 201

@app.route('/members', methods=['GET'])
def get_members():
    members = Member.query.all()
    return jsonify(member_schema.dump(members, many=True)), 200

@app.route('/members/sorted_by_birthday', methods=['GET'])
def get_members_sorted_by_birthday():
    today = datetime.now().date()
    members = Member.query.all()
    members_sorted = sorted(members, key=lambda x: ((x.birth_date.replace(year=today.year) - today).days % 365))
    return jsonify(member_schema.dump(members_sorted, many=True)), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    