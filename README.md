#Laboratorio 3

El objetivo de este laboratorio es que practiquen los conceptos que hemos aprendido para hacer un renderizado en tiempo real. 

Su misión es: utilizando únicamente la función get_at y set_at de pygame, deben implementar el algoritmo de the game of life de Conway. 

Nota para los de videojuegos: en lugar de trabajar en pygame, les recomiendo utilizar SDL en C++. Es una buena oportunidad para ustedes, ya que es un ejercicio simple y bien documentado. SDL fue utilizado para crear juegos como Amnesia: The dark descent y varios juegos del source engine, como Half Life 2 y algunos counter strikes. Las antiguas versiones de unreal también estaban hechas en SDL y hasta los engines de python, como pygame y renpy, ambos están hechos en esta librería. Les va a dar un diferenciador en su curriculum. Les dejo este recurso: http://lazyfoo.net/tutorials/SDL/index.php Links to an external site.. Para fines de este laboratorio, no necesitan más que el primer tutorial. 

El algoritmo de conway es muy simple:

Una célula tiene 8 vecinos. Para nosotros, una célula es un pixel, los vecinos son los 8 píxeles alrededor. 
La célula puede estar viva (pintada de blanco, digamos) o muerta (pintada de negro). Pueden usar otros colores, pero esta es la idea.
Cada "turno" va a ser un frame para nosotros. Pueden hacer un delay entre cada frame para poder mejor visualizar su animación.
La resolución queda a su discreción, pero les recomiendo trabajar en una resolución muy baja, de como 100x100, y cuando terminen hacer algunas pruebas a resoluciones altas. 
Las reglas son, para cada turno:

Cualquier célula viva que tenga menos de dos vecinos vivos, muere. (underpopulation)
Una célula viva que tenga dos o tres vecinos vivos, sobrevive. (survival)
Cualquier célula viva que tenga más de tres vecinos vivos, muere. (overpopulation)
Cualquier célula muerta que tenga exactamente tres vecinos vivos, vive. (reproduction)
Además, deben definir un patrón inicial. Este patrón lo pueden hacer simplemente definiendo una lista de píxeles que deben estar vivos al inicio. Usen su creatividad. En wikipedia pueden ver algunos patrones clásicos, pero siempre hay gente descubriendo nuevos, así que quizá pueden descubrir uno y ponerle su nombre. https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life Links to an external site.. Los patrones más interesantes son las spaceships, las guns y los gliders. Solo cargen algunos en una parte de su pantalla y dejen el juego correr un tiempo.

Algo así espero que se mire su pantalla:

Tienen la nota completa si su patrón inicial es creativo y llena una buena parte de la pantalla. Tienen cero si copian el algoritmo de internet o de sus compañeros. Pueden ayudarse, solo no lo copien. 

Tienen 100 puntos en el lab y el curso entero si encuentran una manera de determinar si dado cualquier patrón inicial, eventualmente va a llegar a otro patrón definido. También reformarían la matemática moderna como la conocemos. 

 

Nota sobre las orillas: Hay dos maneras de atacar los puntos de las orillas. Pueden asumir que si el punto está fuera de su framebuffer, está "muerto" o pueden implementar un "loop" en el que se toman en cuenta las células del lado opuesto de la pantalla. Esto hace patrones más interesantes. Por ejemplo: