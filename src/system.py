#
# * =============================================================================
# * FUNÇÕES DE ATUALIZAÇÃO DE SISTEMA
# * =============================================================================


def header(titulo, largura=60, **kwargs):
    """Função responsável por criar um output-status em estilo de título de seção."""
    print("\n" + "=" * largura)
    print(f"{titulo.upper():^{largura}}")
    if kwargs:
        info_str = "  |  ".join([f"{k}: {v}" for k, v in kwargs.items()])
        print(f"{info_str:^{largura}}")
    print("-" * largura)


def status(msg):
    """Função responsável por criar um output-status em estilo de status."""
    print(f"\n  > {msg}...")


def param(nome, valor, unidade=""):
    """Função responsável por criar um output-status em estilo de informar parâmetros."""
    unit_str = f" [{unidade}]" if unidade else ""
    print(f"      {nome} = {valor}{unit_str}")


def space(altura=3):
    """Função responsável por criar um output-status de vertical space."""
    print("\n" * altura)
