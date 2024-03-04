import json

equipes_existentes = set()

with open("C:\\Users\\kayqu\\OneDrive\\Documents\\Bradesco\\nodes.json","r") as arquivo:
    arq = json.load(arquivo)

with open("cypher_creation.txt", "w") as cypher_file:
    for emp in arq['value']:
        try:
            nome_equipe = emp["officeLocation"]
            print()
        except:
            pass

#Cria equipes, cria empregados, atraves das properties conecto ambos
# MATCH (p:Emp)
# MATCH (l:Equipe)
# WHERE p.equipe = l.nome
# MERGE (p)-[:TRABALHA_EM]->(l)
# RETURN *

#Preciso da propriedade maneger para relacionar com os gestores e seguir a mesma logica