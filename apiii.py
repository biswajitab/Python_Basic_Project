# from flask import Flask,jsonify
# app = Flask(__name__)
#
# @app.route('/')
# def biswajit():
#     return 'hello,world das'
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, jsonify, request


# Sample data to mimic a database
students = [
    {
        'id': 1,
        'name': 'Santhosh',
        'email': 'santhosh@gmail.com',
        'phone': '7411694426',
        'createdat': '',
        'updatedat': '',
        'course': 'React'
    },
    {
        'id': 2,
        'name': 'Gayathri',
        'email': 'gayathri@gmail.com',
        'phone': '7826373688',
        'createdat': '',
        'updatedat': '',
        'course': 'Python'
    },
    {
        'id': 3,
        'name': 'Pallavi',
        'email': 'pallavi@gmail.com',
        'phone': '5237388390',
        'createdat': '',
        'updatedat': '',
        'course': 'Frontend'
    },
    {
        'id': 4,
        'name': 'Salina',
        'email': 'salina@gmail.com',
        'phone': '9374746447',
        'createdat': '',
        'updatedat': '',
        'course': 'Frontend'
    }
]

kkk = Flask(__name__)
# Get all students
@kkk.route('/studentss', methods=['GET'])
def get_students():
    return jsonify({'status': 200,"name":"biswajit", 'students': students})

# Get a specific student by ID
# @kkk.route('/studentss/<int:id>', methods=['GET'])
# def get_student(id):
#     for student in students:
#         if student['id'] == id:
#             return jsonify({'status': 200, 'student': student})
#     # Only return 404 after checking all students
#     return jsonify({'status': 404, 'message': 'Student not found'}), 404



@kkk.route('/studentss/<int:id>', methods=['GET'])
def get_student(id):
    for student in students:
        if student['id'] == id:
            return jsonify({'status': 200, 'student': student})
    return jsonify({'status':404,'message':'the api is not working'})


    # for student in student

# Create a new student
@kkk.route('/studentss', methods=['POST'])
def create_student():
    new_student = request.get_json()
    new_student['id'] = len(students) + 1  # Auto-increment ID
    students.append(new_student)
    return jsonify({'status': 201, 'message': 'Student created', 'student': new_student}), 201


# @kkk.route('/studentss', methods=['POST'])
# def create_student():
#     new_student = request.get_json()
#
#     # Check for required fields (name, email, phone, course)
#     required_fields = ['name', 'email', 'phone', 'course']
#     if not all(field in new_student for field in required_fields):
#         return jsonify({'status': 400, 'message': 'Missing required fields'}), 400
#
#     # Set ID for the new student
#     new_student['id'] = students[-1]['id'] + 1 if students else 1  # Auto-increment ID
#     new_student['createdat'] = new_student.get('createdat', '')
#     new_student['updatedat'] = new_student.get('updatedat', '')

    # Add the new student to the list
    students.append(new_student)

    return jsonify({'status': 201, 'message': 'Student created', 'student': new_student}), 201


# Update an existing student by ID
# @app.route('/students/<int:id>', methods=['PUT'])
# def update_student(id):
#     student = next((s for s in students if s['id'] == id), None)
#     if student:
#         data = request.get_json()
#         student.update(data)  # Update student data
#         return jsonify({'status': 200, 'message': 'Student updated', 'student': student})
#     else:
#         return jsonify({'status': 404, 'message': 'Student not found'}), 404

# # Delete a student by ID
# @app.route('/students/<int:id>', methods=['DELETE'])
# def delete_student(id):
#     global students
#     students = [s for s in students if s['id'] != id]
#     return jsonify({'status': 200, 'message': 'Student deleted'})

if __name__ == '__main__':
    kkk.run(debug=True)
