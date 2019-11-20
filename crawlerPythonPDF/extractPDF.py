import tabula
import pandas as pd
# Read pdf into DataFrame
# PODE USAR O LINK ABAIXO COMO FONTE DE INICIAL PARA ENTENDER AS VARIÁVEIS USADAS.
# https://aegis4048.github.io/parse-pdf-files-while-retaining-structure-with-tabula-py
useLattice = False
useStream  = True
usePages   = '2' #coloca o número da página ex '2' ou 'all' para pegar todas as tabelas da página
df = tabula.read_pdf("congeladores.pdf", multiple_tables=True, lattice=useLattice, stream=useStream, pages=usePages)

# Também é possível ler um pdf direto de um link
# df = tabula.read_pdf("https://github.com/tabulapdf/tabula-java/raw/master/src/test/resources/technology/tabula/arabic.pdf")
print(df)
# convert PDF into CSV
# tabula.convert_into("congeladores.pdf", "output.csv", output_format="csv", pages='all')