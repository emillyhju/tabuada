class Veiculo:
  def __init__(self, marca, modelo, ano):
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  def __repr__(self):
    return f"{self.marca}, {self.modelo}, {self.ano}"

class Carro(Veiculo):
  def __init__(self, marca, modelo, ano, num_portas):
    super().__init__(marca, modelo, ano)
    self.num_portas = num_portas

  def acelerar(self):
    print(f"0 carro {self.marca} e {self.modelo} acelerou...vrummmm!!!")

class Moto(Veiculo):
  def __init__(self, marca, modelo, ano, cilindradas):
    super().__init__(marca, modelo, ano)
    self.cilindradas = cilindradas

  def acelerar(self):
    print(f"A Moto {self.marca} e {self.modelo} acelerou...randandan!!!")

carro1 = Carro("Nissan", "Skyline R34", 2024, 5)
moto1 = Moto("BMW", "F888", 2024, 800)
print(carro1)
carro1.acelerar()
print(moto1)
moto1.acelerar()
