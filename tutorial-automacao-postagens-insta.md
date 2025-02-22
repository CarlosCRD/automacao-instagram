# 📸 Script: Automação de Postagens no Instagram

![Instagram Automation](https://via.placeholder.com/1200x600.png?text=Instagram+Post+Automation+by+Python)

Automatize postagens no Instagram diretamente de um arquivo CSV! Poste imagens com legendas e hashtags no horário programado.

---

## 📥 **Script**
import os
import time
import pandas as pd
from instabot import Bot
from PIL import Image
from datetime import datetime

def redimensionar_imagem(caminho, saida_dir='processed'):
    img = Image.open(caminho)
    # Mantém aspect ratio (4:5 recomendado para Instagram)
    largura, altura = img.size
    nova_altura = int(largura * 1.25)  # Proporção 4:5
    img = img.crop((0, 0, largura, min(altura, nova_altura)))
    img.thumbnail((1080, 1350))  # Tamanho máximo permitido
    
    # Salvar imagem processada
    Path(saida_dir).mkdir(exist_ok=True)
    novo_caminho = Path(saida_dir) / f"ig_{Path(caminho).name}"
    img.save(novo_caminho, quality=95)
    return novo_caminho

def postar_no_instagram(usuario, senha, arquivo_csv='posts.csv'):
    bot = Bot()
    
    try:
        # Login seguro
        if not bot.login(username=usuario, password=senha, use_cookie=False):
            raise Exception("Falha no login - verifique credenciais/2FA")

        # Ler agenda de posts
        df = pd.read_csv(arquivo_csv, parse_dates=['data_postagem'])
        df = df[df['data_postagem'] <= datetime.now()]  # Filtrar posts atrasados

        for _, row in df.iterrows():
            try:
                print(f"\nProcessando: {row['imagem']}")
                
                # Processar imagem
                img_path = redimensionar_imagem(row['imagem'])
                caption = f"{row['legenda']}\n\n{row['hashtags']}"
                
                # Upload e postagem
                if bot.upload_photo(img_path, caption=caption):
                    print(f"Postado: {row['imagem']}")
                    df.drop(index=_, inplace=True)  # Remover da fila
                else:
                    print(f"Erro ao postar: {bot.get_last_response()}")
                
                time.sleep(30)  # Evitar bloqueio

            except Exception as e:
                print(f"Erro no post: {str(e)}")
                continue

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

---

## 🔧 **Pré-requisitos**
- Python 3.8+
- Conta profissional do Instagram
- Bibliotecas:
  ```bash
  pip install instabot pandas pillow

  🗂 Estrutura de Arquivos

  automacao_instagram/
├── instagram_automation.py    # Script principal
├── posts_instagram.csv       # Agenda de posts
├── imagens/                  # Pasta com fotos para postar
└── processed/                # Pasta de imagens processadas (auto-criada)

⚙️ Configuração Passo a Passo

1. Prepare o CSV de Posts

Coluna	          Exemplo	                  Descrição
imagem	       "imagens/sunset.jpg"	     Caminho relativo da imagem
legenda	       "Pôr do sol incrível 🌅"  Legenda principal (emojis OK)
hashtags       "#natureza #viagem"	     Hashtags separadas por espaço
data_postagem  "2024-03-25 17:00"        Data/hora UTC do post

2. Edite as Credenciais

# No script instagram_automation.py:
USERNAME = "sua_conta_profissional"  # 👈 Substituir
PASSWORD = "sua_senha_segura"        # 👈 Substituir

🚀 Execução

# 1. Navegue até a pasta do projeto
cd automacao_instagram

# 2. Execute o script
python instagram_automation.py

# Saída esperada:
# ✔ Imagem redimensionada: processed/ig_sunset.jpg
# ✔ Postado: imagens/sunset.jpg
# ✔ Processo concluído em 45s!

🛠 Funcionalidades Principais
Redimensionamento Automático

    Converte para proporção 4:5 (1080x1350px)

    Mantém qualidade (95% JPG)

    Suporta JPG/PNG

img.thumbnail((1080, 1350))  # Tamanho ideal para feed

Gestão Inteligente de Hashtags

# Adiciona hashtags fixas + do CSV
hashtags_fixas = "#automacao #python"
caption = f"{legenda}\n{hashtags_fixas} {row['hashtags']}"

⚠️ Boas Práticas

    ⏱ Intervalo mínimo entre posts: 30 minutos

    📅 Limite diário recomendado: 3-5 posts

    🔒 Use uma conta secundária para testes

    🚫 Evite hashtags banidas (lista oficial)

🚨 Solução de Problemas
Erro: "Challenge Required"

Instagram Challenge

    Faça login manualmente via navegador

    Complete a verificação de segurança

    Aguarde 24h antes de tentar novamente

Erro: "Unable to upload photo"

    Verifique o formato da imagem

    Reduza a qualidade para 85%

    Adicione um delay maior entre posts:

time.sleep(120)  # 👈 Aumente para 2 minutos

📄 Licença MIT - Use por sua conta e risco. Mantenha suas credenciais seguras!