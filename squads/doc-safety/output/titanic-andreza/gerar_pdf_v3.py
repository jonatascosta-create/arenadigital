#!/usr/bin/env python3
"""Gera PDF do Roteiro v3 — RMS Titanic: A Arquitetura do Desastre."""

from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 5, 'RMS Titanic: A Arquitetura do Desastre - Roteiro v3', 0, 1, 'C')
            self.ln(3)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Pagina {self.page_no()}/{{nb}}', 0, 0, 'C')

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(27, 58, 92)
        self.cell(0, 10, title, 0, 1, 'L')
        self.set_draw_color(27, 58, 92)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def sub_title(self, title):
        self.set_font('Helvetica', 'B', 11)
        self.set_text_color(60, 60, 60)
        self.cell(0, 8, title, 0, 1, 'L')
        self.ln(2)

    def speaker_text(self, speaker, text):
        self.set_font('Helvetica', 'B', 10)
        self.set_text_color(139, 37, 0)
        self.cell(0, 6, speaker, 0, 1, 'L')
        self.set_font('Helvetica', '', 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 5, text)
        self.ln(3)

    def direction_text(self, text):
        self.set_font('Helvetica', 'I', 9)
        self.set_text_color(100, 100, 100)
        self.multi_cell(0, 5, text)
        self.ln(2)

    def screen_text(self, text):
        self.set_font('Courier', 'B', 10)
        self.set_text_color(200, 162, 92)
        self.multi_cell(0, 5, text)
        self.set_font('Helvetica', '', 10)
        self.ln(2)


def safe(text):
    replacements = {
        '\u2014': '-', '\u2013': '-', '\u2018': "'", '\u2019': "'",
        '\u201c': '"', '\u201d': '"', '\u2026': '...', '\u00e9': 'e',
        '\u00e3': 'a', '\u00e7': 'c', '\u00e1': 'a', '\u00ed': 'i',
        '\u00f3': 'o', '\u00fa': 'u', '\u00ea': 'e', '\u00f4': 'o',
        '\u00e2': 'a', '\u00f5': 'o', '\u00e0': 'a', '\u00fc': 'u',
        '\u00f1': 'n', '\u00c9': 'E', '\u00cd': 'I', '\u00d3': 'O',
        '\u2022': '*', '\u00ba': 'o', '\u00aa': 'a',
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text.encode('latin-1', 'replace').decode('latin-1')


def build_pdf():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)

    # === COVER PAGE ===
    pdf.add_page()
    pdf.ln(30)
    pdf.set_font('Helvetica', 'B', 28)
    pdf.set_text_color(27, 58, 92)
    pdf.cell(0, 15, safe('RMS TITANIC'), 0, 1, 'C')
    pdf.set_font('Helvetica', '', 18)
    pdf.set_text_color(139, 37, 0)
    pdf.cell(0, 12, safe('A Arquitetura do Desastre'), 0, 1, 'C')
    pdf.ln(8)
    pdf.set_draw_color(200, 162, 92)
    pdf.set_line_width(0.8)
    pdf.line(60, pdf.get_y(), 150, pdf.get_y())
    pdf.ln(8)
    pdf.set_font('Helvetica', '', 14)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 8, safe('ROTEIRO v3 — PIGEON FORGE'), 0, 1, 'C')
    pdf.ln(8)
    pdf.set_font('Helvetica', 'I', 11)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 7, safe('Apresentadora: Andreza Araujo'), 0, 1, 'C')
    pdf.cell(0, 7, safe('Engenheiro Mecanico | Historiador'), 0, 1, 'C')
    pdf.ln(5)
    pdf.cell(0, 7, safe('Locacao principal: Titanic Museum, Pigeon Forge, TN'), 0, 1, 'C')
    pdf.cell(0, 7, safe('Locacao adicional: Manhattan, NYC'), 0, 1, 'C')
    pdf.ln(5)
    pdf.cell(0, 7, safe('Gerado em: 2026-03-08'), 0, 1, 'C')
    pdf.ln(20)
    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(128, 128, 128)
    pdf.cell(0, 5, safe('Duracao estimada: 45-60 minutos | 8 blocos'), 0, 1, 'C')

    # === ELENCO ===
    pdf.add_page()
    pdf.section_title('ELENCO')

    elenco = [
        ("ANDREZA ARAUJO", "Apresentadora e Especialista em Cultura de Seguranca",
         "Conduz a narrativa, conecta o acidente com seguranca moderna. Ponte passado-presente. Tom: autoridade calma, emocao contida."),
        ("ENGENHEIRO MECANICO", "Analista tecnico",
         "Analisa a engenharia do navio: rebites, anteparas, portas estanques, casco. Explica por que o navio falhou mecanicamente. Tom: tecnico, preciso, didatico."),
        ("HISTORIADOR", "Conhecedor das historias das pessoas",
         "Traz as historias humanas, contexto social, White Star Line, Capitao Smith, romantizacao, pos-acidente. Tom: narrativo, envolvente, dramatico."),
    ]

    for nome, funcao, desc in elenco:
        pdf.set_font('Helvetica', 'B', 12)
        pdf.set_text_color(139, 37, 0)
        pdf.cell(0, 7, safe(nome), 0, 1, 'L')
        pdf.set_font('Helvetica', 'B', 10)
        pdf.set_text_color(27, 58, 92)
        pdf.cell(0, 6, safe(funcao), 0, 1, 'L')
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(40, 40, 40)
        pdf.multi_cell(0, 5, safe(desc))
        pdf.ln(5)

    # === BLOCOS ===
    blocos = [
        ("BLOCO 1 — ABERTURA: CODIGO MORSE + CRIME SCENE (~3 min)", [
            ("TEXTO NA TELA:", None, "CQD CQD SOS SOS de MGY"),
            ("TEXTO NA TELA:", None, "We are sinking fast. Passengers being put into boats.\n- Jack Phillips, operador Marconi do RMS Titanic\n15 de abril de 1912, 00:45"),
            ("ANDREZA:", "Esse som que voce acabou de ouvir e o ultimo pedido de socorro do Titanic. CQD - Come Quickly, Danger. Depois SOS - o novo codigo universal. Jack Phillips, o operador de radio, mandou os dois. Porque naquela noite, ninguem sabia qual codigo os outros navios iam reconhecer. Ele mandou tudo. E quase ninguem respondeu.", None),
            (None, None, "[Pausa - 3 segundos]"),
            ("ANDREZA:", "Eu trabalho com seguranca ha mais de 25 anos. Ja entrei em fabricas, plataformas, canteiros de obra em 19 paises. E em cada lugar, encontrei a mesma coisa: nao um defeito, nao uma negligencia - uma pergunta. A mesma pergunta: como foi possivel?", None),
            ("ANDREZA:", "Este nao e um navio naufragado. E uma cena de crime. E como toda investigacao, a gente nao procura culpados - procura causas.", None),
        ]),

        ("BLOCO 2 — O NAVIO E A ERA (~7 min)", [
            (None, None, "--- A WHITE STAR LINE ---"),
            ("HISTORIADOR:", "A White Star Line nao era qualquer companhia. Era a rival direta da Cunard - as duas maiores empresas de navegacao transatlantica do mundo. A Cunard tinha os navios mais rapidos: o Lusitania e o Mauretania. A White Star decidiu competir de outro jeito: nao seria a mais rapida, seria a MAIOR. A mais luxuosa. A que faria voce sentir que estava num hotel flutuante, nao num navio.", None),
            ("HISTORIADOR:", "E aqui entra um detalhe que pouca gente sabe. A White Star vendia tickets para todas as classes. A primeira classe pagava o equivalente a 100 mil dolares de hoje por uma suite. A terceira classe pagava o equivalente a mil dolares - e a maioria desses passageiros eram imigrantes. Irlandeses, italianos, suecos, libaneses. Gente que vendia tudo o que tinha pra comprar aquele ticket. Pra eles, o Titanic nao era luxo - era a porta pra uma vida nova na America.", None),
            ("ANDREZA:", "A White Star vendia uma promessa: progresso, seguranca, grandeza. O slogan nao era oficial, mas todo mundo sabia: o navio que Deus nao podia afundar. Quando a seguranca vira slogan de marketing em vez de engenharia, o desastre e questao de tempo.", None),
            (None, None, "--- A TECNOLOGIA DA EPOCA ---"),
            ("ENGENHEIRO:", "Pra epoca, o Titanic era uma obra-prima de engenharia. 269 metros de comprimento. 46 mil toneladas. Casco duplo no fundo. Anteparas transversais que dividiam o navio em 16 compartimentos. Dois motores a vapor de triplice expansao e uma turbina de baixa pressao. Velocidade maxima de 23 nos. Tinha ate telegrafo sem fio Marconi - tecnologia de ponta.", None),
            ("ENGENHEIRO:", "O problema e que toda essa tecnologia criou uma ilusao. As anteparas, por exemplo - o navio podia flutuar com ate 4 compartimentos alagados. Impressionante, certo? So que as anteparas nao iam ate o topo. Paravam no conves E. Quando a agua enchia um compartimento, ela TRANSBORDAVA por cima da antepara pro compartimento seguinte. Como uma forma de gelo - voce enche um cubinho, a agua passa pro seguinte.", None),
            ("ANDREZA:", "A tecnologia estava la. A engenharia estava la. O que nao estava la era a humildade de perguntar: e se nao for suficiente?", None),
            (None, None, "--- O CAPITAO EDWARD SMITH ---"),
            ("HISTORIADOR:", "Edward John Smith. 62 anos. Talvez o capitao mais respeitado do Atlantico Norte. Quarenta anos de carreira na marinha mercante. Chamavam ele de 'o capitao dos milionarios' - porque sempre comandava os navios mais importantes da White Star. Era quem os passageiros de primeira classe pediam pelo nome.", None),
            ("HISTORIADOR:", "Smith era um homem serio, meticuloso, respeitado pela tripulacao. Casado com Eleanor, pai de uma filha, Helen. Vivia em Southampton. Era tao querido que quando chegou ao porto pra comandar o Titanic na viagem inaugural, a tripulacao aplaudiu. Era pra ser a ultima viagem dele - ia se aposentar depois. A ironia e brutal: o capitao mais experiente do mundo, no navio mais seguro do mundo, na ultima viagem. E nada disso bastou.", None),
            ("ANDREZA:", "Smith tinha 40 anos de experiencia. E nesses 40 anos, NUNCA tinha enfrentado um desastre maritimo serio. A experiencia dele era toda de sucesso. E experiencia de sucesso pode ser a coisa mais perigosa do mundo - porque ensina que 'sempre funcionou assim.' Na linguagem de Dekker, isso se chama 'drift into failure.' Voce nao percebe que esta se aproximando do desastre porque cada dia parece normal.", None),
        ]),

        ("BLOCO 3 — AS PESSOAS: FAMOSOS + 2 HISTORIAS DRAMATICAS (~8 min)", [
            (None, None, "--- OS FAMOSOS A BORDO ---"),
            ("HISTORIADOR:", "O Titanic era como um who's who da elite mundial. Tinha gente que, sozinha, tinha mais dinheiro que paises inteiros.", None),
            ("HISTORIADOR:", "John Jacob Astor IV - o homem mais rico a bordo. Fortuna equivalente a 2 bilhoes e meio de dolares de hoje. Estava voltando da lua-de-mel com a segunda esposa, Madeleine, que estava gravida de 5 meses. Benjamin Guggenheim - magnata do minerio. Um dos Guggenheims, a familia que depois fundaria o museu. Isidor Straus - co-fundador da Macy's, a maior loja de departamentos dos Estados Unidos. Estava com a esposa Ida. Casados ha 41 anos. Margaret Brown - a 'Molly Brown.' Herdeira de mineracao, mulher determinada. Os Widener, os Thayer, a Condessa de Rothes. Era um navio de milionarios. Mas tambem de 710 imigrantes na terceira classe que ninguem conhecia pelo nome.", None),
            (None, None, "--- HISTORIA DRAMATICA 1: ISIDOR E IDA STRAUS ---"),
            ("HISTORIADOR:", "Isidor e Ida Straus. Ele tinha 67 anos, ela 63. Casados ha 41 anos. Quando os botes comecaram a ser baixados, um oficial ofereceu lugar a Ida no bote 8. Ela comecou a entrar...", None),
            (None, None, "[Pausa - 3 segundos]"),
            ("HISTORIADOR:", "...e parou. Voltou. Tirou o casaco de pele e entregou pra empregada, Ellen Bird. Disse: 'Voce vai precisar mais do que eu.' Depois se virou, tomou o braco do marido e disse:", None),
            ("TEXTO NA TELA:", None, "Vivi com meu marido por 40 anos. Nao vou deixa-lo agora.\n- Ida Straus"),
            ("HISTORIADOR:", "Isidor tambem recusou. Disse que nao entraria em bote nenhum enquanto houvesse mulheres e criancas esperando. Um oficial insistiu - Smith tinha dado ordens de que homens mais velhos poderiam embarcar. Isidor recusou de novo. Foram vistos pela ultima vez sentados juntos em cadeiras de deck, de maos dadas, enquanto a agua subia ao redor deles.", None),
            (None, None, "[SILENCIO - 5 segundos]"),
            ("ANDREZA:", "Quando a gente fala de seguranca, a gente fala de sistemas, de processos, de normas. Mas no final, seguranca e sobre isso: gente. Gente que ama, gente que escolhe, gente que fica. Isidor e Ida nao sao um numero. Sao um casamento de 41 anos que terminou junto porque o sistema falhou.", None),
            (None, None, "--- HISTORIA DRAMATICA 2: AS CRIANCAS DA TERCEIRA CLASSE ---"),
            ("HISTORIADOR:", "Agora eu quero contar uma historia que ninguem conta. Que nenhum filme mostra. As criancas da terceira classe.", None),
            ("HISTORIADOR:", "Na primeira classe, TODAS as criancas sobreviveram. Todas. Na segunda classe, quase todas. Na terceira classe, das 79 criancas a bordo, 27 morreram. Mais de um terco.", None),
            ("HISTORIADOR:", "Tinha a familia Goodwin, de Londres. Frederick e Augusta Goodwin, com seis filhos - o mais velho tinha 16 anos, o mais novo, Sidney, tinha 19 meses. Estavam emigrando para Niagara Falls, onde Frederick ia trabalhar numa usina eletrica. Todos os oito morreram. Nenhum sobreviveu.", None),
            ("HISTORIADOR:", "Quando encontraram o corpo de um bebe no oceano dias depois, nao conseguiram identificar. Por quase um seculo, acreditou-se que era o pequeno Sidney Goodwin. So em 2007, com DNA, confirmaram.", None),
            (None, None, "[SILENCIO - 5 segundos]"),
            ("HISTORIADOR:", "A familia Sage - de Peterborough, Inglaterra. John e Annie Sage com nove filhos. Onze pessoas. A maior familia a bordo. Estavam indo pra Jacksonville, Florida. Todos os onze morreram. Nenhum corpo foi recuperado.", None),
            ("ANDREZA:", "75% dos passageiros de terceira classe morreram. Na primeira classe, a taxa de morte foi 37%. Quando voce olha esses numeros, voce entende que nao foi um acidente democratico. Foi um desastre com endereco. Morreu mais quem tinha menos.", None),
        ]),

        ("BLOCO 4 — O DESCASO: PROBLEMAS DE SEGURANCA (~10 min)", [
            (None, None, "--- OS COLETES SALVA-VIDAS ---"),
            ("ENGENHEIRO:", "Os coletes salva-vidas de 1912 nao eram como os de hoje. Eram blocos de cortica - ou em alguns casos, lona preenchida com fibra vegetal. Pesados, volumosos, e com uma limitacao critica: nao viravam a pessoa de barriga pra cima na agua. Se voce desmaiasse de hipotermia - e a agua estava a menos 2 graus, entao isso acontecia em minutos - o colete te mantinha na agua, mas com o rosto pra baixo. Voce afogava USANDO o colete.", None),
            ("ANDREZA:", "Tinha colete pra todo mundo a bordo. 3.560 coletes. Mas um colete que nao te mantem de barriga pra cima na agua a menos 2 graus... ele da a ilusao de seguranca, nao seguranca de verdade. E esse e um dos padroes que eu vejo ate hoje nas empresas: o EPI existe, esta la, marca no check - mas quando voce precisa dele, ele nao funciona como deveria.", None),
            (None, None, "--- OS BOTES SALVA-VIDAS ---"),
            ("ENGENHEIRO:", "O Titanic tinha capacidade para 2.224 pessoas. Tinha 20 botes salva-vidas com capacidade total para 1.178 pessoas. Faz a conta: 1.046 pessoas NAO TINHAM lugar em bote nenhum. Nem se todos os botes fossem preenchidos completamente. E nao foram - muitos saiam pela metade.", None),
            ("HISTORIADOR:", "E o mais revoltante: o navio FOI projetado para ter 48 botes. Os davits - os guinchos que baixam os botes - tinham capacidade pra 48. Alexander Carlisle, o projetista anterior a Thomas Andrews, propos 48 botes em 1907. A reuniao durou cinco minutos. A White Star decidiu que 48 botes iam atrapalhar a vista do deck de passeio dos passageiros de primeira classe.", None),
            ("ANDREZA:", "A legislacao da epoca - o Merchant Shipping Act de 1894 - exigia botes apenas para navios de ate 10 mil toneladas. O Titanic tinha 46 mil toneladas. A lei tinha 18 anos e nunca foi atualizada. O Board of Trade aprovou. Legal? Sim. Seguro? Nao. E esse e o conceito que eu chamo de Indicador Melancia: verde por fora - certificado, legal, conforme. Vermelho por dentro - desatualizado, capturado, letal.", None),
            (None, None, "--- AS PORTAS ESTANQUES E AS ANTEPARAS ---"),
            ("ENGENHEIRO:", "Vamos falar das famosas portas estanques. O Titanic tinha 15 anteparas transversais que dividiam o casco em 16 compartimentos. Cada antepara tinha uma porta estanque que podia ser fechada da ponte de comando com um sistema eletrico - tecnologia avancadissima pra epoca. O Capitao Smith acionou as portas 30 segundos apos a colisao. Funcionaram perfeitamente.", None),
            ("ENGENHEIRO:", "O problema nao eram as portas. O problema eram as anteparas em si. Elas nao iam ate o topo do navio. Paravam no conves E - ou em alguns casos, ainda mais baixo. Quando os primeiros 5 compartimentos comecaram a alagar, a agua subia e PASSAVA POR CIMA da antepara pro compartimento seguinte. O efeito domino. O navio alagou de proa a popa, compartimento por compartimento. As portas seguraram. As paredes, nao.", None),
            ("ANDREZA:", "As portas funcionaram. As anteparas falharam. E esse e um padrao classico: voce investe no que e visivel - a porta, o botao, o sistema automatico - e esquece do estrutural. A antepara que nao chega ao teto e como a politica de seguranca que nao chega ao chao de fabrica. Existe no papel. Na pratica, a agua passa por cima.", None),
            (None, None, "--- OS REBITES ---"),
            ("ENGENHEIRO:", "Em 1998, pesquisadores do NIST analisaram rebites recuperados do Titanic. O que encontraram foi assustador: os rebites da proa e da popa eram de FERRO FORJADO, nao de aco. E pior - tinham teores de escoria de ate 9%. Isso torna o rebite fragil, quebradico. Quando o iceberg empurrou as placas do casco, esses rebites nao resistiram. As costuras se abriram. A agua entrou.", None),
            ("ENGENHEIRO:", "E quanto custaria ter usado aco em todos os rebites? Menos de 0.3% do custo total do navio. Centavos por passageiro. Centavos.", None),
            (None, None, "[SILENCIO - 5 segundos]"),
            ("ANDREZA:", "Eles SABIAM. Harland and Wolff - o estaleiro - reclamou ao fornecedor sobre a qualidade dos rebites. O fornecedor respondeu. E nada mudou. Os rebites foram instalados. Isso nao e um acidente. Isso e uma decisao.", None),
        ]),

        ("BLOCO 5 — A NOITE: A COLISAO, OS NAVIOS, O CAOS (~8 min)", [
            (None, None, "--- A COLISAO - 37 SEGUNDOS ---"),
            ("HISTORIADOR:", "14 de abril de 1912. 23:39. Noite sem lua. Mar liso como espelho - o que e PIOR, porque sem ondas quebrando na base do iceberg, voce nao ve ele se aproximar.", None),
            ("HISTORIADOR:", "Frederick Fleet, no ninho-de-corvo, avista algo. Sem binoculos - estavam trancados num armario e a chave tinha ficado com um oficial que saiu do navio em Southampton. Fleet toca o sino tres vezes. Liga pro telefone da ponte: 'Iceberg, right ahead!' Da ponte, o primeiro oficial Murdoch ordena: 'Hard-a-starboard!' O leme vira. O navio comeca a virar. 37 segundos entre o avistamento e a colisao. Nao foi suficiente.", None),
            (None, None, "--- O TITANIC PEDE SOCORRO ---"),
            ("HISTORIADOR:", "Apos a colisao, o Capitao Smith ordena que Jack Phillips, o operador de radio, comece a transmitir pedidos de socorro. Phillips manda o CQD - o codigo antigo - e depois o SOS, o codigo novo que quase ninguem usava ainda.", None),
            ("HISTORIADOR:", "O primeiro navio a responder foi o Carpathia, a 58 milhas nauticas de distancia. O capitao Arthur Rostron fez o impossivel - virou o navio, mandou preparar tudo: botes, cobertores, cafe, medicos nos postos. Correu a velocidade maxima no meio de um campo de gelo. Chegou em 3 horas e meia. Tarde demais pra maioria.", None),
            (None, None, "--- O CALIFORNIAN - O NAVIO QUE VIU E NAO FEZ NADA ---"),
            ("HISTORIADOR:", "Mas havia outro navio. O Californian. Estava a no maximo 20 milhas do Titanic. Talvez 10. Seu operador de radio, Cyril Evans, tinha tentado avisar o Titanic sobre gelo mais cedo naquela noite. Phillips respondeu: 'Shut up, I'm working Cape Race' - cala a boca, estou transmitindo telegramas de passageiros. Evans desligou o radio e foi dormir. Estava autorizado a isso.", None),
            ("HISTORIADOR:", "O oficial de quarto do Californian VIU foguetes de sinalizacao do Titanic. Foguetes brancos - o sinal universal de emergencia. Reportou ao Capitao Stanley Lord. Lord mandou tentar contato com lampada de sinais. Ninguem respondeu. Lord nao ligou o radio. Nao mudou de rumo. O Californian ficou parado a menos de 20 milhas enquanto 1.517 pessoas morriam.", None),
            (None, None, "[SILENCIO - 5 segundos]"),
            ("ANDREZA:", "Stanley Lord nao era mau. Evans nao era negligente. O sistema e que era desenhado de um jeito que o operador de radio podia dormir, que foguetes podiam ser ignorados, que ninguem tinha obrigacao de fazer nada. O sistema permitia que voce VISSE gente morrendo e nao agisse. Isso nao e falha humana. Isso e falha de sistema.", None),
            (None, None, "--- OS BOTES SAEM PELA METADE ---"),
            ("ENGENHEIRO:", "Dos 20 botes, muitos sairam com metade da capacidade. O bote 1 tinha capacidade pra 40 pessoas. Saiu com 12. O bote 6, com 28 pra 65 vagas. Por que? Ninguem tinha treinado. Nunca houve um simulacro de evacuacao. Os marinheiros nao sabiam quantas pessoas cabia em cada bote. Os passageiros nao sabiam onde ficavam os botes.", None),
            ("ANDREZA:", "Se todos os botes tivessem saido cheios, pelo menos 500 pessoas a mais teriam sobrevivido. 500 pessoas morreram nao porque nao havia espaco - porque ninguem treinou. E isso eu vejo TODA semana nas empresas que audito: o plano de emergencia existe no papel. O treinamento, nunca.", None),
        ]),

        ("BLOCO 6 — A ROMANTIZACAO DO ACIDENTE (~5 min)", [
            ("HISTORIADOR:", "O naufragio do Titanic e provavelmente o desastre mais romantizado da historia. E comecou cedo - em 1912 mesmo, os jornais ja transformavam a tragedia em narrativa heroica. 'Os homens morreram como cavalheiros.' 'A banda tocou ate o fim.' 'As mulheres foram salvas primeiro.' A historia virou mito antes dos corpos esfriarem.", None),
            ("HISTORIADOR:", "Depois veio Hollywood. Filmes em 1943, 1953, 1958, 1997. O filme do James Cameron - que e brilhante cinematograficamente - criou uma geracao inteira que associa o Titanic a uma historia de amor. Jack e Rose. 'I'm the king of the world.' A cena do colar. A porta que flutuava ou nao flutuava. As pessoas DISCUTEM se a porta era grande o suficiente pra dois. E esquecem que 1.517 pessoas REAIS morreram. Nao personagens - pessoas.", None),
            ("ANDREZA:", "A romantizacao faz uma coisa perigosa: transforma negligencia em destino. 'Foi tragico mas inevitavel.' 'Era o destino.' 'Deus quis assim.' Nao. Nao foi destino. Foram decisoes. Decisoes de reduzir botes, de nao atualizar a lei, de manter a velocidade, de ignorar avisos. Quando voce romantiza, voce tira a responsabilidade. E quando tira a responsabilidade, ninguem aprende. E quando ninguem aprende, acontece de novo.", None),
            ("HISTORIADOR:", "Benjamin Guggenheim vestiu o smoking e disse 'vamos morrer como cavalheiros.' E bonito? E dramatico? E cinematografico? Com certeza. Mas tambem e um homem de 46 anos que ia morrer porque o sistema de botes nao tinha lugar pra ele. A elegancia da morte esconde a brutalidade da causa.", None),
            ("ANDREZA:", "Eu nao sou contra lembrar. Eu sou contra lembrar errado. Lembrar o Titanic como romance e esquecer como crime.", None),
        ]),

        ("BLOCO 7 — O POS-ACIDENTE: O QUE MUDOU NO MUNDO NAVAL (~5 min)", [
            ("HISTORIADOR:", "O naufragio do Titanic mudou o mundo naval de uma forma que poucos desastres mudaram qualquer industria. As consequencias foram enormes e imediatas.", None),
            ("HISTORIADOR:", "Primeiro, em 1913, foi criada a International Ice Patrol - uma patrulha permanente do Atlantico Norte pra monitorar icebergs. Existe ate hoje. Financiada por 13 paises. Desde sua criacao, NENHUM navio que seguiu suas orientacoes colidiu com um iceberg.", None),
            ("HISTORIADOR:", "Segundo, em 1914, foi assinado o SOLAS - Safety of Life at Sea. O tratado internacional de seguranca maritima mais importante da historia. Pela primeira vez, exigiu: botes salva-vidas pra TODOS os passageiros e tripulantes. Exercicios de evacuacao obrigatorios. Radio operando 24 horas - nunca mais um operador podia dormir. Foguetes de sinalizacao vermelhos como sinal exclusivo de emergencia.", None),
            ("HISTORIADOR:", "Terceiro, anteparas foram redesenhadas em toda a industria. Passaram a ir ate o topo do navio. Portas estanques foram padronizadas. Cascos duplos se tornaram norma.", None),
            ("ENGENHEIRO:", "Do ponto de vista de engenharia, o Titanic reescreveu o manual. A classificacao de navios mudou. Os testes de estanqueidade ficaram mais rigorosos. Os materiais passaram a ser especificados com muito mais cuidado - inclusive os rebites. Tudo o que Thomas Andrews e Alexander Carlisle propuseram e foram ignorados virou lei depois que 1.517 pessoas morreram.", None),
            ("ANDREZA:", "E aqui esta a ironia mais dolorosa de toda essa historia. TUDO o que foi implementado depois do desastre JA TINHA SIDO PROPOSTO ANTES. Carlisle propos 48 botes - depois do desastre, ficou obrigatorio ter botes pra todos. Andrews propos anteparas mais altas - depois do desastre, anteparas foram redesenhadas. Evans avisou sobre o gelo - depois do desastre, radio 24 horas. Tres homens. Tres alarmes. Tres vezes o sistema silenciou. E so depois de 1.517 mortos o mundo ouviu.", None),
            (None, None, "[SILENCIO - 5 segundos]"),
            ("ANDREZA:", "Na minha profissao, a gente chama isso de 'aprender pelo sangue.' E o tipo de aprendizado mais caro que existe. Porque o custo nao e dinheiro - sao vidas. E a pergunta que eu faco pra toda empresa: quantas vidas voce precisa perder antes de ouvir o seu Carlisle?", None),
        ]),

        ("BLOCO 8 — ENCERRAMENTO: LICOES E REFLEXAO (~4 min)", [
            ("ANDREZA:", "Este navio conta uma historia. Nao a historia de um iceberg. A historia de um sistema. De decisoes que pareciam razoaveis. De vozes que foram silenciadas. De uma civilizacao tao apaixonada pelo seu progresso que esqueceu de perguntar: 'e se estivermos errados?'", None),
            (None, None, "[Pausa - 3 segundos]"),
            ("ANDREZA:", "O Capitao Smith tinha 40 anos de experiencia. A White Star era a companhia mais prestigiosa do mundo. O Board of Trade era o regulador oficial. Os rebites eram os mesmos de sempre. O radio funcionava - dentro do horario comercial. Cada peca do sistema estava 'certa.' E o sistema inteiro estava errado.", None),
            ("TEXTO NA TELA:", None, "1.517 mortos.\nAlexander Carlisle propos 48 botes em 1907.\nForam instalados 20.\nA regra que permitiu tinha 18 anos."),
            (None, None, "[PAUSA - 5 segundos]"),
            ("ANDREZA:", "Voce nao e capitao de navio. Provavelmente nao esta projetando transatlanticos. Mas voce ESTA dentro de um sistema. E dentro desse sistema, todo dia alguem levanta a mao e diz: 'acho que isso pode dar errado.' Observe o que acontece. Observe os rostos. Observe o silencio.", None),
            ("ANDREZA:", "Celebre o vermelho. Valorize quem reporta o problema. Pergunte todo dia: o que pode me matar hoje? Seguranca nao e uma prioridade - prioridades mudam. Seguranca e um valor. Valores nao mudam.", None),
            (None, None, "[SILENCIO - 3 segundos]"),
            ("TEXTO NA TELA:", None, "Na sua industria, quantas regras estao esperando seu iceberg?"),
            ("ANDREZA:", "O mar nao mudou. A pergunta e: e voce?", None),
            (None, None, "--- FIM ---"),
        ]),

        ("BLOCO ADICIONAL — MANHATTAN (SE DISPONIVEL)", [
            ("ANDREZA (Pier area, NYC):", "Aqui. Nesta area de Manhattan. Na madrugada de 18 de abril de 1912, o RMS Carpathia atracou com 710 sobreviventes. Trinta mil pessoas esperavam no cais. Familias com cartazes. Nomes escritos em papel. E a cada passageiro que descia, um nome era chamado. E para cada nome chamado, dezenas nao eram.", None),
            (None, None, "[Pausa - olha ao redor]"),
            ("ANDREZA:", "Os sobreviventes desciam em silencio. Muitos ainda em roupas de dormir. Alguns enrolados em cobertores do Carpathia. As mulheres procuravam maridos. As criancas procuravam pais. E 1.517 familias comecaram a entender que ninguem mais ia descer.", None),
            ("ANDREZA:", "Eu comeco todo diagnostico de cultura de seguranca com uma pergunta: quem pagou o preco? Nao o preco financeiro - o preco humano. Porque quando a gente esquece quem pagou, a gente comeca a normalizar de novo.", None),
        ]),
    ]

    for bloco_title, items in blocos:
        pdf.add_page()
        pdf.section_title(safe(bloco_title))
        for item in items:
            speaker, speech, screen = item
            if screen and not speaker:
                if screen.startswith("---"):
                    pdf.ln(2)
                    pdf.sub_title(safe(screen.replace("---", "").strip()))
                else:
                    pdf.direction_text(safe(screen))
            elif screen and speaker:
                pdf.set_font('Helvetica', 'B', 10)
                pdf.set_text_color(200, 162, 92)
                pdf.cell(0, 6, safe(speaker), 0, 1, 'L')
                pdf.screen_text(safe(screen))
            elif speaker and speech:
                pdf.speaker_text(safe(speaker), safe(speech))
        pdf.ln(4)

    # === NOTAS DE PRODUCAO ===
    pdf.add_page()
    pdf.section_title('NOTAS DE PRODUCAO')

    pdf.sub_title('Gravacao em Pigeon Forge (Dia 1)')

    prioridades = [
        ("ALTA", "Bloco 1", "Andreza na abertura - 'cena de crime'"),
        ("ALTA", "Bloco 3", "Andreza + Historiador nas historias dramaticas"),
        ("ALTA", "Bloco 4", "Engenheiro explicando coletes, botes, portas, rebites"),
        ("ALTA", "Bloco 8", "Andreza no encerramento - 'o mar nao mudou'"),
        ("MEDIA", "Bloco 2", "Historiador sobre White Star, Smith"),
        ("MEDIA", "Bloco 5", "Historiador sobre a noite, o Californian"),
        ("MEDIA", "Bloco 6", "Historiador + Andreza sobre romantizacao"),
        ("MEDIA", "Bloco 7", "Andreza + Engenheiro sobre pos-acidente"),
    ]

    w = [30, 30, 130]
    pdf.set_fill_color(27, 58, 92)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(w[0], 7, ' Prioridade', 1, 0, 'L', True)
    pdf.cell(w[1], 7, ' Bloco', 1, 0, 'L', True)
    pdf.cell(w[2], 7, ' O que gravar', 1, 1, 'L', True)

    pdf.set_text_color(40, 40, 40)
    for i, (prio, bloco, desc) in enumerate(prioridades):
        if i % 2 == 0:
            pdf.set_fill_color(240, 240, 240)
        else:
            pdf.set_fill_color(255, 255, 255)
        pdf.set_font('Helvetica', 'B' if prio == 'ALTA' else '', 9)
        if prio == 'ALTA':
            pdf.set_text_color(139, 37, 0)
        else:
            pdf.set_text_color(40, 40, 40)
        pdf.cell(w[0], 7, safe(f' {prio}'), 1, 0, 'L', True)
        pdf.set_text_color(40, 40, 40)
        pdf.set_font('Helvetica', '', 9)
        pdf.cell(w[1], 7, safe(f' {bloco}'), 1, 0, 'L', True)
        pdf.cell(w[2], 7, safe(f' {desc}'), 1, 1, 'L', True)

    pdf.ln(8)

    pdf.sub_title('Dinamica do Elenco')

    dinamica = [
        ("Andreza", "Abertura, fechamento, conexoes com seguranca moderna", "Autoridade calma, emocao contida"),
        ("Engenheiro", "Tecnologia, falhas mecanicas, rebites, anteparas", "Tecnico, preciso, didatico"),
        ("Historiador", "Historias das pessoas, contexto social, romantizacao", "Narrativo, envolvente, dramatico"),
    ]

    w2 = [35, 80, 75]
    pdf.set_fill_color(27, 58, 92)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 9)
    pdf.cell(w2[0], 7, ' Pessoa', 1, 0, 'L', True)
    pdf.cell(w2[1], 7, ' Quando fala', 1, 0, 'L', True)
    pdf.cell(w2[2], 7, ' Tom', 1, 1, 'L', True)

    pdf.set_text_color(40, 40, 40)
    pdf.set_font('Helvetica', '', 9)
    for i, (pessoa, quando, tom) in enumerate(dinamica):
        if i % 2 == 0:
            pdf.set_fill_color(240, 240, 240)
        else:
            pdf.set_fill_color(255, 255, 255)
        pdf.cell(w2[0], 7, safe(f' {pessoa}'), 1, 0, 'L', True)
        pdf.cell(w2[1], 7, safe(f' {quando}'), 1, 0, 'L', True)
        pdf.cell(w2[2], 7, safe(f' {tom}'), 1, 1, 'L', True)

    # === RESUMO ===
    pdf.ln(10)
    pdf.section_title('RESUMO ESTATISTICO')

    stats = [
        ("Falas Andreza (apresentadora)", "~22"),
        ("Falas Historiador", "~18"),
        ("Falas Engenheiro", "~10"),
        ("Textos na tela", "5"),
        ("Momentos de silencio marcados", "8"),
        ("Duracao estimada", "45-60 min"),
        ("Blocos totais", "8 + 1 adicional"),
    ]

    w3 = [130, 50]
    pdf.set_fill_color(27, 58, 92)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(w3[0], 7, '  Tipo', 1, 0, 'L', True)
    pdf.cell(w3[1], 7, 'Quantidade', 1, 1, 'C', True)

    pdf.set_text_color(40, 40, 40)
    for i, (tipo, qtd) in enumerate(stats):
        if i % 2 == 0:
            pdf.set_fill_color(240, 240, 240)
        else:
            pdf.set_fill_color(255, 255, 255)
        pdf.set_font('Helvetica', '', 10)
        pdf.cell(w3[0], 7, safe(f'  {tipo}'), 1, 0, 'L', True)
        pdf.set_font('Helvetica', 'B', 10)
        pdf.cell(w3[1], 7, qtd, 1, 1, 'C', True)

    # Save
    output_path = '/Users/johnnycosta/Documents/Projetos/Social Media/squads/doc-safety/output/titanic-andreza/RMS-Titanic-Roteiro-v3.pdf'
    pdf.output(output_path)
    print(f'PDF gerado: {output_path}')


if __name__ == '__main__':
    build_pdf()
