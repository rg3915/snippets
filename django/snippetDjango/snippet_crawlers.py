# -*- coding: utf-8 -*-

import urllib2

from suds.client import Client
from suds.transport.http import HttpTransport

from BeautifulSoup import BeautifulSoup, Tag


class ICReclameAquiApi(object):

    def __init__(self):
        self.username = 'ws01_plussoft'
        self.password = '9U@xDirF'
        self.conectar()
        self.chave = self.get_access_token()

    def conectar(self):
        url = 'http://ws01.reclameaqui.com.br/webservice.php?wsdl'
        t = HttpTransport()
        proxy = urllib2.ProxyHandler({'http': 'http://5.9.41.147:6680'})
        opener = urllib2.build_opener(proxy)
        t.urlopener = opener
        self.client = Client(
            url, transport=t, username=self.username, password=self.password)

    def get_access_token(self):
        dadosParceiro = self.client.factory.create('dadosParceiro')
        dadosParceiro.usuario = self.username
        dadosParceiro.senha = self.password
        dadosParceiro.empresa = 3335
        return unicode(self.client.service.autenticaParceiro(dadosParceiro))

    def get_reclamacao(self, data_inicial, data_final):

        dadosListaReclamacao = self.client.factory.create(
            'dadosListaReclamacao')
        dadosListaReclamacao.chaveAcesso = self.chave
        dadosListaReclamacao.dataInicial = int(
            data_inicial.strftime(u'%Y%m%d%H%M'))
        dadosListaReclamacao.dataFinal = int(
            data_final.strftime(u'%Y%m%d%H%M'))

        xml = self.client.service.listarReclamacoes(dadosListaReclamacao)
        result = self.parse_xml_result(xml)
        return result

    def parse_xml_result(self, xml):

        soup = BeautifulSoup(xml)
        result = soup.findAll('reclamacao')

        lista_reclamacoes = []

        for no in result:
            # dict_ra = {}
            r = ICReclamacao()
            for tag in no:

                if type(tag) == Tag:
                    # dict_ra[tag.name] = tag.contents[0]
                    if tag.name == 'id':
                        r.id = tag.contents[0]
                    if tag.name == 'data':
                        r.data = tag.contents[0]
                    if tag.name == 'assunto':
                        r.assunto = tag.contents[0]
                    if tag.name == 'titulo':
                        r.titulo = tag.contents[0]
                    if tag.name == 'texto':
                        r.texto = tag.contents[0]

            lista_reclamacoes.append(r)
        return lista_reclamacoes

    def print_result(self, result):
        for i in result:
            print(i.id, i.data, i.assunto, i.titulo, i.texto)

    def salvar(self, result):
        with open('output.csv', 'w') as f:
            t = ''
            for i in result:
                t += str(i.id) + ";" + str(i.data) + ";" + \
                    str(i.assunto) + ";" + str(i.titulo) + "\n"
            f.write(t[:-1])
            f.close()

# a = {'id': 123, 'assunto': 'xyz', 'titulo': 'abc', ...}
# r = ICReclamacao(**a)


class ICReclamacao(object):

    def __init__(self):
        self.id = ''
        self.data = ''
        self.assunto = ''
        self.titulo = ''
        self.texto = ''
        self.xml = ''
