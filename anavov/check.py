from flask import Flask,Request
from flask_restful import Resource,Api
from json import dumps
from sqlalchemy import create_engine

e= create_engine(r"F:/anavov/anavov.db")

app=Flask(__name__)
api=Api(app)

class Department_Meta():
    def get(self):
        conn=e.connect()
        query=conn.execute("select * from first")
        return {'name':[i[0] for i in query.cursor.fetchall()]}

    api.add_resource(Department_Meta,'/department')

if __name__=='__main__':
    app.run()