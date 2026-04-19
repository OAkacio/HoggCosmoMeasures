import matplotlib.pyplot as plt

def plot(x, y, titulo="", titulo_x="X", titulo_y="Y", tam_fonte=12, espessura=2):
    plt.style.use('seaborn-v0_8-muted')
    fig, ax = plt.subplots(figsize=(10, 6), dpi=100)

    ax.plot(x, y, 
            linewidth=espessura, 
            color='#1a73e8',
            alpha=0.9,
            solid_capstyle='round')

    ax.set_title(titulo, fontsize=tam_fonte + 4, fontweight='bold', pad=20, color='#333333')
    ax.set_xlabel(titulo_x, fontsize=tam_fonte, fontweight='500', labelpad=10)
    ax.set_ylabel(titulo_y, fontsize=tam_fonte, fontweight='500', labelpad=10)

    ax.tick_params(axis='both', which='major', labelsize=tam_fonte - 2)

    ax.grid(True, linestyle='--', alpha=0.6, which='both')
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#cccccc')
    ax.spines['bottom'].set_color('#cccccc')

    plt.tight_layout()
    
    plt.show()