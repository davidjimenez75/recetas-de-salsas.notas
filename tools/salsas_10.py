"""Sauce data, part 10: Italian sauces."""

IT_ES = ["italia", "pasta"]
IT_EN = ["italy", "pasta"]

SALSAS = [
{
 "slug": "amatriciana", "tags_es": IT_ES + ["tomate"], "tags_en": IT_EN + ["tomato"],
 "es": {
  "title": "Salsa amatriciana", "meta": "Para **4 personas** · ⏱️ 30 minutos · Dificultad: fácil",
  "intro": "Guanciale crujiente, tomate y pecorino romano: la salsa de Amatrice para los bucatini, con un toque opcional de guindilla.",
  "ing": ["150 g de guanciale (o panceta curada)", "400 g de tomate pelado en lata, triturado a mano", "50 ml de vino blanco (opcional)", "1 guindilla seca pequeña (opcional)", "60 g de pecorino romano rallado", "Sal", "400 g de bucatini o espaguetis"],
  "steps": [
   "**El guanciale.** Córtalo en tiras y dóralo en una sartén sin aceite, a fuego medio, hasta que suelte la grasa y esté crujiente por fuera. Retira la mitad si quieres que quede crujiente.",
   "**El vino.** Si lo usas, añádelo con la guindilla y deja que se evapore.",
   "**El tomate.** Añade el tomate y una pizca de sal y cuece 15 minutos a fuego medio, hasta que espese.",
   "**La pasta.** Cuece la pasta al dente, escúrrela y saltéala en la salsa 1 minuto con un poco de su agua.",
   "**El queso.** Fuera del fuego, añade el pecorino, mezcla y sirve con más queso por encima.",
  ],
  "tips": ["**Sin ajo ni cebolla:** la receta de Amatrice no los lleva.", "**Guanciale** es papada de cerdo curada; la panceta es la mejor alternativa.", "**Sala poco:** el guanciale y el pecorino ya son salados."],
 },
 "en": {
  "title": "Amatriciana sauce", "meta": "Serves **4** · ⏱️ 30 minutes · Difficulty: easy",
  "intro": "Crisp guanciale, tomato and pecorino romano: the sauce from Amatrice for bucatini, with an optional pinch of chile.",
  "ing": ["5 oz guanciale (or pancetta)", "1 can (14 oz) whole peeled tomatoes, crushed by hand", "3½ tablespoons dry white wine (optional)", "1 small dried chile (optional)", "⅔ cup grated pecorino romano", "Salt", "14 oz bucatini or spaghetti"],
  "steps": [
   "**Guanciale.** Cut it into strips and render it in a dry skillet over medium heat until the fat runs and the edges are crisp. Remove half if you want it to stay crunchy.",
   "**Wine.** If using, add it with the chile and let it cook off.",
   "**Tomato.** Add the tomatoes and a pinch of salt and simmer 15 minutes, until thick.",
   "**Pasta.** Cook the pasta al dente, drain and toss it in the sauce for 1 minute with a splash of pasta water.",
   "**Cheese.** Off the heat, stir in the pecorino and serve with more on top.",
  ],
  "tips": ["**No garlic or onion:** the Amatrice recipe has neither.", "**Guanciale** is cured pork jowl; pancetta is the best substitute.", "**Go easy on salt:** guanciale and pecorino are already salty."],
 },
},
{
 "slug": "carbonara", "tags_es": IT_ES + ["huevo"], "tags_en": IT_EN + ["egg"],
 "es": {
  "title": "Salsa carbonara", "meta": "Para **4 personas** · ⏱️ 20 minutos · Dificultad: media",
  "intro": "Yemas de huevo, pecorino, pimienta negra y guanciale, ligados con el calor de la pasta: la carbonara romana, sin nata.",
  "ing": ["150 g de guanciale (o panceta curada)", "4 yemas y 1 huevo entero", "80 g de pecorino romano rallado (o mitad parmesano)", "Pimienta negra recién molida", "400 g de espaguetis o rigatoni"],
  "steps": [
   "**El guanciale.** Córtalo en tiras y dóralo en una sartén sin aceite hasta que esté crujiente. Apaga el fuego y deja la grasa en la sartén.",
   "**La crema.** Bate las yemas y el huevo con el queso y mucha pimienta hasta tener una crema espesa.",
   "**La pasta.** Cuécela al dente en agua con poca sal. Guarda un vaso del agua de cocción.",
   "**Ligar.** Echa la pasta escurrida en la sartén con el guanciale, fuera del fuego, y espera 30 segundos. Añade la crema de huevo y mezcla rápido, con un chorrito del agua de cocción, hasta que quede cremosa y brillante.",
   "**Servir.** Sirve enseguida con más queso y pimienta.",
  ],
  "tips": ["**Sin nata:** la cremosidad sale del huevo, el queso y el agua de la pasta.", "**Si cuaja,** el fuego estaba encendido o la sartén muy caliente: hazlo siempre fuera del fuego.", "**Seguridad:** el huevo queda poco cocinado; usa huevos muy frescos o pasteurizados."],
 },
 "en": {
  "title": "Carbonara sauce", "meta": "Serves **4** · ⏱️ 20 minutes · Difficulty: medium",
  "intro": "Egg yolks, pecorino, black pepper and guanciale, bound by the heat of the pasta: Roman carbonara, with no cream.",
  "ing": ["5 oz guanciale (or pancetta)", "4 egg yolks plus 1 whole egg", "¾ cup grated pecorino romano (or half parmesan)", "Freshly ground black pepper", "14 oz spaghetti or rigatoni"],
  "steps": [
   "**Guanciale.** Cut it into strips and crisp it in a dry skillet. Turn off the heat and leave the fat in the pan.",
   "**Cream.** Whisk the yolks and egg with the cheese and plenty of pepper into a thick cream.",
   "**Pasta.** Cook it al dente in lightly salted water. Save a cup of the cooking water.",
   "**Bind.** Add the drained pasta to the skillet with the guanciale, off the heat, and wait 30 seconds. Add the egg mixture and toss quickly with a splash of pasta water until creamy and glossy.",
   "**Serve.** Serve right away with more cheese and pepper.",
  ],
  "tips": ["**No cream:** the creaminess comes from egg, cheese and pasta water.", "**If it scrambles,** the heat was on or the pan too hot: always do it off the heat.", "**Food safety:** the egg is lightly cooked; use very fresh or pasteurized eggs."],
 },
},
{
 "slug": "pesto", "tags_es": IT_ES + ["albahaca", "frutos-secos", "sin-alcohol"], "tags_en": IT_EN + ["alcohol-free", "basil", "nuts"],
 "es": {
  "title": "Pesto genovés (pesto alla genovese)", "meta": "Para **4 personas** · ⏱️ 15 minutos · Dificultad: fácil",
  "intro": "Albahaca, piñones, ajo, parmesano, pecorino y aceite de oliva majados en el mortero: la salsa cruda de Génova.",
  "ing": ["50 g de hojas de albahaca fresca", "30 g de piñones", "1 diente de ajo", "40 g de parmesano rallado", "20 g de pecorino rallado", "100 ml de aceite de oliva virgen extra suave", "1 pizca de sal gruesa"],
  "steps": [
   "**El ajo.** En el mortero, machaca el ajo con la sal hasta hacer una pasta.",
   "**Los piñones.** Añade los piñones y machácalos.",
   "**La albahaca.** Añade las hojas, limpias y bien secas, poco a poco, y machácalas con un movimiento circular, sin golpear, hasta que suelten un líquido verde.",
   "**El queso y el aceite.** Añade los quesos y, al final, el aceite en un hilo, removiendo con la mano del mortero.",
  ],
  "tips": ["**Con batidora:** usa el vaso frío y pulsos cortos, para que la albahaca no se caliente y se oscurezca.", "**Con** trofie, trenette, patata y judías verdes, como en Liguria, o en sopa minestrone.", "**Vegano:** cambia los quesos por 2 cucharadas de levadura nutricional y un poco más de piñones."],
 },
 "en": {
  "title": "Genoese basil pesto", "meta": "Serves **4** · ⏱️ 15 minutes · Difficulty: easy",
  "intro": "Basil, pine nuts, garlic, parmesan, pecorino and olive oil pounded in a mortar: the raw sauce from Genoa.",
  "ing": ["2 oz fresh basil leaves (about 2 packed cups)", "¼ cup pine nuts", "1 garlic clove", "½ cup grated parmesan", "¼ cup grated pecorino", "Scant ½ cup mild extra virgin olive oil", "1 pinch coarse salt"],
  "steps": [
   "**Garlic.** In a mortar, crush the garlic with the salt into a paste.",
   "**Pine nuts.** Add the pine nuts and crush them.",
   "**Basil.** Add the clean, very dry leaves gradually and grind them with a circular motion, not pounding, until they release a green liquid.",
   "**Cheese and oil.** Add the cheeses and, last, the oil in a thin stream, stirring with the pestle.",
  ],
  "tips": ["**Food processor:** use a chilled bowl and short pulses so the basil doesn't warm up and darken.", "**Serve with** trofie or trenette with potato and green beans, as in Liguria, or in minestrone.", "**Vegan:** replace the cheeses with 2 tablespoons nutritional yeast and a few more pine nuts."],
 },
},
{
 "slug": "pomodoro", "tags_es": IT_ES + ["albahaca", "sin-alcohol", "tomate", "vegana"], "tags_en": IT_EN + ["alcohol-free", "basil", "tomato", "vegan"],
 "es": {
  "title": "Salsa al pomodoro", "meta": "Para **4 personas** · ⏱️ 30 minutos · Dificultad: fácil",
  "intro": "Tomate, ajo, aceite de oliva y albahaca: la salsa italiana de tomate más sencilla, vegana y sin alcohol.",
  "ing": ["800 g de tomate pelado en lata (mejor San Marzano), o tomates maduros pelados", "2 dientes de ajo", "4 cucharadas de aceite de oliva virgen extra", "1 ramita de albahaca fresca", "Sal"],
  "steps": [
   "**El ajo.** Calienta el aceite a fuego suave con los ajos pelados y aplastados hasta que se doren un poco. Retíralos si quieres un sabor suave.",
   "**El tomate.** Añade el tomate triturado a mano y una pizca de sal.",
   "**Cocer.** Cuece a fuego medio-suave 20–25 minutos, removiendo de vez en cuando, hasta que espese y el aceite empiece a separarse.",
   "**La albahaca.** Al final, añade las hojas de albahaca rotas con la mano.",
  ],
  "tips": ["**Con** espaguetis, en pizza, lasaña, berenjenas a la parmesana o albóndigas.", "**Más dulce:** añade media cebolla entera durante la cocción y retírala al final.", "**Termina la pasta en la salsa** con un poco de agua de cocción."],
 },
 "en": {
  "title": "Italian tomato and basil sauce", "meta": "Serves **4** · ⏱️ 30 minutes · Difficulty: easy",
  "intro": "Tomato, garlic, olive oil and basil: the simplest Italian tomato sauce, vegan and alcohol-free.",
  "ing": ["1 can (28 oz) whole peeled tomatoes (San Marzano if possible), or ripe peeled tomatoes", "2 garlic cloves", "4 tablespoons extra virgin olive oil", "1 sprig fresh basil", "Salt"],
  "steps": [
   "**Garlic.** Warm the oil over low heat with the peeled, crushed garlic until lightly golden. Remove it for a milder flavor.",
   "**Tomato.** Add the hand-crushed tomatoes and a pinch of salt.",
   "**Simmer.** Simmer over medium-low heat 20–25 minutes, stirring now and then, until thick and the oil starts to separate.",
   "**Basil.** At the end, add the basil leaves torn by hand.",
  ],
  "tips": ["**Use with** spaghetti, on pizza, in lasagna, eggplant parmigiana or meatballs.", "**Sweeter:** add half an onion during cooking and remove it at the end.", "**Finish the pasta in the sauce** with a splash of cooking water."],
 },
},
{
 "slug": "puttanesca", "tags_es": IT_ES + ["tomate"], "tags_en": IT_EN + ["tomato"],
 "es": {
  "title": "Salsa puttanesca", "meta": "Para **4 personas** · ⏱️ 25 minutos · Dificultad: fácil",
  "intro": "Tomate, ajo, anchoas, aceitunas negras y alcaparras: la salsa napolitana de despensa, intensa y salada.",
  "ing": ["400 g de tomate pelado en lata", "2 dientes de ajo", "4 filetes de anchoa en aceite", "80 g de aceitunas negras (mejor de Gaeta), sin hueso", "1 cucharada de alcaparras, desaladas", "1 guindilla seca pequeña (opcional)", "1 cucharada de perejil picado", "4 cucharadas de aceite de oliva", "400 g de espaguetis"],
  "steps": [
   "**La base.** Calienta el aceite a fuego suave con el ajo laminado, la guindilla y las anchoas, aplastándolas hasta que se deshagan.",
   "**El tomate.** Añade el tomate triturado a mano y cuece 10 minutos.",
   "**El resto.** Añade las aceitunas en trozos y las alcaparras y cuece 5 minutos más.",
   "**La pasta.** Saltea los espaguetis al dente en la salsa con un poco de su agua y termina con el perejil.",
  ],
  "tips": ["**No hace falta sal:** las anchoas, las aceitunas y las alcaparras ya salan la salsa.", "**Sin queso:** es tradicional servirla sin parmesano.", "**Sin anchoas** se vuelve vegana, aunque pierde parte de su sabor."],
 },
 "en": {
  "title": "Puttanesca sauce", "meta": "Serves **4** · ⏱️ 25 minutes · Difficulty: easy",
  "intro": "Tomato, garlic, anchovies, black olives and capers: the Neapolitan pantry sauce, bold and briny.",
  "ing": ["1 can (14 oz) whole peeled tomatoes", "2 garlic cloves", "4 anchovy fillets in oil", "½ cup pitted black olives (Gaeta if possible)", "1 tablespoon capers, rinsed", "1 small dried chile (optional)", "1 tablespoon chopped parsley", "4 tablespoons olive oil", "14 oz spaghetti"],
  "steps": [
   "**Base.** Warm the oil over low heat with the sliced garlic, chile and anchovies, mashing them until they melt.",
   "**Tomato.** Add the hand-crushed tomatoes and simmer 10 minutes.",
   "**The rest.** Add the chopped olives and capers and simmer 5 more minutes.",
   "**Pasta.** Toss the al dente spaghetti in the sauce with a splash of pasta water and finish with parsley.",
  ],
  "tips": ["**No salt needed:** anchovies, olives and capers season it.", "**No cheese:** it's traditionally served without parmesan.", "**Without anchovies** it becomes vegan, though it loses some depth."],
 },
},
{
 "slug": "ragu", "tags_es": IT_ES + ["carne", "tomate"], "tags_en": IT_EN + ["meat", "tomato"],
 "es": {
  "title": "Ragú a la boloñesa (ragù alla bolognese)", "meta": "Para **6 personas** · ⏱️ 3 horas · Dificultad: media",
  "intro": "Carne picada guisada muy despacio con sofrito, vino, tomate y leche: el ragú de Bolonia, más carne que tomate.",
  "ing": ["300 g de carne picada de ternera", "150 g de panceta picada (o carne de cerdo)", "1 cebolla", "1 zanahoria", "1 rama de apio", "150 ml de vino blanco seco (o tinto)", "2 cucharadas de tomate concentrado", "200 g de tomate triturado", "200 ml de leche entera", "300 ml de caldo de carne", "3 cucharadas de aceite de oliva", "20 g de mantequilla", "Sal y pimienta"],
  "steps": [
   "**El sofrito.** Pica muy fino la cebolla, la zanahoria y el apio y póchalos en el aceite y la mantequilla a fuego suave 10 minutos.",
   "**La carne.** Añade la panceta y la carne y dórala a fuego medio, deshaciéndola, hasta que pierda el agua y empiece a tostarse.",
   "**El vino.** Moja con el vino y deja que se evapore.",
   "**El tomate.** Añade el concentrado disuelto en un poco de caldo, el tomate y sal.",
   "**Guisar.** Cuece tapado a fuego muy suave 2–3 horas, añadiendo caldo cuando haga falta. Añade la leche en la última media hora.",
  ],
  "tips": ["**Con** tagliatelle frescas o en lasaña; en Bolonia no se sirve con espaguetis.", "**Mejor de un día para otro.** Se congela muy bien.", "**La leche** suaviza la acidez del tomate y hace la carne más tierna."],
 },
 "en": {
  "title": "Bolognese meat sauce", "meta": "Serves **6** · ⏱️ 3 hours · Difficulty: medium",
  "intro": "Ground meat slowly braised with soffritto, wine, tomato and milk: the ragù of Bologna, more meat than tomato.",
  "ing": ["10 oz ground beef", "5 oz pancetta, finely chopped (or ground pork)", "1 onion", "1 carrot", "1 celery stalk", "⅔ cup dry white wine (or red)", "2 tablespoons tomato paste", "¾ cup crushed tomatoes", "¾ cup plus 1 tablespoon whole milk", "1¼ cups beef stock", "3 tablespoons olive oil", "1½ tablespoons butter", "Salt and pepper"],
  "steps": [
   "**Soffritto.** Finely chop the onion, carrot and celery and cook them in the oil and butter over low heat for 10 minutes.",
   "**Meat.** Add the pancetta and beef and brown over medium heat, breaking it up, until the liquid evaporates and it starts to color.",
   "**Wine.** Pour in the wine and let it cook off.",
   "**Tomato.** Add the tomato paste dissolved in a little stock, the crushed tomatoes and salt.",
   "**Braise.** Simmer, covered, over very low heat for 2–3 hours, adding stock as needed. Add the milk in the last half hour.",
  ],
  "tips": ["**Serve with** fresh tagliatelle or in lasagna; in Bologna it isn't served with spaghetti.", "**Better the next day.** It freezes very well.", "**The milk** softens the tomato's acidity and makes the meat more tender."],
 },
},
]
