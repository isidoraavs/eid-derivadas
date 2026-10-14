from manim import *

if __name__ == "__main__":
    import subprocess
    import sys
    from pathlib import Path

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


class ComparacionExtremos(Scene):
    def construct(self):
        titulo = Text(
            "Sumas de Riemann: extremos izquierdos y derechos",
            font_size=34,
        ).to_edge(UP, buff=0.25)

        ejes = Axes(
            x_range=[0, 4, 1],
            y_range=[0, 6, 1],
            x_length=7,
            y_length=4.4,
            axis_config={"include_numbers": True, "font_size": 24},
            tips=False,
        ).shift(UP * 0.25)
        etiquetas = ejes.get_axis_labels(
            x_label=MathTex("x", font_size=32),
            y_label=MathTex("f(x)", font_size=32),
        )
        etiquetas[1].shift(DOWN * 0.55)
        curva = ejes.plot(
            lambda x: x + 1,
            x_range=[0, 4],
            color=YELLOW,
            stroke_width=4,
        )
        nombre_funcion = MathTex("f(x)=x+1", color=YELLOW, font_size=34)
        nombre_funcion.next_to(ejes.c2p(4, 5), UR, buff=0.1)

        self.play(Write(titulo))
        self.play(Create(ejes), Write(etiquetas))
        self.play(Create(curva), Write(nombre_funcion))

        def crear_rectangulos(usando_extremo_derecho, color):
            rectangulos = VGroup()
            puntos = VGroup()
            for i in range(4):
                x_izq = i
                x_der = i + 1
                x_muestra = x_der if usando_extremo_derecho else x_izq
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

        izquierdos, puntos_izq = crear_rectangulos(False, BLUE)
        encabezado_izq = Text(
            "Altura tomada en el extremo izquierdo",
            color=BLUE,
            font_size=27,
        ).move_to(UP * 2.55)
        suma_izq = MathTex(
            r"S_I=1(1+2+3+4)=10",
            color=BLUE,
            font_size=40,
        ).to_edge(DOWN, buff=0.3)

        self.play(FadeIn(izquierdos))
        self.add(puntos_izq)
        self.bring_to_front(ejes, curva, etiquetas, nombre_funcion)
        self.play(Write(encabezado_izq), Write(suma_izq))
        self.wait(1.5)

        derechos, puntos_der = crear_rectangulos(True, ORANGE)
        encabezado_der = Text(
            "Altura tomada en el extremo derecho",
            color=ORANGE,
            font_size=27,
        ).move_to(encabezado_izq)
        suma_der = MathTex(
            r"S_D=1(2+3+4+5)=14",
            color=ORANGE,
            font_size=40,
        ).move_to(suma_izq)

        self.play(
            FadeOut(izquierdos),
            FadeOut(puntos_izq),
            FadeOut(suma_izq),
            Transform(encabezado_izq, encabezado_der),
            FadeIn(derechos),
            FadeIn(puntos_der),
        )
        self.add(encabezado_izq)
        self.bring_to_front(ejes, curva, etiquetas, nombre_funcion)
        self.play(Write(suma_der))
        self.wait(1.5)

        comparacion = VGroup(
            MathTex(
                r"\int_0^4(x+1)\,dx=12",
                font_size=32,
            ),
            MathTex(
                r"S_I=10<12<S_D=14",
                font_size=36,
            ),
            Text(
                "Con más rectángulos, ambas sumas se acercan al área exacta.",
                font_size=20,
            ),
        ).arrange(DOWN, buff=0.08).to_edge(DOWN, buff=0.15)

        self.play(
            FadeOut(suma_der),
            FadeOut(encabezado_izq),
            FadeIn(comparacion),
        )
        self.wait(2)
