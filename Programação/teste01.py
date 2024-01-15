import matplotlib.pyplot as plt

# Configurações do plot
fig, ax = plt.subplots(figsize=(8, 6), dpi=80)
ax.set_xlim([0, 10])
ax.set_ylim([0, 10])
ax.set_aspect('equal')

# Parâmetros do texto
text = "Haroldo"
x = 5
y = 5
font_size = 80
font_color = 'black'
font_family = 'serif'
font_weight = 'bold'

# Desenhar o texto
plt.text(x, y, text, fontsize=font_size, color=font_color, fontfamily=font_family, fontweight=font_weight,
         ha='center', va='center')

# Exibir o plot
plt.show()