#
# * =============================================================================
# * FUNÇÕES DE ATUALIZAÇÃO DE SISTEMA
# * =============================================================================


def header(titulo, largura=60, **kwargs):
    print("\n" + "=" * largura)
    print(f"{titulo.upper():^{largura}}")
    if kwargs:
        info_str = "  |  ".join([f"{k}: {v}" for k, v in kwargs.items()])
        print(f"{info_str:^{largura}}")
    print("-" * largura)


def status(msg):
    print(f"\n  > {msg}...")


def param(nome, valor, unidade=""):
    unit_str = f" [{unidade}]" if unidade else ""
    print(f"      {nome} = {valor}{unit_str}")

def bar(largura=60):
    print("\n")
    print("◇"*largura)
    print("\n")