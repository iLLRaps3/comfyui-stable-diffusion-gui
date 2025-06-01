import hashlib
import uuid

# In-memory storage for demo purposes
users = {}
sessions = {}
contents = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_creator(full_name, email, password):
    if email in users:
        raise ValueError("User already exists")
    user_id = str(uuid.uuid4())
    users[email] = {
        "id": user_id,
        "full_name": full_name,
        "email": email,
        "password_hash": hash_password(password),
    }
    contents[user_id] = []
    return user_id

def login_creator(email, password):
    user = users.get(email)
    if not user or user["password_hash"] != hash_password(password):
        raise ValueError("Invalid credentials")
    session_token = str(uuid.uuid4())
    sessions[session_token] = user["id"]
    return session_token

def get_user_id_from_session(token):
    return sessions.get(token)

def create_content(user_id, title, content_type, content_text):
    content_id = str(uuid.uuid4())
    content_item = {
        "id": content_id,
        "title": title,
        "type": content_type,
        "text": content_text,
    }
    contents[user_id].append(content_item)
    return content_item

def list_content(user_id):
    return contents.get(user_id, [])

def edit_content(user_id, content_id, new_data):
    user_contents = contents.get(user_id, [])
    for content in user_contents:
        if content["id"] == content_id:
            content.update(new_data)
            return content
    raise ValueError("Content not found")

def delete_content(user_id, content_id):
    user_contents = contents.get(user_id, [])
    for i, content in enumerate(user_contents):
        if content["id"] == content_id:
            del user_contents[i]
            return True
    raise ValueError("Content not found")
