import os
import json
from flask import Flask, request, render_template
from src.utils_scripts.utils import save_json_data,load_data
from src.utils_scripts.db_conn import insert,fetch,close_connection


app = Flask(__name__)

list_dict=[]
file_path = os.path.join(os.getcwd(), 'data.json')

@app.route('/', methods=['GET', 'POST'])
def user_info():
    json_data = {}
    message=" "
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        json_data = {"first_name": first_name, "last_name": last_name, "email": email}
        save_json_data(json_data,file_path)
        message="Below User Successfully Saved"
        
        #Database insertion
        my_sql="insert into my_database.user_info(first_name,last_name,email_id) values(%s,%s,%s)"
        params=[first_name,last_name,email]
        insert(my_sql,params)
        close_connection()
        
        # Retrieve user data and populate user_data variable to the same UI Page
        return render_template('index.html',user_data=json_data,message=message)
        
        
    return render_template('index.html',user_data={},message='')


@app.route("/tabular")
def tabular_data():
    my_data=load_data(file_path)
    return render_template('extract_user.html',user_list=my_data)





if __name__ == '__main__':
    app.run(debug=True)