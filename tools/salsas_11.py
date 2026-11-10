"""Sauce data, part 11: French sauces."""

FR_ES = ["clasica", "francia"]
FR_EN = ["classic", "france"]

SALSAS = [
{
 "slug": "bearnaise", "tags_es": FR_ES + ["emulsion", "estragon"], "tags_en": FR_EN + ["emulsion", "tarragon"],
 "es": {
  "title": "Salsa bearnesa (sauce béarnaise)", "meta": "Para **4 personas** · ⏱️ 30 minutos · Dificultad: difícil",
  "intro": "Yemas emulsionadas con mantequilla sobre una reducción de vinagre, chalota y estragón: la salsa del entrecot y las patatas fritas.",
  "ing": ["3 yemas de huevo", "200 g de mantequilla", "2 chalotas picadas muy finas", "4 cucharadas de vinagre de vino blanco (o de estragón)", "2 cucharadas de vino blanco seco (opcional)", "2 cucharadas de estragón fresco picado (más un poco para el final)", "Pimienta blanca machacada", "Sal"],
  "steps": [
   "**La reducción.** Cuece la chalota, el vinagre, el vino, la mitad del estragón y la pimienta a fuego suave hasta que quede 1 cucharada de líquido. Deja templar.",
   "**La mantequilla.** Fúndela y déjala templar, retirando la espuma de arriba.",
   "**Las yemas.** Pon la reducción y las yemas con 1 cucharada de agua en un bol al baño maría, sin que el agua hierva. Bate hasta que espese y la varilla deje marcas, unos 3–4 minutos.",
   "**Montar.** Fuera del fuego, añade la mantequilla templada en un hilo muy fino, batiendo sin parar, hasta que quede espesa y brillante.",
   "**Terminar.** Cuela si quieres, añade el resto del estragón y sal. Sírvela templada.",
  ],
  "tips": ["**Con** entrecot, solomillo, pescado a la plancha, huevos o espárragos.", "**Si se corta:** bate 1 cucharada de agua caliente en otro bol y añade la salsa cortada poco a poco.", "**Sin alcohol:** quita el vino y usa solo vinagre."],
 },
 "en": {
  "title": "Béarnaise sauce", "meta": "Serves **4** · ⏱️ 30 minutes · Difficulty: hard",
  "intro": "Egg yolks emulsified with butter over a reduction of vinegar, shallot and tarragon: the sauce for steak frites.",
  "ing": ["3 egg yolks", "14 tablespoons (1¾ sticks) butter", "2 shallots, very finely chopped", "4 tablespoons white wine (or tarragon) vinegar", "2 tablespoons dry white wine (optional)", "2 tablespoons chopped fresh tarragon (plus a little to finish)", "Crushed white pepper", "Salt"],
  "steps": [
   "**Reduction.** Simmer the shallot, vinegar, wine, half the tarragon and the pepper until about 1 tablespoon of liquid remains. Let cool slightly.",
   "**Butter.** Melt it and let it cool a little, skimming off the foam.",
   "**Yolks.** Put the reduction and yolks with 1 tablespoon water in a bowl over barely simmering water. Whisk until thick and the whisk leaves trails, 3–4 minutes.",
   "**Mount.** Off the heat, whisk in the warm butter in a very thin stream until thick and glossy.",
   "**Finish.** Strain if you like, add the rest of the tarragon and salt. Serve warm.",
  ],
  "tips": ["**Serve with** steak, tenderloin, grilled fish, eggs or asparagus.", "**If it breaks:** whisk 1 tablespoon hot water in a clean bowl and slowly whisk in the broken sauce.", "**Alcohol-free:** skip the wine and use only vinegar."],
 },
},
{
 "slug": "bechamel", "tags_es": FR_ES + ["leche", "sin-alcohol"], "tags_en": FR_EN + ["alcohol-free", "milk"],
 "es": {
  "title": "Bechamel (sauce béchamel)", "meta": "Para **unos 500 ml** · ⏱️ 15 minutos · Dificultad: fácil",
  "intro": "Mantequilla, harina y leche con nuez moscada: la salsa blanca de las lasañas, los canelones y las croquetas, una de las salsas madre francesas.",
  "ing": ["40 g de mantequilla", "40 g de harina", "500 ml de leche entera", "1 pizca de nuez moscada", "Sal"],
  "steps": [
   "**El roux.** Funde la mantequilla a fuego medio-suave, añade la harina y cocínala 2 minutos removiendo, sin que tome color.",
   "**La leche.** Añade la leche caliente poco a poco, batiendo con varillas para que no queden grumos.",
   "**Espesar.** Cuece 5–8 minutos a fuego suave, removiendo, hasta que espese y pierda el sabor a harina.",
   "**Terminar.** Añade la nuez moscada y la sal.",
  ],
  "tips": ["**Más espesa** (para croquetas): 80 g de mantequilla y 80 g de harina por cada 500 ml de leche.", "**Para que no haga costra:** cúbrela con film pegado a la superficie.", "**Vegana:** usa aceite de oliva suave y bebida de soja o avena sin azúcar."],
 },
 "en": {
  "title": "Béchamel sauce", "meta": "Makes **about 2 cups** · ⏱️ 15 minutes · Difficulty: easy",
  "intro": "Butter, flour and milk with nutmeg: the white sauce for lasagna, cannelloni and croquettes, one of the French mother sauces.",
  "ing": ["3 tablespoons butter", "⅓ cup all-purpose flour", "2 cups whole milk", "1 pinch nutmeg", "Salt"],
  "steps": [
   "**Roux.** Melt the butter over medium-low heat, add the flour and cook 2 minutes, stirring, without browning.",
   "**Milk.** Gradually whisk in the hot milk so no lumps form.",
   "**Thicken.** Simmer gently 5–8 minutes, stirring, until thick and no longer floury.",
   "**Finish.** Add the nutmeg and salt.",
  ],
  "tips": ["**Thicker** (for croquettes): double the butter and flour for the same milk.", "**To prevent a skin:** press plastic wrap onto the surface.", "**Vegan:** use mild olive oil and unsweetened soy or oat milk."],
 },
},
{
 "slug": "beurre-blanc", "tags_es": FR_ES + ["emulsion", "mantequilla", "pescado"], "tags_en": FR_EN + ["butter", "emulsion", "fish"],
 "es": {
  "title": "Beurre blanc (mantequilla blanca)", "meta": "Para **4 personas** · ⏱️ 20 minutos · Dificultad: media",
  "intro": "Reducción de chalota, vino blanco y vinagre montada con mantequilla fría: la salsa del Loira para el pescado.",
  "ing": ["2 chalotas picadas muy finas", "100 ml de vino blanco seco (muscadet, si puedes)", "50 ml de vinagre de vino blanco", "200 g de mantequilla muy fría, en dados", "Sal y pimienta blanca"],
  "steps": [
   "**La reducción.** Cuece la chalota con el vino y el vinagre a fuego medio hasta que solo queden 2 cucharadas de líquido.",
   "**Montar.** Baja el fuego al mínimo y añade la mantequilla dado a dado, batiendo sin parar. Espera a que cada dado se funda antes de añadir el siguiente.",
   "**Sin hervir.** La salsa no debe hervir: si se calienta demasiado, apártala del fuego un momento mientras bates.",
   "**Terminar.** Cuela si la quieres fina, salpimienta y sírvela enseguida.",
  ],
  "tips": ["**Con** pescado blanco, salmón, vieiras, espárragos o verduras al vapor.", "**Mantenla templada** en un termo o al baño maría muy suave; si se enfría, se separa.", "**Sin alcohol:** cambia el vino por caldo de pescado con unas gotas de limón."],
 },
 "en": {
  "title": "French white butter sauce", "meta": "Serves **4** · ⏱️ 20 minutes · Difficulty: medium",
  "intro": "A reduction of shallot, white wine and vinegar mounted with cold butter: the Loire Valley sauce for fish.",
  "ing": ["2 shallots, very finely chopped", "Scant ½ cup dry white wine (Muscadet if possible)", "3½ tablespoons white wine vinegar", "14 tablespoons (1¾ sticks) very cold butter, cubed", "Salt and white pepper"],
  "steps": [
   "**Reduction.** Simmer the shallot with the wine and vinegar over medium heat until only 2 tablespoons of liquid remain.",
   "**Mount.** Turn the heat to its lowest and whisk in the butter one cube at a time, waiting for each to melt before adding the next.",
   "**Never boil.** If the sauce gets too hot, lift it off the heat for a moment while whisking.",
   "**Finish.** Strain for a smooth sauce, season and serve right away.",
  ],
  "tips": ["**Serve with** white fish, salmon, scallops, asparagus or steamed vegetables.", "**Keep it warm** in a thermos or over very gentle heat; if it cools, it separates.", "**Alcohol-free:** use fish stock with a few drops of lemon instead of wine."],
 },
},
{
 "slug": "hollandaise", "tags_es": FR_ES + ["emulsion", "huevo", "sin-alcohol"], "tags_en": FR_EN + ["alcohol-free", "egg", "emulsion"],
 "es": {
  "title": "Salsa holandesa (sauce hollandaise)", "meta": "Para **4 personas** · ⏱️ 20 minutos · Dificultad: media",
  "intro": "Yemas emulsionadas con mantequilla y limón al baño maría: la salsa de los espárragos y los huevos Benedict.",
  "ing": ["3 yemas de huevo", "200 g de mantequilla", "1 cucharada de zumo de limón", "1 cucharada de agua", "1 pizca de sal", "1 pizca de cayena o de pimienta blanca (opcional)"],
  "steps": [
   "**La mantequilla.** Fúndela y déjala templar, retirando la espuma.",
   "**Las yemas.** En un bol al baño maría, sin que el agua hierva, bate las yemas con el agua y el limón hasta que espesen y doblen su volumen, 3–4 minutos.",
   "**Montar.** Fuera del fuego, añade la mantequilla templada en un hilo fino, batiendo sin parar, hasta que quede espesa y brillante.",
   "**Terminar.** Añade la sal y la cayena y ajusta de limón. Sírvela templada.",
  ],
  "tips": ["**Con** espárragos, huevos Benedict, salmón, pescado al vapor o brócoli.", "**Con batidora:** pon las yemas, el limón y la sal en el vaso y añade la mantequilla muy caliente en un hilo con la batidora en marcha.", "**Si se corta:** bate 1 cucharada de agua caliente en otro bol y añade la salsa poco a poco."],
 },
 "en": {
  "title": "Hollandaise sauce", "meta": "Serves **4** · ⏱️ 20 minutes · Difficulty: medium",
  "intro": "Egg yolks emulsified with butter and lemon over a water bath: the sauce for asparagus and eggs Benedict.",
  "ing": ["3 egg yolks", "14 tablespoons (1¾ sticks) butter", "1 tablespoon lemon juice", "1 tablespoon water", "1 pinch salt", "1 pinch cayenne or white pepper (optional)"],
  "steps": [
   "**Butter.** Melt it and let it cool slightly, skimming off the foam.",
   "**Yolks.** In a bowl over barely simmering water, whisk the yolks with the water and lemon until thick and doubled, 3–4 minutes.",
   "**Mount.** Off the heat, whisk in the warm butter in a thin stream until thick and glossy.",
   "**Finish.** Add salt and cayenne and adjust the lemon. Serve warm.",
  ],
  "tips": ["**Serve with** asparagus, eggs Benedict, salmon, steamed fish or broccoli.", "**Blender method:** put the yolks, lemon and salt in the cup and stream in very hot butter with the blender running.", "**If it breaks:** whisk 1 tablespoon hot water in a clean bowl and slowly whisk in the sauce."],
 },
},
{
 "slug": "mornay", "tags_es": FR_ES + ["leche", "queso", "sin-alcohol"], "tags_en": FR_EN + ["alcohol-free", "cheese", "milk"],
 "es": {
  "title": "Salsa Mornay (sauce Mornay)", "meta": "Para **unos 600 ml** · ⏱️ 20 minutos · Dificultad: fácil",
  "intro": "Bechamel enriquecida con queso gruyer y yema de huevo: la salsa de los gratinados, el croque-monsieur y la coliflor al horno.",
  "ing": ["40 g de mantequilla", "40 g de harina", "500 ml de leche entera", "100 g de queso gruyer (o emmental) rallado", "1 yema de huevo (opcional)", "1 pizca de nuez moscada", "Sal"],
  "steps": [
   "**La bechamel.** Funde la mantequilla, añade la harina y cocínala 2 minutos. Añade la leche caliente batiendo y cuece 5–8 minutos hasta que espese.",
   "**El queso.** Fuera del fuego, añade el queso rallado y remueve hasta que se funda.",
   "**La yema.** Si la usas, bátela con 2 cucharadas de la salsa y añádela al cazo, removiendo.",
   "**Terminar.** Añade la nuez moscada y prueba antes de salar: el queso ya es salado.",
  ],
  "tips": ["**Para gratinar:** cubre verduras, pescado o pasta, espolvorea más queso y gratina hasta que se dore.", "**Croque-monsieur:** pan de molde, jamón cocido, la salsa y queso, al horno.", "**No la hiervas** después de añadir el queso y la yema."],
 },
 "en": {
  "title": "Mornay cheese sauce", "meta": "Makes **about 2½ cups** · ⏱️ 20 minutes · Difficulty: easy",
  "intro": "Béchamel enriched with Gruyère and egg yolk: the sauce for gratins, croque-monsieur and baked cauliflower.",
  "ing": ["3 tablespoons butter", "⅓ cup all-purpose flour", "2 cups whole milk", "1 cup grated Gruyère (or Emmental)", "1 egg yolk (optional)", "1 pinch nutmeg", "Salt"],
  "steps": [
   "**Béchamel.** Melt the butter, add the flour and cook 2 minutes. Whisk in the hot milk and simmer 5–8 minutes until thick.",
   "**Cheese.** Off the heat, stir in the grated cheese until melted.",
   "**Yolk.** If using, whisk it with 2 tablespoons of the sauce and stir it into the pan.",
   "**Finish.** Add the nutmeg and taste before salting: the cheese is salty.",
  ],
  "tips": ["**To gratinate:** cover vegetables, fish or pasta, sprinkle more cheese and broil until golden.", "**Croque-monsieur:** sandwich bread, ham, the sauce and cheese, baked.", "**Don't boil it** once the cheese and yolk are in."],
 },
},
{
 "slug": "veloute", "tags_es": FR_ES + ["caldo", "sin-alcohol"], "tags_en": FR_EN + ["alcohol-free", "stock"],
 "es": {
  "title": "Salsa velouté", "meta": "Para **unos 500 ml** · ⏱️ 25 minutos · Dificultad: fácil",
  "intro": "Un roux blanco cocido con caldo claro de ave, de ternera o de pescado: la salsa madre francesa más ligera. En la foto, una salsa blanca al cocinarse.",
  "ing": ["40 g de mantequilla", "40 g de harina", "600 ml de caldo claro (de pollo, de ternera o de pescado), caliente", "Unas gotas de zumo de limón", "Sal y pimienta blanca"],
  "steps": [
   "**El roux.** Funde la mantequilla a fuego medio-suave, añade la harina y cocínala 2–3 minutos removiendo, hasta que tome un color muy pálido.",
   "**El caldo.** Añade el caldo caliente poco a poco, batiendo con varillas.",
   "**Cocer.** Cuece a fuego suave 15 minutos, desespumando, hasta que napee la cuchara.",
   "**Terminar.** Cuela, añade unas gotas de limón y salpimienta.",
  ],
  "tips": ["**Con caldo de pescado** es la base de la salsa de vino blanco; con caldo de pollo, de la salsa suprema (con nata).", "**Con** pollo escalfado, pescado al vapor, vol-au-vent o verduras.", "**El caldo** es la clave: cuanto mejor sea, mejor la salsa."],
 },
 "en": {
  "title": "Velouté sauce", "meta": "Makes **about 2 cups** · ⏱️ 25 minutes · Difficulty: easy",
  "intro": "A blond roux simmered with light chicken, veal or fish stock: the lightest French mother sauce. The photo shows a white sauce being cooked.",
  "ing": ["3 tablespoons butter", "⅓ cup all-purpose flour", "2½ cups light stock (chicken, veal or fish), hot", "A few drops lemon juice", "Salt and white pepper"],
  "steps": [
   "**Roux.** Melt the butter over medium-low heat, add the flour and cook 2–3 minutes, stirring, until very pale golden.",
   "**Stock.** Gradually whisk in the hot stock.",
   "**Simmer.** Simmer gently for 15 minutes, skimming, until it coats a spoon.",
   "**Finish.** Strain, add a few drops of lemon and season.",
  ],
  "tips": ["**With fish stock** it's the base for white wine sauce; with chicken stock, for sauce suprême (with cream).", "**Serve with** poached chicken, steamed fish, vol-au-vent or vegetables.", "**Stock is key:** the better the stock, the better the sauce."],
 },
},
]
