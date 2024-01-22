User
class Main:
    pass


print("Testando o projeto")


from Cliente import Cliente

from Conta import Conta



c1 = Cliente("João", "114444-2222")
conta = Conta(c1._nome, 6565, 0)

print(conta.titular, "numero: ", conta.numero, "seu saldo: ", conta.saldo)

conta.deposista(100)
conta.saque(50)
conta.extrato()