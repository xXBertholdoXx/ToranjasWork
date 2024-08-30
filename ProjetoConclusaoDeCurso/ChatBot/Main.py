# \VARIAVEIS PARA TODAS AS CAMADAS DO CHATBOT
encaminhar = "Você Será Encaminhado..."
erro = "Vamo querer???"

# INICIO DA SINTAXE DOS IF E ELSES DO NOSSO CHATBOX, COM UM TERMO DE INTEIROS E DECLARANDO AS VARIAVEIS ATIVAS NO PROCESSO
print("ESCOLHA UMA ABAIXO:\\n1 - Esportes\\n2 - Dança\\n3 - Carteirinha\\n4 - Academia\\n5 - Aulas de Modal\\n6 - Studio Pilates\\n7 - Atendimento Presencial\\n8 - Locação de Espaços\\n9 - Super Ferias")
pageOne = int(input())
if pageOne == 1:

    # AREA DOS ESPORTES
    # 
    # SINTAXE DOS ESPORTES PARA FAZER A FUNCIONALIDE E ENCAMINHAMENTO PARA AS INSCRIÇÕES
    print("ESPORTES, 1 - ATLETA DO FUTURO, 2 TREINAMENTO")
    esportes = int(input())
    if esportes == 1:
        print(" TEMOS: 1 - Ginastica Artista 2 - Judo 3 - Atletismo 4 - Polo Aquatico ")
        esportesSecundarios = int(input())
        if esportesSecundarios == 1:
            print("Voce quer Se inscrever em Ginastica Artista?? 1 - Sim 2 -não")
            ginasticaArtisitica = int(input())
            if ginasticaArtisitica == 1:
                print(encaminhar)
            else:
                print("ops... voce irá pro inicio")
        else:
            if esportesSecundarios == 2:
                print("Você Pretende se Inscrever Judo??     1 - sim 2 - Nao")
                judo = int(input())
                if judo == 1:
                    print(encaminhar)
                else:
                    print("ops... voce irá pro inicio")
            else:
                if esportesSecundarios == 3:
                    print("Voce esta afim de correr para pegar a sua incrição??     1 - sim 2 - Nao")
                    atletismo = int(input())
                    if atletismo == 1:
                        print(encaminhar)
                    else:
                        print("ops... voce irá pro inicio")
                else:
                    print("Voce quer fazer a sua Inscrever em Polo Aquatico??      1 - sim 2 - Nao")
                    poloAquatico = int(input())
                    if poloAquatico == 1:
                        print(encaminhar)
                    else:
                        print(erro)
    else:
        print(" TEMOS: 1 - Ginastica Artista 2 - Judo 3 - Atletismo 4 - Polo Aquatico ")
        esportsTreinamento = int(input())
        if esportsTreinamento == 1:
            print("Voce quer Se inscrever em Ginastica Artista?? 1 - Sim 2 -não")
            ginasticaArtisitica = int(input())
            if ginasticaArtisitica == 1:
                print(encaminhar)
            else:
                print("ops... voce irá pro inicio")
        else:
            if esportsTreinamento == 2:
                print("Você Pretende se Inscrever Judo??     1 - sim 2 - Nao")
                judo = int(input())
                if judo == 1:
                    print(encaminhar)
                else:
                    print("ops... voce irá pro inicio")
            else:
                if esportsTreinamento == 3:
                    print("Voce esta afim de correr para pegar a sua incrição??     1 - sim 2 - Nao")
                    atletismo = int(input())
                    if atletismo == 1:
                        print(encaminhar)
                    else:
                        print("ops... voce irá pro inicio")
                else:
                    print("Voce quer fazer a sua Inscrever em Polo Aquatico??      1 - sim 2 - Nao")
                    poloAquatico = int(input())
                    if poloAquatico == 1:
                        print(encaminhar)
                    else:
                        print(erro)
else:
    if pageOne == 2:

        # DANÇA
        # 
        # ENCAMINHAMENTO
        print("Você deseja se inscrever em Dança?? 1 - Sim     2 - Não")
        danca = int(input())
        if danca == 1:
            print(encaminhar)
        else:
            print("Ops... Estamos Voltando Entao")
    else:
        if pageOne == 3:

            # PARTE DA CARTEIRINHA PARTE ABUSARDAMENTE GRANDE E BEM PENSADA, PARA RESOLVER O TRABALHO
            print("ESCOLHA 1 - Beneficiario da Industria 2  - Piublico Geral 3 - Aluno SESI 4 - Funcionario SESI")
            carteirinha = int(input())
            if carteirinha == 1:
                print("Escolha estas Opções dos Beneficiarios: 1 - Plano Individual 2 - Plano Familiar ")
                beneficiarios = int(input())
                if beneficiarios == 1:
                    print("Plano Individual")
                else:
                    print("Plano Familiar")
            else:
                if carteirinha == 2:
                    print("Publico Geral, Qual voce busca?? 1 - Plano Individual 2 - Plano Familiar")
                    publicoGeral = int(input())
                    if publicoGeral == 1:
                        print("Plano Individual")
                    else:
                        print("Plano Familiar")
                else:
                    if carteirinha == 3:
                        print("Aluno SESI")
                    else:
                        if carteirinha == 4:
                            print("Funcionario SESI")
                        else:
                            print("Escolha um numero de 1 a 4 por Favor")
        else:
            if pageOne == 4:

                # ACADEMIA
                # QUE VAI HAVER UMA VERIFICAÇÃO NAS VAGAS
                print("ACADEMIA")
                print("Você Será encaminhado para a Verificação de Vagas")
            else:
                if pageOne == 5:

                    # SINTAXE DAS AULAS DE MODALIDADE ESPECIAS
                    print("Aulas de Modalidade: Escolhas umas das Opções 1 - Natação 2 - Hidroginastica 3 - Judo Adulto 4 - Pilates Solo ")
                    aulasModalidade = int(input())
                    if aulasModalidade == 1:
                        print("Fazer Inscrição para natação???  1 - Sim 2 - Nao")
                        natacao = int(input())
                        if natacao == 1:
                            print(encaminhar)
                        else:
                            print(erro)
                    else:
                        if aulasModalidade == 2:
                            print("Fazer Inscrição para HidroGinastica???  1 - Sim 2 - Nao")
                            hidroginastica = int(input())
                            if hidroginastica == 1:
                                print(encaminhar)
                            else:
                                print(erro)
                        else:
                            if aulasModalidade == 3:
                                print("Voce quer se inscrever em Judo Adulto?       1 - Sim    2 - Não")
                                judoAdulto = int(input())
                                if judoAdulto == 1:
                                    print(encaminhar)
                                else:
                                    print(erro)
                            else:
                                if aulasModalidade == 4:
                                    print("Voce vai se Inscrever em  pilates solo??   1 - Sim   2 - Nao")
                                    pilatesSolo = int(input())
                                    if pilatesSolo == 1:
                                        print(encaminhar)
                                    else:
                                        print(erro)
                                else:
                                    print("Escolha um numero de 1 a 4")
                else:
                    if pageOne == 6:

                        # STUDIOS DE PILATES PARA FAZER ELE ENCAMINHAR
                        print("Voce quer ser Encaminhado para Studios de Pilates????")
                        studiosPilates = int(input())
                        if studiosPilates == 1:
                            print(encaminhar)
                        else:
                            print(erro)
                    else:
                        if pageOne == 7:

                            # PARTE DA AREA PRESENCIAL ONDE IRA MANDAR UM PROTOCOLO PARA A SECRETARIA E A ONDE ELE PODERA MANDAR MARCAR UMA CONSULTA
                            print("Realmente Voce vai querer um Atendimento Presencial?")
                            presencial = int(input())
                            if presencial == 1:
                                print(encaminhar)
                            else:
                                print(erro)
                        else:
                            if pageOne == 8:

                                # LOCAIS DOS CATS PARA PODER RESERVAR OU VE COMO FUNCIONA
                                print("Locação de Espaços Opções: 1 - Quiosques 2 - Pista de Atletismo 3 - Campo de Futebol")
                                locationSports = int(input())
                                if locationSports == 1:
                                    print("Quiosque")
                                else:
                                    if locationSports == 2:
                                        print("Pista Atletismo")
                                    else:
                                        print("Campo de Futebol")
                                print(encaminhar)
                            else:

                                # SUPER FERIAS DO SESI, SERA ENVIADO PARA A PARTE DO SITE DO SUPER FERIAS
                                print("Super Férias")
                                print("Voce quer ser Encaminhado para a o Super Ferias??")
                                superFerias = int(input())
                                if superFerias == 1:
                                    print(encaminhar)
                                else:
                                    print(erro)
protocolo = "Estamos criando um Protocolo será Enviado Via E-mail Para você ^--^ "
