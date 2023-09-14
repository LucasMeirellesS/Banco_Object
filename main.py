from ContasBancos import ContaCorrente, CartaoCredito

conta1 = ContaCorrente("Zé", "044-744-895.65", "5555-111", "55559999")
cartao1 = CartaoCredito("Lucas", conta1)


print("Mostrando atributos das classes com seus valores:")
print(conta1.__dict__)
print("")
print(f"Printando utilizando o getter: {conta1.nome}")
print(f"Printando utilizando o atributo interno: {conta1._ContaCorrente__nome}")
#Alterando o valor da variável utilizando o nome alterado pelo python.
conta1._ContaCorrente__nome = "Jão"
print(f"Printando o atributo com o novo valor utilizando o atributo interno  {conta1._ContaCorrente__nome}")
print(f"Printando o atributo com o novo valor utilizando o getter  {conta1.nome}")