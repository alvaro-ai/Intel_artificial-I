# Trabajo práctico agentes racionales
## Ejercicio C
#### Pruebas agente simple

Cantidad de cuadros recorridos:

| Entornos/cuadros | 2x2  | 4x4 | 8x8 | 16x16 | 32x32 | 64x64 | 128x128 |
|--------|--------|--------|--------|--------|--------|--------|--------|
|0.1     |1 de 1|0 de 2|6 de 6|18 de 26|77 de 102|95 de 410|80 de 1638|
|0.2     |1 de 1|3 de 3|9 de 13|16 de 51|145 de 205|183 de 819|174 de 3277|
|0.4     |2 de 2|1 de 6|9 de 26|52 de 102|142 de 410|198 de 1638|314 de 6554|
|0.8     |3 de 3|8 de 13|9 de 51|37 de 205|371 de 819|549 de 3277|542 de 13107|


## Ejercicio D
#### Pruebas agente random
Cantidad de cuadros recorridos:

| Entornos/cuadros | 2x2  | 4x4 | 8x8 | 16x16 | 32x32 | 64x64 | 128x128 |
|--------|--------|--------|--------|--------|--------|--------|--------|
|0.1     |1 de 1|2 de 2|6 de 6|17 de 26|27 de 102|37 de 410|31 de 1638|
|0.2     |1 de 1|3 de 3|13 de 13|43 de 51|41 de 205|48 de 819|42 de 3277|
|0.4     |2 de 2|5 de 6|18 de 26|53 de 102|93 de 410|79 de 1638|81 de 6554|
|0.8     |3 de 3|10 de 13|33 de 51|77 de 205|185 de 819|137 de 3277|153 de 13107|


## Ejercicio E
#### 2.9)
**a)** No es posible porque el agente carece de la capacidad de encontrar el camino más eficiente.

**b)** Dependiendo de las condiciones ,un agente con estados sería potencialmente racional ya que el agente sabe por cuales cuadros (estados) ha pasado, evitando repetirlos.

**c)** Sin importar la información disponible , el agente simple, seguiría sin ser racional porque no es capaz de saber por cuales “casillas” pasó, repitiendo movimiento, aunque da lugar a un algoritmo sin duda más eficiente. Un agente con estados seguirá siendo racional.

#### 2.10)

**a)** No. La mínima racionalidad atribuible, en este caso ,es posible por las limitaciones conocidas del mundo.

**b)** El agente reactivo simple que hemos planteado depende de conocer el medio, no capaz de percibir obstáculos. Por otro lado el comportamiento aleatorio del agente random brinda la capacidad , al menos por azar, de sortearlos . Es posible 

**c)** En un mundo muy grande es probable ,por la pérdida de acciones en su aleatoriedad. Cabiendo esperar que si el mundo es muy grande la distribución de la suciedad sea muy dispersa

**d)** Es posible  por el hecho de tener un “comportamiento” que evita repetir decisiones , pero por otro lado repetir decisiones quizás sea una buena decisión , valga la redundancia . Considero a los agentes más o menos aptos a un  entorno y no adaptables. 

