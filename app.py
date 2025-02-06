from flask import Flask, render_template, request

app = Flask(__name__)

def validar_texto(texto):
    """Verifica se o texto não contém carateres especiais ou acentos"""
    texto = texto.upper()
    for c in texto:
        if c.isalpha():
            if ord(c)<65 or ord(c)>90:
                valid = False
                return valid
    valid = True
    return valid

def cifrar_texto(texto, chave):
    """Cifra o texto usando um deslocamento circular no alfabeto"""
    texto = texto.upper()
    resultado = ""
    for char in texto:
        if char.isalpha():  # Apenas letras são cifradas
            nova_letra = chr(((ord(char) - ord('A') + chave) % 26) + ord('A'))
            resultado += nova_letra
        else:
            resultado += char  # Mantém inalterado o que não é letra 
    return resultado

def decifrar_texto(texto, chave):
    """Decifra o texto revertendo o deslocamento"""
    texto = texto.upper()
    resultado = ""
    for char in texto:
        if char.isalpha():
            nova_letra = chr(((ord(char) - ord('A') - chave) % 26) + ord('A'))
            resultado += nova_letra
        else:
            resultado += char
    return resultado


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cifrar', methods=['GET', 'POST'])
def cifrar():
    
    mensagem = None
    resultado = ""
    
    if request.method == 'POST':
        
        texto = request.form.get('texto')
        chave = request.form.get('chave')
        
        if not texto or not chave:
            mensagem = "Erro: Preencha todos os campos."
        elif not validar_texto(texto):
            mensagem = "Erro: A mensagem não deve conter acentos nem carateres especiais."
        elif not chave.isdigit():
            mensagem = "Erro: A chave deve ser um número inteiro."
        else:
            chave = int(chave)
            resultado = cifrar_texto(texto, chave)
    
    return render_template('cifrar.html', resultado=resultado, mensagem=mensagem)


@app.route('/decifrar', methods=['GET', 'POST'])
def decifrar():
    
    mensagem = None
    resultado = ""
    
    if request.method == 'POST':
        
        texto = request.form.get('texto')
        chave = request.form.get('chave')
        
        if not texto or not chave:
            mensagem = "Erro: Preencha todos os campos."
        elif not validar_texto(texto):
            mensagem = "Erro: A mensagem não deve conter acentos nem carateres especiais."
        elif not chave.isdigit():
            mensagem = "Erro: A chave deve ser um número inteiro."
        else:
            chave = int(chave)
            resultado = decifrar_texto(texto, chave)
    
    return render_template('decifrar.html', resultado=resultado, mensagem=mensagem)


if __name__ == '__main__':
    app.run(debug=False)

