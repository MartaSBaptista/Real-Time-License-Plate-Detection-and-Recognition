import os


pasta_carros = "pasta_carros"


matriculas = [
   .....
    #you should write manually
#note that this solution is not our main plan but if your computer is not working as fast as this sort of work needs, you should invest on this simple version
    
    
]


with open("lista_de_chapas_de_matricula.txt", "w") as txt_file:
    for chapa in matriculas:
        txt_file.write(chapa + "\n")

# HTML
with open("tabela_comparativa.html", "w") as html_file:
    html_file.write("<html><head><title>Tabela Comparativa</title></head><body>\n")
    html_file.write("<h1>Comparação de Carros e Matrículas</h1>\n")
    html_file.write("<table border='1' style='border-collapse: collapse;'>\n")
    html_file.write("<tr><th>Imagem</th><th>Matrícula</th></tr>\n")

    for i in range(1, len(matriculas) + 1):
        nome_imagem = f"car{i}.jpg"
        caminho = os.path.join(pasta_carros, nome_imagem)

        if os.path.exists(caminho):
            chapa = matriculas[i - 1]
            # Caminho relativo para a imagem no HTML
            html_file.write(f"<tr><td><img src='{caminho}' width='300'></td><td>{chapa}</td></tr>\n")

    html_file.write("</table></body></html>")

