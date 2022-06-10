def get_user_code():
    with open('author.py', "r") as f:
        user_code_input = f.read()
        user_code = ""
        for line in user_code_input.split("\n"):
            line = ' '.join(line.split())
            if line:
                user_code += line + "\n"
    return user_code
