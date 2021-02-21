from flask import request
from flask_restx import Resource, Api, Namespace, fields
import dbconnect

todos = {}
count = 1

Users = Namespace(
    name="Users",
    description="Users 리스트를 작성하기 위해 사용하는 API.",
)


@Users.route('')
class TodoPost(Resource):
    @Users.response(201, 'Success')
    def get(self):
        """Users 리스트를 출력합니다"""
        db = dbconnect.db_con()
        cursor = db.cursor()
        sql = '''SELECT * FROM ast.users;'''
        cursor.execute(sql)
        result = cursor.fetchall()
        db.close()
        return str(result)