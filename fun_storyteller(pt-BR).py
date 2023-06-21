import random
quando = ['Há muitos anos atrás', 'Ontem', 'Semana passada', 'Hoje de manhã', 'Há 15 anos', 'Hoje a noite', 'No dia 3 de junho de 2023']
quem = ['o coelho Maurício', 'meu marido', 'minha amiga Sabrina', 'um cavalo', 'meu pet', 'um elefante', 'o presidente dos Estados Unidos', 'o dono do bar', 'o mestre dos magos', 'Volwerine']
nome = ['Silvio Santos', 'Cláudio', 'Luke Skywalker', 'William Boner', 'Ross Gueller']
casa = ['em Barcelona', 'na cidadezinha de Catanduva', 'no bairro Tibery', 'na África do Sul', 'no Ministério da Magia', 'na toca dos zumbis']
foi = ['circo', 'cinema', 'show da Britney Spears', 'submundo', 'Beto Carreiro World', 'banheiro da casa da Shakira', 'jogo do Palmeiras', 'centro da cidade']
acontecimento = ['comeu 4 hambúrgueres de siri', 'pediu uma pizza de pepperoni com banana', 'derramou cerveja em uma senhora que estava passando', 'caiu em um buraco', 'deu uma palestra de 3 horas', 'fez um feitiço maligno', 'casou-se com Dona Florinda', 'brigou comigo']
print(random.choice(quando) + ', ' + random.choice(quem) + ', que mora ' + random.choice(casa) + ', foi ao ' + random.choice(foi) + ' e ' + random.choice(acontecimento) + '!')

