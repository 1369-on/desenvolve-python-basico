
livros = [
    ["O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1200],
    ["1984", "George Orwell", 1949, 328],
    ["Dom Casmurro", "Machado de Assis", 1899, 256],
    ["A Revolução dos Bichos", "George Orwell", 1945, 112],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
    ["A Menina que Roubava Livros", "Markus Zusak", 2005, 480],
    ["O Código Da Vinci", "Dan Brown", 2003, 480],
    ["Morte Súbita", "J.K. Rowling", 2012, 512],
    ["O Hobbit", "J.R.R. Tolkien", 1937, 310]
]

with open("meus_livros.csv", "w") as arquivo:
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        arquivo.write(",".join(map(str, livro)) + "\n")
