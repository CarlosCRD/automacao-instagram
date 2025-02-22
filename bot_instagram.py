import os
import time
import pandas as pd
from instabot import Bot
from PIL import Image
from datetime import datetime
from pathlib import Path  # Importação corrigida

def redimensionar_imagem(caminho, saida_dir='processed'):
    img = Image.open(caminho).convert("RGB")  # Garantir que a imagem esteja em RGB
    largura, altura = img.size
    
    # Ajustar proporção (4:5 recomendado para Instagram)
    nova_altura = int(largura * 1.25)
    if altura < nova_altura:
        nova_altura = altura  # Não cortar se a imagem já estiver ajustada
    
    img = img.crop((0, 0, largura, nova_altura))
    img.thumbnail((1080, 1350))  # Ajuste para tamanho máximo permitido
    
    # Criar diretório de saída se não existir
    Path(saida_dir).mkdir(exist_ok=True)
    
    # Novo caminho com extensão .jpg
    novo_caminho = Path(saida_dir) / f"ig_{Path(caminho).stem}.jpg"
    img.save(novo_caminho, format="JPEG", quality=95)
    
    return novo_caminho

def postar_no_instagram(usuario, senha, arquivo_csv='posts.csv'):
    bot = Bot()

    try:
        # Verificar se o arquivo existe
        if not os.path.exists(arquivo_csv):
            raise FileNotFoundError(f"Arquivo '{arquivo_csv}' não encontrado.")

        # Login seguro
        if not bot.login(username=usuario, password=senha, use_cookie=False):
            raise Exception("Falha no login - verifique credenciais/2FA")

        # Ler agenda de posts
        df = pd.read_csv(arquivo_csv, parse_dates=['data_postagem'])
        df = df[df['data_postagem'] <= datetime.now()]  # Filtrar posts pendentes

        linhas_para_excluir = []

        for i, row in df.iterrows():
            try:
                print(f"\nProcessando: {row['imagem']}")

                # Processar imagem
                img_path = redimensionar_imagem(row['imagem'])
                caption = f"{row['legenda']}\n\n{row['hashtags']}"

                # Upload e postagem
                if bot.upload_photo(str(img_path), caption=caption):
                    print(f"Postado: {row['imagem']}")
                    linhas_para_excluir.append(i)  # Adicionar índice para remoção
                else:
                    print(f"Erro ao postar: {bot.get_last_response()}")

                time.sleep(30)  # Evitar bloqueio

            except Exception as e:
                print(f"Erro no post: {str(e)}")
                continue

        # Remover linhas processadas sem modificar o DataFrame durante a iteração
        df.drop(linhas_para_excluir, inplace=True)

        # Salvar CSV atualizado
        df.to_csv(arquivo_csv, index=False)

    finally:
        bot.logout()

if __name__ == "__main__":
    # Configurações (substitua com seus dados)
    USERNAME = "seu_usuario"
    PASSWORD = "sua_senha_segura"
    CSV_FILE = "posts_instagram.csv"

    # Executar
    try:
        postar_no_instagram(USERNAME, PASSWORD, CSV_FILE)
        print("\nPostagem concluída!")
    except Exception as e:
        print(f"\nErro crítico: {str(e)}")
