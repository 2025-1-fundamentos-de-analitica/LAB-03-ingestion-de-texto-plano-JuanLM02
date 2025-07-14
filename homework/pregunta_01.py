"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel



def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    import pandas as pd
    import re
 # Leer archivo completo
    with open("files/input/clusters_report.txt", encoding="utf-8") as f:
        lines = f.readlines()

    # Saltar cabecera (4 primeras líneas)
    lines = lines[4:]

    registros = []
    bloque_actual = ""
    for line in lines:
        if line.strip() == "":
            continue
        if re.match(r"^\s*\d+\s+", line):
            if bloque_actual:
                registros.append(bloque_actual.strip())
                bloque_actual = ""
        bloque_actual += " " + line.strip()
    if bloque_actual:
        registros.append(bloque_actual.strip())


    datos = []
    for bloque in registros:

        m = re.match(r"^(\d+)\s+(\d+)\s+([\d,]+)\s*%\s+(.*)$", bloque)
        if m:
            cluster = int(m.group(1))
            cantidad = int(m.group(2))
            porcentaje = float(m.group(3).replace(",", "."))
            palabras = m.group(4)


            palabras = re.sub(r"\s+", " ", palabras)
            palabras = palabras.strip()

            if palabras.endswith("."):
                palabras = palabras[:-1]
            datos.append(
                [
                    cluster,
                    cantidad,
                    porcentaje,
                    palabras,
                ]
            )

    # Construir DataFrame
    df = pd.DataFrame(
        datos,
        columns=[
            "cluster",
            "cantidad_de_palabras_clave",
            "porcentaje_de_palabras_clave",
            "principales_palabras_clave",
        ],
    )

    return df
print(pregunta_01())
