# planets
Copyright (C) Juan Manuel Cabo, 2025. Todos los derechos reservados.

Planets. Check planet conjunctions transits and equidistances: [https://zenstep.com.ar/files/canvas_planets_1900.html](https://zenstep.com.ar/files/canvas_planets_1900.html)

also at:
[https://jmcabo.github.io/planets/canvas_planets_1900.html](https://jmcabo.github.io/planets/canvas_planets_1900.html)

![Ejemplo en 2024-09](https://github.com/jmcabo/planets/blob/main/Screenshot_2025-09-09_093039_2024_oct_28.png)

Tomarse todo lo que sigue con humor!! :-) :-) Es solo un programita HTML (código fuente javascript autocontenido en el html), que tardé 2 días en desarrollar (y que quise programar desde los 90s que siempre quise visualizar las órbitas en un programita gráfico y lo postponía como ejercicio gráfico.).

RATIONALE:
Hay líos de concentración, cansancio y volumen mental de acuerdo a la posición de los planetas?

No lo sé.

Pero hay ciclos de 8 años en el humor y otros fenómenos, que tienen que ver con Venus, y se forma una estrella de 5 puntas si uno lo dibuja en un plano Geocéntrico, es decir, con la Tierra en el centro. Eso se llama el ciclo sinóico.
Eso me llenó de preguntas. No era solo Venus.

Bajé data de la NASA, libremente disponible, y simulé las órbitas.

Encontré correlación entre estos temas, cuando Mercurio está pasando justo enfrente o justo detrás del Sol, Y A LA VEZ EQUIDISTANTE a Venus o a Marte. SOBRE TODO MERCURIO EQUIDISTANTE A VENUS. En esos casos, el simulador pone una alerta en circulito rojo semitransparente.

Me ayudaron a hacer este programa las sugerencias y presiones de amigos de la comunidad. Cada 2 años ellos experimentan lío inexplicable. Todo culmina en una semana terrible donde el lío aumenta, y luego por 3 o 4 días desaparece o reaparece. Attention Training Technique es muy útil: https://www.youtube.com/watch?v=kbTkwMJExCc

Fechas en ls que pasa eso son por ejemplo 2024-09 y 2025-10 (septiembre 2024 y septiembre 2025).

Qué relación existe?

![Ejemplo en 2025-09](https://github.com/jmcabo/planets/blob/main/Screenshot_2025-09-09_072914.png)


Las rayas magenta entre planetas indican equidistancias dentro del umbral (0.3 AU por default, que son 2.5 minutos luz).
Los conos indican cercanía al Sol, y que el Sol está por alterar nuestra capacidad de resolver esos planetas (aumentando escala y offset, es decir, brillo y contraste). Primero se aumenta la ganancia al verlos, luego se pierden, luego pueden reaparecer a los 3 días. Por ejemplo ahora 2025-09-09, Mercurio está por transitar atrás del Sol, el día más alineado es 2025-09-12 y 2025-09-13 viernes y sábado).

Alrededor del día 8 de Enero 2026, 2026-01-08, se van a alinear Marte y Venus justo detrás del Sol. Esto ya pasó por ejemplo en 1968-06-22 como se puede ver con mi simulador.

![Alineacion 2026](https://github.com/jmcabo/planets/blob/main/Screenshot_2025-09-09_091324.png)

Hay varias de esas alineaciones por década, pero la que se viene es tan impresionante como la de Junio 22 de 1968:

![Alineacion 1968](https://github.com/jmcabo/planets/blob/main/Screenshot_2025-09-09_091440_1968_June.png)

La década del 70 fue dura en varios países, mucha gente se cayó del sistema, se los perseguía por no emitir? Solo por eso? Por no estar loopeados/filtrados por un planeta? Quien sabe. O quizás por emitir de más?

DELIRIO A CONTINUACIÓN:

La mente ve el pasado de su robot biológico, y actúa en su presente, eligiendo a qué prestar atención. Si estamos absortos en la lectura de un libro, ignorando la radio o la lluvia, prestamos justo atención a la radio o la lluvia cuando algo nos llama la atención (un nombre) o suena un rayo.

Quizás la única manera de retrasar una señal que va a la velocidad de la luz es loopearla por los planetas, por algo bien distante. Quizás sus núcleos de hierro hacen de espejo para la señal. Quizás por eso dicen que las mujeres son de Venus, y los hombres de Marte (y Mercurio serán los jóvenes). Quizás los bebés nacen con las mismas habilidades que necesitarían los paralíticos para empezar a moverse. Quizás esa es la naturaleza de buddha, o quizás estoy mezclando todo :) 
Da para novela de ciencia ficción.

En fin, daba para hacer un grafiquito. Hice este simulador con detector de equidistancias entre Venus y Marte y con detector de alineamientos tras o enfrente del Sol (baja SNR) en 2 días de programar sin parar mucho. Era fácil, la NASA provee gratis las coordenadas de los planetas en marco de referencia geocéntrico llamado J2000.

Hay algunos temas de salud física (y también de salud mental) que mucha gente experimenta con un período de 2 años, modulado en otros períodos de 4 y 8 años. Estas son las distancias ejemplo en 2024 y en 2025, los entrecruzamientos en las curvas de colores a continuación son las fechas en cuando 2 planetas están a los mismos minutos luz (algo se pegotea cuando tienen la misma diferencia de tiempo. Se pegotean las almas cuando piensan lo mismo? Se pegotean hasta los linfocitos, que parecen tener vida propia? Telepáticamente? Quien sabe, es un delirio. Pero dicen que unos son de Venus y los otros de Marte. Cuando la distancia es 10 minutos, el roundtrip es 20minutos. Cuando Venus está a 10m10s luz y Mercurio está a 10m20s luz, hay solo 10 segundos de diferencia entre ambos. Qué sucede cuando dos personas piensan la misma idea a 10 segundos de distancia si son de distintos loopeamientos? (durante varias horas seguidas varios días seguidos?. NO LO HAGAN NUNCA!. Lo que a nuestras computadoras cuesta O(N²) calcular que es ver si dos elementos entre N coinciden, al Universo le sale gratis en complejidad temporal, es otro tipo de computadora?. Fin del deliriop :)

Justamente, Marte se aleja y vuelve cada 2 años:

![Gráfico distancias 2024](https://github.com/jmcabo/planets/blob/main/grafico_planetas_minutos_2024.jpg)

![Gráfico distancias 2025](https://github.com/jmcabo/planets/blob/main/grafico_planetas_minutos_2025.jpg)

![Gráfico distancias 2026](https://github.com/jmcabo/planets/blob/main/grafico_planetas_minutos_2026.jpg)

Delirio:  Qué va a pasar el 2026-01-08 cuando se alínien Marte y Venus detrás del Sol? Si mi teoría divertidamente delirante fuera cierta, los humanos se desloopearían tal vez de esos planetas y se conectarían mejor a sí mismos, dejando de desparramarse en el espacio tiempo, pero quedando cerrados en sí mismos. Sin emitir.

Advertencia (Idea para historia ciencia ficción): Si mucha gente hace cadenita de oración de loopeos pasando por Marte cuando este se encuentra más alejado, cada uno suma 40 minutos de delay. Pero esto es peligroso, y podría ver el pasado de una mente (en algún aspecto, tal vez emocional, tal vez sensorial o de humor, bienestar o malestar), si fuera cierto que se pueden sincronizar pensando lo mismo, durante horas, días y meses. El problema de eso, es que imaginando una cadena de 10 años de duración, cualquier mente escuchando en ese HUB, podría saltar a cualquier otra mente y mamarrachar el espacio tiempo. Sería impredecible a dónde saltan, porque no todos los que oyen pueden hablar (depende de si están antes o después en la cadenita). Me pregunto si siempre siempre siempre esos saltos tienen de efecto pretérito, causar luego el salto futuro hacia atrás una vez más, cerrando la cinta de Moebius.
Esta puede ser la verdadera caja de Pandora.

Y las consecuencias de semejantes cadenitas, es que quizás todas esas almas sean la misma alma, con los mismos qualia y significantes, saltando unas a otras, viviendo una vida que nunca avanza de este siglo. La misma alma viviendo 8mil millones de vidas, que nunca puede avanzar del siglo. 

Suena terrible. Mejor ni lo intenten. 

La cinta de Moebius esa, sería dificilísima de cerrar. O tal vez no, si tiene algunos criterios de monotonía estricta, y orden entre antecesor y sucesor (parent -> child), pero no creo que pueda haber disciplina o predictibilidad en eso.

El fin de la historia registrada, puede ser simplemente reconocer que no hace falta loopear a nadie, que en esas fechas de mala salud uno debe guardarse, no conectar, y que lo único que empeora con la edad es la cantidad de gente que a uno lo conoce y forma la cadenita. Que debería disolverse en vez de uno borrarse. (Fin idea para ciencia ficción).



Resumen links:

Hice un simulador de órbitas de los planetas Mercurio, Venus y Marte. Acá está (versión completa desde año 1600 hasta 2649, pesado de cargar):

[https://zenstep.com.ar/files/canvas_planets_v5.html](https://zenstep.com.ar/files/canvas_planets_v5.html)

(el código fuente es el HTML mismo pero abierto en editor, no depende de librerías/bibliotecas de código)
Versión corta, liviana de cargar entre 1900 y 2050:
[https://zenstep.com.ar/files/canvas_planets_1900.html](https://zenstep.com.ar/files/canvas_planets_1900.html)

o en, para bajar:

[https://github.com/jmcabo/planets/releases/download/releaseV5/canvas_planets_v5.html](https://github.com/jmcabo/planets/releases/download/releaseV5/canvas_planets_v5.html)

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
[https://zenstep.com.ar/files/canvas_planets_v5.html](https://zenstep.com.ar/files/canvas_planets_v5.html)

Versión liviana reducida a solo 150 años:
[https://zenstep.com.ar/files/canvas_planets_1900.html](https://zenstep.com.ar/files/canvas_planets_1900.html)


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



