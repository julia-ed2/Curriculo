def imagem():
    foto = open('Imagem.txt', 'w', encoding='utf-8')
    foto.write('<div class = "foto">')
    imagem = input('Digite o caminho da imagem: ')
    foto.write('<img src="' + imagem + '">')
    foto.write('</div>')
    foto.close()

def nomeInfo():
    nome = open('Nomes.txt', 'w', encoding='utf-8')
    nome.write('<div class = "nome">')
    n = input('Digite o nome: ')
    nome.write('<h1>' + n + '</h1>')
    nome.write('</div>')
    nome.close()

def emailInfo():
    email = open('Emails.txt', 'w', encoding='utf-8')
    email.write('<div class = "email">')
    e = input('Digite o email: ')
    email.write('<p>' + e + '</p>')
    email.write('</div>')
    email.close()

def celularInfo():
    celular = open('Celulares.txt', 'w', encoding='utf-8')
    celular.write('<div class = "celular">')
    c = input('Digite o número de celular: ')
    celular.write('<p>' + c + '</p>')
    celular.write('</div>')
    celular.close()

# nome, email e celular => chamar tudo de uma vez
def informacoesContato():
    nomeInfo()
    emailInfo()
    celularInfo()
    
def formacaoAcademica():
    formacao = open('FormaçõesAcademicas.txt', 'w', encoding='utf-8')
    formacao.write('<div class = "formacaoAcademica">')
    curso = input('Digite o curso: ')
    formacao.write('<h3>' + curso + '</h3>')
    instituicao = input('Digite o nome da instituição de ensino: ')
    formacao.write('<p>' + instituicao + '</p>')
    ano = input('Digite o ano de ingresso no curso: ')
    formacao.write('<p>' + ano + '</p>')
    formacao.write('</div>')
    formacao.close()

def conhecimentosTecnicos():
    conhecimentosTecnicos = open('ConhecimentosTecnicos.txt', 'w', encoding='utf-8')
    conhecimentosTecnicos.write('<div class = "conhecimentosTecnicos">') 
    conhecimentosTecnicos.write('<ul>')
    resp = 's'
    while resp == 's' or resp == 'S':
        conhecimento = input('Digite seu conhecimento técnico: ')
        conhecimentosTecnicos.write('<li>' + conhecimento + '</li>')
        resp = input('Deseja adicionar outra habilidade? s/n: ')
    conhecimentosTecnicos.write('</ul>')
    conhecimentosTecnicos.write('</div>')
    conhecimentosTecnicos.close()


def projetosAcademicos():
    projeto = open('ProjetosAcademicos.txt', 'w', encoding='utf-8')
    projeto.write('<div class = "projetos">')
    resp = 's'
    while resp == 's' or resp == 'S':
        tituloProjeto = input('Digite o nome do projeto: ')
        projeto.write('<h3>' + tituloProjeto + '</h3>')
        descricaoProjeto = input('Digite uma breve descrição das funcionalidade do projeto: ')
        projeto.write('<p>' + descricaoProjeto + '</p>')
        resp = input('Deseja adicionar outro projeto? s/n: ')
    projeto.write('</div>')
    projeto.close()

def competenciasComportamentais():
    competenciasComportamentais = open('CompetenciasComportamentais.txt', 'w', encoding='utf-8')
    competenciasComportamentais.write('<div class = "competencias"> ')
    competenciasComportamentais.write('<ul>')
    resp = 's'
    while resp == 's' or resp == 'S':
        competencia = input('Digite sua competencia comportamental: ')
        competenciasComportamentais.write('<li>' + competencia + '</li>')
        resp = input('Deseja adicionar outra competencia comportamental? s/n: ')
    competenciasComportamentais.write('</ul>')
    competenciasComportamentais.write('</div>')
    competenciasComportamentais.close()


# ********************************* Exibir ****************************************************************

def exibirCurriculo():
    curriculo = open('Curriculo.txt', 'w', encoding='utf-8')
    fotos = open('Imagem.txt', 'r', encoding='utf-8')
    nomes = open('Nomes.txt', 'r', encoding='utf-8')
    emails = open('Emails.txt', 'r', encoding='utf-8')
    celulares = open('Celulares.txt', 'r', encoding='utf-8')
    formacoes = open('FormaçõesAcademicas.txt', 'r', encoding='utf-8')
    conhecimentosTecnicos = open('ConhecimentosTecnicos.txt', 'r', encoding='utf-8') 
    projetos = open('ProjetosAcademicos.txt', 'r', encoding='utf-8')
    competenciasComportamentais = open('CompetenciasComportamentais.txt', 'r', encoding='utf-8')
    for nome in nomes:
        foto = fotos.readline()
        email = emails.readline()
        celular = celulares.readline()
        formacao = formacoes.readline()
        conhecimentos = conhecimentosTecnicos.readline()
        projeto = projetos.readline()
        competencia = competenciasComportamentais.readline()
        conteudoCurriculo = foto + nome + email + celular + '<h1> Formação Acadêmica </h1>' + formacao + '<h1> Conhecimentos Técnicos </h1>' + conhecimentos + '<h1> Projetos Relevantes </h1>' + projeto + '<h1> Habilidades Comportamentais </h1>' + competencia
        curriculo.write(conteudoCurriculo)
    fotos.close()
    nomes.close()
    emails.close()
    celulares.close()
    formacoes.close()
    conhecimentosTecnicos.close()
    projetos.close() 
    competenciasComportamentais.close()
    curriculo.close()
    return conteudoCurriculo

# ***************************** estrutura html ****************************************************

def estruturaHTML():
    curriculoEstruturado = open('Curriculo.html', 'w', encoding='utf-8')
    curriculo = open('Curriculo.txt', 'r', encoding='utf-8')
    html = '<!DOCTYPE html>'
    html += '<html lang="pt-br">'
    html += '<head>'
    html += '<meta charset="UTF-8">'
    html += '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    html+='<title>Curriculo</title>'
    html += '<link rel="stylesheet" href="styles.css">'
    html += '</head>'
    html += '<body>'
    html += exibirCurriculo()
    html += '</body>'
    html += '</html>'
    curriculoEstruturado.write(html)
    curriculo.close()
    curriculoEstruturado.close()

# ************************** CODIGO PRINCIPAL **************************************************************

imagem()
informacoesContato()
formacaoAcademica()
conhecimentosTecnicos()
projetosAcademicos()
competenciasComportamentais()

exibirCurriculo()
estruturaHTML()