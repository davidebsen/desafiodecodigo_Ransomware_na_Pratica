import os
import pyaes

def decrypt_file(file_name, key):
    try:
        # Abrir o arquivo criptografado
        with open(file_name, "rb") as file:
            file_data = file.read()

        # Chave para descriptografia
        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        # Remover o arquivo criptografado
        os.remove(file_name)

        # Criar o arquivo descriptografado
        decrypted_file_name = file_name.replace(".ransowaredesafiodecodigo", "")
        with open(decrypted_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"Arquivo '{file_name}' descriptografado com sucesso como '{decrypted_file_name}'.")

    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {e}")

if __name__ == "__main__":
    file_name = "desafiodio.txt.ransowaredesafiodecodigo"
    key = b"ransowarediodesafio"
    decrypt_file(file_name, key)