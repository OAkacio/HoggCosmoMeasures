import numpy as np
import matplotlib.pyplot as plt


def save_data(
    nome_arquivo="data",
    decimais=10,
    vecX=[],
    vecY=[],
    description="",
    dominio_inferior=0.0,
    dominio_superior=0.0,
    x_grand="",
    x_unit="",
    y_grand="",
    y_unit="",
):
    data = np.column_stack((vecX, vecY))

    header_text = (
        f"Descripiton: {description}\n"
        f"Domain: {x_grand} in [{dominio_inferior}, {dominio_superior}]\n"
        f"Units: {x_grand} [{x_unit}], {y_grand} [{y_unit}] \n"
        f"{x_grand},{y_grand}"
    )

    np.savetxt(
        f"data/{nome_arquivo}.txt",
        data,
        fmt=f"%.{decimais}f",
        delimiter=",",
        header=header_text,
        comments="# ",
    )