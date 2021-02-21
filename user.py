from flask import request
from flask_restx import Resource, Api, Namespace, fields
import pymysql

User = Namespace(
    name="User",
    description="User 리스트를 작성하기 위해 사용하는 API.",
)

user_fields = User.model('User', {  # Model 객체 생성
    'data': fields.String(description='a User', required=True, example="test user")
})

user_fields_with_id = User.inherit('User With ID and all', user_fields, {
    'user_id': fields.Integer(description='a User ID'),
    'user_email': fields.Integer(description='a User email'),
    'user_name': fields.Integer(description='a User name'),
    'user_password': fields.Integer(description='a User password'),
    'user_hp': fields.Integer(description='a User handphone number'),
    'user_nickname': fields.Integer(description='a User nickname')
})

@User.route('')
class UserPost(Resource):
    @User.expect(user_fields_with_id)
    # @User.response(201, 'Success', user_fields_with_id)
    def post(self):
        """User 리스트에 사용자를 새로 등록 합니다."""

        # 요청에서 인자받아오기
        user_id = request.json.get('user_id')
        user_email = request.json.get('user_email')
        user_name = request.json.get('user_name')
        user_password = request.json.get('user_password')
        user_hp = request.json.get('user_hp')
        user_nickname = request.json.get('user_nickname')

        data = (
            user_id,
            user_email,
            user_name,
            user_password,
            user_hp,
            user_nickname
        )

        #db에 아이디 추가하기
        db = pymysql.connect(
        host='127.0.0.1', 
        port=3306, 
        user='root', 
        passwd='123123', 
        db='ast', 
        charset='utf8'
        )
        cursor = db.cursor()
        sql = '''
            Insert into users (user_id, user_email, user_name, user_password, user_hp, user_nickname, leave_flag)
            values (%s, %s, %s, %s, %s, %s, 'N'); '''
        cursor.execute(sql,data)
        db.commit()
        db.close()
        
        return data[0]

# @User.route('/<int:user_id>')
# @User.doc(params={'user_id': 'An ID'})
# Class User
# class TodoSimple(Resource):
#     @Todo.response(200, 'Success', todo_fields_with_id)
#     @Todo.response(500, 'Failed')
#     def get(self, todo_id):
#         """Todo 리스트에 todo_id와 일치하는 ID를 가진 할 일을 가져옵니다."""
#         return {
#             'todo_id': todo_id,
#             'data': todos[todo_id]
#         }
    
#     @Todo.response(202, 'Success', todo_fields_with_id)
#     @Todo.response(500, 'Failed')
#     def put(self, todo_id):
#         """Todo 리스트에 todo_id와 일치하는 ID를 가진 할 일을 수정합니다."""
#         todos[todo_id] = request.json.get('data')
#         return {
#             'todo_id': todo_id,
#             'data': todos[todo_id]
#         }, 202
    
#     @Todo.doc(responses={202: 'Success'})
#     @Todo.doc(responses={500: 'Failed'})
#     def delete(self, todo_id):
#         """Todo 리스트에 todo_id와 일치하는 ID를 가진 할 일을 삭제합니다."""
#         del todos[todo_id]
#         return {
#             "delete" : "success"
#         }, 202