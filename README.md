# 🧙‍♂️ Character Cards UI with Flet

Uma interface animada e estilizada feita com [Flet](https://flet.dev), onde você pode exibir cards de personagens com raridades diferentes, bordas animadas, gradientes personalizados e barras de progresso para habilidades ataque, defesa, velocidade e mais.

![Preview](./screenshot.png)

---

## 🚀 Funcionalidades

- 🟫 Cards com bordas coloridas e gradientes conforme a **raridade**:
  - **Comum** – cinza
  - **Incomum** – vermelho
  - **Raro** – azul
  - **Épico** – roxo
  - **Lendário** – dourado com borda animada ✨
- ✨ **Gradientes personalizados** para cada raridade
- 🎯 Animações suaves com `AnimatedSwitcher` e `Rotation`
- 📊 Visualização de **atributos** com `ProgressBar`
- 📱 Interface responsiva, centralizada, ideal para dashboards, apps de RPG ou coleções

---

## 🛠 Tecnologias utilizadas

- [Flet](https://flet.dev) – UI declarativa com Python
- Python 3.10+
- Estilização com gradientes e animações
- Estrutura baseada em `Container`, `Column`, `Stack` e `AnimatedSwitcher`

---

## 📷 Prévia

![Gif ou imagem da interface](./preview.gif)

---

## 🧩 Como rodar o projeto

1. Clone o repositório:
```bash
+ git clone https://github.com/Rafael-Melo/cards.git
+ cd cards
```
2. Crie um ambiente virtual e ative:
`python -m venv venv`
`venv\Scripts\activate`

3. Instale as dependências:
`pip install flet`

4. Execute o projeto:
`flet run main.py`

📁 Estrutura do Projeto
📦 cards/
 ┣ 📜 main.py
 ┣ 📁 assets/
 ┃ ┗ 🖼️ imagens de personagens
 ┗ 📄 README.md

✨ Inspiração
Este projeto foi inspirado em webtoons como Solo Leveling e card games como Clash Royale e interfaces de coleções, com foco em UI fluida e personalizável.

📄 Licença  
Distribuído sob a licença [MIT](LICENSE).

🤝 Contribuições
Contribuições são bem-vindas! Sinta-se livre para abrir issues, enviar pull requests ou dar sugestões.

Desenvolvido com 💻 e paixão por Rafael Melo (@rafael-melo)
