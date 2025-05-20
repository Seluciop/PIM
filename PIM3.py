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

    # Estrutura ATUALIZADA para aulas de perguntas com 5 alternativas por pergunta
    if not os.path.exists(ARQUIVO_AULAS_PERGUNTAS):
        aulas_perguntas = {
            "Segurança Digital": {
                "Básico": [
                    {"titulo": "Criando Senhas Fortes", "pergunta": "Para criar uma senha forte e segura, qual das seguintes combinações é a MAIS recomendada?", "opcoes": ["Seu nome e data de nascimento.", "Uma sequência de números simples como 12345678.", "Uma combinação aleatória de letras maiúsculas/minúsculas, números e símbolos com mais de 8 caracteres.", "Palavras comuns encontradas no dicionário.", "O nome do seu animal de estimação."], "correta": "3"},
                    {"titulo": "Reconhecendo Golpes Comuns", "pergunta": "Você recebe um e-mail inesperado de um banco conhecido, pedindo para clicar em um link para 'confirmar seus dados' devido a uma 'atividade suspeita'. Qual a melhor atitude a tomar?", "opcoes": ["Clicar no link imediatamente para verificar sua conta.", "Responder ao e-mail pedindo mais informações sobre a atividade suspeita.", "Encaminhar o e-mail para seus contatos para alertá-los.", "Ligar para o número de telefone que veio no e-mail.", "Ignorar o e-mail, não clicar em links e, se necessário, entrar em contato direto com o banco pelos canais oficiais."], "correta": "5"},
                    {"titulo": "Compartilhamento Consciente", "pergunta": "Ao compartilhar informações online, especialmente em redes sociais, qual tipo de informação apresenta MAIOR risco de ser usada indevidamente para fraudes ou roubo de identidade?", "opcoes": ["Fotos de paisagens ou comidas.", "Opiniões sobre filmes ou livros.", "Nome completo e cidade onde mora.", "Seu estado civil.", "Documentos pessoais como RG, CPF, ou comprovantes de endereço visíveis."], "correta": "5"}
                ],
                "Intermediário": [
                    {"titulo": "Autenticação em Dois Fatores (2FA)", "pergunta": "A Autenticação em Dois Fatores (2FA) é uma medida de segurança recomendada porque:", "opcoes": ["Ela apenas solicita seu e-mail duas vezes.", "Ela exige que você insira um código adicional (geralmente enviado para seu celular) além da sua senha, aumentando a segurança mesmo que sua senha seja descoberta.", "Ela substitui completamente a necessidade de uma senha.", "Ela torna o login mais rápido e simples.", "Ela funciona apenas em computadores, não em celulares."], "correta": "2"},
                    {"titulo": "Importância das Atualizações", "pergunta": "Manter seus softwares (sistema operacional, navegadores, aplicativos) sempre atualizados é crucial para a segurança digital porque:", "opcoes": ["As atualizações apenas mudam a aparência do software.", "As atualizações corrigem falhas de segurança (vulnerabilidades) que podem ser exploradas por hackers.", "As atualizações tornam seu computador mais lento.", "As atualizações adicionam apenas novos recursos desnecessários.", "As atualizações aumentam o consumo de internet."], "correta": "2"},
                    {"titulo": "Segurança em Redes Wi-Fi Públicas", "pergunta": "Você está conectado a uma rede Wi-Fi pública e gratuita em um café. Qual atividade é MENOS segura realizar neste tipo de rede?", "opcoes": ["Navegar em sites de notícias.", "Fazer uma compra online ou acessar sua conta bancária.", "Assistir a um vídeo no YouTube.", "Pesquisar um endereço no mapa.", "Ler artigos em blogs."], "correta": "2"}
                ],
                "Avançado": [
                    {"titulo": "Entendendo Engenharia Social", "pergunta": "Engenharia social é uma técnica usada por criminosos para:", "opcoes": ["Invadir computadores diretamente explorando falhas técnicas.", "Manipular psicologicamente as pessoas para que revelem informações confidenciais ou realizem ações que beneficiam o golpista.", "Criar vírus de computador complexos.", "Melhorar a performance de sistemas computacionais.", "Desenvolver novos sistemas operacionais."], "correta": "2"},
                    {"titulo": "Benefícios dos Gerenciadores de Senhas", "pergunta": "Qual a principal vantagem de utilizar um gerenciador de senhas?", "opcoes": ["Ele armazena todas as suas senhas em um arquivo de texto simples no seu computador.", "Ele permite que você use a mesma senha fácil de lembrar para todos os seus sites.", "Ele compartilha suas senhas com seus amigos.", "Ele te envia lembretes por e-mail para trocar de senha frequentemente.", "Ele gera senhas complexas e únicas para cada site e as armazena de forma segura, exigindo que você se lembre de apenas uma senha mestra."], "correta": "5"},
                    {"titulo": "Identificando Phishing Avançado", "pergunta": "Você recebe um link em uma mensagem que parece ser do seu banco. O link é 'seubanco-seguro.phishing.com'. Mesmo que a página de login pareça idêntica, qual o sinal de alerta MAIS evidente de que pode ser um golpe de phishing?", "opcoes": ["A página pede seu nome de usuário e senha.", "O site tem um layout moderno.", "O site usa o protocolo HTTPS.", "A página carrega muito rapidamente.", "O endereço do site (URL) na barra do navegador não corresponde ao endereço oficial do seu banco (o domínio principal é 'phishing.com', não 'seubanco.com')."], "correta": "5"}
                ]
            },
            "Pensamento Lógico Computacional": {
                "Básico": [
                    {"titulo": "Identificação de Padrões", "pergunta": "Considere a sequência: 5, 10, 15, 20, ... Qual o próximo número na sequência, seguindo o padrão lógico?", "opcoes": ["21", "25", "30", "35", "40"], "correta": "2"},
                    {"titulo": "Sequências e Algoritmos Simples", "pergunta": "Para cozinhar um ovo frito, a sequência correta de passos em um algoritmo simples é:", "opcoes": ["Quebrar o ovo na panela, aquecer o óleo, salgar.", "Aquecer o óleo na panela, quebrar o ovo, salgar.", "Salgar o ovo, aquecer o óleo, quebrar o ovo na panela.", "Quebrar o ovo no prato, salgar, aquecer o óleo na panela.", "Salgar a panela, aquecer o óleo, quebrar o ovo."], "correta": "2"},
                    {"titulo": "Introdução à Lógica Booleana", "pergunta": "Na lógica booleana, se a afirmação 'Está chovendo' é VERDADEIRA e a afirmação 'Está frio' é FALSA, qual o resultado da expressão 'Está chovendo E Está frio'?", "opcoes": ["VERDADEIRO", "FALSO", "Depende do dia.", "Indeterminado.", "Verdadeiro se estiver ventando."], "correta": "2"}
                ],
                "Intermediário": [
                    {"titulo": "Instruções Condicionais (If/Else)", "pergunta": "Um programa deve verificar a idade de um usuário. Se a idade for maior ou igual a 18, ele deve exibir 'Maior de idade'. Caso contrário, deve exibir 'Menor de idade'. Qual estrutura lógica é mais apropriada para isso?", "opcoes": ["Um laço de repetição (loop).", "Uma instrução condicional (if/else).", "Apenas uma sequência de instruções diretas.", "Uma função matemática complexa.", "Um dicionário."], "correta": "2"},
                    {"titulo": "Laços de Repetição (Loops)", "pergunta": "Você precisa executar um bloco de código exatamente 10 vezes. Qual tipo de laço de repetição é tipicamente usado quando o número de repetições é conhecido previamente?", "opcoes": ["Laço 'while'.", "Laço 'for'.", "Instrução 'if'.", "Instrução 'else'.", "Uma função."], "correta": "2"},
                    {"titulo": "Algoritmos com Validação de Entrada", "pergunta": "Um algoritmo pede ao usuário para digitar um número inteiro. O que significa 'validar a entrada' neste contexto?", "opcoes": ["Garantir que o usuário digite apenas letras.", "Garantir que o usuário digite apenas um número inteiro e não texto ou símbolos.", "Garantir que o número digitado seja maior que 100.", "Garantir que o usuário digite um número par.", "Permitir que o usuário digite qualquer coisa."], "correta": "2"}
                ],
                "Avançado": [
                    {"titulo": "Tabelas Verdade e Operadores Lógicos", "pergunta": "Na lógica booleana, qual o resultado da expressão (VERDADEIRO OU FALSO) E NÃO(VERDADEIRO)?", "opcoes": ["VERDADEIRO", "FALSO", "Nulo", "Erro", "Depende do contexto"], "correta": "2"},
                    {"titulo": "Expressões Lógicas Compostas", "pergunta": "Considere as variáveis lógicas A=VERDADEIRO, B=FALSO, C=VERDADEIRO. Qual o valor da expressão (A E B) OU (NÃO C)?", "opcoes": ["VERDADEIRO", "FALSO", "Nulo", "Erro", "Indeterminado"], "correta": "2"},
                    {"titulo": "Desenvolvendo Algoritmos com Decisão e Repetição", "pergunta": "Para encontrar todos os números entre 1 e 100 que são múltiplos de 3 E 5, qual combinação de estruturas lógicas é essencial?", "opcoes": ["Apenas um laço de repetição (loop).", "Apenas instruções condicionais (if).", "Uma combinação de laço de repetição (loop) para verificar cada número E instruções condicionais (if) para checar a condição de múltiplo de 3 e 5.", "Apenas sequências de instruções diretas.", "Apenas funções matemáticas."], "correta": "3"}
                ]
            },
             "Programação Python": {
                "Básico": [
                    {"titulo": "Variáveis e Tipos de Dados Fundamentais", "pergunta": "Em Python, qual o tipo de dado mais adequado para armazenar a frase 'Olá, mundo!'?", "opcoes": ["Integer (int).", "String (str).", "Boolean (bool).", "Float (float).", "List (list)."], "correta": "2"},
                    {"titulo": "Operadores Matemáticos e de Comparação", "pergunta": "Qual o resultado da expressão Python: `(5 * 2) - 3`?", "opcoes": ["7", "10", "13", "8", "9"], "correta": "1"},
                     {"titulo": "Estruturas Condicionais em Python", "pergunta": "Dado o código Python: `idade = 17\nif idade >= 18:\n    print('Maior de idade')\nelse:\n    print('Menor de idade')` Qual será a saída?", "opcoes": ["Maior de idade", "Menor de idade", "Nenhum dos dois (erro).", "17", "Verdadeiro"], "correta": "2"}
                ],
                "Intermediário": [
                    {"titulo": "Listas e Como Iterar Sobre Elas", "pergunta": "Qual a forma MAIS comum de percorrer todos os elementos de uma lista em Python?", "opcoes": ["Usando uma instrução `if`.", "Usando um laço `for`.", "Usando uma função matemática.", "Usando a instrução `print`.", "Usando a instrução `return`."], "correta": "2"},
                    {"titulo": "Criando e Usando Funções", "pergunta": "Em Python, qual o principal benefício de definir e usar funções?", "opcoes": ["Elas tornam o código mais longo e difícil de entender.", "Elas permitem reutilizar blocos de código, organizar o programa e evitar repetição.", "Elas servem apenas para realizar cálculos complexos.", "Elas aumentam o consumo de memória do programa.", "Elas tornam o código mais difícil de debugar."], "correta": "2"},
                    {"titulo": "Dicionários: Pares Chave-Valor", "pergunta": "Um dicionário em Python é uma coleção que armazena dados na forma de:", "opcoes": ["Uma lista ordenada de valores.", "Pares de chave e valor, onde cada chave é única.", "Apenas números inteiros.", "Uma sequência de caracteres.", "Uma coleção de funções."], "correta": "2"}
                ],
                "Avançado": [
                    {"titulo": "Manipulação Básica de Arquivos", "pergunta": "Para adicionar novas linhas de texto a um arquivo existente sem apagar o conteúdo anterior em Python, qual modo de abertura de arquivo você usaria?", "opcoes": ["'r' (read - leitura)", "'w' (write - escrita, sobrescreve o arquivo)", "'a' (append - adição, escreve no final)", "'x' (exclusive creation - criação exclusiva)", "'t' (text mode - modo texto)"], "correta": "3"},
                    {"titulo": "Lidando com Erros: Exceções", "pergunta": "Em Python, o que é uma exceção?", "opcoes": ["Um tipo especial de variável.", "Um erro que ocorre durante a execução do programa e interrompe seu fluxo normal.", "Uma função usada para criar loops.", "Um tipo de dado numérico.", "Uma palavra reservada da linguagem."], "correta": "2"},
                    {"titulo": "Introdução à Programação Orientada a Objetos (POO)", "pergunta": "Na Programação Orientada a Objetos (POO) em Python, o que é uma 'classe'?", "opcoes": ["Um valor numérico.", "Um tipo de erro.", "Um modelo ou 'molde' usado para criar objetos (instâncias), definindo seus atributos (propriedades) e métodos (comportamentos).", "Uma função que retorna um valor booleano.", "Um tipo de laço de repetição."], "correta": "3"}
                ]
            }
        }
        with open(ARQUIVO_AULAS_PERGUNTAS, 'w') as f:
            json.dump(aulas_perguntas, f, indent=4)

    # Nova estrutura para aulas teóricas (mantida a mesma)
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
                    {"titulo": "Estruturas Condicionais em Python (if, elif, else)", "pergunta": "Dado o código Python: `idade = 17\nif idade >= 18:\n    print('Maior de idade')\nelse:\n    print('Menor de idade')` Qual será a saída?", "opcoes": ["Maior de idade", "Menor de idade", "Nenhum dos dois (erro).", "17", "Verdadeiro"], "correta": "2"}
                ],
                "Intermediário": [
                    {"titulo": "Listas e Como Iterar Sobre Elas", "pergunta": "Qual a forma MAIS comum de percorrer todos os elementos de uma lista em Python?", "opcoes": ["Usando uma instrução `if`.", "Usando um laço `for`.", "Usando uma função matemática.", "Usando a instrução `print`.", "Usando a instrução `return`."], "correta": "2"},
                    {"titulo": "Criando e Usando Funções", "pergunta": "Em Python, qual o principal benefício de definir e usar funções?", "opcoes": ["Elas tornam o código mais longo e difícil de entender.", "Elas permitem reutilizar blocos de código, organizar o programa e evitar repetição.", "Elas servem apenas para realizar cálculos complexos.", "Elas aumentam o consumo de memória do programa.", "Elas tornam o código mais difícil de debugar."], "correta": "2"},
                    {"titulo": "Dicionários: Pares Chave-Valor", "pergunta": "Um dicionário em Python é uma coleção que armazena dados na forma de:", "opcoes": ["Uma lista ordenada de valores.", "Pares de chave e valor, onde cada chave é única.", "Apenas números inteiros.", "Uma sequência de caracteres.", "Uma coleção de funções."], "correta": "2"}
                ],
                "Avançado": [
                    {"titulo": "Manipulação Básica de Arquivos", "pergunta": "Para adicionar novas linhas de texto a um arquivo existente sem apagar o conteúdo anterior em Python, qual modo de abertura de arquivo você usaria?", "opcoes": ["'r' (read - leitura)", "'w' (write - escrita, sobrescreve o arquivo)", "'a' (append - adição, escreve no final)", "'x' (exclusive creation - criação exclusiva)", "'t' (text mode - modo texto)"], "correta": "3"},
                    {"titulo": "Lidando com Erros: Exceções", "pergunta": "Em Python, o que é uma exceção?", "opcoes": ["Um tipo especial de variável.", "Um erro que ocorre durante a execução do programa e interrompe seu fluxo normal.", "Uma função usada para criar loops.", "Um tipo de dado numérico.", "Uma palavra reservada da linguagem."], "correta": "2"},
                    {"titulo": "Introdução à Programação Orientada a Objetos (POO)", "pergunta": "Na Programação Orientada a Objetos (POO) em Python, o que é uma 'classe'?", "opcoes": ["Um valor numérico.", "Um tipo de erro.", "Um modelo ou 'molde' usado para criar objetos (instâncias), definindo seus atributos (propriedades) e métodos (comportamentos).", "Uma função que retorna um valor booleano.", "Um tipo de laço de repetição."], "correta": "3"}
                ]
            }
        }
        with open(ARQUIVO_AULAS_PERGUNTAS, 'w') as f:
            json.dump(aulas_perguntas, f, indent=4)

    # Nova estrutura para aulas teóricas (mantida a mesma)
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
                    {"titulo": "Variáveis e Tipos de Dados Fundamentais", "pergunta": "Em Python, qual o tipo de dado mais adequado para armazenar a frase 'Olá, mundo!'?", "opcoes": ["Integer (int).", "String (str).", "Boolean (bool).", "Float (float).", "List (list)."], "correta": "2"},
                    {"titulo": "Operadores Matemáticos e de Comparação", "pergunta": "Qual o resultado da expressão Python: `(5 * 2) - 3`?", "opcoes": ["7", "10", "13", "8", "9"], "correta": "1"},
                     {"titulo": "Estruturas Condicionais em Python", "pergunta": "Dado o código Python: `idade = 17\nif idade >= 18:\n    print('Maior de idade')\nelse:\n    print('Menor de idade')` Qual será a saída?", "opcoes": ["Maior de idade", "Menor de idade", "Nenhum dos dois (erro).", "17", "Verdadeiro"], "correta": "2"}
                ],
                "Intermediário": [
                    {"titulo": "Listas e Como Iterar Sobre Elas", "pergunta": "Qual a forma MAIS comum de percorrer todos os elementos de uma lista em Python?", "opcoes": ["Usando uma instrução `if`.", "Usando um laço `for`.", "Usando uma função matemática.", "Usando a instrução `print`.", "Usando a instrução `return`."], "correta": "2"},
                    {"titulo": "Criando e Usando Funções", "pergunta": "Em Python, qual o principal benefício de definir e usar funções?", "opcoes": ["Elas tornam o código mais longo e difícil de entender.", "Elas permitem reutilizar blocos de código, organizar o programa e evitar repetição.", "Elas servem apenas para realizar cálculos complexos.", "Elas aumentam o consumo de memória do programa.", "Elas tornam o código mais difícil de debugar."], "correta": "2"},
                    {"titulo": "Dicionários: Pares Chave-Valor", "pergunta": "Um dicionário em Python é uma coleção que armazena dados na forma de:", "opcoes": ["Uma lista ordenada de valores.", "Pares de chave e valor, onde cada chave é única.", "Apenas números inteiros.", "Uma sequência de caracteres.", "Uma coleção de funções."], "correta": "2"}
                ],
                "Avançado": [
                    {"titulo": "Manipulação Básica de Arquivos", "pergunta": "Para adicionar novas linhas de texto a um arquivo existente sem apagar o conteúdo anterior em Python, qual modo de abertura de arquivo você usaria?", "opcoes": ["'r' (read - leitura)", "'w' (write - escrita, sobrescreve o arquivo)", "'a' (append - adição, escreve no final)", "'x' (exclusive creation - criação exclusiva)", "'t' (text mode - modo texto)"], "correta": "3"},
                    {"titulo": "Lidando com Erros: Exceções", "pergunta": "Em Python, o que é uma exceção?", "opcoes": ["Um tipo especial de variável.", "Um erro que ocorre durante a execução do programa e interrompe seu fluxo normal.", "Uma função usada para criar loops.", "Um tipo de dado numérico.", "Uma palavra reservada da linguagem."], "correta": "2"},
                    {"titulo": "Introdução à Programação Orientada a Objetos (POO)", "pergunta": "Na Programação Orientada a Objetos (POO) em Python, o que é uma 'classe'?", "opcoes": ["Um valor numérico.", "Um tipo de erro.", "Um modelo ou 'molde' usado para criar objetos (instâncias), definindo seus atributos (propriedades) e métodos (comportamentos).", "Uma função que retorna um valor booleano.", "Um tipo de laço de repetição."], "correta": "3"}
                ]
            }
        }
        with open(ARQUIVO_AULAS_PERGUNTAS, 'w') as f:
            json.dump(aulas_perguntas, f, indent=4)

    # Nova estrutura para aulas teóricas (mantida a mesma)
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
                    {"titulo": "Variáveis e Tipos de Dados Fundamentais", "pergunta": "Em Python, qual o tipo de dado mais adequado para armazenar a frase 'Olá, mundo!'?", "opcoes": ["Integer (int).", "String (str).", "Boolean (bool).", "Float (float).", "List (list)."], "correta": "2"},
                    {"titulo": "Operadores Matemáticos e de Comparação", "pergunta": "Qual o resultado da expressão Python: `(5 * 2) - 3`?", "opcoes": ["7", "10", "13", "8", "9"], "correta": "1"},
                     {"titulo": "Estruturas Condicionais em Python", "pergunta": "Dado o código Python: `idade = 17\nif idade >= 18:\n    print('Maior de idade')\nelse:\n    print('Menor de idade')` Qual será a saída?", "opcoes": ["Maior de idade", "Menor de idade", "Nenhum dos dois (erro).", "17", "Verdadeiro"], "correta": "2"}
                ],
                "Intermediário": [
                    {"titulo": "Listas e Como Iterar Sobre Elas", "pergunta": "Qual a forma MAIS comum de percorrer todos os elementos de uma lista em Python?", "opcoes": ["Usando uma instrução `if`.", "Usando um laço `for`.", "Usando uma função matemática.", "Usando a instrução `print`.", "Usando a instrução `return`."], "correta": "2"},
                    {"titulo": "Criando e Usando Funções", "pergunta": "Em Python, qual o principal benefício de definir e usar funções?", "opcoes": ["Elas tornam o código mais longo e difícil de entender.", "Elas permitem reutilizar blocos de código, organizar o programa e evitar repetição.", "Elas servem apenas para realizar cálculos complexos.", "Elas aumentam o consumo de memória do programa.", "Elas tornam o código mais difícil de debugar."], "correta": "2"},
                    {"titulo": "Dicionários: Pares Chave-Valor", "pergunta": "Um dicionário em Python é uma coleção que armazena dados na forma de:", "opcoes": ["Uma lista ordenada de valores.", "Pares de chave e valor, onde cada chave é única.", "Apenas números inteiros.", "Uma sequência de caracteres.", "Uma coleção de funções."], "correta": "2"}
                ],
                "Avançado": [
                    {"titulo": "Manipulação Básica de Arquivos", "pergunta": "Para adicionar novas linhas de texto a um arquivo existente sem apagar o conteúdo anterior em Python, qual modo de abertura de arquivo você usaria?", "opcoes": ["'r' (read - leitura)", "'w' (write - escrita, sobrescreve o arquivo)", "'a' (append - adição, escreve no final)", "'x' (exclusive creation - criação exclusiva)", "'t' (text mode - modo texto)"], "correta": "3"},
                    {"titulo": "Lidando com Erros: Exceções", "pergunta": "Em Python, o que é uma exceção?", "opcoes": ["Um tipo especial de variável.", "Um erro que ocorre durante a execução do programa e interrompe seu fluxo normal.", "Uma função usada para criar loops.", "Um tipo de dado numérico.", "Uma palavra reservada da linguagem."], "correta": "2"},
                    {"titulo": "Introdução à Programação Orientada a Objetos (POO)", "pergunta": "Na Programação Orientada a Objetos (POO) em Python, o que é uma 'classe'?", "opcoes": ["Um valor numérico.", "Um tipo de erro.", "Um modelo ou 'molde' usado para criar objetos (instâncias), definindo seus atributos (propriedades) e métodos (comportamentos).", "Uma função que retorna um valor booleano.", "Um tipo de laço de repetição."], "correta": "3"}
                ]
            }
        }
        with open(ARQUIVO_AULAS_PERGUNTAS, 'w') as f:
            json.dump(aulas_perguntas, f, indent=4)

    # Nova estrutura para aulas teóricas (mantida a mesma)
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
                    {"titulo": "Variáveis e Tipos de Dados Fundamentais", "conteudo": "Em Python, qual o tipo de dado mais adequado para armazenar a frase 'Olá, mundo!'?", "opcoes": ["Integer (int).", "String (str).", "Boolean (bool).", "Float (float).", "List (list)."], "correta": "2"},
                    {"titulo": "Operadores Matemáticos e de Comparação", "conteudo": "Qual o resultado da expressão Python: `(5 * 2) - 3`?", "opcoes": ["7", "10", "13", "8", "9"], "correta": "1"},
                     {"titulo": "Estruturas Condicionais em Python", "conteudo": "Dado o código Python: `idade = 17\nif idade >= 18:\n    print('Maior de idade')\nelse:\n    print('Menor de idade')` Qual será a saída?", "opcoes": ["Maior de idade", "Menor de idade", "Nenhum dos dois (erro).", "17", "Verdadeiro"], "correta": "2"}
                ],
                "Intermediário": [
                    {"titulo": "Listas e Como Iterar Sobre Elas", "conteudo": "Qual a forma MAIS comum de percorrer todos os elementos de uma lista em Python?", "opcoes": ["Usando uma instrução `if`.", "Usando um laço `for`.", "Usando uma função matemática.", "Usando a instrução `print`.", "Usando a instrução `return`."], "correta": "2"},
                    {"titulo": "Criando e Usando Funções", "conteudo": "Em Python, qual o principal benefício de definir e usar funções?", "opcoes": ["Elas tornam o código mais longo e difícil de entender.", "Elas permitem reutilizar blocos de código, organizar o programa e evitar repetição.", "Elas servem apenas para realizar cálculos complexos.", "Elas aumentam o consumo de memória do programa.", "Elas tornam o código mais difícil de debugar."], "correta": "2"},
                    {"titulo": "Dicionários: Pares Chave-Valor", "conteudo": "Um dicionário em Python é uma coleção que armazena dados na forma de:", "opcoes": ["Uma lista ordenada de valores.", "Pares de chave e valor, onde cada chave é única.", "Apenas números inteiros.", "Uma sequência de caracteres.", "Uma coleção de funções."], "correta": "2"}
                ],
                "Avançado": [
                    {"titulo": "Manipulação Básica de Arquivos", "conteudo": "Para adicionar novas linhas de texto a um arquivo existente sem apagar o conteúdo anterior em Python, qual modo de abertura de arquivo você usaria?", "opcoes": ["'r' (read - leitura)", "'w' (write - escrita, sobrescreve o arquivo)", "'a' (append - adição, escreve no final)", "'x' (exclusive creation - criação exclusiva)", "'t' (text mode - modo texto)"], "correta": "3"},
                    {"titulo": "Lidando com Erros: Exceções", "conteudo": "Em Python, o que é uma exceção?", "opcoes": ["Um tipo especial de variável.", "Um erro que ocorre durante a execução do programa e interrompe seu fluxo normal.", "Uma função usada para criar loops.", "Um tipo de dado numérico.", "Uma palavra reservada da linguagem."], "correta": "2"},
                    {"titulo": "Introdução à Programação Orientada a Objetos (POO)", "conteudo": "Na Programação Orientada a Objetos (POO) em Python, o que é uma 'classe'?", "opcoes": ["Um valor numérico.", "Um tipo de erro.", "Um modelo ou 'molde' usado para criar objetos (instâncias), definindo seus atributos (propriedades) e métodos (comportamentos).", "Uma função que retorna um valor booleano.", "Um tipo de laço de repetição."], "correta": "3"}
                ]
            }
        }
        with open(ARQUIVO_AULAS_PERGUNTAS, 'w') as f:
            json.dump(aulas_perguntas, f, indent=4)

    # Nova estrutura para aulas teóricas (mantida a mesma)
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
                    {"titulo": "Variáveis e Tipos de Dados Fundamentais", "conteudo": "Em Python, qual o tipo de dado mais adequado para armazenar a frase 'Olá, mundo!'?", "opcoes": ["Integer (int).", "String (str).", "Boolean (bool).", "Float (float).", "List (list)."], "correta": "2"},
                    {"titulo": "Operadores Matemáticos e de Comparação", "conteudo": "Qual o resultado da expressão Python: `(5 * 2) - 3`?", "opcoes": ["7", "10", "13", "8", "9"], "correta": "1"},
                    {"titulo": "Estruturas Condicionais em Python", "conteudo": "Dado o código Python: `idade = 17\nif idade >= 18:\n    print('Maior de idade')\nelse:\n    print('Menor de idade')` Qual será a saída?", "opcoes": ["Maior de idade", "Menor de idade", "Nenhum dos dois (erro).", "17", "Verdadeiro"], "correta": "2"}
                ],
                "Intermediário": [
                    {"titulo": "Listas e Como Iterar Sobre Elas", "conteudo": "Qual a forma MAIS comum de percorrer todos os elementos de uma lista em Python?", "opcoes": ["Usando uma instrução `if`.", "Usando um laço `for`.", "Usando uma função matemática.", "Usando a instrução `print`.", "Usando a instrução `return`."], "correta": "2"},
                    {"titulo": "Criando e Usando Funções", "conteudo": "Em Python, qual o principal benefício de definir e usar funções?", "opcoes": ["Elas tornam o código mais longo e difícil de entender.", "Elas permitem reutilizar blocos de código, organizar o programa e evitar repetição.", "Elas servem apenas para realizar cálculos complexos.", "Elas aumentam o consumo de memória do programa.", "Elas tornam o código mais difícil de debugar."], "correta": "2"},
                    {"titulo": "Dicionários: Pares Chave-Valor", "conteudo": "Um dicionário em Python é uma coleção que armazena dados na forma de:", "opcoes": ["Uma lista ordenada de valores.", "Pares de chave e valor, onde cada chave é única.", "Apenas números inteiros.", "Uma sequência de caracteres.", "Uma coleção de funções."], "correta": "2"}
                ],
                "Avançado": [
                    {"titulo": "Manipulação Básica de Arquivos", "conteudo": "Para adicionar novas linhas de texto a um arquivo existente sem apagar o conteúdo anterior em Python, qual modo de abertura de arquivo você usaria?", "opcoes": ["'r' (read - leitura)", "'w' (write - escrita, sobrescreve o arquivo)", "'a' (append - adição, escreve no final)", "'x' (exclusive creation - criação exclusiva)", "'t' (text mode - modo texto)"], "correta": "3"},
                    {"titulo": "Lidando com Erros: Exceções", "conteudo": "Em Python, o que é uma exceção?", "opcoes": ["Um tipo especial de variável.", "Um erro que ocorre durante a execução do programa e interrompe seu fluxo normal.", "Uma função usada para criar loops.", "Um tipo de dado numérico.", "Uma palavra reservada da linguagem."], "correta": "2"},
                    {"titulo": "Introdução à Programação Orientada a Objetos (POO)", "conteudo": "Na Programação Orientada a Objetos (POO) em Python, o que é uma 'classe'?", "opcoes": ["Um valor numérico.", "Um tipo de erro.", "Um modelo ou 'molde' usado para criar objetos (instâncias), definindo seus atributos (propriedades) e métodos (comportamentos).", "Uma função que retorna um valor booleano.", "Um tipo de laço de repetição."], "correta": "3"}
                ]
            }
        }
        with open(ARQUIVO_AULAS_PERGUNTAS, 'w') as f:
            json.dump(aulas_perguntas, f, indent=4)

    # Nova estrutura para aulas teóricas (mantida a mesma)
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
                    {"titulo": "Variáveis e Tipos de Dados Fundamentais", "conteudo": "Em Python, qual o tipo de dado mais adequado para armazenar a frase 'Olá, mundo!'?", "opcoes": ["Integer (int).", "String (str).", "Boolean (bool).", "Float (float).", "List (list)."], "correta": "2"},
                    {"titulo": "Operadores Matemáticos e de Comparação", "conteudo": "Qual o resultado da expressão Python: `(5 * 2) - 3`?", "opcoes": ["7", "10", "13", "8", "9"], "correta": "1"},
                    {"titulo": "Estruturas Condicionais em Python", "conteudo": "Dado o código Python: `idade = 17\nif idade >= 18:\n    print('Maior de idade')\nelse:\n    print('Menor de idade')` Qual será a saída?", "opcoes": ["Maior de idade", "Menor de idade", "Nenhum dos dois (erro).", "17", "Verdadeiro"], "correta": "2"}
                ],
                "Intermediário": [
                    {"titulo": "Listas e Como Iterar Sobre Elas", "conteudo": "Qual a forma MAIS comum de percorrer todos os elementos de uma lista em Python?", "opcoes": ["Usando uma instrução `if`.", "Usando um laço `for`.", "Usando uma função matemática.", "Usando a instrução `print`.", "Usando a instrução `return`."], "correta": "2"},
                    {"titulo": "Criando e Usando Funções", "conteudo": "Em Python, qual o principal benefício de definir e usar funções?", "opcoes": ["Elas tornam o código mais longo e difícil de entender.", "Elas permitem reutilizar blocos de código, organizar o programa e evitar repetição.", "Elas servem apenas para realizar cálculos complexos.", "Elas aumentam o consumo de memória do programa.", "Elas tornam o código mais difícil de debugar."], "correta": "2"},
                    {"titulo": "Dicionários: Pares Chave-Valor", "conteudo": "Um dicionário em Python é uma coleção que armazena dados na forma de:", "opcoes": ["Uma lista ordenada de valores.", "Pares de chave e valor, onde cada chave é única.", "Apenas números inteiros.", "Uma sequência de caracteres.", "Uma coleção de funções."], "correta": "2"}
                ],
                "Avançado": [
                    {"titulo": "Manipulação Básica de Arquivos", "conteudo": "Para adicionar novas linhas de texto a um arquivo existente sem apagar o conteúdo anterior em Python, qual modo de abertura de arquivo você usaria?", "opcoes": ["'r' (read - leitura)", "'w' (write - escrita, sobrescreve o arquivo)", "'a' (append - adição, escreve no final)", "'x' (exclusive creation - criação exclusiva)", "'t' (text mode - modo texto)"], "correta": "3"},
                    {"titulo": "Lidando com Erros: Exceções", "conteudo": "Em Python, o que é uma exceção?", "opcoes": ["Um tipo especial de variável.", "Um erro que ocorre durante a execução do programa e interrompe seu fluxo normal.", "Uma função usada para criar loops.", "Um tipo de dado numérico.", "Uma palavra reservada da linguagem."], "correta": "2"},
                    {"titulo": "Introdução à Programação Orientada a Objetos (POO)", "conteudo": "Na Programação Orientada a Objetos (POO) em Python, o que é uma 'classe'?", "opcoes": ["Um valor numérico.", "Um tipo de erro.", "Um modelo ou 'molde' usado para criar objetos (instâncias), definindo seus atributos (propriedades) e métodos (comportamentos).", "Uma função que retorna um valor booleano.", "Um tipo de laço de repetição."], "correta": "3"}
                ]
            }
        }
        with open(ARQUIVO_AULAS_PERGUNTAS, 'w') as f:
            json.dump(aulas_perguntas, f, indent=4)

    # Nova estrutura para aulas teóricas (mantida a mesma)
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
                    {"titulo": "Variáveis e Tipos de Dados Fundamentais", "pergunta": "Em Python, qual o tipo de dado mais adequado para armazenar a frase 'Olá, mundo!'?", "opcoes": ["Integer (int).", "String (str).", "Boolean (bool).", "Float (float).", "List (list)."], "correta": "2"},
                    {"titulo": "Operadores Matemáticos e de Comparação", "pergunta": "Qual o resultado da expressão Python: `(5 * 2) - 3`?", "opcoes": ["7", "10", "13", "8", "9"], "correta": "1"},
                     {"titulo": "Estruturas Condicionais em Python", "pergunta": "Dado o código Python: `idade = 17\nif idade >= 18:\n    print('Maior de idade')\nelse:\n    print('Menor de idade')` Qual será a saída?", "opcoes": ["Maior de idade", "Menor de idade", "Nenhum dos dois (erro).", "17", "Verdadeiro"], "correta": "2"}
                ],
                "Intermediário": [
                    {"titulo": "Listas e Como Iterar Sobre Elas", "pergunta": "Qual a forma MAIS comum de percorrer todos os elementos de uma lista em Python?", "opcoes": ["Usando uma instrução `if`.", "Usando um laço `for`.", "Usando uma função matemática.", "Usando a instrução `print`.", "Usando a instrução `return`."], "correta": "2"},
                    {"titulo": "Criando e Usando Funções", "pergunta": "Em Python, qual o principal benefício de definir e usar funções?", "opcoes": ["Elas tornam o código mais longo e difícil de entender.", "Elas permitem reutilizar blocos de código, organizar o programa e evitar repetição.", "Elas servem apenas para realizar cálculos complexos.", "Elas aumentam o consumo de memória do programa.", "Elas tornam o código mais difícil de debugar."], "correta": "2"},
                    {"titulo": "Dicionários: Pares Chave-Valor", "pergunta": "Um dicionário em Python é uma coleção que armazena dados na forma de:", "opcoes": ["Uma lista ordenada de valores.", "Pares de chave e valor, onde cada chave é única.", "Apenas números inteiros.", "Uma sequência de caracteres.", "Uma coleção de funções."], "correta": "2"}
                ],
                "Avançado": [
                    {"titulo": "Manipulação Básica de Arquivos", "pergunta": "Para adicionar novas linhas de texto a um arquivo existente sem apagar o conteúdo anterior em Python, qual modo de abertura de arquivo você usaria?", "opcoes": ["'r' (read - leitura)", "'w' (write - escrita, sobrescreve o arquivo)", "'a' (append - adição, escreve no final)", "'x' (exclusive creation - criação exclusiva)", "'t' (text mode - modo texto)"], "correta": "3"},
                    {"titulo": "Lidando com Erros: Exceções", "pergunta": "Em Python, o que é uma exceção?", "opcoes": ["Um tipo especial de variável.", "Um erro que ocorre durante a execução do programa e interrompe seu fluxo normal.", "Uma função usada para criar loops.", "Um tipo de dado numérico.", "Uma palavra reservada da linguagem."], "correta": "2"},
                    {"titulo": "Introdução à Programação Orientada a Objetos (POO)", "pergunta": "Na Programação Orientada a Objetos (POO) em Python, o que é uma 'classe'?", "opcoes": ["Um valor numérico.", "Um tipo de erro.", "Um modelo ou 'molde' usado para criar objetos (instâncias), definindo seus atributos (propriedades) e métodos (comportamentos).", "Uma função que retorna um valor booleano.", "Um tipo de laço de repetição."], "correta": "3"}
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
        # Garante que sempre imprimirá 5 opções se a lista tiver 5
        for i, op in enumerate(opcoes, 1):
            print(f"[{i}] {op}")
        escolha = input(pergunta + " ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes): # Verifica se a escolha é um número válido dentro do range de opções
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
                     # Mostrar progresso nas perguntas (opcional, mas consistente com teóricas)
                    total_aulas_nivel = len(aulas_perguntas[modulo][nivel])
                    aulas_concluidas_nivel = len(progresso.get(modulo, {}).get(nivel, []))
                    status = f"({aulas_concluidas_nivel}/{total_aulas_nivel} concluídas)"
                    print(f"[{i}] {nivel} {status}")

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
                        # Agora input_opcao_valida garantirá 5 opções são mostradas se disponíveis
                        resp = input_opcao_valida("Sua resposta", aula["opcoes"])

                        # Note: a correção ainda usa o índice da opção na lista
                        if resp == aula["correta"]:
                            print("✅ Correto!")
                        else:
                            # Mostra a resposta correta usando o índice salvo
                            indice_correta = int(aula["correta"]) - 1 # Converte "1", "2", etc. para índice 0, 1, etc.
                            print(f"❌ Incorreto. Resposta correta: {aula['opcoes'][indice_correta]}")
                        # Marca a aula de pergunta como concluída
                        progresso[modulo][nivel].append(aula["titulo"])
                        usuarios[usuario]["progresso"]["perguntas"] = progresso
                        salvar_usuarios(usuarios)

                    # Verifica se todas as aulas de pergunta do nível foram concluídas
                    total_aulas_nivel = len(aulas_perguntas[modulo][nivel])
                    aulas_concluidas_nivel = len(progresso.get(modulo, {}).get(nivel, []))
                    if aulas_concluidas_nivel == total_aulas_nivel:
                         print(f"\n🎉 Nível {nivel} de Perguntas concluído!")
                    else:
                         print(f"\nContinuando no Nível {nivel} de Perguntas. {aulas_concluidas_nivel}/{total_aulas_nivel} aulas concluídas.")


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
                if escolha_nivel.isdigit() and 1 <= int(escolha_nivel) and int(escolha_nivel) <= len(niveis):
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