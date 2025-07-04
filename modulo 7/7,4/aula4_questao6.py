
import csv

with open("spotify-2023.csv", encoding='latin-1') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    next(leitor_csv)  # Pular o cabeçalho

    mais_tocadas_por_ano = {}

    for linha in leitor_csv:
        track_name = linha[0]
        artist_name = linha[1]
        released_year = int(linha[3])
        streams = int(linha[8])

        if 2012 <= released_year <= 2022:
            if released_year not in mais_tocadas_por_ano or streams > mais_tocadas_por_ano[released_year][3]:
                mais_tocadas_por_ano[released_year] = [track_name, artist_name, released_year, streams]

musicas_mais_tocadas = sorted(mais_tocadas_por_ano.values(), key=lambda x: x[2])
print(musicas_mais_tocadas)
