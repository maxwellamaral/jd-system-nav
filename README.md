# JD System

O **JD System** é uma ferramenta de busca e navegação por pastas baseada no sistema Johnny Decimal. Ela permite encontrar rapidamente pastas em uma estrutura organizada.

## Pré-requisitos

- **Python:** Certifique-se de ter o Python instalado. Você pode baixá-lo em [python.org](https://www.python.org/downloads/).

## Configuração

1. **Clone o Repositório:**

```
git clone https://github.com/seu-usuario/jd-system.git
cd jd-system
```

2. **Configuração do Ambiente:**

- Crie um ambiente virtual (opcional, mas recomendado):

  ```
  python -m venv venv
  ```

- Ative o ambiente virtual:

  - **Windows:**

    ```
    venv\Scripts\activate
    ```

  - **Linux/Mac:**

    ```
    source venv/bin/activate
    ```

1. **Instalação das Dependências:**

```
pip install -r requirements.txt
```

2. **Configuração do Arquivo `config.yaml`:**

- Edite o arquivo `config.yaml` no diretório do projeto com as informações necessárias:

  ```yaml
  path: "Caminho/para/suas/pastas"
  vscode_path: "Caminho/para/seu/code.exe"
  ```

## Uso

- **Pesquisar e Abrir uma Pasta:**

  ```
    python jd_system.py <termo_de_pesquisa>
  ```

- Para abrir com o VSCode:

  ```
  python jd_system.py <termo_de_pesquisa> -o code
  ```

## Opções

- **Termo de Pesquisa:** O termo para buscar nas pastas.
- **Opções de Abertura:**
- `-o explorer`: Abre no Windows Explorer (padrão).
- `-o code`: Abre no VSCode.

## Exemplos

- Pesquisa e abre uma pasta com o termo "projeto":
  `python jd_system.py projeto`

- Pesquisa e abre a mesma pasta com o termo "projeto" usando o VSCode:
  `python jd_system.py projeto -o code`

## Contribuição

Contribuições são bem-vindas! Por favor, faça um fork do repositório e crie um pull request com suas melhorias.

## Licença

Este projeto está licenciado sob a Licença GNU v3 - veja o arquivo [LICENSE](LICENSE) para detalhes.
