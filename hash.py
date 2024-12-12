from werkzeug.security import generate_password_hash

# Gera o hash da senha
hashed_password = generate_password_hash('senha')

print(hashed_password)  # Saída: uma string longa com o hash
