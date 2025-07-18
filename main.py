import flet as ft
import asyncio
from math import radians

def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_min_width = 500
    page.window_width = 700
    page.window_height = 900
    page.bgcolor = ft.colors.BLACK

    list_items = {
        'solo1':('Solo1.png', 'LEVEL 10 — 🟫', 'Sung Jin Woo', 'O Caçador Mais Fraco da Humanidade', 'Stealth', '0.10', '0.10', '0.10','Comum'),
        'solo2':('Solo2.png', 'LEVEL 10 — 🟫', 'Yoo Jinho', 'Tank Rank D', "I'll Protect You!", '0.10', '0.25', '0.10','Comum'),
        'solo3':('Solo3.png', 'LEVEL 20 — 🔺', 'Lee Joohee', 'Healer Rank B', 'Healing Magic', '0.20', '0.10', '0.15', 'Incomum'),
        'solo4':('Solo4.png', 'LEVEL 20 — 🔺', 'Seo Jiwoo', 'Caçadora Rank A', 'Water Dragon Strike', '0.20', '0.15', '0.25', 'Incomum'),
        'solo5':('Solo5.png', 'LEVEL 30 — 🔷', 'Baek Yoonho', 'Líder da Tigre Branco', 'Eyes of the Beast', '0.35', '0.35', '0.30', 'Raro'),
        'solo6':('Solo6.png', 'LEVEL 40 — 🔷', 'Cha Hae-In', 'A Dançarina', 'Sword of Light', '0.45', '0.30', '0.55', 'Raro'),
        'solo7':('Solo7.png', 'LEVEL 50 — 🔷', 'Choi Jong-In', 'A Arma Mais Forte', 'Flame Prison', '0.55', '0.30', '0.30', 'Raro'),
        'solo8':('Solo8.png', 'LEVEL 60 — 🔷', 'Liu Zhigang', 'Caçador 7 Estrelas da China', "Ruler's Authority", '0.60', '0.40', '0.60', 'Raro'),
        'solo9':('Solo9.png', 'LEVEL 70 — 🟣', 'Igris', 'Sombra do General do Monarca das Sombras', "The Commander's Touch", '0.75', '0.80', '0.75', 'Épico'),
        'solo10':('Solo10.png', 'LEVEL 80 — 🟣', 'Beru', 'Sombra do Rei Formiga', 'I Shall Devour You!', '0.85', '0.70', '0.95', 'Épico'),
        'solo11':('Solo11.png', 'LEVEL 90 — 🟣', 'Kandiaru', 'Arquiteto do Sistema', "Ruler's Authority", '0.90', '0.90', '0.90', 'Épico'),
        'solo12':('Solo12.png', 'LEVEL 100 - ✨', 'Querehsha', 'Monarca das Pragas', 'Poison Manipulation', '10', '0.95', '0.95', 'Lendário'),
        'solo13':('Solo13.png', 'LEVEL 100 - ✨', 'Monarca', 'Novo Monarca das Sombras', 'Shadow Extraction', '1', '1', '1', 'Lendário')
    }

    keys = list(list_items.keys())
    current_index = [0]

    animated_border = ft.Ref[ft.Container]()

    async def animate_card(direction: str):
        dx = 1 if direction == "left" else -1
        slide_ref.current.offset = ft.Offset(dx, 0)
        slide_ref.current.opacity = 0
        page.update()
        await asyncio.sleep(0.3)
        card_container.content = build_card(current_index[0])
        slide_ref.current.offset = ft.Offset(0, 0)
        slide_ref.current.opacity = 1
        page.update()

    async def next_card(e):
        if current_index[0] > 0:
            current_index[0] -= 1
            await animate_card("right")

    async def preview_card(e):
        if current_index[0] < len(keys) - 1:
            current_index[0] += 1
            await animate_card("left")

    def gradiente_por_raridade(raridade):
        match raridade:
            case "Comum":
                return ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=["#ADADAD", "#333232"]  # Cinza escuro degradê
                )
            case "Incomum":
                return ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=["#FF0000", "#420303"]  # Cinza escuro degradê
                )
            case "Raro":
                return ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=["#42A5F5", "#0E76D1"]  # Azul claro → escuro
                )
            case "Épico":
                return ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=["#BA68C8", "#7B1FA2"]  # Roxo claro → escuro
                )
            case "Lendário":
                return ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=["#F8D81F", "#E29404"]  # Ouro → Laranja
                )
            case _:
                return ft.LinearGradient(
                    begin=ft.alignment.top_left,
                    end=ft.alignment.bottom_right,
                    colors=["#BDBDBD", "#757575"]  # fallback cinza
                )

    def build_card(index):
        item = list_items[keys[index]]
        raridade = item[8]

        card_content = ft.Container(
            key=str(index),
            height=700,
            width=400,
            shadow=ft.BoxShadow(blur_radius=100, color=ft.colors.GREY),
            clip_behavior=ft.ClipBehavior.NONE,
            border_radius=ft.border_radius.all(30),
            bgcolor=ft.colors.BLACK,
            content=ft.Container(
                key=str(index),
                height=700,
                width=400,
                shadow=ft.BoxShadow(
                    blur_radius=100,
                    color=ft.colors.GREY,
                ),
                clip_behavior=ft.ClipBehavior.NONE,
                border_radius=ft.border_radius.all(30),
                bgcolor=ft.colors.BLACK,
                content=ft.Column(
                    spacing=0,
                    controls=[
                        ft.Container(
                            expand=1,
                            alignment=ft.alignment.center,
                            bgcolor=ft.colors.BLACK,
                            border_radius=ft.border_radius.vertical(top=20),
                            content=ft.Image(src='Logo.png'),
                        ),
                        ft.Container(
                            expand=2,
                            alignment=ft.alignment.center,
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.bottom_left,
                                end=ft.alignment.top_right,
                                colors=[ft.colors.PURPLE, ft.colors.SURFACE],
                            ),
                            content=ft.Image(src=item[0], scale=ft.Scale(1.5)),
                        ),
                        ft.Container(
                            expand=2,
                            padding=ft.padding.all(10),
                            alignment=ft.alignment.center,
                            content=ft.Column(
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(
                                        content=ft.Text(
                                            value=item[1],
                                            color='#898788',
                                            size=18,
                                            weight=ft.FontWeight.BOLD,
                                            style=ft.TextStyle(
                                                shadow=ft.BoxShadow(
                                                    blur_radius=2,
                                                    color=ft.colors.BLACK,
                                                    offset=ft.Offset(1, 1),
                                                )
                                            )
                                        ),
                                        bgcolor=ft.colors.with_opacity(0.4, ft.colors.PURPLE),
                                        border_radius=15,
                                        padding=8
                                    ),
                                    ft.Text(value=item[2], size=40, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE),
                                    ft.Text(value=item[3], color=ft.colors.GREY, italic=True, text_align=ft.TextAlign.CENTER),
                                    ft.Divider(color="#7B1FA2", opacity=0.5),
                                    ft.Container(
                                        content=ft.Text(
                                            spans=[
                                                ft.TextSpan(text='HABILIDADE: ', style=ft.TextStyle(color=ft.colors.AMBER, size=16, weight=ft.FontWeight.BOLD,)),
                                                ft.TextSpan(text=item[4], style=ft.TextStyle(color=ft.colors.YELLOW, size=16)),
                                            ],
                                            text_align=ft.TextAlign.CENTER
                                        ),
                                        bgcolor=ft.colors.with_opacity(0.2, ft.colors.WHITE),
                                        border_radius=15,
                                        padding=8
                                    )
                                ]
                            )
                        ),
                        ft.Container(
                            expand=1,
                            padding=ft.padding.symmetric(horizontal=20),
                            border_radius=ft.border_radius.vertical(bottom=20),
                            alignment=ft.alignment.center,
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.bottom_left,
                                end=ft.alignment.top_right,
                                colors=[ft.colors.PURPLE, ft.colors.SURFACE],
                            ),
                            content=ft.Row(
                                controls=[
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        expand=1,
                                        controls=[
                                            ft.Text(value='ATAQUE', color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                                            ft.ProgressBar(
                                                value=item[5],
                                                color=ft.colors.RED,
                                                height=20
                                            ),
                                        ]
                                    ),
                                    ft.VerticalDivider(opacity=0.5),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        expand=1,
                                        controls=[
                                            ft.Text(value='DEFESA', color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                                            ft.ProgressBar(
                                                value=item[6],
                                                color=ft.colors.BLUE,
                                                height=20
                                            ),
                                        ]
                                    ),
                                    ft.VerticalDivider(opacity=0.5),
                                    ft.Column(
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        expand=1,
                                        controls=[
                                            ft.Text(value='VELOCIDADE', color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                                            ft.ProgressBar(
                                                value=item[7],
                                                color=ft.colors.GREEN,
                                                bgcolor=ft.colors.BLACK26,
                                                height=20
                                            ),
                                        ]
                                    ),
                                ],
                                vertical_alignment=ft.CrossAxisAlignment.CENTER
                            )
                        ),
                    ],
                )
            )
        )

        if raridade != "Lendário":
            return ft.Container(
                padding=6,
                gradient=gradiente_por_raridade(raridade),
                border_radius=ft.border_radius.all(30),
                content=card_content,
            )
        
        return ft.Container(
            width=400,
            height=700,
            padding=ft.padding.all(1),
            border_radius=ft.border_radius.all(36),
            clip_behavior=ft.ClipBehavior.HARD_EDGE,  # <- Isso impede o estouro
            content=ft.Stack(
                controls=[
                    ft.Container(  # Borda animada girando
                        ref=animated_border,
                        width=408,
                        height=708,
                        border_radius=ft.border_radius.all(36),
                        gradient=gradiente_por_raridade(raridade),
                        rotate=ft.Rotate(angle=0),
                        scale=ft.Scale(scale=1.2),
                        animate_rotation=ft.Animation(duration=3000, curve=ft.AnimationCurve.LINEAR),
                    ),
                    ft.Container(  # Card normal por cima
                        padding=6,
                        border_radius=ft.border_radius.all(30),
                        content=card_content
                    )
                ]
            )
        )
    
    async def rotate_border():
        await asyncio.sleep(0.2)
        while True:
            if animated_border.current:
                animated_border.current.rotate.angle += radians(360)
                animated_border.current.update()
            await asyncio.sleep(3)
            
    slide_ref = ft.Ref[ft.Container]()

    card_container = ft.Container(
        ref=slide_ref,
        animate_offset=500,
        offset=ft.Offset(0, 0),
        opacity=1,
        content=build_card(current_index[0]),
    )

    layout = ft.Container(
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.Container(
                    content=ft.ElevatedButton(text='<', on_click=next_card)
                ),
                card_container,
                ft.Container(
                    content=ft.ElevatedButton(text='>', on_click=preview_card)
                ),
            ],
        )
    )

    page.add(layout)
    
    page.run_task(rotate_border)




if __name__ == '__main__':
    asyncio.run(ft.app_async(target=main, assets_dir='assets', view=ft.WEB_BROWSER))
