import spacy 
from spacy.language import Language
from spacy.tokens import Doc 

non_veg_ingredients = ['abalone', 'alligator', 'alpaca', 'ambergris', 'anchovies', 'anchovy essence', 'anchovy paste', 'animal blood', 'animal ears', 'animal rennet', 'animal squalene', 'animal tendons', 'beef', 'belacan', 'beondegi', "bird's nest", 'bison', 'black pudding', 'blood tofu', 'blue crab', 'bone marrow', 'bone meal', 'bone phosphate', 'bonito flakes', 'bottarga', 'bowhead whale', 'brain', 'buffalo', 'cabrito', 'calamari', 'calcium stearate', 'camel', 'cane rats', 'capybara', 'caribou', 'carmine', 'carp', 'castoreum', 'catfish', 'caviar', 'chapulines', 'chevon', 'chicken', 'chicken eggs', 'chicken feet', 'chitosan', 'chitterlings', 'chymosin', 'civet musk', 'civetone', 'clams', 'coagulated blood cakes', 'cobra', 'cochineal', 'cockscomb', 'cod', 'cod liver oil', 'conchs', 'coypu', 'crawfish', 'crayfish', 'cricket flour', 'cricket powder', 'crocodile', 'cuttlefish', 'cuy', 'dashi powder', 'deer', 'demi-glace', 'disodium inosinate', 'dolphin meat', 'domestic pigeon', 'donkey', 'duck', 'duck eggs', 'dungeness crab', 'e120', 'e422', 'e470a', 'e471', 'e542', 'e570', 'e572', 'e631', 'e904', 'edible dormouse', 'eel', 'elk', 'emu', 'escamoles', 'escargot', 'fin whale', 'fish oil', 'fish sauce', 'flounder', 'foie gras', 'frog legs', 'gelatin', 'gizzard', 'glace de viande', 'glycerin', 'glycerol', 'goat', 'goose', 'goose barnacles', 'goose eggs', 'grasscutters', 'grouper', 'grouse', 'guinea fowl', 'guinea pig', 'haddock', 'haggis', 'halibut', 'hare', 'haslet', 'head cheese', 'heart', 'herring', 'hondashi', 'horse', 'horseshoe crab roe', 'hoya', 'igunaq', 'ikura', 'iriko', 'ishiru', 'isinglass', 'jellyfish', 'kai mod daeng', 'kangaroo', 'karasumi', 'katsuobushi', 'kidney', 'king crab', 'kopi luwak beans', 'krill', 'l-cysteine', 'lamb', 'lard', 'lipase', 'liver', 'llama', 'lobster', 'locusts', 'lungs', 'mackerel', 'mahi-mahi', 'mallard', 'marlin', 'masago', 'mealworms', 'mentaiko', 'migratory cicadas', 'milt', 'minke whale', 'mono- and diglycerides of fatty acids', 'moose', 'mopane worms', 'muktuk', 'muskrat', 'mussels', 'mutton', 'nam pla', 'niboshi', 'nuoc mam', 'nutria', 'octopus', 'opossum', 'ortiguillas', 'ostrich', 'ostrich eggs', 'oxtail', 'oyster sauce', 'oysters', 'pancreas', 'partridge', 'pepsin', 'percebes', 'perch', 'pheasant', 'pig mask', 'pig snout', "pig's trotters", 'pike', 'plasma powder', 'pollock', 'pork', 'prawns', 'primate bushmeat', 'python', 'quail', 'quail eggs', 'rabbit', 'ray', 'red caviar', 'reindeer', 'sago grubs', 'sago worms', 'salmon', 'sardines', 'scallops', 'schmaltz', 'scorpions', 'sea anemones', 'sea bass', 'sea cucumber', 'sea snails', 'sea squirts', 'sea urchin', 'seal flippers', 'seal liver', 'seal meat', 'shark', 'shark fin', 'shellac', 'shirako', 'shottsuru', 'shrimp', 'shrimp paste', 'silkworm pupae', 'skate', 'snake meat', 'snapper', 'snow crab', 'sole', 'spleen', 'squab', 'squid', 'stearates', 'stearic acid', 'sturgeon roe', 'suet', 'sweetbreads', 'swordfish', 'tallow', 'tarako', 'terasi', 'terrapin', 'thai zebra tarantula', 'thymus', 'tilapia', 'tobiko', 'tongue', 'tripe', 'trout', 'tuna', 'tunicates', 'turkey', 'turkey eggs', 'turtle meat', 'uni', 'veal', 'velvet antler', 'venison', 'wallaby', 'walleye', 'walrus meat', 'weaver ant eggs', 'whale blubber', 'whale meat', 'whale oil', 'whelks', 'wild boar', 'wild duck', 'witchetty grubs', 'woodcock', 'yak']

# 1. Set extensions before loading pipeline
Doc.set_extension("is_non_veg", default=False, force=True)
Doc.set_extension("non_veg_items", default=[], force=True)

nlp = spacy.load('en_core_web_sm')

# 2. Define component
@Language.component("non_veg_extractor")
def non_veg_extractor(doc):
    # Create a set of lowercased full token texts for exact matching
    tokens_text = {token.text.lower() for token in doc}
    found_items = []
    
    for non_veg in non_veg_ingredients:
        # For multi-word ingredients (like 'shrimp paste'), check if it's in raw text
        if " " in non_veg:
            if non_veg in doc.text.lower() and non_veg not in found_items:
                found_items.append(non_veg)
        # For single-word ingredients (like 'liver'), match exact complete tokens only
        else:
            if non_veg in tokens_text and non_veg not in found_items:
                found_items.append(non_veg)
                
    doc._.is_non_veg = len(found_items) > 0
    doc._.non_veg_items = found_items
    return doc

# 3. CRITICAL CRUX: Add the component BEFORE parsing the text
nlp.add_pipe("non_veg_extractor", last=True)

recipe = """
### Restaurant-Style Butter Chicken (Murgh Makhani) ###

[Ingredients]
* Chicken Marinade:
  - 500g boneless chicken thighs, cubed
  - 1/2 cup thick yogurt (hung curd)
  - 1 tbsp ginger-garlic paste
  - 1 tsp Kashmiri red chili powder
  - 1/2 tsp garam masala
  - 1 tbsp lemon juice
  - 1 tbsp oil
  - Salt to taste

* Makhani Sauce:
  - 2 tbsp butter
  - 1 tbsp oil
  - 1 large onion, finely chopped
  - 4 large ripe tomatoes, pureed
  - 1 tbsp ginger-garlic paste
  - 1 tsp Kashmiri red chili powder
  - 1/2 tsp garam masala
  - 1/2 cup heavy cream
  - 1 tbsp dried fenugreek leaves (kasuri methi)
  - 1 pinch sugar

[Instructions]
1. MARINATE: Combine all chicken marinade ingredients in a bowl. Coat the chicken thoroughly and refrigerate for at least 30 minutes.
2. SEAR: Heat 1 tbsp oil in a pan over high heat. Sear chicken pieces for 3-4 minutes per side until charred and cooked through. Set aside.
3. SAUCE BASE: Melt 1 tbsp butter and 1 tbsp oil in the same pan. Saute onions until soft. Add ginger-garlic paste and cook for 1 minute. Pour in tomato puree, chili powder, and garam masala. Simmer until the oil separates from the paste.
4. BLEND: Cool the sauce slightly, blend until completely smooth, and strain it back into the pan to remove skins and seeds.
5. FINISH: Bring the smooth sauce to a simmer. Stir in the chicken, remaining 1 tbsp butter, heavy cream, sugar, and crushed kasuri methi. Simmer for 3-5 minutes until rich and velvety.
"""

# 4. Now parse your doc safely
doc = nlp(recipe)
print("Items Found:", doc._.non_veg_items)
print("Is Non-Veg:", doc._.is_non_veg)

kashmiri_pulao_recipe = """
### Kashmiri Pulao (Vegetarian) ###

[Ingredients]
* Rice & Aromatics:
  - 1 cup long-grain Basmati rice (washed and soaked for 30 minutes)
  - 2 tbsp ghee (clarified butter)
  - 1 pinch saffron strands (kesar), soaked in 3 tbsp warm milk
  - 1.5 cups water
  - 1/2 tsp fennel powder (saunf)
  - 1/2 tsp ginger powder (dry sonth)
  - Whole spices: 1 bay leaf, 1-inch cinnamon stick, 2 green cardamoms, 1 black cardamom, 3 cloves
  - Salt to taste

* Royal Garnish (Fruits & Nuts):
  - 1 large onion, sliced thinly (for crisp fried birista)
  - 10-12 almonds, blanched and slivered
  - 10-12 cashew nuts, split
  - 1 tbsp raisins (kishmish)
  - 1/4 cup fresh pomegranate pearls (anar)
  - 1/4 cup apple or pineapple cubes, finely chopped (optional)

[Instructions]
1. FRY GARNISH: Heat ghee in a deep pot over medium heat. Fry sliced onions until deeply golden and crispy; remove and set aside. In the same ghee, fry cashews and almonds until golden, then flash-fry raisins until plump. Set all aside.
2. TEMPER: Turn heat to low. In the remaining fragrant ghee, drop all whole spices (bay leaf, cinnamon, cardamoms, cloves) and let sizzle for 30 seconds.
3. COOK RICE: Add drained basmati rice to the pot. Gently saute for 1-2 minutes until grains are glossy. Pour in water, fennel powder, ginger powder, and salt. Bring to a boil, cover tightly, and simmer on the lowest heat for 10 minutes until water is absorbed.
4. INFUSE SAFFRON: Uncover and drizzle the saffron milk in patches over the rice. Replace the lid and let the pot steam off the heat for 5 minutes.
5. ASSEMBLE: Gently fluff the rice with a fork. Transfer to a serving platter and top generously with the fried onions, toasted nuts, and fresh pomegranate/fruit pieces just before serving.
"""

doc = nlp(kashmiri_pulao_recipe)
print("Items Found:", doc._.non_veg_items)
print("Is Non-Veg:", doc._.is_non_veg)