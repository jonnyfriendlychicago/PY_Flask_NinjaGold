# the next two lines always need to be atop this server.py file 
from collections import UserList
from flask import Flask, render_template, request, redirect, session # Import Flask to allow us to create our app
import random 
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'ESR4T4RWT2345tyu' 

@app.route('/')
def beHome():
    if "transactionsList" not in session:
        session['transactionsList'] = []
    
    if "StudentInfoList" not in session: 
        session['StudentInfoList'] = [
            # {'name' : 'Leo', 'age' : 17}
            # , {'name' : 'Donny', 'age' : 16 }
            # ,{'name' : 'Raph', 'age' : 18}
            # , {'name' : 'Mikey', 'age' : 17}
        ]

        # session['StudentInfoList'] = listo
        # session['StudentInfoListDos'] = listo


    return render_template("index.html")

@app.route('/processMoney', methods=['Post'])
def processMoney():
    if (request.form['which_form'] =='transType1'):
        
        delta = random.randint(10,20)
        session['transactionsList'].append(delta)
        session['sumTransactionList'] = sum(session['transactionsList'])

        
        # below is the Cameron design that works!
        a_dictionary = {'loc' : 'Farmville', 'amt' : delta}
        mylist = session['StudentInfoList']
        mylist.append(a_dictionary)
        session['StudentInfoList'] = mylist
        
        # below is the Cameron design that works!  commenting out for future ref as i now hck it up further
        # a_dictionary = {'name' : 'JonnyFriend', 'age' : 42}
        # mylist = session['StudentInfoList']
        # mylist.append(a_dictionary)
        # session['StudentInfoList'] = mylist

    # elif request.form['which_form'] =='transType2':
        # session['transactionsList'].append(40)
        # session['transactionsList2'].append(40)
        # session['sumTransactionList'] = sum(session['transactionsList'])
        # session['transactionsDetailsList'].append(2)

    elif request.form['which_form'] =='transTypeReset':
        session.clear()
        # session['transactionsList'] = []
        # session['transactionsList2'] = []
        # session['transactionsDetailsList'] = []
        # session['sumTransactionList'] = sum(session['transactionsList'])
        # session['sumTransactionList2'] = sum(session['transactionsList2'])
#
    return redirect('/displayCompletedProcessMoney') # this entire two-step redirect is only needed when you've got a results page. 

@app.route('/displayCompletedProcessMoney')
def displayProcessMoney():
    return redirect("/")


"""DON'T TOUCH BELOW :-) below always needs to be at the bottom of the script, yes!"""
# below is stuff you oughta have, per TA Cameron Smith, from Coding Dojo: 

@app.route('/', defaults={'cookies': ''})
@app.route('/<path:cookies>')
def catch_all(cookies):
    return 'Sorry! No response here. Try url again.'

# below is flask boiler plate; exclude it and stuff won't work    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

