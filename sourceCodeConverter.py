import flet as ft


def main(page: ft.Page):
    # Function to perform the conversion
    def convert(e):
        try:
            # Get values from the input and dropdowns
            number = txt_number.value.strip()
            source = cbo_source.value
            target = cbo_target.value

            # If the number is decimal (with a decimal point)
            if "." in number:
                if source != "Decimal":
                    result.value = "Error: Only floating point numbers are supported for the Decimal system"
                    result.update()
                    return
                decimal = float(number)
            else:
                # Convert the number to the decimal system first
                if source == "Decimal":
                    decimal = int(number)
                elif source == "Binary":
                    decimal = int(number, 2)
                elif source == "Octal":
                    decimal = int(number, 8)
                elif source == "Hexadecimal":
                    decimal = int(number, 16)
                else:
                    raise ValueError("Invalid source system")

            # If the source and target are the same
            if source == target:
                result.value = f"Result: {number}"
            else:
                # Convert from decimal to the required system
                if target == "Decimal":
                    result.value = f"Result: {decimal}"
                elif target == "Binary":
                    if "." in str(decimal):  # Handle the decimal point
                        integer_part = int(decimal)
                        fractional_part = decimal - integer_part
                        bin_integer = bin(integer_part)[2:]
                        bin_fractional = convert_fraction_binary(fractional_part)
                        result.value = f"Result: {bin_integer}.{bin_fractional}"
                    else:
                        result.value = f"Result: {bin(int(decimal))[2:]}"
                elif target == "Octal":
                    result.value = f"Result: {oct(int(decimal))[2:]}"
                elif target == "Hexadecimal":
                    result.value = f"Result: {hex(int(decimal))[2:]}"
                else:
                    raise ValueError("Invalid target system")

        except ValueError:
            result.value = "Error: Invalid input"
        except Exception as ex:
            result.value = f"Error: {ex}"

        result.update()

    # Function to convert the fractional part of a decimal to binary
    def convert_fraction_binary(fraction):
        binary = ""
        for _ in range(10):
            fraction *= 2
            if fraction >= 1:
                binary += "1"
                fraction -= 1
            else:
                binary += "0"
            if fraction == 0:
                break
        return binary

    # Page setup
    page.title = "Number System Converter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Center vertically
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Center horizontally
    page.padding = 20

    # Interface elements
    txt_number = ft.TextField(label="Number to convert", width=300)
    cbo_source = ft.Dropdown(
        label="Source system",
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
        label="System to convert to",
        options=[
            ft.dropdown.Option("Decimal"),
            ft.dropdown.Option("Binary"),
            ft.dropdown.Option("Octal"),
            ft.dropdown.Option("Hexadecimal"),
        ],
        value="Binary",
        width=300,
    )
    btn_convert = ft.ElevatedButton("Convert", on_click=convert)
    result = ft.Text("Result:", size=18)

    # Add elements to the page
    page.add(
        ft.Column(
            [
                ft.Text("Number System Converter", size=24, weight=ft.FontWeight.BOLD),
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


# Run the application
ft.app(target=main)
