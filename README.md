# planets
(Check planet conjunctions transits and equidistances.)

RATIONALE:
Hay líos de concentración, cansancio y volumen mental de acuerdo a la posición de los planetas?
No lo sé.
Pero hay ciclos de 8 años en el humor y otros fenómenos, que tienen que ver con Venus, y se forma una estrella de 5 puntas si uno lo dibuja en un plano Geocéntrico, es decir, con la Tierra en el centro. Eso se llama el ciclo sinóico.
Eso me llenó de preguntas. No era solo Venus.
Bajé data de la NASA, libremente disponible, y simulé las órbitas.
Encontré correlación entre estos temas, cuando Mercurio está pasando justo enfrente o justo detrás del Sol, Y A LA VEZ EQUIDISTANTE a Venus o a Marte. SOBRE TODO MERCURIO EQUIDISTANTE A VENUS. En esos casos, el simulador pone una alerta en circulito rojo semitransparente.

Me ayudaron a hacer este programa las sugerencias y presiones de amigos de la comunidad.

Fechas en ls que pasa eso son por ejemplo 2024-09 y 2025-10 (septiembre 2024 y septiembre 2025).


Hice un simulador de órbitas de los planetas Mercurio, Venus y Marte. Acá está:

[https://zenstep.com.ar/files/canvas_planets_v4.html](https://zenstep.com.ar/files/canvas_planets_v4.html)

o en, para bajar:

[https://github.com/jmcabo/planets/releases/download/releaseV4/canvas_planets_v4.html](https://github.com/jmcabo/planets/releases/download/releaseV4/canvas_planets_v4.html)

y el fondo en:

[https://github.com/jmcabo/planets/releases/download/releaseV3/IMG-20200121-WA0046_fotoCieloJanis.jpg](https://github.com/jmcabo/planets/releases/download/releaseV3/IMG-20200121-WA0046_fotoCieloJanis.jpg)

también:

[https://jmcabo.github.io/planets/](https://jmcabo.github.io/planets/)

Sirve para ver conjunciones, como las de 1981 o 2019 o la que va a haber en Enero 2026.

También para ver equidistancias.

Usé data bajable del JPL / NASA / CalTech para las órbitas respecto de marco de referencia J2000.

También hice un script en python que outputea la data para el javascript. Originalmente ese python era un script hecho por alguien de stackexchange para graficar solamente Marte, en un gráfico tipo excel de línea (distancia a tierra versus tiempo):

[https://space.stackexchange.com/questions/41619/how-to-determine-the-distance-between-where-earth-and-mars-are-two-specific-date](https://space.stackexchange.com/questions/41619/how-to-determine-the-distance-between-where-earth-and-mars-are-two-specific-date)



URLS:
Simulador:
[https://zenstep.com.ar/files/canvas_planets_v3.html](https://zenstep.com.ar/files/canvas_planets_v3.html)


Fondo de pantalla del simulador (mi hermana hizo curso de astrofotógrafa). Click botón derecho y guardar en mismo directorio que el html:
[https://zenstep.com.ar/files/IMG-20200121-WA0046_fotoCieloJanis.jpg](https://zenstep.com.ar/files/IMG-20200121-WA0046_fotoCieloJanis.jpg)


Script que genera la data origen y alternativamente también gráficos de
distancias (pueden ser distancias en minutos luz o AU):
[https://zenstep.com.ar/files/planets.py](https://zenstep.com.ar/files/planets.py)


Todo completo con excel de graficos y la lib AWP que uso en el script python:
[https://zenstep.com.ar/files/Planets_2025-09-08_2.7z](https://zenstep.com.ar/files/Planets_2025-09-08_2.7z)


Esto también está en:
[https://github.com/jmcabo/planets](https://github.com/jmcabo/planets)


--jm

















