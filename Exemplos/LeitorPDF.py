import PyPDF2

caminho_pdf = input("Digite o caminho do arquivo PDF: ")
arquivo_pdf = open(caminho_pdf, "rb")
leitor_pdf = PyPDF2.PdfFileReader(arquivo_pdf)

for pagina in range(leitor_pdf.getNumPages()):
    texto = leitor_pdf.getPage(pagina).extractText()
    print(texto)
