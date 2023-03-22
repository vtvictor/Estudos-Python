import matplotlib.pyplot as plt

meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]
vendas = [15000, 18000, 20000, 22000, 19000, 23000]

plt.plot(meses, vendas)
plt.title("Vendas por mês")
plt.xlabel("Mês")
plt.ylabel("Vendas")
plt.show()
