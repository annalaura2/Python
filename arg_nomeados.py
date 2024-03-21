def salvar_livros(autor, editora, ano, nome):
    print(f"livro salvo! {autor}, {editora}, {ano}, {nome}")


salvar_livros(**{"autor": "Raphael Montes","editora": "seguinte", "ano": "2014","nome": "dias perfeitos"})
#criei um dicionário