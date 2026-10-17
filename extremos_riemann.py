from manim import *


def etiqueta_voz(nombre):
    return Text(
        f"Voz: {nombre}",
        font_size=16,
        color=GRAY_B,
    ).to_corner(UL, buff=0.25)


class ComparacionExtremos(Scene):
    def construct(self):

        # ==========================================
        # 1. PORTADA:
        # ==========================================

        cabecera = Text(
            "CALCULO INTERMEDIO | EID 2026",
            font_size=23,
            color=BLUE_B,
        ).to_edge(UP, buff=0.4)

        titulo = Text(
            "SUMAS DE RIEMANN",
            font_size=42,
            weight=BOLD,
        ).move_to(UP * 1.65)

        subtitulo = Text(
            "Extremos izquierdos y derechos",
            font_size=26,
            color=BLUE_B,
        ).next_to(titulo, DOWN, buff=0.25)

        grupo = Text(
            "GRUPO 2",
            font_size=24,
            color=YELLOW,
        ).next_to(subtitulo, DOWN, buff=0.35)

        integrantes = VGroup(
            Text("INTEGRANTES", font_size=21, color=BLUE_B),
            Text("Camila Fuentes", font_size=20),
            Text("Francisca Alvarado", font_size=20),
            Text("Isidora Valverde", font_size=20),
        ).arrange(
            DOWN,
            aligned_edge=LEFT,
            buff=0.12,
        ).move_to(LEFT * 3 + DOWN * 1.35)

        fecha = Text(
            "21/10/2026",
            font_size=20,
            color=GRAY_B,
        ).to_corner(DR, buff=0.4)

        portada = VGroup(
            cabecera,
            titulo,
            subtitulo,
            grupo,
            integrantes,
            fecha,
        )

        self.play(FadeIn(cabecera), run_time=1)
        self.play(
            Write(titulo),
            FadeIn(subtitulo),
            run_time=2,
        )
        self.play(
            FadeIn(grupo),
            FadeIn(integrantes),
            FadeIn(fecha),
            run_time=2,
        )
        self.wait(13)
        self.play(FadeOut(portada), run_time=2)

        # ==========================================
        # 2. PREGUNTA CENTRAl:
        # ==========================================

        voz_camila = etiqueta_voz("Camila Fuentes")

        encabezado_pregunta = Text(
            "PREGUNTA CENTRAL",
            font_size=25,
            color=BLUE_B,
        ).to_edge(UP, buff=0.8)

        pregunta = Paragraph(
            "¿Por qué dos sumas construidas sobre la misma",
            "partición pueden entregar valores distintos?",
            font_size=32,
            alignment="center",
            line_spacing=0.9,
        )

        self.play(
            Write(encabezado_pregunta),
            run_time=1,
        )
        self.play(
            FadeIn(voz_camila),
            FadeIn(pregunta, shift=UP * 0.2),
            run_time=2,
        )
        self.wait(15)
        self.play(
            FadeOut(encabezado_pregunta),
            FadeOut(pregunta),
            FadeOut(voz_camila),
            run_time=2,
        )

        # ==========================================
        # 3. TEORIA: 
        # ==========================================

        voz_francisca = etiqueta_voz("Francisca Alvarado")

        titulo_teoria = Text(
            "¿Que elementos intervienen?",
            font_size=31,
            color=BLUE_B,
        ).to_edge(UP, buff=0.35)

        conceptos = VGroup(
            MathTex(r"f(x)=x+1", font_size=34),
            MathTex(r"[a,b]=[0,4], \qquad n=4", font_size=31),
            MathTex(
                r"\Delta x=\frac{b-a}{n}"
                r"=\frac{4-0}{4}=1",
                font_size=31,
            ),
            Text(
                "Particion: 0, 1, 2, 3, 4",
                font_size=26,
            ),
            MathTex(
                r"S_n=\sum_{i=1}^{n}"
                r"f(x_i^*)\,\Delta x",
                font_size=31,
            ),
            Text(
                "Altura por ancho; despues sumamos las areas.",
                font_size=22,
            ),
        ).arrange(
            DOWN,
            buff=0.23,
        ).scale_to_fit_height(4.8).move_to(DOWN * 0.15)

        self.play(
            FadeIn(voz_francisca),
            Write(titulo_teoria),
            run_time=1,
        )
        self.play(FadeIn(conceptos), run_time=2)
        self.wait(40)
        self.play(
            FadeOut(voz_francisca),
            FadeOut(titulo_teoria),
            FadeOut(conceptos),
            run_time=2,
        )
