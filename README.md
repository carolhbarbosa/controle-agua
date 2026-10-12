# 💧 Controle de Níveis de Água

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![colorama](https://img.shields.io/badge/colorama-0.4.6-green)
![Status](https://img.shields.io/badge/status-conclu%C3%ADdo-brightgreen)
![Terminal](https://img.shields.io/badge/execu%C3%A7%C3%A3o-terminal-black)

Sistema de monitoramento de um reservatório de água, executado no terminal.
Ele exibe mensagens de alerta com cores diferentes conforme o nível da água.

## 🎯 Objetivo

Simular um ambiente real de monitoramento, mostrando a situação do reservatório
com uma cor correspondente à progressão de risco.

## 🚦 Níveis e cores

| Nível | Situação              | Cor      |
|-------|-----------------------|----------|
| 1     | Muito baixo (crítico) | Vermelho |
| 2     | Baixo                 | Amarelo  |
| 3     | Médio                 | Verde    |
| 4     | Alto                  | Ciano    |
| 5     | Muito alto (alerta)   | Azul     |

## ▶️ Como executar

1. Tenha o Python instalado.
2. Instale a biblioteca colorama:
```bash
   pip install colorama
```
3. Execute o programa:
```bash
   python controle_agua.py
```

## 📁 Estrutura do projeto

```
controle-niveis-agua/
├── controle_agua.py
└── README.md
```

## 👩‍💻 Autora

Feito por **Carolina Barbosa** como atividade do curso Técnico em Desenvolvimento de Sistemas.

