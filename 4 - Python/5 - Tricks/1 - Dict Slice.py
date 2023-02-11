# ---- DICT SLICE ----
users_dict = { 
    'usernames': { 
        user['key']: { 'name': user['name'], 'password': user['password'] } for user in users 
    } 
}