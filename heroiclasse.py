class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    
    def atacar(self):
        ataques = {
            'mago': 'magia',
            'guerreiro': 'espada',
            'monge': 'artes marciais',
            'ninja': 'shuriken'
        }
        
        ataque = ataques.get(self.tipo, 'desconhecido')
        
        print(f"O {self.tipo} atacou usando {ataque}")

nome = input("Digite o nome do herói: ")
idade = int(input("Digite a idade do herói: "))
tipo = input("Digite o tipo do herói (mago, guerreiro, monge, ninja): ").lower()


heroi = Heroi(nome, idade, tipo)

print(f"Herói: {heroi.nome}")
print(f"Idade: {heroi.idade}")
print(f"Tipo: {heroi.tipo}")

print()
heroi.atacar()