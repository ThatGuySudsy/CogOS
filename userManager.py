from pathlib import Path
import shutil as sh

USERS_PATH = Path("Files/Users")
DEFAULT_USER_PATH = Path("Files/Default")

#return codes:
# 0: Logged in
# 1: Account created
# 2: Password wrong

def login(username, password):
    user_path = USERS_PATH / username
    if user_path.exists():
        if password == (user_path / "data" / "password.txt").read_text().strip():
            return 0
        return 2
    sh.copytree(DEFAULT_USER_PATH, user_path)
    password_file = user_path / "data" / "password.txt"
    password_file.write_text(password)
    return 1