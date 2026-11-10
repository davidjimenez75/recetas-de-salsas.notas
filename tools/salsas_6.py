"""Sauce data, part 6: vegan, alcohol-free sauces. All are pepper-free except piquillo."""

VEG_ES = ["sin-alcohol", "vegana"]
VEG_EN = ["alcohol-free", "vegan"]

SALSAS = [
{
 "slug": "almendras", "tags_es": VEG_ES + ["frutos-secos"], "tags_en": VEG_EN + ["nuts"],
 "es": {
  "title": "Salsa de almendras", "meta": "Para **4 personas** · ⏱️ 25 minutos · Dificultad: fácil",
  "intro": "Almendras, ajo y pan fritos, majados y cocidos en caldo de verduras con azafrán: una salsa vegana, sin alcohol y sin pimiento. La foto muestra las almendras, no el plato.",
  "ing": ["80 g de almendras crudas peladas", "2 dientes de ajo", "1 rebanada de pan del día anterior", "400 ml de caldo de verduras", "Unas hebras de azafrán", "1 cucharada de perejil picado", "4 cucharadas de aceite de oliva", "Sal"],
  "steps": [
   "**Freír.** En el aceite, a fuego medio, fríe por separado las almendras, los ajos pelados y el pan, hasta que estén dorados. Retíralos y guarda el aceite.",
   "**Majar.** Machaca en el mortero (o tritura) las almendras, los ajos, el pan, el azafrán y el perejil con un poco de caldo, hasta tener una pasta.",
   "**Cocer.** En la misma cazuela con su aceite, añade la pasta y el resto del caldo. Cuece a fuego suave 10 minutos, removiendo, hasta que espese.",
   "**Ajustar.** Prueba de sal. Si la quieres más fina, tritúrala otra vez y cuélala.",
  ],
  "tips": ["**Con** albóndigas veganas, garbanzos, patatas, coliflor o setas.", "**Más ligera:** añade más caldo; más espesa, un poco más de pan.", "**Sin gluten:** sustituye el pan por más almendras."],
 },
 "en": {
  "title": "Spanish almond sauce", "meta": "Serves **4** · ⏱️ 25 minutes · Difficulty: easy",
  "intro": "Fried almonds, garlic and bread, pounded and simmered in vegetable stock with saffron: a vegan sauce with no alcohol and no peppers. The photo shows the almonds, not the dish.",
  "ing": ["½ cup blanched raw almonds", "2 garlic cloves", "1 slice day-old bread", "1⅔ cups vegetable stock", "A few saffron threads", "1 tablespoon chopped parsley", "4 tablespoons olive oil", "Salt"],
  "steps": [
   "**Fry.** In the oil over medium heat, fry the almonds, peeled garlic and bread separately until golden. Remove them and keep the oil.",
   "**Pound.** Pound in a mortar (or blend) the almonds, garlic, bread, saffron and parsley with a little stock into a paste.",
   "**Simmer.** In the same pot with its oil, add the paste and the rest of the stock. Simmer 10 minutes, stirring, until thickened.",
   "**Adjust.** Season with salt. For a smoother sauce, blend again and strain.",
  ],
  "tips": ["**Serve with** vegan meatballs, chickpeas, potatoes, cauliflower or mushrooms.", "**Thinner:** add more stock; thicker, a little more bread.", "**Gluten-free:** replace the bread with more almonds."],
 },
},
{
 "slug": "lactonesa", "tags_es": VEG_ES + ["emulsion"], "tags_en": VEG_EN + ["emulsion"],
 "es": {
  "title": "Lactonesa (mahonesa vegana)", "meta": "Para **unos 300 ml** · ⏱️ 5 minutos · Dificultad: fácil",
  "intro": "Mahonesa sin huevo, ligada con bebida de soja: vegana, sin alcohol y sin pimiento.",
  "ing": ["100 ml de bebida de soja sin azúcar, bien fría", "200 ml de aceite de girasol (o mitad de oliva suave)", "1 cucharada de zumo de limón o de vinagre de manzana", "1 diente de ajo (opcional, para un alioli vegano)", "Sal"],
  "steps": [
   "**Al vaso.** Pon la bebida de soja, el limón, la sal y el ajo, si lo usas, en el vaso de la batidora.",
   "**Emulsionar.** Con la batidora en marcha en el fondo, añade el aceite en un hilo fino.",
   "**Subir.** Cuando empiece a espesar, sube y baja la batidora hasta que todo el aceite esté integrado.",
   "**Probar.** Ajusta de sal y limón. Si queda líquida, añade un poco más de aceite batiendo.",
  ],
  "tips": ["**Tiene que ser de soja:** las bebidas de avena o de almendra emulsionan peor.", "**Aguanta** 4–5 días en la nevera.", "**Base** para una ensaladilla vegana o una salsa rosa vegana."],
 },
 "en": {
  "title": "Vegan soy milk mayonnaise", "meta": "Makes **about 1¼ cups** · ⏱️ 5 minutes · Difficulty: easy",
  "intro": "Egg-free mayonnaise emulsified with soy milk: vegan, with no alcohol and no peppers.",
  "ing": ["Scant ½ cup unsweetened soy milk, well chilled", "¾ cup plus 1 tablespoon sunflower oil (or half mild olive oil)", "1 tablespoon lemon juice or apple cider vinegar", "1 garlic clove (optional, for a vegan aioli)", "Salt"],
  "steps": [
   "**Into the cup.** Put the soy milk, lemon juice, salt and garlic, if using, in the immersion blender cup.",
   "**Emulsify.** With the blender running at the bottom, pour in the oil in a thin stream.",
   "**Lift.** Once it starts to thicken, move the blender up and down until all the oil is incorporated.",
   "**Taste.** Adjust salt and lemon. If it's runny, blend in a little more oil.",
  ],
  "tips": ["**It must be soy milk:** oat or almond milk emulsify poorly.", "**Keeps** 4–5 days in the fridge.", "**A base** for vegan Spanish potato salad or vegan cocktail sauce."],
 },
},
{
 "slug": "membrillo", "tags_es": VEG_ES + ["cataluna", "emulsion"], "tags_en": VEG_EN + ["catalonia", "emulsion"],
 "es": {
  "title": "Alioli de membrillo (allioli de codony)", "meta": "Para **6 personas** · ⏱️ 45 minutos · Dificultad: media",
  "intro": "Membrillo asado, ajo y aceite de oliva ligados en el mortero, sin huevo: una salsa catalana de otoño, vegana, sin alcohol y sin pimiento.",
  "ing": ["2 membrillos maduros", "2–3 dientes de ajo", "150 ml de aceite de oliva suave", "Unas gotas de zumo de limón", "Sal"],
  "steps": [
   "**El membrillo.** Ásalo entero en el horno a 180 °C unos 40 minutos (o cuécelo en agua 25 minutos), hasta que esté muy tierno. Pélalo y quítale el corazón.",
   "**Machacar.** En el mortero, machaca los ajos con la sal hasta hacer una pasta.",
   "**El puré.** Añade la pulpa de membrillo, todavía templada, y machácala con el ajo hasta que quede fina.",
   "**Ligar.** Añade el aceite poco a poco, removiendo siempre en el mismo sentido, hasta tener una salsa espesa. Termina con unas gotas de limón.",
  ],
  "tips": ["**Con** verduras y setas a la brasa, patatas asadas o tofu a la plancha.", "**Con manzana** también se hace (allioli de poma), igual que con membrillo.", "**Con batidora** sale más rápido y más fino."],
 },
 "en": {
  "title": "Quince and garlic aioli", "meta": "Serves **6** · ⏱️ 45 minutes · Difficulty: medium",
  "intro": "Roasted quince, garlic and olive oil emulsified in a mortar, with no egg: a Catalan autumn sauce that is vegan, with no alcohol and no peppers.",
  "ing": ["2 ripe quinces", "2–3 garlic cloves", "⅔ cup mild olive oil", "A few drops lemon juice", "Salt"],
  "steps": [
   "**Quince.** Roast it whole at 350 °F for about 40 minutes (or simmer it in water 25 minutes) until very tender. Peel and core it.",
   "**Pound.** In a mortar, crush the garlic with the salt into a paste.",
   "**Purée.** Add the still-warm quince flesh and pound it with the garlic until smooth.",
   "**Emulsify.** Add the oil gradually, always stirring in the same direction, until thick. Finish with a few drops of lemon.",
  ],
  "tips": ["**Serve with** grilled vegetables and mushrooms, roast potatoes or seared tofu.", "**Apple works too** (allioli de poma), made the same way.", "**A blender** is faster and smoother."],
 },
},
{
 "slug": "piquillo", "tags_es": VEG_ES + ["navarra", "pimiento"], "tags_en": VEG_EN + ["navarre", "pepper"],
 "es": {
  "title": "Salsa de piquillos", "meta": "Para **4 personas** · ⏱️ 20 minutos · Dificultad: fácil",
  "intro": "Pimientos del piquillo asados, cebolla pochada y bebida de avena: una salsa cremosa, vegana y sin alcohol. La foto muestra el pimiento del piquillo, no la salsa.",
  "ing": ["1 lata de pimientos del piquillo asados (unos 250 g)", "1 cebolla", "1 diente de ajo", "150 ml de bebida de avena sin azúcar (o caldo de verduras)", "1 pizca de azúcar", "3 cucharadas de aceite de oliva", "Sal"],
  "steps": [
   "**Pochar.** Pocha la cebolla y el ajo picados en el aceite a fuego suave unos 10 minutos.",
   "**Los piquillos.** Añade los pimientos escurridos (guarda su jugo) y cocina 5 minutos.",
   "**Triturar.** Añade la bebida de avena, el azúcar y la sal y tritura hasta que quede muy fina. Si está espesa, aclárala con el jugo de los pimientos.",
   "**Calentar.** Dale un hervor de 2 minutos y ajusta de sal.",
  ],
  "tips": ["**Con** pasta, arroz, tofu, garbanzos o verduras asadas.", "**Fría** sirve como crema para untar o mojar.", "**Si los quieres rellenos,** rellena otros piquillos con verduras salteadas y nápalos con la salsa."],
 },
 "en": {
  "title": "Piquillo pepper cream sauce", "meta": "Serves **4** · ⏱️ 20 minutes · Difficulty: easy",
  "intro": "Roasted piquillo peppers, slowly cooked onion and oat milk: a creamy sauce that is vegan and alcohol-free. The photo shows the piquillo pepper, not the sauce.",
  "ing": ["1 jar or can roasted piquillo peppers (about 9 oz)", "1 onion", "1 garlic clove", "⅔ cup unsweetened oat milk (or vegetable stock)", "1 pinch sugar", "3 tablespoons olive oil", "Salt"],
  "steps": [
   "**Soften.** Gently cook the chopped onion and garlic in the oil for about 10 minutes.",
   "**Peppers.** Add the drained peppers (save their juice) and cook 5 minutes.",
   "**Blend.** Add the oat milk, sugar and salt and blend until very smooth. Thin with the pepper juice if needed.",
   "**Heat.** Bring to a boil for 2 minutes and adjust the salt.",
  ],
  "tips": ["**Serve with** pasta, rice, tofu, chickpeas or roasted vegetables.", "**Cold,** it works as a spread or dip.", "**For stuffed peppers,** fill more piquillos with sautéed vegetables and coat them with the sauce."],
 },
},
{
 "slug": "setas", "tags_es": VEG_ES + ["setas"], "tags_en": VEG_EN + ["mushrooms"],
 "es": {
  "title": "Salsa de setas vegana", "meta": "Para **4 personas** · ⏱️ 25 minutos · Dificultad: fácil",
  "intro": "Setas salteadas con cebolla, ajo y tomillo, ligadas con bebida de avena: sin nata, sin vino y sin pimiento. En la foto, la salsa va sobre unos canelones.",
  "ing": ["400 g de setas variadas o champiñones", "1 cebolla", "2 dientes de ajo", "1 cucharada de harina", "300 ml de bebida de avena sin azúcar", "100 ml de caldo de verduras", "1 ramita de tomillo", "1 pizca de nuez moscada", "1 cucharada de perejil picado", "4 cucharadas de aceite de oliva", "Sal"],
  "steps": [
   "**Pochar.** Pocha la cebolla y el ajo picados en el aceite a fuego suave unos 8 minutos.",
   "**Las setas.** Sube el fuego, añade las setas troceadas y el tomillo y saltéalas hasta que suelten el agua y se doren.",
   "**La harina.** Añade la harina y remueve 1 minuto.",
   "**Ligar.** Añade el caldo y la bebida de avena poco a poco, removiendo, y cuece 5–8 minutos a fuego suave hasta que espese.",
   "**Terminar.** Añade la nuez moscada, el perejil y la sal. Tritura la mitad si la quieres más cremosa.",
  ],
  "tips": ["**Con** pasta, arroz, patatas, tofu, seitán o canelones de verduras.", "**Más sabor:** añade un puñado de setas secas remojadas y su agua en lugar del caldo.", "**Sin gluten:** espesa con 1 cucharadita de maicena en vez de harina."],
 },
 "en": {
  "title": "Vegan mushroom cream sauce", "meta": "Serves **4** · ⏱️ 25 minutes · Difficulty: easy",
  "intro": "Mushrooms sautéed with onion, garlic and thyme, thickened with oat milk: no cream, no wine and no peppers. The photo shows the sauce over cannelloni.",
  "ing": ["14 oz mixed wild mushrooms or button mushrooms", "1 onion", "2 garlic cloves", "1 tablespoon all-purpose flour", "1¼ cups unsweetened oat milk", "Scant ½ cup vegetable stock", "1 thyme sprig", "1 pinch nutmeg", "1 tablespoon chopped parsley", "4 tablespoons olive oil", "Salt"],
  "steps": [
   "**Soften.** Gently cook the chopped onion and garlic in the oil for about 8 minutes.",
   "**Mushrooms.** Raise the heat, add the chopped mushrooms and thyme and sauté until their liquid evaporates and they brown.",
   "**Flour.** Stir in the flour for 1 minute.",
   "**Thicken.** Gradually stir in the stock and oat milk and simmer 5–8 minutes until thickened.",
   "**Finish.** Add the nutmeg, parsley and salt. Blend half of it for a creamier sauce.",
  ],
  "tips": ["**Serve with** pasta, rice, potatoes, tofu, seitan or vegetable cannelloni.", "**More flavor:** add a handful of soaked dried mushrooms and use their water instead of the stock.", "**Gluten-free:** thicken with 1 teaspoon cornstarch instead of flour."],
 },
},
]
