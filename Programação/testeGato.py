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
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

# Criar o objeto de texto
txt = plt.text(x, y, text, fontsize=font_size, color=font_color, fontfamily=font_family, fontweight=font_weight,
               ha='center', va='center')

# Função de animação
def animate(frame):
    # Lógica para atualizar o texto a cada quadro
    new_x = x + frame*0.1  # Exemplo de alteração de posição
    new_y = y - frame*0.1
    txt.set_position((new_x, new_y))

# Criar a animação
ani = animation.FuncAnimation(fig, animate, frames=100, interval=50)

# Exibir o plot
plt.show()