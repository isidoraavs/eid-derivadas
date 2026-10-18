from pathlib import Path
import subprocess
import sys

from manim import *


def etiqueta_voz(nombre):
    return Text(
        f"Voz: {nombre}",
        font_size=16,
        color=GRAY_B,
    ).to_corner(UL, buff=0.25)


class ComparacionExtremos(Scene):
    def iniciar_voz(self, archivo, ganancia=None):
        ruta_audio = Path(__file__).resolve().parent / "media" / "audio" / archivo
        if not ruta_audio.is_file():
            raise FileNotFoundError(f"No se encontro el audio: {ruta_audio}")

        self.add_sound(str(ruta_audio), gain=ganancia)
        return self.time

    def esperar_duracion_voz(self, inicio, duracion):
        restante = duracion - (self.time - inicio)
        if restante < 0:
            raise RuntimeError(
                "Las animaciones exceden la duracion de la grabacion "
                f"por {-restante:.2f} segundos."
            )
        self.wait(restante)

    def crear_rectangulos(self, ejes, extremo_derecho, color):
        rectangulos = VGroup()
        puntos = VGroup()

        for i in range(4):
            x_izq = i
            x_der = i + 1
            x_muestra = x_der if extremo_derecho else x_izq
            altura = x_muestra + 1

            rectangulo = Polygon(
                ejes.c2p(x_izq, 0),
                ejes.c2p(x_der, 0),
                ejes.c2p(x_der, altura),
                ejes.c2p(x_izq, altura),
                color=color,
                stroke_width=2,
                fill_color=color,
                fill_opacity=0.42,
            )
            punto = Dot(
                ejes.c2p(x_muestra, altura),
                radius=0.065,
                color=color,
            )
            rectangulos.add(rectangulo)
            puntos.add(punto)

        return rectangulos, puntos

    def construct(self):
        cabecera = Text(
            "CALCULO INTERMEDIO | EID",
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
        self.play(Write(titulo), FadeIn(subtitulo), run_time=1)
        self.play(
            FadeIn(grupo),
            FadeIn(integrantes),
            FadeIn(fecha),
            run_time=1,
        )
        self.wait(3)
        self.play(FadeOut(portada), run_time=1)

        inicio_voz = self.iniciar_voz("camila_presentacion.ogg", ganancia=5)
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
        self.play(Write(encabezado_pregunta), run_time=1)
        self.play(
            FadeIn(voz_camila),
            FadeIn(pregunta, shift=UP * 0.2),
            run_time=2,
        )
        self.esperar_duracion_voz(inicio_voz, 35.306125)

        inicio_voz = self.iniciar_voz("camila_teoria.ogg", ganancia=6)
        voz_camila_teoria = etiqueta_voz("Camila Fuentes")
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
            Text("Particion: 0, 1, 2, 3, 4", font_size=26),
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
            FadeOut(encabezado_pregunta),
            FadeOut(pregunta),
            FadeOut(voz_camila),
            FadeIn(voz_camila_teoria),
            Write(titulo_teoria),
            run_time=1,
        )
        self.play(FadeIn(conceptos), run_time=2)
        self.esperar_duracion_voz(inicio_voz, 96.147833)

        inicio_voz = self.iniciar_voz(
            "francisca_extremos_izquierdos.ogg",
            ganancia=3,
        )
        voz_francisca = etiqueta_voz("Francisca Alvarado")
        ejes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 6, 1],
            x_length=7,
            y_length=3.6,
            axis_config={
                "include_numbers": True,
                "font_size": 20,
            },
            tips=False,
        ).shift(DOWN * 0.45)
        etiquetas = ejes.get_axis_labels(
            x_label=MathTex("x", font_size=27),
            y_label=MathTex("f(x)", font_size=27),
        )
        curva = ejes.plot(
            lambda x: x + 1,
            x_range=[0, 4],
            color=YELLOW,
            stroke_width=4,
        )
        nombre_funcion = MathTex(
            r"f(x)=x+1",
            color=YELLOW,
            font_size=28,
        ).next_to(ejes.c2p(3, 4), UR, buff=0.1)
        titulo_grafica = Text(
            "Ejemplo: f(x)=x+1 en [0,4]",
            font_size=27,
        ).to_edge(UP, buff=0.25)
        izquierdos, puntos_izq = self.crear_rectangulos(ejes, False, BLUE)
        encabezado_izq = Text(
            "Extremos izquierdos",
            color=BLUE,
            font_size=27,
        ).move_to(UP * 2.25)
        suma_izq = MathTex(
            r"S_I=1(1+2+3+4)=10",
            color=BLUE,
            font_size=36,
        ).to_edge(DOWN, buff=0.2)
        puntos_texto_izq = Text(
            "Puntos muestra: 0, 1, 2, 3",
            color=BLUE,
            font_size=20,
        ).next_to(suma_izq, UP, buff=0.12)

        self.play(
            FadeOut(voz_camila_teoria),
            FadeOut(titulo_teoria),
            FadeOut(conceptos),
            FadeIn(voz_francisca),
            Write(titulo_grafica),
            Create(ejes),
            Write(etiquetas),
            Create(curva),
            run_time=3,
        )
        self.play(FadeIn(izquierdos), FadeIn(puntos_izq), run_time=2)
        self.bring_to_front(ejes, curva, etiquetas, nombre_funcion, puntos_izq)
        self.play(
            Write(nombre_funcion),
            Write(encabezado_izq),
            Write(puntos_texto_izq),
            Write(suma_izq),
            run_time=2,
        )
        self.esperar_duracion_voz(inicio_voz, 51.52)

        inicio_voz = self.iniciar_voz("isidora_extremos_derechos.ogg")
        voz_isidora = etiqueta_voz("Isidora Valverde")
        derechos, puntos_der = self.crear_rectangulos(ejes, True, ORANGE)
        encabezado_der = Text(
            "Extremos derechos",
            color=ORANGE,
            font_size=27,
        ).move_to(encabezado_izq)
        puntos_texto_der = Text(
            "Puntos muestra: 1, 2, 3, 4",
            color=ORANGE,
            font_size=20,
        ).move_to(puntos_texto_izq)
        suma_der = MathTex(
            r"S_D=1(2+3+4+5)=14",
            color=ORANGE,
            font_size=36,
        ).move_to(suma_izq)
        self.play(
            FadeOut(voz_francisca),
            FadeIn(voz_isidora),
            FadeOut(izquierdos),
            FadeOut(puntos_izq),
            FadeOut(puntos_texto_izq),
            FadeOut(suma_izq),
            Transform(encabezado_izq, encabezado_der),
            FadeIn(derechos),
            FadeIn(puntos_der),
            run_time=3,
        )
        self.bring_to_front(ejes, curva, etiquetas, nombre_funcion, puntos_der)
        self.play(Write(puntos_texto_der), Write(suma_der), run_time=2)
        self.esperar_duracion_voz(inicio_voz, 50.4865)

        inicio_voz = self.iniciar_voz("camila_comparacion.ogg", ganancia=6)
        voz_camila_compara = etiqueta_voz("Camila Fuentes")
        titulo_comparacion = Text(
            "Comparemos los resultados",
            font_size=30,
            color=BLUE_B,
        ).to_edge(UP, buff=0.35)
        comparacion = VGroup(
            MathTex(r"S_I=10", color=BLUE, font_size=35),
            MathTex(
                r"\int_0^4 (x+1)\,dx"
                r"=\left[\frac{x^2}{2}+x\right]_0^4=12",
                font_size=27,
            ),
            MathTex(r"S_D=14", color=ORANGE, font_size=35),
            MathTex(r"10<12<14", font_size=36),
        ).arrange(
            DOWN,
            buff=0.22,
        ).move_to(UP * 0.45)
        interpretacion = VGroup(
            Text(
                "Izquierda: subestima el area.",
                color=BLUE,
                font_size=22,
            ),
            Text(
                "Derecha: sobreestima el area.",
                color=ORANGE,
                font_size=22,
            ),
        ).arrange(
            DOWN,
            buff=0.12,
        ).to_edge(DOWN, buff=0.2)
        self.play(
            FadeOut(voz_isidora),
            FadeOut(titulo_grafica),
            FadeOut(ejes),
            FadeOut(etiquetas),
            FadeOut(curva),
            FadeOut(nombre_funcion),
            FadeOut(derechos),
            FadeOut(puntos_der),
            FadeOut(encabezado_izq),
            FadeOut(puntos_texto_der),
            FadeOut(suma_der),
            FadeIn(voz_camila_compara),
            Write(titulo_comparacion),
            run_time=2,
        )
        self.play(FadeIn(comparacion), run_time=3)
        self.play(FadeIn(interpretacion), run_time=2)
        self.esperar_duracion_voz(inicio_voz, 51.007208)

        inicio_voz = self.iniciar_voz("isidora_conclusion.ogg")
        voz_isidora_cierre = etiqueta_voz("Isidora Valverde")
        cierre = Paragraph(
            "Dos sumas pueden diferir porque el punto muestra",
            "cambia la altura de los rectangulos.",
            font_size=30,
            alignment="center",
        ).move_to(UP * 0.65)
        cierre_2 = Text(
            "Al refinar la particion, las sumas se relacionan",
            font_size=23,
        ).next_to(cierre, DOWN, buff=0.45)
        cierre_3 = Text(
            "con la integral definida.",
            font_size=23,
            color=BLUE_B,
        ).next_to(cierre_2, DOWN, buff=0.18)
        self.play(
            FadeOut(titulo_comparacion),
            FadeOut(voz_camila_compara),
            FadeOut(comparacion),
            FadeOut(interpretacion),
            Write(cierre),
            run_time=2,
        )
        self.play(
            FadeIn(voz_isidora_cierre),
            Write(cierre_2),
            Write(cierre_3),
            run_time=2,
        )
        self.esperar_duracion_voz(inicio_voz, 26.8265)

        creditos = VGroup(
            Text(
                "CREDITOS Y FUENTES",
                font_size=24,
                color=BLUE_B,
            ),
            Text(
                "OpenStax / LibreTexts: Aproximacion de areas",
                font_size=15,
            ),
            Text(
                "https://espanol.libretexts.org/Bookshelves/Matematicas/",
                font_size=11,
            ),
            Text(
                "Libro%3A_Calculo_%28OpenStax%29/05%3A_Integraci%C3%B3n/",
                font_size=11,
            ),
            Text(
                "5.01%3A_Aproximaci%C3%B3n_de_%C3%A1reas",
                font_size=11,
            ),
            Text(
                "Khan Academy en espanol: Sumas de Riemann",
                font_size=15,
            ),
            Text(
                "https://es.khanacademy.org/math/integral-calculus/",
                font_size=11,
            ),
            Text(
                "ic-integration/a/left-and-right-riemann-sums",
                font_size=11,
            ),
            Text(
                "Manim Community: Documentacion oficial",
                font_size=15,
            ),
            Text(
                "https://docs.manim.community/en/stable/tutorials/",
                font_size=11,
            ),
            Text("quickstart.html", font_size=11),
        ).arrange(
            DOWN,
            buff=0.13,
        ).scale_to_fit_height(6.5).move_to(ORIGIN)
        self.play(
            FadeOut(voz_isidora_cierre),
            FadeOut(cierre),
            FadeOut(cierre_2),
            FadeOut(cierre_3),
            FadeIn(creditos),
            run_time=2,
        )
        self.wait(16)
        self.play(FadeOut(creditos), run_time=2)


if __name__ == "__main__":
    proyecto = Path(__file__).resolve().parent
    subprocess.run(
        [
            sys.executable,
            "-m",
            "manim",
            "-pqm",
            str(Path(__file__).resolve()),
            "ComparacionExtremos",
        ],
        cwd=proyecto,
        check=True,
    )
