import json
import os
import re
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_USUARIOS = os.path.join(BASE_DIR, 'users.json')
# Mantemos o arquivo de aulas de perguntas
ARQUIVO_AULAS_PERGUNTAS = os.path.join(BASE_DIR, 'aulas_perguntas.json')
# Novo arquivo para aulas teóricas
ARQUIVO_AULAS_TEORICAS = os.path.join(BASE_DIR, 'aulas_teoricas.json')


def garantir_arquivos():
    """Garante que os arquivos JSON existam com estrutura inicial."""
    if not os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, 'w') as f:
            json.dump({}, f)

    # Estrutura existente para aulas de perguntas
    if not os.path.exists(ARQUIVO_AULAS_PERGUNTAS):
        aulas_perguntas = {
            "Segurança Digital": {
                "Básico": [
                    {"titulo": "Senhas Fortes", "pergunta": "Qual dessas é a senha mais segura?", "opcoes": ["12345678", "maria2020", "@M4r1a!#"], "correta": "3"},
                    {"titulo": "Golpes na Internet", "pergunta": "O que fazer ao receber um e-mail pedindo senha?", "opcoes": ["Enviar senha", "Ignorar e denunciar"], "correta": "2"},
                    {"titulo": "Compartilhamento Responsável", "pergunta": "O que fazer ao postar foto com RG visível?", "opcoes": ["Postar sem se preocupar", "Esconder informações"], "correta": "2"}
                ],
                "Intermediário": [
                    {"titulo": "Autenticação em Dois Fatores", "pergunta": "2FA no celular significa o que?", "opcoes": ["Aviso para ignorar", "Inserir código para confirmar"], "correta": "2"},
                    {"titulo": "Atualizações de Segurança", "pergunta": "O que fazer com atualizações de segurança?", "opcoes": ["Ignorar", "Atualizar"], "correta": "2"},
                    {"titulo": "Segurança em Redes Wi-Fi", "pergunta": "Qual atitude é segura em Wi-Fi público?", "opcoes": ["Usar VPN", "Fazer login normal"], "correta": "1"}
                ],
                "Avançado": [
                    {"titulo": "Engenharia Social", "pergunta": "Ligação pedindo senha, o que fazer?", "opcoes": ["Confiar e passar", "Recusar e desligar"], "correta": "2"},
                    {"titulo": "Gerenciadores de Senhas", "pergunta": "Vantagem de usar gerenciador de senhas?", "opcoes": ["Senhas em papel", "Senhas únicas e fortes"], "correta": "2"},
                    {"titulo": "Reconhecimento de Golpes Avançados", "pergunta": "Acessar 'seubanco-seguro.com' e pedem senha?", "opcoes": ["Digitar a senha", "Verificar o domínio"], "correta": "2"}
                ]
            },
            "Pensamento Lógico Computacional": {
                "Básico": [
                    {"titulo": "Identificando Padrões", "pergunta": "Complete a sequência: 2, 4, 6, 8, ?", "opcoes": ["10", "12", "14"], "correta": "1"},
                    {"titulo": "Sequência de Instruções", "pergunta": "Ordem correta para escovar os dentes?", "opcoes": ["Pasta, escovar, molhar", "Molhar, pasta, escovar"], "correta": "2"},
                    {"titulo": "Verdadeiro ou Falso", "pergunta": "Cães são animais, animais respiram, logo cães respiram. V ou F?", "opcoes": ["V", "F"], "correta": "1"}
                ],
                "Intermediário": [
                    {"titulo": "Condicionais", "pergunta": "Está chovendo? (s/n)", "opcoes": ["s", "n"], "correta": "1"},
                    {"titulo": "Laços de Repetição", "pergunta": "Qual laço usar com número fixo de repetições?", "opcoes": ["while", "for"], "correta": "2"},
                    {"titulo": "Algoritmos com Validação", "pergunta": "Entrada inválida para par ou ímpar?", "opcoes": ["Letras", "Números"], "correta": "1"}
                ],
                "Avançado": [
                    {"titulo": "Tabelas Verdade", "pergunta": "Resultado de (V OU F) E (F OU F)?", "opcoes": ["V", "F"], "correta": "2"},
                    {"titulo": "Expressões Lógicas Compostas", "pergunta": "Valor de (A OR B) AND NOT(C) com A=V, B=F, C=V?", "opcoes": ["True", "False"], "correta": "2"},
                    {"titulo": "Algoritmos com Decisão e Repetição", "pergunta": "Número múltiplo de 3 e 5?", "opcoes": ["15", "7"], "correta": "1"}
                ]
            },
            "Programação Python": {
                "Básico": [
                    {"titulo": "Variáveis e Tipos de Dados", "pergunta": "Tipo de 'Maria'?", "opcoes": ["String", "Integer", "Float"], "correta": "1"},
                    {"titulo": "Operações Matemáticas", "pergunta": "2 + 2 = ?", "opcoes": ["3", "4", "5"], "correta": "2"},
                    {"titulo": "Estruturas Condicionais", "pergunta": "Tenho 18 anos, Sou maior de idade ou menor?", "opcoes": ["Maior de idade", "Menor de idade"], "correta": "1"}
                ],
                "Intermediário": [
                    {"titulo": "Listas e Laços de Repetição", "pergunta": "Como percorrer uma lista?", "opcoes": ["if", "for"], "correta": "2"},
                    {"titulo": "Funções em Python", "pergunta": "Funções reutilizam o que?", "opcoes": ["Variáveis", "Blocos de código"], "correta": "2"},
                    {"titulo": "Dicionários", "pergunta": "Dicionários armazenam o que?", "opcoes": ["Listas", "Pares chave-valor"], "correta": "2"}
                ]
                ,
                "Avançado": [
                    {"titulo": "Manipulação de Arquivos", "pergunta": "Comando para escrever em arquivo?", "opcoes": ["read", "write"], "correta": "2"},
                    {"titulo": "Exceções Personalizadas", "pergunta": "O que são Exceções Personalizadas?", "opcoes": ["Tipos de erros personalizados", "Funções"], "correta": "1"},
                    {"titulo": "Programação Orientada a Objetos", "pergunta": "POO usa o que para representar objetos?", "opcoes": ["Variáveis", "Classes"], "correta": "2"}
                ]
            }
        }
        with open(ARQUIVO_AULAS_PERGUNTAS, 'w') as f:
            json.dump(aulas_perguntas, f, indent=4)

    # Nova estrutura para aulas teóricas
    if not os.path.exists(ARQUIVO_AULAS_TEORICAS):
        aulas_teoricas = {
            "Segurança Digital": {
                "Básico": [
                    {"titulo": "Introdução à Segurança Digital", "conteudo": "Segurança digital envolve proteger seus dados e privacidade online. É essencial para evitar golpes e vazamentos de informações."},
                    {"titulo": "Criando Senhas Fortes", "conteudo": "Uma senha forte tem pelo menos 8 caracteres, inclui letras maiúsculas e minúsculas, números e símbolos. Evite informações pessoais óbvias."},
                    {"titulo": "Reconhecendo Golpes Comuns", "conteudo": "Fique atento a e-mails e mensagens suspeitas pedindo informações pessoais ou financeiras. Desconfie de ofertas boas demais para ser verdade."},
                    {"titulo": "Compartilhamento Consciente", "conteudo": "Pense duas vezes antes de postar informações pessoais nas redes sociais. Dados como RG, CPF, endereço ou número de telefone podem ser usados indevidamente."},
                ],
                "Intermediário": [
                    {"titulo": "O Que é Autenticação em Dois Fatores (2FA)?", "conteudo": "2FA adiciona uma camada extra de segurança. Além da senha, você precisa de um segundo fator, como um código enviado para seu celular, para acessar sua conta."},
                    {"titulo": "Importância das Atualizações", "conteudo": "Manter sistemas operacionais, aplicativos e antivírus atualizados corrige falhas de segurança que podem ser exploradas por criminosos."},
                    {"titulo": "Segurança em Redes Wi-Fi Públicas", "conteudo": "Redes Wi-Fi públicas são menos seguras. Evite realizar transações bancárias ou acessar informações confidenciais. Usar uma VPN pode proteger sua conexão."},
                ],
                "Avançado": [
                    {"titulo": "Entendendo Engenharia Social", "conteudo": "Engenharia social é a manipulação psicológica para que pessoas revelem informações confidenciais. Desconfie de pedidos urgentes ou incomuns por telefone ou e-mail."},
                    {"titulo": "Benefícios dos Gerenciadores de Senhas", "conteudo": "Gerenciadores de senhas criam e armazenam senhas complexas e únicas para cada site, exigindo que você se lembre de apenas uma senha mestra."},
                    {"titulo": "Identificando Phishing Avançado", "conteudo": "Phishing sofisticado imita sites legítimos. Sempre verifique o endereço do site (URL) antes de inserir suas credenciais. Procure pelo 'https://' e o cadeado na barra de endereço."},
                ]
            },
            "Pensamento Lógico Computacional": {
                 "Básico": [
                    {"titulo": "O Que é Pensamento Lógico?", "conteudo": "Pensamento lógico é a habilidade de organizar ideias e informações para chegar a uma conclusão ou resolver um problema de forma estruturada."},
                    {"titulo": "Identificação de Padrões", "conteudo": "Reconhecer padrões é fundamental para prever o próximo passo em uma sequência ou entender a lógica por trás de um conjunto de dados."},
                    {"titulo": "Sequências e Algoritmos Simples", "conteudo": "Uma sequência de instruções é um conjunto de passos ordenados para realizar uma tarefa. Um algoritmo é uma sequência finita de instruções bem definidas."},
                    {"titulo": "Introdução à Lógica Booleana (Verdadeiro ou Falso)", "conteudo": "A lógica booleana lida com valores de Verdadeiro (True) e Falso (False) e operações como AND, OR e NOT. É a base para decisões em programação."},
                ],
                "Intermediário": [
                    {"titulo": "Instruções Condicionais (If/Else)", "conteudo": "Condicionais permitem que um programa tome decisões. 'Se' uma condição for Verdadeira, faça algo; 'Senão', faça outra coisa."},
                    {"titulo": "Laços de Repetição (Loops)", "conteudo": "Laços permitem executar um bloco de código várias vezes. O laço 'for' é comum para repetições com um número conhecido, e 'while' para repetições baseadas em uma condição."},
                    {"titulo": "Algoritmos com Validação de Entrada", "conteudo": "Validar a entrada de dados garante que o programa receba informações no formato esperado, evitando erros e comportamentos inesperados."},
                ],
                "Avançado": [
                    {"titulo": "Tabelas Verdade e Operadores Lógicos", "conteudo": "Tabelas verdade mostram todos os resultados possíveis de uma expressão lógica. Operadores lógicos (AND, OR, NOT) combinam ou modificam valores booleanos."},
                    {"titulo": "Expressões Lógicas Compostas", "conteudo": "Combinar múltiplos operadores lógicos e condições cria expressões complexas usadas para tomar decisões mais elaboradas em algoritmos."},
                    {"titulo": "Desenvolvendo Algoritmos com Decisão e Repetição", "conteudo": "Algoritmos mais complexos combinam estruturas de decisão (if/else) e repetição (loops) para resolver problemas que requerem múltiplos passos e verificações."},
                ]
            },
             "Programação Python": {
                "Básico": [
                    {"titulo": "O Que é Python?", "conteudo": "Python é uma linguagem de programação versátil e fácil de aprender, usada para desenvolvimento web, análise de dados, inteligência artificial e mais."},
                    {"titulo": "Variáveis e Tipos de Dados Fundamentais", "conteudo": "Variáveis armazenam dados. Tipos de dados comuns incluem texto (string), números inteiros (int), números decimais (float) e booleanos (bool)."},
                    {"titulo": "Operadores Matemáticos e de Comparação", "conteudo": "Python suporta operações matemáticas (+, -, *, /) e de comparação (==, !=, >, <, >=, <=) para manipular dados numéricos e tomar decisões."},
                    {"titulo": "Estruturas Condicionais em Python (if, elif, else)", "conteudo": "As estruturas `if`, `elif` (else if) e `else` permitem executar blocos de código diferentes baseados em condições."},
                ],
                "Intermediário": [
                    {"titulo": "Listas e Como Iterar Sobre Elas", "conteudo": "Listas são coleções ordenadas de itens. O laço `for` é frequentemente usado para percorrer todos os elementos de uma lista."},
                    {"titulo": "Criando e Usando Funções", "conteudo": "Funções são blocos de código reutilizáveis que executam uma tarefa específica. Elas ajudam a organizar o código e evitar repetição."},
                    {"titulo": "Dicionários: Pares Chave-Valor", "conteudo": "Dicionários armazenam dados como pares de chave e valor. Cada chave é única e associada a um valor correspondente."},
                ],
                "Avançado": [
                    {"titulo": "Manipulação Básica de Arquivos", "conteudo": "Python permite ler e escrever dados em arquivos usando funções como `open()`, `read()`, `write()` e `close()`."},
                    {"titulo": "Lidando com Erros: Exceções", "conteudo": "Exceções são erros que ocorrem durante a execução do programa. Usar `try`, `except` e `finally` ajuda a lidar com esses erros de forma controlada."},
                    {"titulo": "Introdução à Programação Orientada a Objetos (POO)", "conteudo": "POO é um paradigma de programação que organiza o código em 'objetos', que são instâncias de 'classes'. Classes definem propriedades (atributos) e comportamentos (métodos)."},
                ]
            }
        }
        with open(ARQUIVO_AULAS_TEORICAS, 'w') as f:
            json.dump(aulas_teoricas, f, indent=4)


def carregar_usuarios():
    """Carrega dados dos usuários do arquivo JSON."""
    try:
        with open(ARQUIVO_USUARIOS, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {} # Retorna dicionário vazio se o arquivo não existir


def salvar_usuarios(usuarios):
    """Salva dados dos usuários no arquivo JSON."""
    with open(ARQUIVO_USUARIOS, 'w') as f:
        json.dump(usuarios, f, indent=4)

def carregar_aulas_perguntas():
    """Carrega as aulas de perguntas do arquivo JSON."""
    try:
        with open(ARQUIVO_AULAS_PERGUNTAS, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def carregar_aulas_teoricas():
    """Carrega as aulas teóricas do arquivo JSON."""
    try:
        with open(ARQUIVO_AULAS_TEORICAS, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def senha_forte(s):
    """Verifica se a senha atende aos critérios de segurança."""
    return len(s) >= 8 and re.search(r"[A-Z]", s) and re.search(r"\d", s) and re.search(r"[!@#$%^&*(),.?\":{}|<>]", s)

def validar_nome(nome):
    """Valida se o nome contém apenas letras e espaços."""
    return bool(re.fullmatch(r"[A-Za-zÀ-ÿ ]+", nome.strip()))

def validar_data(data):
    """Valida se a data está no formato DD/MM/AAAA."""
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False

def validar_email(email):
    """Valida o formato do email."""
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email.strip()))

def input_opcao_valida(pergunta, opcoes):
    """Pede ao usuário para escolher uma opção válida de uma lista."""
    while True:
        for i, op in enumerate(opcoes, 1):
            print(f"[{i}] {op}")
        escolha = input(pergunta + " ")
        if escolha in [str(i) for i in range(1, len(opcoes)+1)]:
            return escolha
        print("❌ Escolha uma das alternativas para prosseguir.")


def cadastrar_usuario():
    """Função para cadastrar um novo usuário."""
    print("\n=== CADASTRO ===")
    usuarios = carregar_usuarios()
    usuario = input("Usuário: ").strip()
    if usuario in usuarios:
        print("❌ Usuário já existe.")
        return
    while True:
        nome = input("Nome completo: ").strip()
        if validar_nome(nome):
            break
        print("❌ Use apenas letras e espaços.")
    while True:
        data_nasc = input("Data de nascimento (DD/MM/AAAA): ").strip()
        if validar_data(data_nasc):
            break
        print("❌ Data inválida. Use o formato DD/MM/AAAA.")
    while True:
        email = input("Email: ").strip()
        if validar_email(email):
            break
        print("❌ Email inválido.")
    while True:
        senha = input("Senha: ").strip()
        if senha_forte(senha):
            break
        print("❌ Senha fraca. Deve ter 8+ caracteres, letra maiúscula, número e símbolo.")
    usuarios[usuario] = {
        "nome": nome,
        "data_nascimento": data_nasc,
        "email": email,
        "senha": senha,
        "progresso": {
            "perguntas": {},
            "teoricas": {}
        } # Inicializa progresso para ambos os tipos de aulas
    }
    salvar_usuarios(usuarios)
    print("✅ Cadastro concluído.")


def login_usuario():
    """Função para login de usuário existente."""
    print("\n=== LOGIN ===")
    usuarios = carregar_usuarios()
    usuario = input("Usuário: ").strip()
    senha = input("Senha: ").strip()
    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        print(f"✅ Bem-vindo, {usuario}")
        # Garante que a estrutura de progresso está completa após login (para usuários antigos)
        if "progresso" not in usuarios[usuario]:
            usuarios[usuario]["progresso"] = {"perguntas": {}, "teoricas": {}}
            salvar_usuarios(usuarios)
        elif "teoricas" not in usuarios[usuario]["progresso"]:
             usuarios[usuario]["progresso"]["teoricas"] = {}
             salvar_usuarios(usuarios)
        elif "perguntas" not in usuarios[usuario]["progresso"]:
             usuarios[usuario]["progresso"]["perguntas"] = {}
             salvar_usuarios(usuarios)

        return usuario
    print("❌ Login inválido.")
    return None


def executar_aulas_perguntas(usuario):
    """Executa o módulo de aulas de perguntas."""
    aulas_perguntas = carregar_aulas_perguntas()
    usuarios = carregar_usuarios()
    # Acessa o progresso específico de perguntas
    progresso = usuarios[usuario].get("progresso", {}).get("perguntas", {})

    while True:
        print("\n=== MÓDULOS DE PERGUNTAS ===")
        modulos = list(aulas_perguntas.keys())
        for i, modulo in enumerate(modulos, 1):
            print(f"[{i}] {modulo}")
        print(f"[{len(modulos) + 1}] Voltar ao Menu Principal")

        escolha = input("\nEscolha um módulo: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(modulos):
            modulo = modulos[int(escolha) - 1]

            while True:
                print(f"\n=== NÍVEIS DO MÓDULO: {modulo} (Perguntas) ===")
                niveis = list(aulas_perguntas[modulo].keys())
                for i, nivel in enumerate(niveis, 1):
                    print(f"[{i}] {nivel}")
                print(f"[{len(niveis) + 1}] Voltar aos Módulos de Perguntas")

                escolha_nivel = input("\nEscolha um nível: ")
                if escolha_nivel.isdigit() and 1 <= int(escolha_nivel) <= len(niveis):
                    nivel = niveis[int(escolha_nivel) - 1]

                    if modulo not in progresso:
                        progresso[modulo] = {}
                    if nivel not in progresso[modulo]:
                        progresso[modulo][nivel] = []

                    lista = aulas_perguntas[modulo][nivel]
                    for aula in lista:
                        if aula["titulo"] in progresso[modulo][nivel]:
                            print(f"\n  ✅ {aula['titulo']} (Concluída)")
                            continue

                        print(f"\n=== {aula['titulo']} ===")
                        print(f"\n{aula['pergunta']}")
                        print("\nEscolha uma opção:")
                        resp = input_opcao_valida("Sua resposta", aula["opcoes"])

                        if resp == aula["correta"]:
                            print("✅ Correto!")
                        else:
                            print(f"❌ Incorreto. Resposta correta: {aula['opcoes'][int(aula['correta'])-1]}")
                        # Marca a aula de pergunta como concluída
                        progresso[modulo][nivel].append(aula["titulo"])
                        usuarios[usuario]["progresso"]["perguntas"] = progresso
                        salvar_usuarios(usuarios)

                    print(f"\n🎉 Nível {nivel} de Perguntas concluído!")
                elif escolha_nivel == str(len(niveis) + 1):
                    break
                else:
                    print("❌ Opção inválida.")

        elif escolha == str(len(modulos) + 1):
            break
        else:
            print("❌ Opção inválida.")


def executar_aulas_teoricas(usuario):
    """Executa o módulo de aulas teóricas."""
    aulas_teoricas = carregar_aulas_teoricas()
    usuarios = carregar_usuarios()
     # Acessa o progresso específico de teoricas
    progresso = usuarios[usuario].get("progresso", {}).get("teoricas", {})

    while True:
        print("\n=== MÓDULOS TEÓRICOS ===")
        modulos = list(aulas_teoricas.keys())
        for i, modulo in enumerate(modulos, 1):
            print(f"[{i}] {modulo}")
        print(f"[{len(modulos) + 1}] Voltar ao Menu Principal")

        escolha = input("\nEscolha um módulo: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(modulos):
            modulo = modulos[int(escolha) - 1]

            while True:
                print(f"\n=== NÍVEIS DO MÓDULO: {modulo} (Teórico) ===")
                niveis = list(aulas_teoricas[modulo].keys())
                for i, nivel in enumerate(niveis, 1):
                    # Mostra se o nível teórico está totalmente lido
                    total_aulas_nivel = len(aulas_teoricas[modulo][nivel])
                    aulas_lidas_nivel = len(progresso.get(modulo, {}).get(nivel, []))
                    status = f"({aulas_lidas_nivel}/{total_aulas_nivel} lidas)"
                    print(f"[{i}] {nivel} {status}")

                print(f"[{len(niveis) + 1}] Voltar aos Módulos Teóricos")

                escolha_nivel = input("\nEscolha um nível: ")
                if escolha_nivel.isdigit() and 1 <= int(escolha_nivel) <= len(niveis):
                    nivel = niveis[int(escolha_nivel) - 1]

                    if modulo not in progresso:
                        progresso[modulo] = {}
                    if nivel not in progresso[modulo]:
                        progresso[modulo][nivel] = []

                    lista = aulas_teoricas[modulo][nivel]
                    for aula in lista:
                        lida = aula["titulo"] in progresso[modulo][nivel]
                        status = "✅ Lido" if lida else "⏳ Não Lido"
                        print(f"\n--- {aula['titulo']} {status} ---")
                        print(aula["conteudo"])

                        if not lida:
                            input("\nPressione Enter para marcar como lida...")
                            progresso[modulo][nivel].append(aula["titulo"])
                            usuarios[usuario]["progresso"]["teoricas"] = progresso
                            salvar_usuarios(usuarios)
                            print("✅ Marcada como lida!")
                        else:
                             input("\nPressione Enter para continuar...")


                    # Verifica se todas as aulas do nível teórico foram lidas
                    total_aulas_nivel = len(aulas_teoricas[modulo][nivel])
                    aulas_lidas_nivel = len(progresso.get(modulo, {}).get(nivel, []))
                    if aulas_lidas_nivel == total_aulas_nivel:
                         print(f"\n🎉 Nível {nivel} Teórico concluído (todas as aulas lidas)!")
                    else:
                         print(f"\nContinuando no Nível {nivel} Teórico. {aulas_lidas_nivel}/{total_aulas_nivel} aulas lidas.")


                elif escolha_nivel == str(len(niveis) + 1):
                    break
                else:
                    print("❌ Opção inválida.")

        elif escolha == str(len(modulos) + 1):
            break
        else:
            print("❌ Opção inválida.")


def menu():
    """Menu principal do programa."""
    garantir_arquivos()
    usuario = None
    while True:
        print("\n=== MENU ===")
        print("[1] Cadastrar")
        print("[2] Login")
        print("[3] Acessar Módulo Teórico") # Ordem invertida
        print("[4] Acessar Módulo de Perguntas") # Ordem invertida
        print("[5] Sair")
        opcao = input("Escolha: ")
        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            usuario = login_usuario()
        elif opcao == "3": # Agora a opção 3 chama o módulo teórico
             if usuario:
                 executar_aulas_teoricas(usuario)
             else:
                 print("❌ Faça login primeiro.")
        elif opcao == "4": # Agora a opção 4 chama o módulo de perguntas
            if usuario:
                executar_aulas_perguntas(usuario)
            else:
                print("❌ Faça login primeiro.")
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()