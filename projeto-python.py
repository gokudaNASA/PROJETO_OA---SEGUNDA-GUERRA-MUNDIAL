import string
import random
#Biblioteca que auxilia para limpar certas partes do código com a intenção de despertar o interesse do usuário
import os
#Biblioteca usada para dar uma pausa em determinado trechos do código, com o objetivo de não ficar com uma leitura cansativa
from time import sleep
#Biblioteca usada para imprimir mesnsagens com diferentes cores, com o objetivo de chamar a atenção do usuário
from colorama import Fore, Style

#Subprograma que irá apresentar um menu interativo
def menu_principal():
    print(Fore.CYAN + '\nSiga o menu abaixo:\n')
    opcoes = ['[1] Introdução e início da Guerra'
            '\n[2] Campo de Batalha'
            '\n[3] Fim da Guerra'
            '\n[4] Quiz geral'
            '\n[5] Caça - Palavras'
            '\n[6] Material de apoio'
            '\n[7] Sair']

    print(Fore.GREEN + '\n'.join(opcoes))


#Subprograma para apresentar os subtópicos do menu principal
def menu_CampoDeBatalha():
    print(Fore.CYAN + f'\nSiga o menu dos Subtópicos tópico escolhido anteriormente:\n')
    opcoes = ['[1] Países na guerra'
            '\n[2] Líderes e seus feitos'
            '\n[3] Principais Batalhas'
            '\n[4] Menu Principal'
            '\n[5] Sair']

    print(Fore.GREEN + '\n'.join(opcoes))


#Subprograma para apresentar os subtópicos do menu principal
def menu_FimDaGuerra():
    print(Fore.CYAN + f'\nSiga o menu dos Subtópicos tópico escolhido anteriormente:\n')
    opcoes = ['[1] Armas'
            '\n[2] Consequências'
            '\n[3] Menu Principal'
            '\n[4] Sair']

    print(Fore.GREEN + '\n'.join(opcoes))


def explicacao_CampoDeBatalha():
    decisao_menuCampoDeBatalha = int(input(Fore.CYAN + '\nDigite um número para o seu respectivo subtema (APÓS DIGITAR, APERTE A TECLA ENTER): '))
    if decisao_menuCampoDeBatalha == 1:
        limpar()
        print(Fore.WHITE + '~'*100)
        print(Fore.CYAN + '                 Países envolvidos na Guerra               ')
        print(Fore.WHITE + '~'*100)
        print(Fore.WHITE + f'A {Fore.YELLOW} Segunda Guerra Mundial {Fore.WHITE} envolveu dois grandes blocos: o {Fore.YELLOW}EIXO {Fore.WHITE}e os {Fore.YELLOW}ALIADOS.\n')
        print(Fore.WHITE + f'O {Fore.CYAN}EIXO {Fore.WHITE}era composto principalmente pela {Fore.CYAN}Alemanha, Itália e Japão {Fore.WHITE}. A {Fore.CYAN} Alemanha {Fore.WHITE}, sob a liderança de Adolf Hitler, e a {Fore.CYAN}Itália {Fore.WHITE}, sob Benito Mussolini, eram governadas por regimes totalitários que buscavam a expansão territorial. O {Fore.CYAN}Japão {Fore.WHITE}também buscava expandir seu império no Pacífico. ')
        print(Fore.WHITE + f'Já os {Fore.YELLOW}ALIADOS {Fore.WHITE}eram compostos principalmente pelo {Fore.YELLOW} Reino Unido, França, União Soviética, Estados Unidos e China. {Fore.WHITE} Esses países se uniram para resistir à agressão e ao expansionismo das Potências do Eixo.')
        print(Fore.WHITE + f'Além desses principais membros, muitos outros países também estiveram envolvidos no conflito. Alguns, como a {Fore.YELLOW} Romênia{Fore.WHITE} e a {Fore.YELLOW}Hungria {Fore.WHITE}, apoiaram o Eixo, enquanto outros, como a {Fore.YELLOW}Bélgica, Austrália, Dinamarca, Canadá, Noruega, Nova Zelândia, Índia, Holanda, Brasil, Grécia, Iugoslávia, África do Sul, Estônia {Fore.WHITE}e {Fore.YELLOW}Lituânia {Fore.WHITE}, apoiaram os Aliados.')
        
        decisao_final = input(f'\n{Fore.CYAN}Deseja voltar para o menu principal? digite {Fore.RED}M {Fore.CYAN}(para menu principal) ou digite {Fore.RED}Mc {Fore.CYAN}(para menu campo de batalha) (APÓS DIGITAR, APERTE A TECLA ENTER): ')
        if decisao_final == 'M' or decisao_final == 'm':
            limpar()
            menu_principal()
            explicacao()
            limpar()

        else:
            limpar()
            menu_CampoDeBatalha()
            explicacao_CampoDeBatalha()
            limpar()
            
    elif decisao_menuCampoDeBatalha == 2:
        limpar()
        print(Fore.WHITE + '~'*70)
        print(Fore.CYAN + '                 Principais Líderes               ')
        print(Fore.WHITE + '~'*70)
        print(Fore.WHITE + f'{Fore.GREEN}ADOLF HITLER (Alemanha): {Fore.WHITE}Hitler, também conhecido como Führer, foi o fundador do Partido Nazista e iniciou a Segunda Guerra com a invasão da Polônia em 1939. Sob sua liderança, o regime nazista executou um dos maiores genocídios da história, matando pelo menos 6 milhões de judeus e milhões de outras pessoas consideradas “sub-humanas” ou "indesejáveis".')
        print(Fore.WHITE + f'{Fore.GREEN}BENEDITO MUSSOLINI (Itália): {Fore.WHITE}Mussolini, conhecido como Duce, foi um dos fundadores do fascismo e tornou a Itália uma das potências do grupo do Eixo. Ele defendia o nacionalismo, o expansionismo, o progresso social e o anticomunismo.')
        print(Fore.WHITE + f'{Fore.GREEN}CHARLES DE GAULLE (França): {Fore.WHITE}De Gaulle foi uma figura central na Segunda Guerra, liderando o movimento Franceses Livres e sendo chefe provisório do governo francês após a libertação do país1. Ele resistiu bravamente às investidas da Alemanha nazista até conseguir retomar o controle das colônias.')
        print(Fore.WHITE + f'{Fore.GREEN}WISNTON CHURCHILL (Reino Unido): {Fore.WHITE}Churchill foi o Primeiro-Ministro da Inglaterra durante a Segunda Guerra. Ele desempenhou um papel crucial na liderança do Reino Unido e na formação da aliança dos Aliados.')
        print(Fore.WHITE + f'{Fore.GREEN}JOSEPH STALIN (União Soviética): {Fore.WHITE}Stalin era o líder da União Soviética e desempenhou um papel crucial na resistência contra a Alemanha nazista. Ele assumiu o cargo de Primeiro-Ministro em 1941 e manteve-o até sua morte em 1953.')
        print(Fore.WHITE + f'{Fore.GREEN}HIROHITO (Japão): {Fore.WHITE}Hirohito era o imperador do Japão e liderou o país durante a Segunda Guerra Mundial. Ele desempenhou um papel crucial na expansão do Império Japonês no Pacífico.')
        
        decisao_final = input(f'\n{Fore.CYAN}Deseja voltar para o menu principal? digite {Fore.RED}M {Fore.CYAN}(para menu principal) ou digite {Fore.RED}Mc {Fore.CYAN}(para menu campo de batalha) (APÓS DIGITAR, APERTE A TECLA ENTER): ')
        if decisao_final == 'M' or decisao_final == 'm':
            limpar()
            menu_principal()
            explicacao()
            limpar()

        else:
            limpar()
            menu_CampoDeBatalha()
            explicacao_CampoDeBatalha()
            limpar()
            
    elif decisao_menuCampoDeBatalha == 3:
        limpar()
        print(Fore.WHITE + '~'*70)
        print(Fore.CYAN + '                 Principais Batalhas               ')
        print(Fore.WHITE + '~'*70)
        print(Fore.WHITE + f'{Fore.GREEN}INVASÃO DA POLÔNIA {Fore.WHITE}(1939): Marcou o início da Segunda Guerra Mundial.')
        print(Fore.WHITE + f'{Fore.GREEN}BATALHA DA GRÃ-BRETANHA {Fore.WHITE}(1940): Foi a primeira grande campanha a ser travada inteiramente por forças aéreas.')
        print(Fore.WHITE + f'{Fore.GREEN}BATALHA DA FRANÇA {Fore.WHITE}(1940): Resultou na queda da França e na sua subsequente ocupação pelas forças alemãs.')
        print(Fore.WHITE + f'{Fore.GREEN}CERCO DE LENINGRADO {Fore.WHITE}(1941): Foi um prolongado cerco militar pelas forças do Eixo contra Leningrado na Frente Oriental.')
        print(Fore.WHITE + f'{Fore.GREEN}OPERAÇÃO BARBAROSSA – IINVASÃO DA URSS {Fore.WHITE}(1941): Foi a invasão da União Soviética pelas forças do Eixo.')
        print(Fore.WHITE + f'{Fore.GREEN}BATALHA DE PEARL HARBOR {Fore.WHITE}(1941): Levou à entrada direta dos Estados Unidos na Segunda Guerra Mundial.')
        print(Fore.WHITE + f'{Fore.GREEN}BATALHA DE MIDWAY {Fore.WHITE}(1942): Foi uma das batalhas mais importantes no teatro do Pacífico.')
        print(Fore.WHITE + f'{Fore.GREEN}BATALHA DE KURSK {Fore.WHITE}(1943): Foi uma grande batalha na Frente Oriental.')
        print(Fore.WHITE + f'{Fore.GREEN}BATALHA DE STALINGRADO {Fore.WHITE}(1943): Foi uma das maiores batalhas da guerra, ocorrendo na cidade russa de Stalingrado.')
        print(Fore.WHITE + f'{Fore.GREEN}BATALHA DA NORMANDIA {Fore.WHITE}(1944): Marcou o início da libertação da Europa Ocidental do controle nazista.')

        decisao_final = input(f'\n{Fore.CYAN}Deseja voltar para o menu principal? digite {Fore.RED}M {Fore.CYAN}(para menu principal) ou digite {Fore.RED}Mc {Fore.CYAN}(para menu campo de batalha) (APÓS DIGITAR, APERTE A TECLA ENTER): ')
        if decisao_final == 'M' or decisao_final == 'm':
            limpar()
            menu_principal()
            explicacao()
            limpar()

        else:
            limpar()
            menu_CampoDeBatalha()
            explicacao_CampoDeBatalha()
            limpar()
    
    elif decisao_menuCampoDeBatalha == 4:
        limpar()
        menu_principal()
        explicacao()
        limpar()

    elif decisao_menuCampoDeBatalha == 5:
        limpar()
        if escolha == 0:
            print(Fore.WHITE + f'Bem, é aqui que acaba a nossa jornada, {saudacao_primeiro_nome}. Espero que não tenha restado nenhuma dúvida, e se sim, pode retornar a qualquer momento. Obrigado por ter escolhido - me como seu método de ensino, agradeço de coração, adeus {saudacao_primeiro_nome}.\n\n')
            print('Saindo...')
            exit()

        else:
            print(Fore.WHITE + f'Bem, é aqui que acaba a nossa jornada, {saudacao_segundo_nome}. Espero que não tenha restado nenhuma dúvida, e se sim, pode retornar a qualquer momento. Obrigado por ter escolhido - me como seu método de ensino, agradeço de coração, adeus {saudacao_segundo_nome}.\n\n')
            print('Saindo...')
            exit()    

    else:
        print('Erro. Digite um número que corresponde ao menu acima.\n')
        menu_CampoDeBatalha()
        explicacao_CampoDeBatalha()
        limpar()


def explicacao_FimDaGuerra():
    decisao_menuFimdaGuerra = int(input(Fore.CYAN + '\nDigite um número para o seu respectivo subtema (APÓS DIGITAR, APERTE A TECLA ENTER): '))
    if decisao_menuFimdaGuerra == 1:
        limpar()
        print(Fore.WHITE + '~'*50)
        print(Fore.CYAN + '                 Principais armas usadas na guerra               ')
        print(Fore.WHITE + '~'*50)
        print(Fore.WHITE + f'{Fore.GREEN}SUBMETRALHADORA THOMPSON {Fore.WHITE}: Uma submetralhadora utilizada pelos Estados Unidos.')
        print(Fore.WHITE + f'{Fore.GREEN}MÍSSEIS V-1 E V-2 {Fore.WHITE}: Estes foram alguns dos primeiros mísseis a serem usados operacionalmente, desenvolvidos pela Alemanha nazista.')
        print(Fore.WHITE + f'{Fore.GREEN}BOMBAS ATÔMICAS {Fore.WHITE}: As bombas atômicas “Little Boy” e “Fat Man” foram lançadas sobre as cidades japonesas de Hiroshima e Nagasaki, respectivamente, em agosto de 1945, marcando a primeira vez na história que armas nucleares foram usadas em combate. Estas bombas foram desenvolvidas como parte do Projeto Manhattan dos Estados Unidos.')

        decisao_final = input(f'\n{Fore.CYAN}Deseja voltar para o menu principal? digite {Fore.RED}M {Fore.CYAN}(para menu principal) ou digite {Fore.RED}Mf {Fore.CYAN}(para menu fim da guerra) (APÓS DIGITAR, APERTE A TECLA ENTER): ')
        if decisao_final == 'M' or decisao_final == 'm':
            limpar()
            menu_principal()
            explicacao()
            limpar()
        
        else:
            limpar()
            menu_FimDaGuerra()
            explicacao_FimDaGuerra()
            limpar()

    elif decisao_menuFimdaGuerra == 2:
        limpar()
        print(Fore.WHITE + '~'*50)
        print(Fore.CYAN + '                 Consequênicas               ')
        print(Fore.WHITE + '~'*50)
        print(Fore.WHITE + f'{Fore.GREEN}ASCENSÃO DOS ESTADOS UNIDOS E DA UNIÃO SOVIÉTICA {Fore.WHITE}: A guerra resultou no fortalecimento da posição dos Estados Unidos e da União Soviética no cenário mundial como duas potências mundiais.')
        print(Fore.WHITE + f'{Fore.GREEN}DIVISÃO DO MUNDO {Fore.WHITE}: O mundo foi dividido entre capitalismo e socialismo, dando início à Guerra Fria.')
        print(Fore.WHITE + f'{Fore.GREEN}CRIAÇÃO DA ONU {Fore.WHITE}: A Organização das Nações Unidas (ONU) foi criada para promover a paz e a cooperação internacional.')
        print(Fore.WHITE + f'{Fore.GREEN}LIBERTAÇÃO DOS CAMPOS DE CONCENTRAÇÃO {Fore.WHITE}: Os campos de concentração nazistas foram libertados, revelando ao mundo os horrores do Holocausto.')
        print(Fore.WHITE + f'{Fore.GREEN}PRISÃO DE OFICIAIS NAZISTAS {Fore.WHITE}: Muitos oficiais nazistas foram presos e julgados por crimes de guerra.')
        print(Fore.WHITE + f'{Fore.GREEN}MUDANÇAS GEOPOLÍTICAS {Fore.WHITE}: Novos países surgiram e as fronteiras de alguns países foram redesenhadas')
        print(Fore.WHITE + f'{Fore.GREEN}PERDAS HUMANAS E ECONÔMICAS {Fore.WHITE}: A guerra resultou na morte de aproximadamente 45 milhões de pessoas e deixou 35 milhões de feridos. Além disso, o conflito custou 1 trilhão e 385 bilhões de dólares em perdas monetárias.')
        print(Fore.WHITE + f'{Fore.GREEN}USO DE ARMAS NUCLEARES {Fore.WHITE}: As bombas atômicas “Little Boy” e “Fat Man” foram lançadas sobre as cidades japonesas de Hiroshima e Nagasaki, respectivamente, marcando a primeira vez na história que armas nucleares foram usadas em combate.')

        decisao_final = input(f'\n{Fore.CYAN} Deseja voltar para o menu principal? digite {Fore.RED}M {Fore.CYAN}(para menu principal) ou digite {Fore.RED}Mf {Fore.CYAN}(para menu fim da guerra) (APÓS DIGITAR, APERTE A TECLA ENTER): ')
        if decisao_final == 'M' or decisao_final == 'm':
            limpar()
            menu_principal()
            explicacao()
            limpar()
    
        else:
            limpar()
            menu_FimDaGuerra()
            explicacao_FimDaGuerra()
            limpar()

    elif decisao_menuFimdaGuerra == 3:
        limpar()
        menu_principal()
        explicacao()
        limpar()

    elif decisao_menuFimdaGuerra == 4:
        limpar()
        if escolha == 0:
            print(Fore.WHITE + f'Bem, é aqui que acaba a nossa jornada, {saudacao_primeiro_nome}. Espero que não tenha restado nenhuma dúvida, e se sim, pode retornar a qualquer momento. Obrigado por ter escolhido - me como seu método de ensino, agradeço de coração, adeus {saudacao_primeiro_nome}.\n\n')
            print('Saindo...')
            exit()

        else:
            print(Fore.WHITE + f'Bem, é aqui que acaba a nossa jornada, {saudacao_segundo_nome}. Espero que não tenha restado nenhuma dúvida, e se sim, pode retornar a qualquer momento. Obrigado por ter escolhido - me como seu método de ensino, agradeço de coração, adeus {saudacao_segundo_nome}.\n\n')
            print('Saindo...')
            exit()

    else:
        limpar()
        print('Erro. Digite um número correspondente ao menu acima.\n')
        menu_FimDaGuerra()
        explicacao_FimDaGuerra()
        limpar()


#Subprograma que irá explicar o assunto a patir do que o usuário escolheu
def explicacao():
    #Esta é uma variável que irá receber a decisão do usuário ao escolher os subtemas apresentados no subporgrama menu_principal
    decisao_menu = int(input(Fore.CYAN + '\nDigite um número para o seu respectivo tema (APÓS DIGITAR, APERTE A TECLA ENTER): '))
    
    #Se o usuário escolheu o subtema 0, irá iniciar uma breve esplicação
    if decisao_menu == 1:
        limpar()
        print(Fore.WHITE + '~'*50)
        print(Fore.CYAN + '                 Introdução               ')
        print(Fore.WHITE + '~'*50)
        print(Fore.WHITE + 'A Segunda Guerra Mundial, que ocorreu entre 1939 e 1945, foi o conflito armado de maior escala na história da humanidade. Foi iniciada com a invasão da Polônia pela Alemanha em 1º de setembro de 1939. A França e a Inglaterra declararam guerra à Alemanha em resposta a essa invasão. As principais causas da guerra estão relacionadas ao expansionismo e ao totalitarismo de países como a Alemanha, a Itália e o Japão. A ideologia nazista, que chegou ao poder na Alemanha em 1933, defendia a superioridade racial e o militarismo. A Alemanha também sofria com as consequências da derrota na Primeira Guerra Mundial, que gerou humilhação e crise econômica.\n')

        #Essa variável irá receber a decisão do usuário após concluir a explicação, que consiste em perguntar se deseja voltar ao menu ou iniciar um quiz interativo sobre o assunto escolhido
        decisao_final = input(f'{Fore.CYAN}Deseja voltar para o menu principal? digite {Fore.RED}S {Fore.CYAN}(para menu principal) ou digite {Fore.RED}N {Fore.CYAN}(para sair) (APÓS DIGITAR, APERTE A TECLA ENTER): ')
        if decisao_final == 's' or decisao_final == 'S':
            limpar()
            menu_principal()
            explicacao()
            limpar()
 
        else:
            limpar()
            if escolha == 0:
                print(Fore.WHITE + f'Bem, é aqui que acaba a nossa jornada, {saudacao_primeiro_nome}. Espero que não tenha restado nenhuma dúvida, e se sim, pode retornar a qualquer momento. Obrigado por ter escolhido - me como seu método de ensino, agradeço de coração, adeus {saudacao_primeiro_nome}.\n')
                print('Saindo...\n\n')
                exit()

            else:
                print(Fore.WHITE + f'Bem, é aqui que acaba a nossa jornada, {saudacao_segundo_nome}. Espero que não tenha restado nenhuma dúvida, e se sim, pode retornar a qualquer momento. Obrigado por ter escolhido - me como seu método de ensino, agradeço de coração, adeus {saudacao_segundo_nome}.\n')
                print('Saindo...\n\n')
                exit()

    elif decisao_menu == 2:
        limpar()
        menu_CampoDeBatalha()
        explicacao_CampoDeBatalha()
        limpar()

    elif decisao_menu == 3:
        limpar()
        menu_FimDaGuerra()
        explicacao_FimDaGuerra()
        limpar()

    elif decisao_menu == 4:
        limpar()
        quiz_geral()
    
    elif decisao_menu == 5:
        limpar()
        print(Fore.WHITE + '~'*60)
        print(Fore.CYAN + '                 Caça palavras               ')
        print(Fore.WHITE + '~'*60)

        print('\nA CRUZADINHA ABAIXO SÓ PODERÁ SER RESPONDIDA POR MEIO DE COORDENADAS, COMO POR EXEMPLO: A2 *ESPAÇO* A10. AGORA APROVEITE :)\n\n')
        # Cria uma matriz 18x18 preenchida com letras aleatórias
        matriz = [[random.choice(string.ascii_uppercase) for _ in range(18)] for _ in range(18)]

        # Adiciona algumas palavras à matriz
        palavras = [('HITLER', 'A2', 'A7'), ('STALIN', 'B2', 'G2'), ('CHURCHILL', 'C3', 'C11'), ('ARMAS', 'D3', 'H3'), ('NAZISMO', 'A18', 'G18'), ('FACISMO', 'R1', 'R7'), ('JUDEU', 'N3', 'N7'), ('BOMBA-ATÔMICA', 'A12', 'M12'), ('HOLOCAUSTO', 'A16', 'J16')]
        for palavra, inicio, fim in palavras:
            inicio_coluna = string.ascii_uppercase.index(inicio[0])
            inicio_linha = int(inicio[1:]) - 1
            fim_coluna = string.ascii_uppercase.index(fim[0])
            fim_linha = int(fim[1:]) - 1

            if inicio_linha == fim_linha:  # Palavra horizontal
                for i in range(len(palavra)):
                    matriz[inicio_linha][inicio_coluna + i] = palavra[i]
            elif inicio_coluna == fim_coluna:  # Palavra vertical
                for i in range(len(palavra)):
                    matriz[inicio_linha + i][inicio_coluna] = palavra[i]

        # Imprime o cabeçalho
        print(Fore.WHITE + '      ' + ' '.join(string.ascii_uppercase[:18]))

        print('')
        # Imprime a matriz com índice lateral
        for i, linha in enumerate(matriz, 1):
            print(f'{i:02}    ' + ' '.join(linha))

        print('\n')
        # Pergunta ao usuário as respostas
        respostas = {}
        for i, (palavra, inicio, fim) in enumerate(palavras, 1):
            resposta = input(f'{i}. {palavra}: ')
            inicio_resposta, fim_resposta = resposta.split()
            respostas[palavra] = (resposta, inicio_resposta.upper() == inicio and fim_resposta.upper() == fim)

        print('\n')
        # Imprime as respostas do usuário e se estão corretas
        for palavra, (resposta, correta) in respostas.items():
            print(f'{palavra}: {resposta} - {"Correta" if correta else "Incorreta"}')

        print('\n')

        decisao_final = input(f'{Fore.CYAN}Deseja voltar para o menu principal? digite {Fore.RED}S {Fore.CYAN}(para menu principal) ou digite {Fore.RED}N {Fore.CYAN}(para sair) (APÓS DIGITAR, APERTE A TECLA ENTER): ')
        if decisao_final == 's' or decisao_final == 'S':
            limpar()
            menu_principal()
            explicacao()
            limpar()
 
        else:
            limpar()
            if escolha == 0:
                print(Fore.WHITE + f'Bem, é aqui que acaba a nossa jornada, {saudacao_primeiro_nome}. Espero que não tenha restado nenhuma dúvida, e se sim, pode retornar a qualquer momento. Obrigado por ter escolhido - me como seu método de ensino, agradeço de coração, adeus {saudacao_primeiro_nome}.\n')
                print('Saindo...\n\n')
                exit()

            else:
                print(Fore.WHITE + f'Bem, é aqui que acaba a nossa jornada, {saudacao_segundo_nome}. Espero que não tenha restado nenhuma dúvida, e se sim, pode retornar a qualquer momento. Obrigado por ter escolhido - me como seu método de ensino, agradeço de coração, adeus {saudacao_segundo_nome}.\n')
                print('Saindo...\n\n')
                exit()

    elif decisao_menu == 6:
        limpar()
        material_de_apoio()

    elif decisao_menu == 7:
        limpar()
        if escolha == 0:
            print(Fore.WHITE + f'Bem, é aqui que acaba a nossa jornada, {saudacao_primeiro_nome}. Espero que não tenha restado nenhuma dúvida, e se sim, pode retornar a qualquer momento. Obrigado por ter escolhido - me como seu método de ensino, agradeço de coração, adeus {saudacao_primeiro_nome}.\n\n')
            print('Saindo...')
            exit()

        else:
            print(Fore.WHITE + f'Bem, é aqui que acaba a nossa jornada, {saudacao_segundo_nome}. Espero que não tenha restado nenhuma dúvida, e se sim, pode retornar a qualquer momento. Obrigado por ter escolhido - me como seu método de ensino, agradeço de coração, adeus {saudacao_segundo_nome}.\n\n')
            print('Saindo...\n')
            exit()

    else:
        print('Digite um número que corresponde ao menu exibido anteriormente: ')
        menu_principal()
        explicacao()


#Subprograma que inicia um quiz geral sobre a segunda guerra mundial
def quiz_geral():
    #Variável que irá receber as perguntas, juntamente com as alternativas e a resposta correta, sendo 10 questões no total (que abrange tudo que foi explicado durante a execução do código)
    perguntas = [
        {
            'pergunta': 'Qual país foi invadido pela Alemanha, marcando o início da Segunda Guerra Mundial?',
            "respostas": ['França', 'Polônia', 'Áustria', 'Bélgica'],
            'correta': 1
        },
        {
            'pergunta': 'Quem era o líder da Alemanha durante a Segunda Guerra Mundial?',
            'respostas': ['Winston Churchill', 'Benito Mussolini', 'Adolf Hitler', 'Franklin D. Roosevelt'],
            'correta': 2
        },
        {
            'pergunta': 'Quais países formavam o Eixo durante a Segunda Guerra Mundial?',
            'respostas': ['Alemanha, Itália e Japão', 'Estados Unidos, Reino Unido e União Soviética', 'França, Bélgica e Holanda', 'China, Coreia e Vietnã'],
            'correta': 0
        },
        {
            'pergunta': 'O que foi o Holocausto?',
            'respostas': ['A libertação da França', 'O genocídio de seis milhões de judeus', 'A queda do Muro de Berlim', 'A criação da União Europeia'],
            'correta': 1
        },
        {
            'pergunta': 'Qual foi uma das armas mais devastadoras usadas durante a guerra?',
            'respostas': ['Metralhadora', 'Bomba Atômica', 'Espada', 'Arco e Flecha'],
            'correta': 1
        },
        {
            'pergunta': 'Qual foi uma das consequências da Segunda Guerra Mundial?',
            'respostas': ['Ascensão dos Estados Unidos e da União Soviética como superpotências', 'Início da Primeira Guerra Mundial', 'Criação da Liga das Nações', 'Fim da Revolução Industrial'],
            'correta': 0
        },
        {
            'pergunta': 'Qual foi a operação militar que marcou o início do fim da Segunda Guerra Mundial na Europa?',
            'respostas': ['Operação Barbarossa', 'Batalha de Stalingrado', 'Batalha da Normandia', 'Batalha de Berlim'],
            'correta': 2
        },
        {
            'pergunta': 'Qual tecnologia de comunicação foi crucial para os Aliados durante a Segunda Guerra Mundial?',
            'respostas': ['Telefone', 'Rádio', 'Telegrafo', 'Internet'],
            'correta': 1
        },
        {
            'pergunta': 'Qual inovação tecnológica permitiu uma melhor navegação e detecção de submarinos durante a Segunda Guerra Mundial?',
            'respostas': ['GPS', 'Radar', 'Sonar', 'Satélite'],
            'correta': 2
        },
        {
            'pergunta': 'Qual foi uma das tecnologias mais significativas desenvolvidas durante a Segunda Guerra Mundial?',
            'respostas': ['Computador', 'Telefone', 'Televisão', 'Internet'],
            'correta': 0
        }
    ]

    pontos = 0
    #Função que irá percorrer todas as perguntas
    for i in range(len(perguntas)):
        #Mostrando elas no terminal com a cor Ciano, percorrendo uma de cada (de 1 - 10)
        print(Fore.CYAN + f"\nPergunta {i+1}: {perguntas[i]['pergunta']}")
        #Função que mostrará as alternativas (de 0 - 4)
        for j in range(4):
            #Mostrando o conteúdo das alternativas com a cor Verde
            print(Fore.GREEN + f"{j}. {perguntas[i]['respostas'][j]}")
        #Variável que irá receber a resposta do usuário
        resposta = int(input(Fore.CYAN + 'Digite o número da sua resposta: '))
        #Verifica se a resposta é igual o que está no dicionário acima
        if resposta == perguntas[i]['correta']:
            #Mostrando a resposta correta na cor Amarela
            print(Fore.YELLOW + 'Resposta correta!')
            pontos += 1
        #Ou, se a resposta estiver errada, irá mostrar no terminal a mensagem "Resposta errada"
        else:
            print(Fore.RED + 'Resposta incorreta.')
            #E em seguida mostrará a resposta correta
            print(Fore.RED + 'A resposta correta era: ' + perguntas[i]['respostas'][perguntas[i]['correta']])
    #Print que irá mostrar a pontuação do usuário
    print(Fore.YELLOW + f'VOCÊ FEZ UM TOTAL DE {pontos}/{len(perguntas)} PONTOS.')

    #Após concluir o quiz, essa variável irá receber e perguntar se o usuário quer retornar ao menun ao sair do código
    decisao = input(Fore.CYAN + f'\nDeseja voltar para o menu? digite {Fore.RED} S {Fore.RESET} / {Fore.RED} N {Fore.CYAN} (para menu): ')
    #Se sim (S ou s), irá voltar ao menu pelo subprograma 'menu_prinical' e irá retomar a explicações
    if decisao == 's' or decisao == 'S':
        limpar()
        menu_principal()
        explicacao()
        limpar()

    #Se o usuário digitar não (N), irá sair do código por meio da função exit()
    else:
        print('Saindo...')
        sleep(1)
        exit()


def material_de_apoio():
    print(Fore.GREEN + 'Aqui está um vídeo explicativo sobre o tema: ')
    video = 'https://youtu.be/RedndCHHtYc'
    print(Fore.RESET + video)

    print(Fore.GREEN + 'E aqui está um site sobre os temas aboradados: ')
    site = 'https://escolakids.uol.com.br/historia/ii-guerra-mundial-1939-1945.htm'
    print(Fore.RESET + site)

    decisao = input(Fore.CYAN + f'\nDeseja voltar para o menu? digite {Fore.RED} S {Fore.RESET} / {Fore.RED} N {Fore.CYAN} (para menu): ')
    if decisao == 's' or decisao == 'S':
        limpar()
        menu_principal()
        explicacao()
        limpar()
    else:
        limpar()
        if escolha == 0:
            print(Fore.WHITE + f'Bem, é aqui que acaba a nossa jornada, {saudacao_primeiro_nome}. Espero que não tenha restado nenhuma dúvida, e se sim, pode retornar a qualquer momento. Obrigado por ter escolhido - me como seu método de ensino, agradeço de coração, adeus {saudacao_primeiro_nome}.\n\n')
            print('Saindo...')
            exit()

        else:
            print(Fore.WHITE + f'Bem, é aqui que acaba a nossa jornada, {saudacao_segundo_nome}. Espero que não tenha restado nenhuma dúvida, e se sim, pode retornar a qualquer momento. Obrigado por ter escolhido - me como seu método de ensino, agradeço de coração, adeus {saudacao_segundo_nome}.\n\n')
            print('Saindo...')
            exit()


def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')


#No programa principal, irá chamar os subprogramas acima, que irá realizar uma espécie de "loop" que irá entrar em um ciclo que só o usuário permita que saia
#Print de apresentando o tema e mostrando o que fazer após digitar uma resposta ao código
print(Fore.GREEN + 'Olá estudante, eu vim com o objetivo de te ajudar a entender sobre o conflito mais intenso que ocorreu na humanidade, a SEGUNDA GUERRA MUNDIAL!')
#Pedindo o nome e sobrenome do, com o intuito de gerar uma interação com o usuáiro
nome = input(Fore.GREEN + 'Mas antes de começar, digite o seu nome e sobrenome (APÓS DIGITAR, APERTE A TECLA ENTER): ')
#Função que testa se o usuário realmente digitou um número
while True:
    try:
        escolha = int(input(Fore.RESET + 'Você prefere que eu te chame pelo seu primeiro nome ou sobrenome? Digite 1 para sobrenome e 0 para primeiro nome: '))
        if escolha in [0, 1]:
            break
        else:
            print(Fore.RED + 'Por favor, insira 0 ou 1.')
    except ValueError:
        print(Fore.RED + 'Por favor, insira um número válido.')

#Variável que receberá o nome e o sobrenome do usuário e irá divi-la
nome_dividido = nome.split()

#Se o usuário preferir, será chamado pelo segundo nome
if escolha == 1:
    saudacao_segundo_nome = nome_dividido[-1]
    print(Fore.GREEN + f'Muito bem, mas antes de iniciar o nosso conteúdo, jovem {saudacao_segundo_nome}, vou passar um menu para facilitar a sua navegação.')
    #Senão, será chamado pelo primeiro nome
else:
    saudacao_primeiro_nome = nome_dividido[0]
    print(Fore.GREEN + f'Muito bem, mas antes de iniciar o nosso conteúdo, jovem {saudacao_primeiro_nome}, vou passar um menu para facilitar a sua navegação.')

menu_principal()
explicacao()
