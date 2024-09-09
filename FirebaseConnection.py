SYSTEM_PROMPT = {
    "role": "system",
    "content": "You are an annoyed student at Ben Gurion University. I want you to generate complaints on the student organization as if it’s written from your point of view on the facebook platform."
               "Use casual language and include specific details relevant to the issue. Express emotions like frustration or disappointment if appropriate "
               "dont use hashtags and emphasize that the student organization isn't doing enough for the reservists. never change the subject of the conversation"

}


def creating_new_user_and_chat(user_uuid: str, db):
    users_ref = db.collection('users').document(user_uuid)
    chat_history = []
    chat_history.append(SYSTEM_PROMPT)
    users_ref.set({
        'chat': chat_history
    })


def uuid_exist_in_firebase(user_uuid: str, db):
    doc_ref = db.collection('users').document(user_uuid)
    doc = doc_ref.get()
    return doc.exists


def get_chat(user_uuid: str, db):
    doc_ref = db.collection('users').document(user_uuid)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict().get('chat')


def update_chat(user_uuid: str, new_message: dict, db):
    doc_ref = db.collection('users').document(user_uuid)
    doc = doc_ref.get()
    if doc.exists:
        chat = doc.to_dict().get('chat')
        chat.append(new_message)
        doc_ref.update({'chat': chat})
