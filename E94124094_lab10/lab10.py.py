#coding=utf-8
# 不加上就無法使用中文註解
import random

from flask import *
app = Flask(__name__)


@app.route("/")
def root():

    return render_template('lab10.html')


@app.route('/student_data',methods = ['POST'])
def index():
    name = request.form['name']
    id = request.form['id']
    print(f'name : {name}\nstudent_id : {id}')
    return 'ok'

@app.route('/rsp',methods = ['GET'])
def jotao():
    gado = request.args.get('choice',default= "error")#r石頭 s剪刀 p布
    enemy = random.randint(1,3)#1是石頭 2是剪刀 3是布
    if enemy == 1:
        enemy = 'r'
    elif enemy == 2:
        enemy = 's'
    elif enemy == 3:
        enemy = 'p'
    if gado == 'r':
        if enemy == 'r':
            print(f'computer : {enemy} user : {gado}')
            return 'It is Tie'
        elif enemy == 's':
            print(f'computer : {enemy} user : {gado}')
            return 'You win!'        
        elif enemy == 'p' :
            print(f'computer : {enemy} user : {gado}')
            return 'You lose!'   
    elif gado == 's':
        if enemy == 'r':
            print(f'computer : {enemy} user : {gado}')
            return 'You lose!' 
        elif enemy == 's':
            print(f'computer : {enemy} user : {gado}')
            return 'It is Tie'        
        elif enemy == 'p':
            print(f'computer : {enemy} user : {gado}')
            return 'You win!'
    elif gado == 'p':
        if enemy == 'r':
            print(f'computer : {enemy} user : {gado}')
            return 'You win!'
        elif enemy == 's':
            print(f'computer : {enemy} user : {gado}')
            return 'You lose!'         
        elif enemy == 'p':
            print(f'computer : {enemy} user : {gado}')
            return 'It is Tie'
    else :
        return  " Wrong input ! try again "
app.run(host="0.0.0.0", port=3000, debug=True)