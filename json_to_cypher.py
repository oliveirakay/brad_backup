import json

equipes_existentes = set()

with open("nodes-path.json","r") as arquivo:
    arq = json.load(arquivo)

with open("cypher_creation.txt", "w") as cypher_file:
    for emp in arq['value']:
        try:
            nome_equipe = emp["officeLocation"]
            if nome_equipe not in equipes_existentes:
                cypher_file.write("CREATE (:Equipe{nome:'" + nome_equipe + "'})\n")
                equipes_existentes.add(nome_equipe)
            
            cypher_file.write("CREATE (:Emp{nome:'" + emp["displayName"] + "',cargo: '"+ emp["jobTitle"]+"',equipe:'"+emp["officeLocation"]+"', gestor:'"+emp['manager']['displayName']+"'})\n")
        except:
            pass

#Cria equipes, cria empregados, atraves das properties conecto ambos
# MATCH (p:Emp)
# MATCH (l:Equipe)
# WHERE p.equipe = l.nome
# MERGE (p)-[:TRABALHA_EM]->(l)
# RETURN *

#Preciso da propriedade maneger para relacionar com os gestores e seguir a mesma logica
