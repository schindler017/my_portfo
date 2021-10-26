from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_in_file(data):
    with open('database.txt', mode='a') as save:
        user_email = data['email']
        user_subject = data['subject']
        user_message = data['message']
        save.write(f'Email: {user_email}, Subject: {user_subject}, Message: {user_message}\n')

def write_in_csv(data):
    with open('database.csv', mode='a', newline='') as save2:
        user_email = data['email']
        user_subject = data['subject']
        user_message = data['message']
        csv_write = csv.writer(save2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL )
        csv_write.writerow([user_email, user_subject, user_message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_in_csv(data)
            return redirect('thankyou.html')
        except:
            return 'Failed to save the form to in the database!'
    else:
        return 'Something went wrong! Go check it out'
