# ---- NEW USAGE FOR LIST SLICES ----
usernames = [user['key'] for user in users]
names = [user['name'] for user in users]
hashed_passwords = [user['password'] for user in users]