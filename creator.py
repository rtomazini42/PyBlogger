import os
import vars_html_css




def criar_blog(name):
    
    if not name:
        print("Nome do blog não pode ser vazio!")
        return
    
    try:

        os.mkdir(name)
        os.mkdir(os.path.join(name, 'assets'))
        os.mkdir(os.path.join(name, 'css'))
        os.mkdir(os.path.join(name, 'js'))
        os.mkdir(os.path.join(name, 'posts'))

        arquivo_path = os.path.join(name, "index.html")
        with open(arquivo_path, "w") as arquivo:
            arquivo.write(vars_html_css.creation_index(name))

        arquivo_path = os.path.join(name, "posts.html")
        with open(arquivo_path, "w") as arquivo:
            arquivo.write(vars_html_css.creation_posts(name))

        arquivo_path = os.path.join(name, "contact.html")
        with open(arquivo_path, "w") as arquivo:
            arquivo.write(vars_html_css.creation_contact(name))

        arquivo_path = os.path.join(name, "about.html")
        with open(arquivo_path, "w") as arquivo:
            arquivo.write(vars_html_css.creation_about(name))

        arquivo_path = os.path.join(name+"/css/", "reset.css")
        with open(arquivo_path, "w") as arquivo:
            arquivo.write(vars_html_css.creation_reset_css())

        arquivo_path = os.path.join(name+"/css/", "styles.css")
        with open(arquivo_path, "w") as arquivo:
            arquivo.write(vars_html_css.creation_styles_css(2))

            
        print(f"Blog '{name}' criado com sucesso!")

    except OSError as e:
        print(f"Erro ao criar o blog: {e}")
