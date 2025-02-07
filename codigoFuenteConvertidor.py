import flet as ft


def main(page: ft.Page):
    # Función para realizar la conversión
    def convertir(e):
        try:
            # Obtener valores del input y los combobox
            numero = txt_numero.value.strip()
            origen = cbo_origen.value
            destino = cbo_destino.value

            # Si el número es decimal (con punto decimal)
            if "." in numero:
                if origen != "Decimal":
                    resultado.value = "Error: Solo se soporta punto flotante para el sistema Decimal"
                    resultado.update()
                    return
                decimal = float(numero)
            else:
                # Convertir el número al sistema decimal primero
                if origen == "Decimal":
                    decimal = int(numero)
                elif origen == "Binario":
                    decimal = int(numero, 2)
                elif origen == "Octal":
                    decimal = int(numero, 8)
                elif origen == "Hexadecimal":
                    decimal = int(numero, 16)
                else:
                    raise ValueError("Sistema de origen no válido")

            # Si origen y destino son iguales
            if origen == destino:
                resultado.value = f"Resultado: {numero}"
            else:
                # Convertir del decimal al sistema requerido
                if destino == "Decimal":
                    resultado.value = f"Resultado: {decimal}"
                elif destino == "Binario":
                    if "." in str(decimal):  # Manejo de punto decimal
                        parte_entera = int(decimal)
                        parte_fraccionaria = decimal - parte_entera
                        bin_entero = bin(parte_entera)[2:]
                        bin_fraccionario = convertir_fraccion_binario(parte_fraccionaria)
                        resultado.value = f"Resultado: {bin_entero}.{bin_fraccionario}"
                    else:
                        resultado.value = f"Resultado: {bin(int(decimal))[2:]}"
                elif destino == "Octal":
                    resultado.value = f"Resultado: {oct(int(decimal))[2:]}"
                elif destino == "Hexadecimal":
                    resultado.value = f"Resultado: {hex(int(decimal))[2:]}"
                else:
                    raise ValueError("Sistema de destino no válido")

        except ValueError:
            resultado.value = "Error: Entrada no válida"
        except Exception as ex:
            resultado.value = f"Error: {ex}"

        resultado.update()

    # Función para convertir la parte fraccionaria de un decimal a binario
    def convertir_fraccion_binario(fraccion):
        binario = ""
        for _ in range(10):
            fraccion *= 2
            if fraccion >= 1:
                binario += "1"
                fraccion -= 1
            else:
                binario += "0"
            if fraccion == 0:
                break
        return binario

    # Configuración de la página
    page.title = "Conversor de Sistemas Numéricos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Centrar verticalmente
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Centrar horizontalmente
    page.padding = 20

    # Elementos de la interfaz
    txt_numero = ft.TextField(label="Número a convertir", width=300)
    cbo_origen = ft.Dropdown(
        label="Sistema de origen",
        options=[
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Binario"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Hexadecimal"),
        ],
        value="Decimal",
        width=300,
    )
    cbo_destino = ft.Dropdown(
        label="Sistema a convertir",
        options=[
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Binario"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Hexadecimal"),
        ],
        value="Binario",
        width=300,
    )
    btn_convertir = ft.ElevatedButton("Convertir", on_click=convertir)
    resultado = ft.Text("Resultado:", size=18)

    # Agregar los elementos a la página
    page.add(
        ft.Column(
            [
                ft.Text("Conversor de Sistemas Numéricos", size=24, weight=ft.FontWeight.BOLD),
                txt_numero,
                cbo_origen,
                cbo_destino,
                btn_convertir,
                resultado,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )


# Ejecutar la aplicación
ft.app(target=main)
