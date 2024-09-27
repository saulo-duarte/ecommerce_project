import pandas as pd
from pandas import DataFrame
import numpy as np
import hashlib
import faker
from typing import List

class UserDataGenerator:

    def __init__(self, n) -> None:
        self.n = n
        pass
    
    def generate_user_data(self, n: int) -> DataFrame:
        """Método para gerar dados de usuários fictícios.
        
        Args:
            n (int): Número de registros a serem gerados.
            
        Métodos:
            generate_user_id(n: int) -> list: Gera uma lista de IDs de usuários.
            generate_user_name(n: int) -> list: Gera uma lista de nomes de usuários."""

        def generate_user_id(n: int) -> list:
            return [hashlib.md5(str(i).encode()).hexdigest()[:15] for i in range(n)]
        
        def generate_user_name(n: int) -> list:

            nomes = [
            "Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Henrique", "Isabela", "João", 
            "Karina", "Leonardo", "Mariana", "Nicolas", "Olívia", "Pedro", "Quésia", "Rafael", "Sofia", "Thiago",
            "Amanda", "Bernardo", "Cláudio", "Débora", "Elisa", "Fernando", "Giovana", "Heitor", "Iara", "José", 
            "Kamila", "Lucas", "Marcelo", "Natália", "Otávio", "Patrícia", "Ricardo", "Sara", "Tatiana", "Vinícius", 
            "Alice", "Brenda", "Caio", "Diego", "Elaine", "Fábio", "Gláucia", "Hugo", "Ingrid", "Júlia", 
            "Kleber", "Lívia", "Márcio", "Nathalia", "Osvaldo", "Paula", "Rodrigo", "Sílvia", "Talita", "Vítor",
            "Aline", "Bianca", "Carlos", "Diana", "Eduardo", "Fabiana", "Gustavo", "Helena", "Ivana", "Joana", 
            "Keila", "Larissa", "Mateus", "Nicole", "Otília", "Paulo", "Renata", "Simone", "Tiago", "Valéria",
            "Antônio", "Beatriz", "Cristina", "Davi", "Emanuel", "Fernanda", "Giovanni", "Heloísa", "Igor", "Jorge", 
            "Kelly", "Luan", "Mário", "Noemi", "Orlando", "Pedro", "Rebeca", "Samuel", "Tainá", "Vicente"
            ]
            
            return [nomes[i] for i in np.random.randint(0, len(nomes), n)]
        
        def generate_user_last_names() -> list:

            sobrenomes1 = [
            "Silva", "Santos", "Oliveira", "Souza", "Pereira", "Costa", "Rodrigues", "Martins", "Almeida", "Araújo",
            "Lima", "Gomes", "Ribeiro", "Carvalho", "Ferreira", "Melo", "Barbosa", "Rocha", "Dias", "Teixeira",
            "Moreira", "Correia", "Cavalcanti", "Leite", "Farias", "Pinto", "Nunes", "Vieira", "Monteiro", "Moura",
            "Cruz", "Ramos", "Alves", "Cardoso", "Castro", "Borges", "Macedo", "Siqueira", "Tavares", "Freitas",
            "Guimarães", "Andrade", "Machado", "Azevedo", "Reis", "Peixoto", "Amaral", "Fonseca", "Lopes", "Mendes",
            "Braga", "Morais", "Coutinho", "Nogueira", "Xavier", "Duarte", "Miranda", "Pacheco", "Campos", "Lacerda",
            "Neves", "Rezende", "Meireles", "Ferraz", "Cunha", "Saraiva", "Bastos", "Porto", "Aguiar", "Figueiredo",
            "Albuquerque", "Barros", "Maia", "Franco", "Camargo", "Pimentel", "Vasconcelos", "Siqueira", "Vargas", "Coelho",
            "Assis", "Cabral", "Moraes", "Queiroz", "Carneiro", "Pinheiro", "Mattos", "Guedes", "Prado", "Teles",
            "Couto", "Mesquita", "Lacerda", "Severino", "Bittencourt", "Torres", "Guedes", "Tavares", "Valente", "Pedroso"
            ]

            sobrenomes2 = [
                 "Furtado", "Rangel", "Paiva", "Sá", "Anjos", "Damasceno", "Prado", "Meira", "França", "Brum",
            "Valle", "Quevedo", "Brandão", "Canedo", "Peres", "Montenegro", "Cássio", "Rabelo", "Assunção", "Arruda",
            "Serrano", "Nóbrega", "Serra", "Barreto", "Muniz", "Ferreira", "Jardim", "Palmeira", "Leal", "Quintana",
            "Silveira", "Monteiro", "Franco", "Marinho", "Negrão", "Morais", "Sales", "Saldanha", "Carmo", "Meneses",
            "Leme", "Toledo", "Fleury", "Linhares", "Aragão", "Macedo", "Sarmento", "Coimbra", "Flor", "Neves",
            "Borges", "Lessa", "Prates", "Diniz", "Rocha", "Gaspar", "Domingues", "Cabral", "Couto", "Duarte",
            "Teixeira", "Caldas", "Menezes", "Xavier", "Nogueira", "Alcântara", "Castelo", "Queiroz", "Figueiredo", "Lobato",
            "Viana", "Caldas", "Moura", "Pedroso", "Machado", "Batista", "Nery", "Leão", "Frota", "Martins",
            "Saraiva", "Portela", "Coutinho", "Maia", "Porto", "Siqueira", "Ramalho", "Novaes", "Pinto", "Teles",
            "Vasques", "Lopes", "Albuquerque", "Gouveia", "Cordeiro", "Rios", "Fidalgo", "Vilhena", "Rezende", "Carvalho"
            ]

            return [sobrenomes1[i] + " " + sobrenomes2[i] for i in np.random.randint(0, len(sobrenomes1), n)]
        
        def generate_user_email(n: int) -> list:
            return [f"{name.lower()}.{last_name.lower()}@gmail.com" for name, last_name in zip(generate_user_name(n), generate_user_last_names())]
        
        def generate_user_password(n: int) -> list:
            return [hashlib.md5(str(i).encode()).hexdigest()[:10] for i in range(n)]
        
        def generate_cpf_numbers():
            
            def validate_cpf():
                pass
        pass

        def generate_cnpj_numbers():
            pass
        
        def generate_phone_numbers():
            pass

        def generate_user_status(n: int) -> list:
            return [np.random.choice(["Ativo", "Inativo"], p=[0.7, 0.3]) for i in range(n)]
        
        def generate_user_join_date(n: int) -> list:
            return [f"{np.random.randint(1, 29)}-{np.random.randint(1, 13)}-{np.random.randint(2010, 2022)}" for i in range(n)]
        
        
        