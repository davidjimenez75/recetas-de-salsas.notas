"""Sauce data, part 9: mild Mexican sauces."""

MEX_ES = ["mexico", "poco-picante"]
MEX_EN = ["mexico", "mild"]

SALSAS = [
{
 "slug": "guacamole", "tags_es": MEX_ES + ["aguacate", "sin-alcohol", "vegana"], "tags_en": MEX_EN + ["alcohol-free", "avocado", "vegan"],
 "es": {
  "title": "Guacamole", "meta": "Para **4 personas** · ⏱️ 10 minutos · Dificultad: fácil · Picor: suave",
  "intro": "Aguacate machacado en el molcajete con cebolla, tomate, cilantro y lima. El chile es opcional y sin semillas, así que pica muy poco.",
  "ing": ["3 aguacates maduros", "¼ de cebolla blanca", "1 tomate maduro", "1 puñado de cilantro", "El zumo de 1 lima", "½ chile serrano o jalapeño sin semillas (opcional)", "Sal"],
  "steps": [
   "**La base.** En el molcajete (o un bol), machaca la cebolla picada, el chile, si lo usas, y la mitad del cilantro con una pizca de sal hasta tener una pasta.",
   "**El aguacate.** Añade la pulpa de los aguacates y machácala con un tenedor o la mano del molcajete, dejando algunos trozos.",
   "**El resto.** Añade el tomate en dados pequeños, sin semillas, el resto del cilantro picado y el zumo de lima.",
   "**Probar.** Ajusta de sal y lima y sírvelo enseguida.",
  ],
  "tips": ["**Para que no se oscurezca:** cúbrelo con film pegado a la superficie.", "**Sin nada de picante:** quita el chile; el sabor sigue siendo el de un buen guacamole.", "**Con** totopos, tacos, frijoles o carne asada."],
 },
 "en": {
  "title": "Guacamole", "meta": "Serves **4** · ⏱️ 10 minutes · Difficulty: easy · Heat: mild",
  "intro": "Avocado mashed in a molcajete with onion, tomato, cilantro and lime. The chile is optional and seeded, so it's barely spicy.",
  "ing": ["3 ripe avocados", "¼ white onion", "1 ripe tomato", "1 handful cilantro", "Juice of 1 lime", "½ serrano or jalapeño chile, seeded (optional)", "Salt"],
  "steps": [
   "**Base.** In a molcajete (or a bowl), mash the chopped onion, the chile, if using, and half the cilantro with a pinch of salt into a paste.",
   "**Avocado.** Add the avocado flesh and mash it with a fork or the pestle, leaving some chunks.",
   "**The rest.** Add the seeded, finely diced tomato, the rest of the cilantro, chopped, and the lime juice.",
   "**Taste.** Adjust salt and lime and serve right away.",
  ],
  "tips": ["**To keep it green:** press plastic wrap right onto the surface.", "**No heat at all:** skip the chile; it's still a great guacamole.", "**Serve with** tortilla chips, tacos, beans or grilled meat."],
 },
},
{
 "slug": "mole-poblano", "tags_es": MEX_ES + ["chocolate", "frutos-secos", "sesamo"], "tags_en": MEX_EN + ["chocolate", "nuts", "sesame"],
 "es": {
  "title": "Mole poblano", "meta": "Para **6 personas** · ⏱️ 1 h 30 min · Dificultad: difícil · Picor: suave",
  "intro": "La salsa de Puebla: chiles secos suaves, frutos secos, sésamo, especias, tortilla y chocolate, molidos y cocidos despacio. Con los chiles sin semillas ni venas, apenas pica.",
  "ing": ["3 chiles anchos", "3 chiles mulatos", "2 chiles pasilla", "1 tomate", "½ cebolla", "2 dientes de ajo", "30 g de almendras", "30 g de cacahuetes", "3 cucharadas de sésamo (y más para servir)", "30 g de pasas", "1 tortilla de maíz dura (o 1 rebanada de pan)", "½ cucharadita de canela", "2 clavos", "50 g de chocolate de mesa mexicano (o chocolate negro y una pizca más de canela)", "1 litro de caldo de pollo", "1 cucharada de azúcar", "4 cucharadas de manteca o de aceite", "Sal"],
  "steps": [
   "**Los chiles.** Quítales el tallo, las semillas y las venas. Tuéstalos unos segundos por lado en una sartén seca, sin que se quemen, y remójalos 20 minutos en agua caliente.",
   "**Freír.** En un poco de manteca, fríe por separado las almendras, los cacahuetes, el sésamo, las pasas, la tortilla troceada, la canela y los clavos, solo hasta que se doren.",
   "**Asar.** Asa el tomate, la cebolla y el ajo en la sartén hasta que estén tostados.",
   "**Moler.** Tritura los chiles escurridos con todo lo frito y lo asado y con parte del caldo, hasta tener una pasta muy fina. Cuélala si hace falta.",
   "**Cocer.** Fríe la pasta en el resto de la manteca a fuego medio 10 minutos, removiendo. Añade el resto del caldo, el chocolate, el azúcar y la sal y cuece a fuego suave 30–40 minutos, hasta que espese y brille.",
  ],
  "tips": ["**Con** pollo o pavo cocido, enchiladas o arroz rojo; espolvorea sésamo tostado por encima.", "**Mejor al día siguiente.** Se congela muy bien.", "**Si no encuentras los tres chiles,** puedes hacerlo solo con anchos."],
 },
 "en": {
  "title": "Mole poblano", "meta": "Serves **6** · ⏱️ 1 h 30 min · Difficulty: hard · Heat: mild",
  "intro": "The sauce from Puebla: mild dried chiles, nuts, sesame, spices, tortilla and chocolate, ground and slowly simmered. With the chiles seeded and deveined, it's barely spicy.",
  "ing": ["3 ancho chiles", "3 mulato chiles", "2 pasilla chiles", "1 tomato", "½ onion", "2 garlic cloves", "¼ cup almonds", "¼ cup peanuts", "3 tablespoons sesame seeds (plus more to serve)", "¼ cup raisins", "1 stale corn tortilla (or 1 slice bread)", "½ teaspoon cinnamon", "2 cloves", "2 oz Mexican table chocolate (or dark chocolate plus a pinch more cinnamon)", "4 cups chicken stock", "1 tablespoon sugar", "4 tablespoons lard or oil", "Salt"],
  "steps": [
   "**Chiles.** Remove stems, seeds and veins. Toast a few seconds per side in a dry pan without burning, then soak 20 minutes in hot water.",
   "**Fry.** In a little lard, fry the almonds, peanuts, sesame, raisins, torn tortilla, cinnamon and cloves separately, just until golden.",
   "**Char.** Char the tomato, onion and garlic in the pan until blistered.",
   "**Blend.** Blend the drained chiles with everything fried and charred and some of the stock into a very smooth paste. Strain if needed.",
   "**Simmer.** Fry the paste in the rest of the lard over medium heat for 10 minutes, stirring. Add the remaining stock, chocolate, sugar and salt and simmer 30–40 minutes until thick and glossy.",
  ],
  "tips": ["**Serve with** poached chicken or turkey, enchiladas or red rice; sprinkle with toasted sesame.", "**Better the next day.** It freezes very well.", "**Can't find all three chiles?** Anchos alone work."],
 },
},
{
 "slug": "pico-de-gallo", "tags_es": MEX_ES + ["sin-alcohol", "tomate", "vegana"], "tags_en": MEX_EN + ["alcohol-free", "tomato", "vegan"],
 "es": {
  "title": "Pico de gallo (salsa mexicana)", "meta": "Para **4 personas** · ⏱️ 10 minutos · Dificultad: fácil · Picor: suave",
  "intro": "Tomate, cebolla y cilantro picados con lima y sal: la salsa fresca mexicana. Con el chile sin semillas, o sin él, casi no pica.",
  "ing": ["4 tomates maduros pero firmes", "½ cebolla blanca", "1 puñado de cilantro", "El zumo de 1 lima", "½ chile jalapeño o serrano sin semillas (opcional)", "Sal"],
  "steps": [
   "**Picar.** Pica el tomate en dados pequeños, la cebolla muy fina, el cilantro y el chile, si lo usas.",
   "**Mezclar.** Mezcla todo en un bol con el zumo de lima y la sal.",
   "**Reposar.** Déjalo 10 minutos para que suelte jugo y se mezclen los sabores.",
  ],
  "tips": ["**Con** tacos, totopos, huevos, pescado o carne asada.", "**Cebolla más suave:** remójala 5 minutos en agua fría y escúrrela.", "**Mejor del día,** recién hecho."],
 },
 "en": {
  "title": "Pico de gallo (fresh Mexican salsa)", "meta": "Serves **4** · ⏱️ 10 minutes · Difficulty: easy · Heat: mild",
  "intro": "Chopped tomato, onion and cilantro with lime and salt: Mexico's fresh salsa. With the chile seeded, or left out, it's barely spicy.",
  "ing": ["4 ripe but firm tomatoes", "½ white onion", "1 handful cilantro", "Juice of 1 lime", "½ jalapeño or serrano chile, seeded (optional)", "Salt"],
  "steps": [
   "**Chop.** Dice the tomato small and finely chop the onion, cilantro and chile, if using.",
   "**Mix.** Combine everything in a bowl with the lime juice and salt.",
   "**Rest.** Let it sit 10 minutes so the juices release and the flavors blend.",
  ],
  "tips": ["**Serve with** tacos, tortilla chips, eggs, fish or grilled meat.", "**Milder onion:** soak it 5 minutes in cold water and drain.", "**Best the same day,** freshly made."],
 },
},
{
 "slug": "pipian", "tags_es": MEX_ES + ["pepitas"], "tags_en": MEX_EN + ["pumpkin-seeds"],
 "es": {
  "title": "Pipián verde", "meta": "Para **4 personas** · ⏱️ 40 minutos · Dificultad: media · Picor: suave",
  "intro": "Pepitas de calabaza tostadas con tomatillo, chile poblano, lechuga y cilantro: un mole verde cremoso y poco picante.",
  "ing": ["150 g de pepitas de calabaza peladas", "5 tomatillos (tomates verdes)", "½ cebolla", "2 dientes de ajo", "1 chile poblano asado, pelado y sin semillas", "2 hojas de lechuga romana", "1 puñado de cilantro", "500 ml de caldo de pollo (o de verduras)", "2 cucharadas de aceite", "Sal"],
  "steps": [
   "**Tostar.** Tuesta las pepitas en una sartén seca a fuego medio-bajo, moviéndolas, hasta que empiecen a saltar. Que no se quemen o amargarán.",
   "**Los tomatillos.** Quítales la cáscara y cuécelos en agua 5 minutos, hasta que cambien de color.",
   "**Triturar.** Tritura las pepitas con los tomatillos, la cebolla, el ajo, el poblano, la lechuga, el cilantro y parte del caldo hasta que quede fino.",
   "**Cocer.** Fríe la salsa en el aceite a fuego medio 5 minutos, removiendo. Añade el resto del caldo y cuece a fuego suave 15 minutos.",
   "**Ajustar.** Sala al final. No dejes que hierva con fuerza: la salsa se corta.",
  ],
  "tips": ["**Con** pollo, cerdo, enchiladas o verduras asadas.", "**Vegano:** usa caldo de verduras.", "**El poblano** es un chile suave; quítale bien las semillas y las venas."],
 },
 "en": {
  "title": "Green pumpkin seed sauce", "meta": "Serves **4** · ⏱️ 40 minutes · Difficulty: medium · Heat: mild",
  "intro": "Toasted pumpkin seeds with tomatillo, poblano chile, lettuce and cilantro: a creamy, mild green mole.",
  "ing": ["1 cup hulled pumpkin seeds (pepitas)", "5 tomatillos", "½ onion", "2 garlic cloves", "1 poblano chile, roasted, peeled and seeded", "2 romaine lettuce leaves", "1 handful cilantro", "2 cups chicken stock (or vegetable stock)", "2 tablespoons oil", "Salt"],
  "steps": [
   "**Toast.** Toast the pepitas in a dry pan over medium-low heat, stirring, until they start to pop. Don't let them burn or they turn bitter.",
   "**Tomatillos.** Husk them and simmer in water for 5 minutes, until they change color.",
   "**Blend.** Blend the pepitas with the tomatillos, onion, garlic, poblano, lettuce, cilantro and some stock until smooth.",
   "**Simmer.** Fry the sauce in the oil over medium heat for 5 minutes, stirring. Add the remaining stock and simmer gently 15 minutes.",
   "**Adjust.** Salt at the end. Don't let it boil hard or the sauce will split.",
  ],
  "tips": ["**Serve with** chicken, pork, enchiladas or roasted vegetables.", "**Vegan:** use vegetable stock.", "**Poblano** is a mild chile; remove all seeds and veins."],
 },
},
{
 "slug": "ranchera", "tags_es": MEX_ES + ["sin-alcohol", "tomate", "vegana"], "tags_en": MEX_EN + ["alcohol-free", "tomato", "vegan"],
 "es": {
  "title": "Salsa ranchera", "meta": "Para **4 personas** · ⏱️ 25 minutos · Dificultad: fácil · Picor: suave",
  "intro": "Tomate, cebolla y ajo asados en el comal, triturados y fritos: la salsa roja de los huevos rancheros, suave si el chile va sin semillas.",
  "ing": ["4 tomates maduros", "½ cebolla blanca", "2 dientes de ajo con piel", "½ chile jalapeño sin semillas (opcional)", "1 pizca de orégano", "1 puñado de cilantro", "2 cucharadas de aceite", "Sal"],
  "steps": [
   "**Asar.** Asa los tomates, la cebolla, los ajos y el chile en un comal o sartén seca, dándoles la vuelta, hasta que estén tostados y blandos, unos 10 minutos. Pela los ajos.",
   "**Triturar.** Tritura todo con el orégano y una pizca de sal, dejándolo con algo de textura.",
   "**Freír.** Calienta el aceite en una sartén, vierte la salsa (salpicará) y cuécela 8–10 minutos a fuego medio hasta que espese y cambie de color.",
   "**Terminar.** Ajusta de sal y añade el cilantro picado.",
  ],
  "tips": ["**Huevos rancheros:** tortillas de maíz fritas, huevos fritos encima y la salsa caliente por encima.", "**Con** frijoles, enchiladas, tacos o arroz.", "**Sin picante:** quita el chile."],
 },
 "en": {
  "title": "Ranchero sauce", "meta": "Serves **4** · ⏱️ 25 minutes · Difficulty: easy · Heat: mild",
  "intro": "Tomato, onion and garlic charred on a griddle, blended and fried: the red sauce for huevos rancheros, mild if the chile is seeded.",
  "ing": ["4 ripe tomatoes", "½ white onion", "2 garlic cloves, unpeeled", "½ jalapeño, seeded (optional)", "1 pinch oregano", "1 handful cilantro", "2 tablespoons oil", "Salt"],
  "steps": [
   "**Char.** Char the tomatoes, onion, garlic and chile on a comal or dry skillet, turning, until blistered and soft, about 10 minutes. Peel the garlic.",
   "**Blend.** Blend everything with the oregano and a pinch of salt, leaving some texture.",
   "**Fry.** Heat the oil in a skillet, pour in the sauce (it will spatter) and cook 8–10 minutes over medium heat until thickened and darker.",
   "**Finish.** Season with salt and add the chopped cilantro.",
  ],
  "tips": ["**Huevos rancheros:** fried corn tortillas, fried eggs on top and the hot sauce over them.", "**Also with** beans, enchiladas, tacos or rice.", "**No heat:** leave out the chile."],
 },
},
{
 "slug": "tomatillo", "tags_es": MEX_ES + ["sin-alcohol", "vegana"], "tags_en": MEX_EN + ["alcohol-free", "vegan"],
 "es": {
  "title": "Salsa verde de tomatillo", "meta": "Para **4 personas** · ⏱️ 15 minutos · Dificultad: fácil · Picor: suave",
  "intro": "Tomatillos cocidos o asados, triturados con cebolla, ajo y cilantro: la salsa verde mexicana, ácida y fresca, suave si el chile va sin semillas.",
  "ing": ["500 g de tomatillos (tomates verdes)", "¼ de cebolla blanca", "1 diente de ajo", "½ chile serrano sin semillas (opcional)", "1 puñado de cilantro", "Sal"],
  "steps": [
   "**Los tomatillos.** Quítales la cáscara y lávalos. Cuécelos en agua 5–7 minutos, hasta que cambien a verde oliva, o ásalos en el comal.",
   "**Triturar.** Tritúralos con la cebolla, el ajo, el chile, el cilantro y la sal, con un poco del agua de cocción si hace falta.",
   "**Probar.** Ajusta de sal. Si queda muy ácida, una pizca de azúcar.",
  ],
  "tips": ["**Con** tacos, chilaquiles verdes, enchiladas, quesadillas o huevos.", "**Más cremosa:** tritúrala con medio aguacate.", "**Aguanta** 4–5 días en la nevera."],
 },
 "en": {
  "title": "Green tomatillo salsa", "meta": "Serves **4** · ⏱️ 15 minutes · Difficulty: easy · Heat: mild",
  "intro": "Boiled or charred tomatillos blended with onion, garlic and cilantro: Mexico's tangy, fresh salsa verde, mild if the chile is seeded.",
  "ing": ["1 lb tomatillos", "¼ white onion", "1 garlic clove", "½ serrano chile, seeded (optional)", "1 handful cilantro", "Salt"],
  "steps": [
   "**Tomatillos.** Husk and rinse them. Simmer in water 5–7 minutes, until olive green, or char them on a comal.",
   "**Blend.** Blend with the onion, garlic, chile, cilantro and salt, adding a little cooking water if needed.",
   "**Taste.** Adjust the salt. If very tart, add a pinch of sugar.",
  ],
  "tips": ["**Serve with** tacos, chilaquiles verdes, enchiladas, quesadillas or eggs.", "**Creamier:** blend in half an avocado.", "**Keeps** 4–5 days in the fridge."],
 },
},
]
