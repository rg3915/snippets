# coding: utf-8
# https://gist.github.com/DavidLSO/9278f1238bb39458cf04#file-gistfile1-txt
from __future__ import unicode_literals
import sys
import os

proj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eventex.settings")
sys.path.append(proj_path)

os.chdir(proj_path)
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()


def teste_envio_email():

    from django.core.mail import EmailMultiAlternatives
    texto = ''
    for i in range(1, 4):

        texto += """
                <div style="overflow-x:auto;">
                <p><b>{0}</b></p>
                <table width="100%">
                <thead>
                <th width="10%"></th>
                <th width="40%"></th>
                <th width="10%"></th>
                <th width="15%"></th>
                <th width="15%"></th>
                </thead>
                <tbody>
            """.format(i)

        for e in range(1, 10):
            texto += """
                <tr>
                <td><b>N°: </b>{0}</td>
                <td><b>Contratado: </b>{1}</td>
                <td><b>Gestor: </b>{2}</td>
                <td><b>Data Término: </b>{3}</td>
                <td><b>V. Total: </b>{4}</td>
                </tr>
                <tr style="border-bottom: 1px solid black;">
                <td colspan="6"><b>Objeto: </b>{5}</td>
                </tr>
                <tr>
                <td colspan="6" class="line-end">&nbsp;</td>
                </tr>
            """.format(str(e), 'TESTE', 'TESTE', 'TESTE', 'TESTE', 'TESTE')

        texto += """
         </tbody>
         </table>
         </div>
         <br><br>
        """
    style = """
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
            }

            td {
                text-align: left;
                padding: 8px;
            }

            tbody td {
                border-right: 1px solid black;
                border-left: 1px solid black;
                border-top: 1px solid black;
            }

            .line-end {
                border-left: 0px;
                border-right: 0px;
                height: 1px !important;
                padding: 0px;
            }

        </style>
    """
    body = """
        <!DOCTYPE html>
        <html><head><meta charset="UTF-8">
        {0}
    </head>
    <body>
        <p>Prezados(as),</p>
        <p>Segue abaixo a relação dos contratos com vencimento nos próximos dias:</p>
        {1}
        <p>Sem mais, cordialmente.</p>
    </body>
    </html>
    """.format(style, texto)

    subject = 'INFORMATIVO - Contratos com vencimento nos próximos dias.'
    email = EmailMultiAlternatives(
        subject, body, 'regis.santos.100@gmail.com', ['regis.santos.100@gmail.com'])
    # print(body)
    email.attach_alternative(body, "text/html")
    email.send(fail_silently=True)


teste_envio_email()
