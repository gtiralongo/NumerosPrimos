import flet as ft


def main(page: ft.Page):
    page.window_center()
    page.bgcolor = ft.colors.LIGHT_GREEN_100
    page.window_height = 500
    page.window_width = 900
    page.update()
    page.title = "Numeros Primos"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    primeros_primos = [2, 3, 5, 7, 11]
    # Elementos del layout
    title_gp = ft.Row(
        [
            ft.Text("¿Es Primo?", size=50, color=ft.colors.GREEN),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    h1_gp = ft.Row(
        [
            ft.Text("Escriba el numero que desea saber si es primo",
                    size=20, color=ft.colors.GREEN),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    def btn_clean(e):
        page.clean()
        page.add(
            title_gp,
            h1_gp,
            averiguar_primo,
        )

    def primo_btn(e):
        for i in primeros_primos:
            if int(numero.value) % i == 0:
                if int(numero.value) == i:
                    es_primo = ft.Row(
                        [
                            ft.Text(
                                f"¡El numero {numero.value} es primo!", size=20, color=ft.colors.GREEN),
                            ft.ElevatedButton(
                                "Limpiar numero", bgcolor=ft.colors.GREEN_ACCENT, color=ft.colors.GREEN, on_click=btn_clean, )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                    page.add(es_primo)
                    break

                es_primo = ft.Row(
                    [
                        ft.Text(
                            f"¡El numero {numero.value} no es primo porque es divisible por {i} y el resto da {int(numero.value) / i}!", size=20, color=ft.colors.GREEN),
                        ft.ElevatedButton(
                            "Limpiar numero", bgcolor=ft.colors.GREEN_ACCENT, color=ft.colors.GREEN, on_click=btn_clean)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
                page.add(es_primo)
                break
            else:
                if int(numero.value) == 73:
                    es_primo = ft.Row(
                        [
                            ft.Text(
                                f"¡El numero {numero.value} es primo!", size=20, color=ft.colors.GREEN),
                            ft.ElevatedButton(
                                "Limpiar numero", bgcolor=ft.colors.GREEN_ACCENT, color=ft.colors.GREEN, on_click=btn_clean)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                    sc = ft.Row(
                        [
                            ft.Container(
                                content=ft.Text(f"Sabias que el 73 segun Sheldon Cooper es el mejor primo de todos. Porque es el 21º número primo, leído al revés es el 37 que es el 12º número primo que leído al revés es 21 que es el resultado de multiplicar 7 × 3 y en sistema binario 73 es 1001001, un numeral capicúa(palindromo), que posee siete (7) cifras de las cuales tres (3) son unos. En sistema octal 73 es 111 el cual es un capicúa."),
                                margin=10,
                                padding=10,
                                alignment=ft.alignment.center,
                                bgcolor=ft.colors.GREEN,
                                width=750,
                                height=120,
                                border_radius=10,
                            ), ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    )
                    page.add(es_primo, sc)
                    break
                es_primo = ft.Row(
                    [
                        ft.Text(
                            f"¡El numero {numero.value} es primo!", size=20, color=ft.colors.GREEN),
                        ft.ElevatedButton(
                            "Limpiar numero", bgcolor=ft.colors.GREEN_ACCENT, color=ft.colors.GREEN, on_click=btn_clean)
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
                page.add(es_primo)
                break

    numero = ft.TextField(label="Escribe un numero", icon=ft.icons.NUMBERS, color=ft.colors.GREEN, border_color=ft.colors.GREEN_ACCENT,cursor_color=ft.colors.GREEN,
                        focused_border_color=ft.colors.GREEN, autofocus=True)
    btn_primo = ft.ElevatedButton(
        "¿Es primo?", bgcolor=ft.colors.GREEN_ACCENT, color=ft.colors.GREEN, on_click=primo_btn)

    averiguar_primo = ft.Row(
        [
            numero,
            btn_primo
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
    page.add(
        title_gp,
        h1_gp,
        averiguar_primo,
    )


ft.app(target=main)
