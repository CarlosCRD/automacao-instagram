# Bot de Postagem no Instagram com Python

Este projeto automatiza postagens no Instagram usando o **Instabot** e permite agendar publicações com legendas e hashtags a partir de um arquivo CSV.

## 💼 Funcionalidades
✅ Login automático no Instagram  
✅ Redimensionamento de imagens para proporção 4:5  
✅ Postagem automática com legenda e hashtags  
✅ Agendamento baseado na data de postagem  
✅ Salvamento do histórico de postagens  

---

## 🛠 1. Pré-requisitos
Antes de começar, instale os seguintes softwares:
- **Python 3.7+**: [Download](https://www.python.org/downloads/)
- **pip** (gerenciador de pacotes do Python)

---

## 💽 2. Instalação

### **Criar um ambiente virtual (opcional, mas recomendado)**
No terminal, execute:
```bash
python -m venv venv
```
Ative o ambiente virtual:
- **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- **Linux/macOS**:
  ```bash
  source venv/bin/activate
  ```

### **Instalar as dependências**
```bash
pip install instabot pandas pillow
```

---

## 📝 3. Configuração

### **Criar o arquivo CSV com os posts**
Crie o arquivo `posts_instagram.csv` com os seguintes campos:
```csv
imagem,legenda,hashtags,data_postagem
"teste1.jpg","Primeiro post de teste","#python #automacao","2025-02-22"
"teste2.jpg","Segundo post de teste","#bot #instabot","2025-02-22"
```
Cada linha representa um post.

---

## 🚀 4. Uso

### **1️⃣ Executar o bot**
No terminal, execute:
```bash
python bot_instagram.py
```
Ele fará login, redimensionará as imagens e postará no Instagram.

---

## 🛠 5. Solução de Problemas

| Erro | Solução |
|------|---------|
| `ModuleNotFoundError: No module named 'instabot'` | Rode `pip install instabot` |
| `Falha no login - verifique credenciais/2FA` | Certifique-se de que a autenticação de dois fatores está desativada no Instagram |
| `Bot falhou ao postar` | Verifique se a imagem está em `.jpg` e se está no tamanho permitido (1080x1350) |

---

## 📚 6. Licença

Este projeto está sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

🤝 Contribua

    Faça um fork do projeto

    Crie uma branch: git checkout -b feature/nova-funcionalidade

    Commit: git commit -m 'Adiciona recurso incrível'

    Push: git push origin feature/nova-funcionalidade

    Abra um Pull Request

Roadmap:

    Suporte a vídeos/reels

    Análise de engajamento pós-postagem

⚠️ Aviso Legal: Não nos responsabilizamos por bloqueios/perdas de conta. Use com responsabilidade!
