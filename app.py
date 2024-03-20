import flet as ft

def main(page):
    def btn_click(e):
        if not txt_name.value:
            txt_name.error_text = "Escreve algo ai"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Obrigado, {name}!"))

    txt_name = ft.TextField(label="Qual seu nome?")

    page.add(txt_name, ft.ElevatedButton("Enviar!", on_click=btn_click))

ft.app(target=main)