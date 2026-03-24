#!/usr/bin/env python3
"""Gera PDF com falas/narrações e sugestões de locação do roteiro Titanic."""

from fpdf import FPDF
import re

class PDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font('Helvetica', 'I', 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 5, 'RMS Titanic: A Arquitetura do Desastre - Falas e Narracoes', 0, 1, 'C')
            self.ln(3)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Pagina {self.page_no()}/{{nb}}', 0, 0, 'C')

    def section_title(self, title):
        self.set_font('Helvetica', 'B', 14)
        self.set_text_color(27, 58, 92)  # Azul Atlantico
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
        self.set_text_color(139, 37, 0)  # Vermelho Alerta
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
        self.set_text_color(200, 162, 92)  # Ouro Edwardiano
        self.multi_cell(0, 5, text)
        self.set_font('Helvetica', '', 10)
        self.ln(2)

    def table_row(self, cols, widths, bold=False):
        self.set_font('Helvetica', 'B' if bold else '', 9)
        h = 6
        for i, col in enumerate(cols):
            self.cell(widths[i], h, col, 1, 0, 'L')
        self.ln(h)


def safe(text):
    """Remove chars that fpdf can't handle."""
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
    # Remove any remaining non-latin1 chars
    return text.encode('latin-1', 'replace').decode('latin-1')


def build_pdf():
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.set_auto_page_break(auto=True, margin=20)

    # === COVER PAGE ===
    pdf.add_page()
    pdf.ln(40)
    pdf.set_font('Helvetica', 'B', 28)
    pdf.set_text_color(27, 58, 92)
    pdf.cell(0, 15, safe('RMS TITANIC'), 0, 1, 'C')
    pdf.set_font('Helvetica', '', 18)
    pdf.set_text_color(139, 37, 0)
    pdf.cell(0, 12, safe('A Arquitetura do Desastre'), 0, 1, 'C')
    pdf.ln(10)
    pdf.set_draw_color(200, 162, 92)
    pdf.set_line_width(0.8)
    pdf.line(60, pdf.get_y(), 150, pdf.get_y())
    pdf.ln(10)
    pdf.set_font('Helvetica', '', 14)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 8, safe('FALAS, NARRACOES E LOCACOES'), 0, 1, 'C')
    pdf.ln(5)
    pdf.set_font('Helvetica', 'I', 11)
    pdf.cell(0, 7, safe('Apresentadora: Andreza Araujo'), 0, 1, 'C')
    pdf.cell(0, 7, safe('Extraido do Roteiro Final v2'), 0, 1, 'C')
    pdf.cell(0, 7, safe('Gerado em: 2026-03-08'), 0, 1, 'C')
    pdf.ln(30)
    pdf.set_font('Helvetica', '', 9)
    pdf.set_text_color(128, 128, 128)
    pdf.cell(0, 5, safe('Squad doc-safety | McKee (5 beats) + Bernard (3 atos) | 105 minutos'), 0, 1, 'C')

    # === PART 1: FALAS E NARRACOES ===
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 20)
    pdf.set_text_color(27, 58, 92)
    pdf.cell(0, 12, safe('PARTE 1: FALAS E NARRACOES'), 0, 1, 'C')
    pdf.ln(8)

    sequences = [
        ("SEQ 01 - PROLOGO: SOS + O CRIME SCENE (4 min)", [
            ("TEXTO NA TELA:", None, "CQD CQD SOS SOS de MGY"),
            ("TEXTO NA TELA:", None, "We are sinking fast. Passengers being put into boats.\n- Jack Phillips, operador Marconi do RMS Titanic\n15 de abril de 1912, 00:45"),
            ("ANDREZA:", "Eu trabalho com seguranca ha mais de 25 anos. Ja entrei em fabricas, plataformas, canteiros de obra em 19 paises. E em cada lugar, encontrei a mesma coisa: nao um defeito, nao uma negligencia - uma pergunta. A mesma pergunta, em qualquer lingua, em qualquer continente: como foi possivel? O Titanic esta a 3.800 metros de profundidade no Atlantico Norte. Mas a resposta nao esta la embaixo. Esta aqui em cima - nas decisoes que tomamos todo dia.", None),
            ("ANDREZA:", "Este nao e um navio naufragado. E uma cena de crime. E como toda investigacao, a gente nao procura culpados - procura causas.", None),
        ]),
        ("SEQ 02 - A ERA DOS TITANS (6 min)", [
            ("FOECKE:", "Quando analisamos esses rebites em 1998, o que encontramos no microscopio foi... [CORTE - frase suspensa]", None),
            ("BUTLER:", "Para entender o Titanic, voce precisa entender a era. Nao era apenas um navio. Era a prova de que a tecnologia havia vencido a natureza. E se a tecnologia venceu a natureza - para que se preocupar com botes salva-vidas?", None),
        ]),
        ("SEQ 03 - AS VIDAS A BORDO (6 min)", [
            ("ANDREZA (em campo - Pigeon Forge):", "Quando a gente fala de seguranca, a gente fala de numeros. Taxa de acidentalidade. Frequencia. Gravidade. Mas seguranca nao e sobre numeros. E sobre gente. Cada numero e uma pessoa. Uma historia. Uma familia esperando em casa.", None),
            ("VO (narrador - Astor):", "Astor ajudou Madeleine a entrar no bote 4. Perguntou ao oficial Lightoller se podia acompanha-la - 'dada a condicao dela.' Lightoller respondeu: 'Nenhum homem antes que todas as mulheres e criancas.' Astor recuou. Acendeu um cigarro. Ficou.", None),
            ("VO (narrador - Guggenheim):", "Nos vestimos com nossas melhores roupas e estamos preparados para afundar como cavalheiros. Diga a minha esposa que fiz o meu melhor no cumprimento do meu dever.", None),
            ("VO (narrador - Ida Straus):", "Vivi com meu marido por 40 anos. Nao vou deixa-lo agora.", None),
            ("ANDREZA:", "Molly Brown fez o que Carlisle tentou fazer cinco anos antes. Levantou a voz. A diferenca? No bote, nao havia sistema para silencia-la. Na sala de reunioes de 1907, havia.", None),
            ("VO (narrador - banda):", "A ultima musica ouvida no Titanic permanece debatida - 'Nearer, My God, to Thee' ou 'Autumn.' O que nao se debate: oito homens escolheram a musica quando o silencio teria sido mais facil.", None),
            ("ANDREZA (Pigeon Forge - bloco de gelo):", "A agua do Atlantico estava a menos dois graus naquela noite. Voce consegue segurar a mao aqui por 15 segundos. Quem caiu na agua tinha 15 minutos ate a hipotermia. 30 minutos ate a inconsciencia. A maioria dos 1.517 nao morreu afogada. Morreu de frio. No escuro. Esperando um bote que nao voltou.", None),
            (None, None, "[SILENCIO - 5 segundos]"),
            ("ANDREZA:", "2.224 pessoas. Cada uma com uma historia, uma familia, um motivo para estar naquele navio. Quando eu falo de cultura de seguranca, nao estou falando de normas - estou falando de gente como Ida Straus, como os musicos, como as criancas da terceira classe que nunca tiveram nome nos jornais.", None),
        ]),
        ("SEQ 04 - TRES HOMENS E UM NAVIO (8 min)", [
            ("BUTLER:", "Andrews via o navio como engenharia. Carlisle via como risco. Ismay via como produto. Nenhum dos tres estava errado - e exatamente isso que torna a historia terrificante.", None),
        ]),
        ("SEQ 05 - A VOZ QUE NINGUEM OUVIU (2 min)", [
            ("VO (narrador - leitura documental):", "I suggested 48 boats. The meeting lasted five minutes. My proposals were not discussed.", None),
            ("ANDREZA:", "Cinco anos antes do naufragio, Alexander Carlisle sentou-se numa sala e disse o que era preciso fazer. A sala nao ouviu. Eu vi isso acontecer em dezenas de empresas - o tecnico que reporta o risco e encontra o olhar de 'voce de novo?' A pergunta nao e por que Carlisle falou. A pergunta e por que ninguem ouviu. E essa pergunta eu faco todo dia no meu trabalho.", None),
        ]),
        ("SEQ 06 - INCITING INCIDENT: 37 SEGUNDOS (3 min)", [
            (None, None, "[Sequencia visual/sonora - sem falas]"),
        ]),
        ("SEQ 07 - ANATOMIA DA COLISAO (7 min)", [
            ("FOECKE:", "O iceberg nao perfurou o casco do Titanic. Isso e um mito. O que aconteceu foi separacao de placas - os rebites cederam, e as costuras se abriram. E se abriram porque os rebites na proa e na popa eram de FERRO FORJADO, nao de aco. Ferro com teores de escoria muito acima do aceitavel.", None),
            (None, None, "[SILENCIO - 5 segundos]"),
            ("FOECKE:", "Custo. Logistica. Harland & Wolff nao tinha rebitadores hidraulicos suficientes para as secoes curvas da proa e da popa. A rebitagem manual exigia rebites menores e mais macios. Ferro era mais barato e mais facil de trabalhar. Funcionava - em TODOS os navios anteriores.", None),
        ]),
        ("SEQ 08 - COMPLICACAO 1: OS AVISOS SILENCIADOS (7 min)", [
            ("STEPHENSON:", "Phillips nao era tripulante do Titanic. Era empregado da Marconi Company. A Marconi cobrava por telegrama de passageiro transmitido. Os avisos de gelo nao geravam receita. Phillips nao IGNOROU o aviso - o sistema nao permitia que ele o PRIORIZASSE.", None),
            (None, None, "[SILENCIO - 7 segundos]"),
            ("STEPHENSON:", "Comercial. Absolutamente comercial. Com uma funcao de seguranca acidental.", None),
            ("ANDREZA:", "Jack Phillips nao era negligente. Era um trabalhador de 25 anos seguindo as regras do sistema que o empregava. A Marconi Company pagava por telegrama - o aviso de gelo nao valia nada. Eu digo sempre: erro e inerente ao ser humano. O que nao pode ser inerente e um sistema que impede o humano de fazer a coisa certa. Phillips nao PODIA priorizar seguranca. O sistema nao permitia.", None),
        ]),
        ("SEQ 09 - COMPLICACAO 2: OS BOTES FANTASMA (8 min)", [
            ("BUTLER:", "Os davits Welin foram instalados com capacidade para 48 botes. Os davits estavam la. A engenharia estava la. A decisao NAO estava la.", None),
            ("ANDREZA:", "O Board of Trade nao errou por incompetencia. Errou por coerencia - foi coerente com uma regra que ninguem questionava. Eu chamo isso de Indicador Melancia: verde por fora, vermelho por dentro. A regra era verde - certificada, legal, conforme. Por dentro, era vermelha - desatualizada, capturada, letal. Funcionou por 18 anos. Funcionou ate a noite de 14 de abril.", None),
        ]),
        ("SEQ 10 - COMPLICACAO 3: A ARITMETICA DA CLASSE (8 min)", [
            ("ANDREZA (Pigeon Forge - corredores):", "Olha a diferenca. O corredor de primeira classe: largo, iluminado, sinalizacao clara, acesso direto ao deck de botes. Aqui na terceira classe: estreito, escuro, sem indicacao de saida. Em 1912, a justificativa era regulamentacao de imigracao - separar passageiros para inspecao sanitaria em Ellis Island. Na noite de 14 de abril, essas grades viraram barreiras de evacuacao.", None),
            ("BUTLER:", "As grades entre decks tinham uma justificativa legal: regulamentacao americana de imigracao exigia separacao sanitaria para inspecao em Ellis Island. Mas na noite de 14 de abril, essas grades se tornaram barreiras de evacuacao. O design que separava por higiene matou por classe.", None),
            (None, None, "[SILENCIO - 7 segundos]"),
            ("BUTLER:", "O navio foi PROJETADO para que uns morressem mais que outros. Nao por maldade. Por arquitetura.", None),
        ]),
        ("SEQ 11 - COMPLICACAO 4: O NAVIO QUE VIU E NAO AGIU (4 min)", [
            ("STEPHENSON:", "Lord parou por gelo. Isso e prudencia. Evans avisou o Titanic - e foi mandado calar. Quem e culpado? O capitao que parou? O operador que dormiu? Ou o sistema que permitia que o operador dormisse?", None),
            (None, None, "[SILENCIO - 5 segundos]"),
            ("STEPHENSON:", "Stanley Lord foi condenado pela historia. Viveu o resto da vida tentando limpar seu nome. Morreu sem conseguir. O sistema precisava de um culpado individual. Lord serviu. E enquanto todos olhavam para Lord, ninguem olhava para o sistema.", None),
        ]),
        ("SEQ 12 - COMPLICACAO 5: O DNA DO DESASTRE (5 min)", [
            ("FOECKE:", "Recuperamos rebites das expedicoes de Cameron ao wreck. Colocamos sob o microscopio. O teor de escoria nos rebites de ferro forjado da proa excedia 3% - em alguns casos, 9%. Isso e... muito. Um rebite com 9% de escoria e fragil. Quebradico. Quando o gelo empurrou as placas, esses rebites nao resistiram.", None),
            (None, None, "[SILENCIO - 7 segundos]"),
            ("FOECKE:", "Menos de 0.3% do custo total do navio.", None),
            (None, None, "[SILENCIO - 10 segundos]"),
            ("McCARTY:", "Fui aos arquivos de Harland & Wolff em Belfast. Encontrei as reclamacoes sobre a qualidade dos rebites. Eles SABIAM. Harland & Wolff reclamou ao fornecedor. O fornecedor respondeu. E nada mudou. Os rebites foram instalados.", None),
        ]),
        ("SEQ 13 - REVERSAL: AS TRES VOZES SILENCIADAS (5 min)", [
            ("ANDREZA:", "Carlisle propos 48 botes. Andrews propos anteparas mais altas. Evans avisou sobre o gelo. Tres homens. Tres alarmes. Tres vezes o sistema fez o que sistemas patologicos fazem: silenciou. Na Bradley Curve, o nivel mais baixo e o patologico - 'quem se importa enquanto nao somos pegos?' O Titanic nao falhou em comunicar. Funcionou como desenhado - para silenciar. E o oposto disso tem nome: celebrar o vermelho. Valorizar quem reporta o problema.", None),
            (None, None, "[SILENCIO - 5 segundos]"),
            ("ANDREZA:", "Nenhum desses decisores planejou matar 1.517 pessoas. Cada um fez o que parecia certo. Na Piramide de Bird, para cada acidente grave existem 600 quase-acidentes e 30.000 desvios. Todos esses desvios pareciam normais. E foi EXATAMENTE por isso que tantos morreram. Investigacao busca causas, nao culpados.", None),
        ]),
        ("SEQ 14 - CLIMAX: O SISTEMA (7 min)", [
            ("FOECKE:", "Os rebites eram o que sempre usaram.", None),
            ("STEPHENSON:", "Phillips fazia o que a Marconi pagava para fazer.", None),
            ("BUTLER:", "Smith seguia o procedimento de 40 anos.", None),
            ("ANDREZA:", "Dekker chamou de Local Rationality. Cada decisor agia racionalmente dentro do seu contexto. Na PepsiCo, quando comecei o trabalho de transformacao cultural, encontrei a mesma coisa: ninguem fazia nada 'errado' - cada um seguia seu procedimento, sua meta, sua rotina. E as pessoas se machucavam. Porque o sistema estava errado, nao as pessoas.", None),
            (None, None, "[SILENCIO - 3 segundos]"),
            ("ANDREZA:", "Schein disse: o pressuposto mais perigoso e o que nunca precisa ser articulado. E a Cebola da Cultura que eu uso nos meus diagnosticos - o comportamento e a camada de fora, a que voce ve. Mas o pressuposto esta no nucleo, invisivel. O pressuposto do Titanic era: 'Somos grandes demais para falhar.' Ninguem o dizia porque todos o respiravam.", None),
            ("ANDREZA:", "O Titanic NUNCA foi seguro. O sistema existia para afirmar que era. E eu digo sempre: a ausencia de acidentes nao significa cultura forte de seguranca. As vezes significa que ninguem esta reportando.", None),
        ]),
        ("SEQ 15 - CONSEQUENCIAS: O QUE O MUNDO FEZ (5 min)", [
            ("ANDREZA:", "A ironia do inquerito britanico e que ele praticou EXATAMENTE o mecanismo que deveria condenar. O juiz fez o que juizes fazem - protegeu a instituicao. Na linguagem de Hopkins, e o indicador #2 em FALHA: compromisso da alta gestao com seguranca. Mas que compromisso pode existir quando a 'alta gestao' INCLUI o regulador? Quando eu faco diagnostico cultural numa empresa, a primeira coisa que pergunto e: quem audita quem? Se a resposta for 'nos mesmos' - ja sei onde esta o problema.", None),
        ]),
        ("SEQ 16 - A FIX QUE MATA: EASTLAND + BOEING MAX (4 min)", [
            ("ANDREZA:", "Dekker disse: a fix que ataca o sintoma sem entender o sistema cria NOVO desastre. O SOLAS exigiu botes para todos. Ninguem perguntou: e se o peso dos botes matar antes do naufragio? E a Cebola da Cultura ao contrario - mudaram a casca sem tocar no nucleo. Na minha experiencia, licoes aprendidas representam 25% dos acidentes evitaveis. Mas so quando a licao muda crenca, nao formulario.", None),
            ("ANDREZA:", "Em 2018, a FAA delegou ao proprio fabricante - a Boeing - a certificacao do sistema MCAS. A Boeing classificou como 'nao critico.' Dois avioes cairam. Lion Air 610, outubro de 2018: 189 mortos. Ethiopian Airlines 302, marco de 2019: 157 mortos. 346 vidas.", None),
            (None, None, "[SILENCIO - 7 segundos]"),
            ("ANDREZA:", "Reformaram o processo de certificacao. Mais supervisores da FAA. Revisao do ODA. Reformas reais. Mas o modelo fundamental - onde o fabricante desenvolve E certifica - permanece. Os incentivos estruturais permanecem. Se aprenderam apenas 'o que,' o proximo 'Eastland' pode ser o proximo aviao com um sistema que a reforma nao previu.", None),
        ]),
        ("SEQ 17 - PONTE: OS TITANICS DE HOJE (4 min)", [
            ("ANDREZA:", "A TSMC produz 90% dos chips avancados do mundo. Uma fabrica. Uma ilha. Um ponto de falha. O mercado de derivativos excede 600 trilhoes de dolares em valor nocional - nenhum regulador individual compreende o sistema inteiro. A inteligencia artificial esta sendo integrada em sistemas criticos com processos de certificacao que estao sendo escritos ENQUANTO a tecnologia e implantada.", None),
            (None, None, "[SILENCIO - 5 segundos]"),
            ("ANDREZA:", "Estamos em 1907. Os davits estao instalados. Os botes ainda nao foram colocados. E ninguem esta prestando atencao porque o navio e lindo e o mar esta calmo.", None),
        ]),
        ("SEQ 18 - O PIER: ONDE A HISTORIA TERMINOU (4 min)", [
            ("ANDREZA (Pier 54, NYC):", "Aqui. Neste pier. Na madrugada de 18 de abril de 1912, o RMS Carpathia atracou com 710 sobreviventes. Trinta mil pessoas esperavam no cais. Familias com cartazes. Nomes escritos em papel. E a cada passageiro que descia, um nome era chamado. E para cada nome chamado, dezenas nao eram.", None),
            ("ANDREZA:", "Os sobreviventes desciam em silencio. Muitos ainda em roupas de dormir. Alguns enrolados em cobertores do Carpathia. As mulheres procuravam maridos. As criancas procuravam pais. A banda do Salvation Army tocava hinos. E a chuva comecou.", None),
            (None, None, "[SILENCIO - 5 segundos]"),
            ("ANDREZA:", "Ida Straus nao desceu. Benjamin Guggenheim nao desceu. John Jacob Astor nao desceu. Wallace Hartley e seus musicos nao desceram. E 1.517 familias comecaram a entender que ninguem mais ia descer.", None),
            ("ANDREZA:", "Eu comeco todo diagnostico de cultura de seguranca com uma pergunta: quem pagou o preco? Nao o preco financeiro - o preco humano. Porque quando a gente esquece quem pagou, a gente comeca a normalizar de novo.", None),
        ]),
        ("SEQ 19 - EPILOGO: O MAR (3 min)", [
            ("ANDREZA:", "Este navio conta uma historia. Nao a historia de um iceberg. A historia de um sistema. De decisoes que pareciam razoaveis. De vozes que foram silenciadas. De uma civilizacao tao apaixonada pelo seu progresso que esqueceu de perguntar: 'e se estivermos errados?' Eu comecei como engenheira civil. Descobri seguranca pela porta dos fundos. E aprendi que seguranca nao e sobre normas. E sobre gente. E sobre cuidar de gente.", None),
            (None, None, "[SILENCIO - 5 segundos]"),
            ("ANDREZA:", "Voce nao e Carlisle. Provavelmente nao esta projetando navios nem certificando avioes. Mas voce ESTA dentro de um sistema. Eu atendi 33 mil funcionarios em 19 paises na PepsiCo. Cada fabrica, cada pais, cada cultura - e em TODOS encontrei a mesma coisa: regras que 'funcionam' porque nunca foram testadas. Sinais de alarme que ninguem ouve. Drifts lentos e invisiveis movendo o baseline do 'normal' para mais perto do iceberg. Em 180 dias, mudando a cultura - nao o formulario -, reduzimos a acidentalidade em 52%. Em cinco anos, 94%. Nao porque as pessoas passaram a seguir regras. Porque passaram a CUIDAR umas das outras.", None),
            ("ANDREZA:", "Na proxima reuniao em que alguem disser 'acho que isso pode dar errado' - observe o que acontece. Observe os rostos. Observe o silencio. Celebre o vermelho. Valorize quem reporta o problema. Pergunte todo dia: o que pode me matar hoje? Como evitar isso? Seguranca e um valor, nao uma prioridade que muda conforme a situacao. Valores sao transcircunstanciais - estao acima das circunstancias. Temos uma pagina em branco para escrever. Tenha coragem para fazer a diferenca. O mar nao mudou. A pergunta e: e voce?", None),
            ("TEXTO NA TELA:", None, "1.517 mortos.\nAlexander Carlisle propos 48 botes em 1907.\nForam instalados 20.\nA regra que permitiu tinha 18 anos.\n\nNa sua industria, quantas regras estao esperando seu iceberg?"),
            ("TEXTO FINAL:", None, "O mar nao mudou. A pergunta e: e voce?"),
        ]),
    ]

    for seq_title, items in sequences:
        pdf.section_title(safe(seq_title))
        for item in items:
            speaker, speech, screen = item
            if screen and not speaker:
                pdf.direction_text(safe(screen))
            elif screen and speaker:
                pdf.set_font('Helvetica', 'B', 10)
                pdf.set_text_color(200, 162, 92)
                pdf.cell(0, 6, safe(speaker), 0, 1, 'L')
                pdf.screen_text(safe(screen))
            elif speaker and speech:
                pdf.speaker_text(safe(speaker), safe(speech))
        pdf.ln(4)

    # === PART 2: SUGESTOES DE LOCACOES ===
    pdf.add_page()
    pdf.set_font('Helvetica', 'B', 20)
    pdf.set_text_color(27, 58, 92)
    pdf.cell(0, 12, safe('PARTE 2: SUGESTOES DE LOCACOES'), 0, 1, 'C')
    pdf.set_font('Helvetica', '', 11)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 8, safe('Titanic Museum Attraction - Pigeon Forge, TN'), 0, 1, 'C')
    pdf.ln(8)

    pdf.section_title('Espacos do Museu Disponiveis')

    spaces = [
        ("Grand Staircase", "Replica construida a partir dos blueprints originais. Magnificencia e craftsmanship."),
        ("Captain's Bridge", "Galeria interativa com leme do navio e cena de noite estrelada."),
        ("Boiler Room", "Atividade interativa de paletar carvao."),
        ("Dining Gallery", "Renovada em 2026. Cultura gastronomica, operacoes de cozinha e entretenimento a bordo."),
        ("Father Browne Gallery", "Algumas das unicas imagens da vida a bordo do Titanic."),
        ("Third-Class Cabin Recreation", "Replica de cabine de 3a classe."),
        ("Lifeboat Replica", "Replica de bote salva-vidas onde visitantes podem sentar."),
        ("Music Gallery", "Piano de epoca com performances ao vivo."),
        ("Experiencia da Agua a -2C", "Toque na agua a 28F - temperatura do Atlantico naquela noite."),
        ("Boarding Pass Experience", "Cada visitante recebe boarding pass de um passageiro real."),
    ]

    for name, desc in spaces:
        pdf.sub_title(safe(name))
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(40, 40, 40)
        pdf.multi_cell(0, 5, safe(desc))
        pdf.ln(3)

    # === MAPEAMENTO CENAS x LOCACOES ===
    pdf.add_page()
    pdf.section_title('Mapeamento: Cenas do Roteiro x Espacos do Museu')

    mappings = [
        ("SEQ 03 - Bloco de gelo", "Experiencia da agua a -2C", "Andreza colocando a mao na agua gelada. Close extremo nos cristais, pele, condensacao."),
        ("SEQ 03 - Corredor 1a classe", "Grand Staircase + Dining Gallery", "Andreza caminhando pelo luxo - lustres, mogno, carpete. Contraste visual com 3a classe."),
        ("SEQ 03 - Painel de passageiros", "Boarding Pass Experience", "Close nas fotos de passageiros reais. Cada visitante recebe boarding pass."),
        ("SEQ 10 - Corredor 3a classe", "Third-Class Cabin Recreation", "Andreza comparando espaco estreito e escuro com luxo da 1a classe."),
        ("SEQ 10 - Grades entre decks", "Corredores do museu", "B-roll dos corredores estreitos, sinalizacoes minimas."),
    ]

    for cena, espaco, descricao in mappings:
        pdf.set_font('Helvetica', 'B', 10)
        pdf.set_text_color(139, 37, 0)
        pdf.cell(0, 6, safe(cena), 0, 1, 'L')
        pdf.set_font('Helvetica', 'B', 10)
        pdf.set_text_color(27, 58, 92)
        pdf.cell(0, 6, safe(f'  Local: {espaco}'), 0, 1, 'L')
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(40, 40, 40)
        pdf.multi_cell(0, 5, safe(f'  {descricao}'))
        pdf.ln(4)

    # === SUGESTOES EXTRAS ===
    pdf.section_title('Espacos Extras para B-Roll e Cenas Complementares')

    extras = [
        ("Captain's Bridge", "SEQ 06", "B-roll: Andreza no leme, olhando a 'noite estrelada'. Transicao visual antes do Inciting Incident."),
        ("Boiler Room", "SEQ 02", "B-roll: imagens dos operarios, trabalho bracal, escala industrial. Complementa reconstituicao do estaleiro."),
        ("Father Browne Gallery", "SEQ 03", "Fotos unicas da vida a bordo para sobrepor nas historias dos passageiros."),
        ("Lifeboat Replica", "SEQ 09/10", "Cena poderosa: Andreza sentada no bote, falando sobre os 1.178 lugares vs 2.224 pessoas."),
        ("Music Gallery", "SEQ 03", "B-roll: referencia a banda de Wallace Hartley. Piano ao vivo como elemento sonoro."),
        ("Dining Gallery (2026)", "SEQ 02/03", "Recem-renovada. Artefatos de epoca, ambientacao de mesa. Visual rico para contraste luxo/tragedia."),
    ]

    for espaco, seq, desc in extras:
        pdf.set_font('Helvetica', 'B', 10)
        pdf.set_text_color(27, 58, 92)
        pdf.cell(90, 6, safe(espaco), 0, 0, 'L')
        pdf.set_font('Helvetica', 'I', 9)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(0, 6, safe(f'Para: {seq}'), 0, 1, 'R')
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(40, 40, 40)
        pdf.multi_cell(0, 5, safe(desc))
        pdf.ln(3)

    # === CENAS SUGERIDAS ===
    pdf.section_title('Cenas Sugeridas (nao previstas no roteiro)')

    pdf.sub_title('1. Captain\'s Bridge - Transicao para SEQ 06')
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(40, 40, 40)
    pdf.multi_cell(0, 5, safe("Andreza de frente para a janela estrelada, em silencio. Depois vira para a camera. Transicao visual natural para a fala sobre '37 segundos'. O museu oferece a visao noturna que Fleet tinha no ninho-de-corvo."))
    pdf.ln(4)

    pdf.sub_title('2. Lifeboat Replica - Silencio dos botes vazios')
    pdf.set_font('Helvetica', '', 10)
    pdf.multi_cell(0, 5, safe("Andreza sentada sozinha no bote replica. Camera recua mostrando os assentos vazios. Sem fala - apenas silencio. Imagem para cobrir a contagem dos botes arriados parcialmente."))
    pdf.ln(4)

    # === LOCACOES NYC ===
    pdf.add_page()
    pdf.section_title('Locacoes em Nova York (NYC)')
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(80, 80, 80)
    pdf.multi_cell(0, 5, safe("Roteiro de filmagem para 1 tarde em NYC. Todas as locacoes sao publicas. Para filmagem profissional, NYC exige permit da Mayor's Office of Media and Entertainment (MOME)."))
    pdf.ln(6)

    pdf.sub_title('Cena principal prevista no roteiro')
    pdf.set_x(10)
    pdf.speaker_text('SEQ 18 - O Pier: Onde a Historia Terminou (4 min)',
        'Local: Pier 54 / Little Island, Hudson River Park (Chelsea)\n'
        'Endereco: West 13th Street & Hudson River, Manhattan\n'
        'O pier onde o RMS Carpathia atracou com 710 sobreviventes em 18/04/1912. '
        'Hoje e parque publico sobre o Hudson. Andreza caminha pelo pier com sobreposicao de fotos de 1912.')

    pdf.sub_title('Locacoes complementares em NYC')

    nyc_locations = [
        ("SEQ 03 - Historias dos passageiros",
         "South Street Seaport Museum (Pier 16, Financial District)",
         "Museu maritimo com navios historicos. Contexto portuario."),
        ("SEQ 05 - Carlisle / White Star Line",
         "Antigo escritorio White Star Line - Broadway 9, Bowling Green",
         "O predio ORIGINAL ainda existe. Fachada como B-roll documental."),
        ("SEQ 03/18 - Memorial",
         "Titanic Memorial Lighthouse - Fulton St & Pearl St",
         "Memorial de 1913 dedicado as vitimas. Close no farol + placa."),
        ("SEQ 18 - Complemento porto",
         "Chelsea Piers (Pier 59-62)",
         "Vizinho ao Pier 54. Onde os transatlanticos atracavam."),
        ("SEQ 19 - Epilogo / reflexao",
         "Battery Park (vista para o porto)",
         "Andreza olhando o porto por onde o Carpathia entrou."),
        ("SEQ 17 - Os Titanics de hoje",
         "Wall Street / Financial District",
         "Montagem editorial sobre sistemas modernos e regulacao."),
    ]

    for cena, local, desc in nyc_locations:
        pdf.set_x(10)
        pdf.speaker_text(safe(cena), safe(f'Local: {local}\n{desc}'))


    pdf.section_title('Roteiro sugerido para 1 tarde em NYC')
    pdf.set_font('Helvetica', '', 10)
    pdf.set_text_color(40, 40, 40)

    itinerary = [
        ("13:00 - Titanic Memorial Lighthouse (South Street Seaport)", "Close no farol memorial de 1913. Placa comemorativa. Luz do inicio da tarde."),
        ("13:45 - Broadway 9 (antigo escritorio White Star Line)", "Fachada do predio original. B-roll documental. 10 min de caminhada do Seaport."),
        ("14:30 - Battery Park", "Vista para o porto. Andreza olhando o horizonte. Epilogo / reflexao. Luz da tarde."),
        ("15:30 - Chelsea Piers (Pier 59-62)", "Contexto portuario dos transatlanticos. B-roll. Taxi/metro ate Chelsea (~20 min)."),
        ("16:00 - Pier 54 / Little Island (CENA PRINCIPAL)", "SEQ 18 completa. Andreza caminha pelo pier. Sobreposicao com fotos 1912. Luz dourada do fim de tarde (golden hour ~17:00)."),
        ("17:00-17:30 - Pier 54 (golden hour)", "Tomadas finais com luz dourada. Andreza olhando o rio Hudson. Silencio. Morse em eco."),
    ]

    for horario, desc in itinerary:
        pdf.set_font('Helvetica', 'B', 10)
        pdf.set_text_color(27, 58, 92)
        pdf.cell(0, 6, safe(horario), 0, 1, 'L')
        pdf.set_font('Helvetica', '', 10)
        pdf.set_text_color(40, 40, 40)
        pdf.multi_cell(0, 5, safe(f'  {desc}'))
        pdf.ln(3)

    # === RESUMO ESTATISTICO ===
    pdf.add_page()
    pdf.section_title('Resumo Estatistico')

    stats = [
        ("Falas Andreza (apresentadora)", "25"),
        ("Falas entrevistados (Foecke, Butler, Stephenson, McCarty)", "14"),
        ("VO narrador", "6"),
        ("Textos na tela", "4"),
        ("Momentos de silencio marcados", "12"),
        ("Duracao total do documentario", "105 min"),
        ("Sequencias totais", "19"),
    ]

    w = [130, 50]
    pdf.set_fill_color(27, 58, 92)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font('Helvetica', 'B', 10)
    pdf.cell(w[0], 7, '  Tipo', 1, 0, 'L', True)
    pdf.cell(w[1], 7, 'Quantidade', 1, 1, 'C', True)

    pdf.set_text_color(40, 40, 40)
    for i, (tipo, qtd) in enumerate(stats):
        if i % 2 == 0:
            pdf.set_fill_color(240, 240, 240)
        else:
            pdf.set_fill_color(255, 255, 255)
        pdf.set_font('Helvetica', '', 10)
        pdf.cell(w[0], 7, safe(f'  {tipo}'), 1, 0, 'L', True)
        pdf.set_font('Helvetica', 'B', 10)
        pdf.cell(w[1], 7, qtd, 1, 1, 'C', True)

    # Save
    output_path = '/Users/johnnycosta/Documents/Projetos/Social Media/squads/doc-safety/output/titanic-andreza/Titanic-Falas-Narracoes-Locacoes.pdf'
    pdf.output(output_path)
    print(f'PDF gerado: {output_path}')


if __name__ == '__main__':
    build_pdf()
