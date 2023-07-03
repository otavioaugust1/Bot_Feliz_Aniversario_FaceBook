# Importação das bibliotecas necessárias
import random
import facebook
import random
import datetime

# Token de acesso para autenticação na API do Facebook
access_token = '' # Token de acesso

# Inicialização do objeto Graph da API do Facebook
graph = facebook.GraphAPI(access_token)

# Mensagens para desejar Feliz Aniversário
frases = [
'Desejo que este ano seja ainda mais especial e que realizações continuem acontecendo. Feliz aniversário!',
'Desejo que este ano seja incrível e que venha muitas oportunidades e alegrias. 🎉🎂Feliz aniversário!',
'Desejo que este ano seja incrível e que venha muitas realizações. Feliz aniversário!',
'Desejo que este ano seja incrível e que venha muitas surpresas boas. Feliz aniversário!',
'Desejo que este ano seja maravilhoso e que venha muitas oportunidades e alegrias.🎉🎂 Feliz aniversário!',
'Desejo que este ano seja maravilhoso e que venha muitas oportunidades incríveis. Feliz aniversário!',
'Desejo que este ano seja maravilhoso e que venha muitas realizações e alegrias. Feliz aniversário!',
'Desejo que este ano seja repleto de amor, paz e realizações incríveis. Feliz aniversário!',
'Desejo que este ano seja repleto de amor, paz e realizações. Feliz aniversário!',
'Desejo que este ano traga muita alegria, amor e realizações incríveis. Feliz aniversário!🎉🎂',
'Desejo que este ano traga muita alegria, sucesso e realizações incríveis. Feliz aniversário!',
'Desejo que este ano traga muita paz, amor e felicidade. Feliz aniversário!',
'Desejo que este ano traga muito amor, paz e realizações incríveis. Feliz aniversário!',
'Desejo que este ano traga muito sucesso, amor e realizações incríveis.🎉🎂 Feliz aniversário!',
'Parabéns pelo aniversário! Que este novo ano traga muita alegria e realizações incríveis.',
'Parabéns pelo aniversário! Que este novo ano traga muita alegria e realizações.',
'Parabéns pelo aniversário!🎉🎂 Que este novo ano traga muita realização e alegria.',
'Parabéns pelo aniversário! Que o dia seja especial e repleto de alegria.',
'Parabéns pelo aniversário! Que venha muitas alegrias e oportunidades incríveis.',
'Parabéns pelo aniversário! 🎉🎂Que venha muitas alegrias e realizações.',
'Parabéns pelo aniversário! Que venha muitas aventuras e conquistas incríveis.',
'Parabéns pelo aniversário! Que venha muitas aventuras e felicidade.',
'Parabéns pelo aniversário! Que venha muitas aventuras e momentos inesquecíveis.',
'Parabéns pelo aniversário! Que venha muitas aventuras e que os dias sejam repletos de felicidade.',
'Parabéns pelo aniversário! Que venha muitas aventuras e realizações incríveis.',
'Parabéns pelo aniversário! Que venha muitas aventuras e realizações.',
'Que este ano seja maravilhoso e que todos os teus sonhos se tornem realidade. Feliz aniversário!',
'Que este ano seja maravilhoso e que venha muitas realizações e alegrias. Feliz aniversário!',
'Que este ano seja maravilhoso e que venha muitas realizações. Feliz aniversário!',
'Que este ano seja maravilhoso e que venha muitas surpresas boas e realizações. Feliz aniversário!',
'Que este ano seja repleto de realizações e momentos inesquecíveis. Feliz aniversário!',
'Que este ano traga muitas alegrias e realizações incríveis. Feliz aniversário!',
'Que este ano trazida muitas surpresas boas e conquistas incríveis. Feliz aniversário!',
'Que venha muitas alegrias e realizações neste novo ano de vida. Feliz aniversário!',
'Que venha muitas surpresas boas e realizações neste novo ano de vida. Feliz aniversário!',
"Feliz aniversário! Hoje você completa mais um ano de vida e é hora de comemorar com muita alegria. Que seu dia seja repleto de luz e paz. Que as pessoas queridas estejam com você e que o amor invada seu coração!",
"Que seu aniversário seja repleto de palavras de carinho e abraços sinceros. Parabéns! ❤️😍🎉",
"Feliz Aniversário! 🎉🎂 Mais um ano que passou e outro que vai começar. Aproveite ao máximo e que nunca lhe falte felicidade, amor, saúde e amizade. 🤗",
"Feliz aniversário! Que tudo de bom lhe aconteça neste dia tão marcante e especial na sua vida. Aproveite com um grande sorriso no rosto, e divirta-se muito!",
"Completar mais um ano neste mundo é o maior presente que podemos desejar. Feliz aniversário e que a vida lhe sorria sempre!",
"Parabéns! Que o seu dia seja tão lindo quanto o seu sorriso e lhe ofereça tanta felicidade quanto a sua amizade envia para a minha vida. Que esta nova etapa chegue recheada de muita saúde e novas oportunidades para concretizar os seus sonhos mais desejados.",
"Hoje você inicia uma nova jornada, e nesse momento de alegria por você estar completando mais um ano de vida, quero lhe dizer que tenho muito orgulho em compartilhar da sua amizade. Parabéns meu amigo, e feliz aniversário!",
"Parabéns por esta data especial. Que o tempo seja sempre o seu melhor parceiro, trazendo serenidade, equilíbrio e sabedoria – que lhe darão a receita ideal de como viver a vida, aproveitando o melhor que ela tem a oferecer.",
"Nesta data especial em que você comemora mais um ano de vida, eu quero lhe desejar um dia muito feliz e preenchido por doces surpresas e presentes. Que possa celebrar o seu dia em grande estilo e na companhia daqueles que mais ama. Parabéns!",
"Que este aniversário traga muita paz, saúde, alegria e sucesso. O pouco que conheço de você, já me diz que você é uma pessoa muito especial e que sab aproveitar o lado bom da vida.",
"Feliz Aniversário! Este é um dia grandioso, pois o milagre da vida se renova para você em mais um ciclo que começa hoje.",
"Parabéns, e muitos anos de vida! Que o dia seja generoso e cheio de alegria, paz e energia positiva."
]

# Função para obter os amigos aniversariantes na data específica
def obter_amigos_aniversariantes(data):
    amigos = graph.get_connections("me", "friends", fields="birthday")
    aniversariantes = []
    for amigo in amigos["data"]:
        if "birthday" in amigo:
            amigo_birthday = amigo["birthday"].split('/')
            if amigo_birthday[0] == data.split('-')[0] and amigo_birthday[1] == data.split('-')[1]:
                aniversariantes.append(amigo)
    return aniversariantes

# Função para enviar mensagem direta de feliz aniversário04
def enviar_mensagem_aniversario(amigo_id, amigo_nome, frase):
    mensagem = f"Olá {amigo_nome}!\n\n{frase}"
    graph.put_object(parent_object=amigo_id, connection_name='messages', message=mensagem)
    print(f"Mensagem enviada para o amigo {amigo_nome} com ID {amigo_id}. Mensagem: {frase}")

# Solicitar a data para a qual deseja enviar os desejos de feliz aniversário
data_aniversario = input("Digite a data de aniversário (no formato DD-MM): ")

# Obtendo a lista de amigos aniversariantes para a data especificada
amigos_aniversariantes = obter_amigos_aniversariantes(data_aniversario)

# Percorrendo a lista de amigos aniversariantes e enviando as mensagens de feliz aniversário
for amigo in amigos_aniversariantes:
    amigo_id = amigo["id"]
    amigo_nome = amigo["name"]
    frase_sorteada = random.choice(frases)
    enviar_mensagem_aniversario(amigo_id, amigo_nome, frase_sorteada)