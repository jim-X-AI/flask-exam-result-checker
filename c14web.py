from flask import Flask, request
import socket
import pandas as pd

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

my_app = Flask(__name__)

@my_app.route('/examresult')
def examresult():
    value1 = request.args.get('course')
    value1 = value1.lower()
    value2 = request.args.get('matricno')
    value2 = int(value2)
    df1 = pd.read_csv("studentsregister.csv")
    df2 = pd.read_csv("examscores.csv")

    df10 = df1[df1['matricno']==value2]
    df10 = df10.reset_index()
    print(df10)
    nameofstudent = df10['name'][0]

    df20 = df2[df2['matricno']==value2]
    df30 = df20[df20['course']==value1]
    df30 = df30.reset_index()
    print(df30)
    thescore = df30['score'][0]

    if thescore > 50:
        remark = 'The student is promoted'
    else:
        remark = 'Please go back and pay school fees. You still have a long way to go'
    
    return(f'The result in {value1} for {nameofstudent} ({value2}) is {thescore}. {remark}')

if __name__=="__main__":
    my_app.run(host="0.0.0.0", port=80)

