import os
from flask import Flask, request, render_template, make_response
import uuid
import dotenv
import init
import FirebaseConnection



dotenv.load_dotenv()
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.secret_key = os.urandom(24)
db, groq_client = init.init()


@app.route('/')
def home():
    user_uuid = request.cookies.get('user_uuid')
    if user_uuid and FirebaseConnection.uuid_exist_in_firebase(user_uuid, db):
        print(f"Welcome back! Your user ID is {user_uuid}")
        resp = make_response(render_template('index.html'))
    else:
        new_uuid = str(uuid.uuid4())
        FirebaseConnection.creating_new_user_and_chat(new_uuid, db)
        resp = make_response(render_template('index.html'))
        resp.set_cookie('user_uuid', new_uuid, max_age=60 * 60 * 24 * 7)

    return resp


# Function to generate a complaint using OpenAI's API
def generate_complaint(query: str):
    user_uuid = request.cookies.get('user_uuid', 'Cookie not found')
    chat = FirebaseConnection.get_chat(user_uuid, db)
    chat.append({"role": "user", "content": query})
    response = groq_client.chat.completions.create(
        messages=chat,
        model="gemma2-9b-it",
    )
    FirebaseConnection.update_chat(user_uuid, {"role": "user", "content": query}, db)
    FirebaseConnection.update_chat(user_uuid, {"role": "assistant", "content": response.choices[0].message.content}, db)
    return response.choices[0].message.content


@app.route('/get_complaint', methods=['POST'])
def get_complaint():
    query = request.form.get('complaint', '')
    complaint = generate_complaint(query)
    return render_template('index.html', complaint=complaint)



if __name__ == '__main__':
    app.run(port=5000,debug=True,host='0.0.0.0')








