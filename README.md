
# 🕹️ Jogo Pygame

Este projeto foi desenvolvido como parte da disciplina de Estruturas de Linguagens no curso de Ciência da Computação da Universidade do Estado do Rio de Janeiro (UERJ).
Utilizando a biblioteca Pygame, o jogo apresenta elementos como movimentação de personagem, ataques e um sistema de loja em desenvolvimento.

## 📸 Demonstração

*Adicione aqui capturas de tela ou GIFs do jogo em funcionamento para ilustrar a jogabilidade.*

## 🚀 Funcionalidades

- **Movimentação do Personagem**:  
  - Pressione `A` para mover à esquerda  
  - Pressione `D` para mover à direita  
  - Pressione `S` para pular  
  - Pressione `W` para agachar  

- **Ataques**:  
  - Pressione `X` ou `Espaço` para realizar ataques

- **Sistema de Loja**:  
  - Pressione `F` sobre um item para comprá-lo (funcionalidade em desenvolvimento)

## 🧱 Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
Jogo_Pygame/
├── arma/               # Lógica e sprites das armas
├── ataques/            # Módulo de ataques do personagem
├── chapeu/             # Itens de chapéu e acessórios
├── display_utils/      # Utilitários para renderização e exibição
├── personagem/         # Classe e funcionalidades do personagem principal
├── stage/              # Configurações e elementos do cenário
├── main.py             # Arquivo principal para execução do jogo
├── README.md           # Documentação do projeto
└── .gitignore          # Arquivos e pastas ignorados pelo Git
```

## 🛠️ Tecnologias Utilizadas

- [Python 3.x](https://www.python.org/)  
- [Pygame](https://www.pygame.org/docs/)

## 📦 Instalação e Execução

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/DSRodriguess/Jogo_Pygame.git
   cd Jogo_Pygame
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. **Instale as dependências**:

   ```bash
   pip install pygame
   ```

4. **Execute o jogo**:

   ```bash
   python main.py
   ```

## 📝 Observações

- O sistema de loja está em fase de desenvolvimento. Algumas funcionalidades podem não estar completamente implementadas.

- Certifique-se de que todas as dependências estejam corretamente instaladas para o funcionamento adequado do jogo.

## 📄 Licença

Este projeto é de uso acadêmico e não possui uma licença específica definida.

## 👨‍💻 Autores

- [DSRodriguess](https://github.com/DSRodriguess)
- [AlexandreMFilho](https://github.com/AlexandreMFilho)
- [TiagoSenaD](https://github.com/TiagoSenaD)
