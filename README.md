# Sistema de Gestão de Cadastro de Patrimônio - Etec São José dos Campos

Bem-vindo ao repositório do Sistema de Gestão de Cadastro de Patrimônio da Etec São José dos Campos. Este guia contém instruções detalhadas para clonar, instalar e configurar o sistema em sua máquina local.

---

## **Pré-requisitos**

Antes de começar, certifique-se de que os seguintes requisitos estejam atendidos:

- **Python 3.13+** instalado
- **MySQL Server** instalado e configurado
- **Git** instalado para clonar o repositório
- Ambiente virtual configurado para Python (opcional, mas recomendado)

---

## **Clonando o Repositório**

1. Abra um terminal e navegue até o diretório onde deseja clonar o repositório.
2. Execute o seguinte comando para clonar o repositório:

```bash
   git clone https://github.com/jeancosta4/patrimonio.git
```
   
### Entre no diretório do projeto:

```bash
    cd nome-do-repositorio
```

3. nstalando o Ambiente

Configurando o Ambiente Virtual (Recomendado)
Crie um ambiente virtual:

```bash
python -m venv venv
```

4. Ative o ambiente virtual:
4.1 No Windows:
```bash
venv\Scripts\activate
```

4.2 No Linux/Mac:
```bash
source venv/bin/activate
```

5. Instalando as Dependências
Instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

6. Configuração do Banco de Dados

Crie um banco de dados MySQL para o sistema:
Execute o arquivo db_setup.sql no Mysql.

7. Inicie o servidor Flask:
```bash
flask run
```
Acesse o sistema no navegador:
http://127.0.0.1:5000


