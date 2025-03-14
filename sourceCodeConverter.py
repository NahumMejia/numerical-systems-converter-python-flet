import flet as ft

def main(page: ft.Page):
    # Función para realizar la conversión
    def convert(e):
        try:
            # Obtener valores de entrada y selección
            number = txt_number.value.strip()
            source = cbo_source.value
            target = cbo_target.value

            # Validar si el número tiene parte decimal
            if source == "Binary":
                if "." in number:
                    integer_part, fractional_part = number.split(".")
                    decimal_integer = int(integer_part, 2)
                    decimal_fraction = binary_fraction_to_decimal(fractional_part)
                    decimal = decimal_integer + decimal_fraction
                else:
                    decimal = int(number, 2)
            elif source == "Decimal":
                decimal = float(number)
            elif source == "Octal":
                decimal = int(number, 8)
            elif source == "Hexadecimal":
                decimal = int(number, 16)
            else:
                raise ValueError("Sistema de origen inválido")

            # Si el sistema de origen y destino son iguales
            if source == target:
                result.value = f"Resultado: {number}"
            else:
                # Convertir al sistema requerido
                if target == "Decimal":
                    result.value = f"Resultado: {decimal}"
                elif target == "Binary":
                    if isinstance(decimal, float) and not decimal.is_integer():
                        integer_part = int(decimal)
                        fractional_part = decimal - integer_part
                        bin_integer = bin(integer_part)[2:]
                        bin_fractional = convert_fraction_binary(fractional_part)
                        result.value = f"Resultado: {bin_integer}.{bin_fractional}"
                    else:
                        result.value = f"Resultado: {bin(int(decimal))[2:]}"
                elif target == "Octal":
                    result.value = f"Resultado: {oct(int(decimal))[2:]}"
                elif target == "Hexadecimal":
                    result.value = f"Resultado: {hex(int(decimal))[2:]}"
                else:
                    raise ValueError("Sistema de destino inválido")

        except ValueError:
            result.value = "Error: Entrada inválida"
        except Exception as ex:
            result.value = f"Error: {ex}"

        result.update()

    # Función para convertir la parte fraccionaria de binario a decimal
    def binary_fraction_to_decimal(fraction):
        decimal = 0
        for i, digit in enumerate(fraction):
            decimal += int(digit) * (2 ** -(i + 1))
        return decimal

    # Función para convertir la parte fraccionaria de decimal a binario
    def convert_fraction_binary(fraction):
        binary = ""
        for _ in range(10):
            fraction *= 2
            bit = int(fraction)
            binary += str(bit)
            fraction -= bit
            if fraction == 0:
                break
        return binary

    # Configuración de la página
    page.title = "Conversor de Sistemas Numéricos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # Elementos de la interfaz
    txt_number = ft.TextField(label="Número a convertir", width=300)
    cbo_source = ft.Dropdown(
        label="Sistema de origen",
        options=[
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Binary"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Hexadecimal"),
        ],
        value="Decimal",
        width=300,
    )
    cbo_target = ft.Dropdown(
        label="Sistema de destino",
        options=[
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Binary"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Hexadecimal"),
        ],
        value="Binary",
        width=300,
    )
    btn_convert = ft.ElevatedButton("Convertir", on_click=convert)
    result = ft.Text("Resultado:", size=18)

    # Agregar elementos a la página
    page.add(
        ft.Column(
            [
                ft.Text("Conversor de Sistemas Numéricos", size=24, weight=ft.FontWeight.BOLD),
                txt_number,
                cbo_source,
                cbo_target,
                btn_convert,
                result,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )

# Ejecutar la aplicación
ft.app(target=main)