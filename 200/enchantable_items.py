import re
from pathlib import Path
from urllib.request import urlretrieve
from dataclasses import dataclass, field
from bs4 import BeautifulSoup as Soup
from collections import OrderedDict

out_dir = "/tmp"
html_file = f"{out_dir}/enchantment_list_pc.html"

HTML_FILE = Path(html_file)
URL = "https://www.digminecraft.com/lists/enchantment_list_pc.php"

@dataclass
class Enchantment:
    """Minecraft enchantment class
    
    Implements the following: 
        id_name, name, max_level, description, items
    """
    id_name: str
    name: str
    max_level: int
    description: str
    items: list = field(default_factory=list) 

    def __str__(self):
        return f"{self.name} ({self.max_level}): {self.description}"

@dataclass
class Item:
    """Minecraft enchantable item class
    
    Implements the following: 
        name, enchantments
    """
    name: str
    enchantments: list = field(default_factory=list) 

    def __str__(self):
        self.enchantments.sort(key=lambda x: x.id_name)
        enchants = "\n".join([f"  [{enchant.max_level}] {enchant.id_name}" 
                                for enchant 
                                in self.enchantments ] )
        
        return f"{self.name.replace('_',' ').title()}: \n{enchants}" 

def _roman_convert(numeral):
    translate = {"I":1,"II":2,"III":3,"IV":4,"V":5,"VI":6,"VII":7,"VIII":8,"IX":9,"X":10}
    return(translate[numeral])

def _clean_items(matchobject):
    replacements = { pat: repl for pat, repl 
                    in [("\.",""), 
                        ("_", " "),
                        ("enchanted", ""),
                        ("iron", ""),
                        ("png", ""),
                        ("sm", ""),  
                        ("rod", "") ]}
    return replacements.get(matchobject.group(), "")

def generate_enchantments(soup):
    """Generates a dictionary of Enchantment objects
    
    With the key being the id_name of the enchantment.
    """
    replacements = { pat: repl for pat, repl 
                    in [("\.",""), 
                        ("_", " "),
                        ("enchanted", ""),
                        ("iron", ""),
                        ("png", ""),
                        ("sm", ""),  
                        ("rod", "") ]}
    enchanted = dict()
    table = soup.find(class_="std_table")
    for row in table.find_all("tr")[1:]:
        elems = row.find_all("td")
        name = elems[0].a.text
        id_name = elems[0].em.text
        max_level = _roman_convert(elems[1].text)
        description = elems[2].text

        items = elems[4].img.get("data-src").split("/")[3]
        items_cleaned = re.sub("|".join(replacements), _clean_items, items )
        items_cleaned = items_cleaned.split()
        items_finish = [i if "fishing" not in i else "fishing_rod" for i in items_cleaned]
        enchanted[id_name] = Enchantment(name=name, 
                               id_name=id_name, 
                               max_level=max_level,
                               description=description,
                               items=items_finish)
    return enchanted

def generate_items(data):
    """Generates a dictionary of Item objects
    
    With the key being the item name.
    """
    Itemobjects = dict()
    soup = get_soup()
    items = { item for k,v in generate_enchantments(soup).items() for item in v.items}
    for item in items:
        enchantments = [val for key, val in data.items() if item.lower() in val.items] 
        Itemobjects[item] = Item(name=item, enchantments=enchantments)
    return OrderedDict(sorted(Itemobjects.items(), key = lambda x: x[1].name))

def get_soup(file=HTML_FILE):
    """Retrieves/takes source HTML and returns a BeautifulSoup object"""
    if isinstance(file, Path):
        if not HTML_FILE.is_file():
            urlretrieve(URL, HTML_FILE)

        with file.open() as html_source:
            soup = Soup(html_source, "html.parser")
    else:
        soup = Soup(file, "html.parser")

    return soup

def main():
    """This function is here to help you test your final code.
    
    Once complete, the print out should match what's at the bottom of this file"""
    soup = get_soup()
    enchantment_data = generate_enchantments(soup)
    minecraft_items = generate_items(enchantment_data)
    for item in minecraft_items:
        print(minecraft_items[item], "\n")


if __name__ == "__main__":
    main()

"""
Armor: 
  [1] binding_curse
  [4] blast_protection
  [4] fire_protection
  [4] projectile_protection
  [4] protection
  [3] thorns 

Axe: 
  [5] bane_of_arthropods
  [5] efficiency
  [3] fortune
  [5] sharpness
  [1] silk_touch
  [5] smite 

Boots: 
  [3] depth_strider
  [4] feather_falling
  [2] frost_walker 

Bow: 
  [1] flame
  [1] infinity
  [5] power
  [2] punch 

Chestplate: 
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Crossbow: 
  [1] multishot
  [4] piercing
  [3] quick_charge 

Fishing Rod: 
  [3] luck_of_the_sea
  [3] lure
  [1] mending
  [3] unbreaking
  [1] vanishing_curse 

Helmet: 
  [1] aqua_affinity
  [3] respiration 

Pickaxe: 
  [5] efficiency
  [3] fortune
  [1] mending
  [1] silk_touch
  [3] unbreaking
  [1] vanishing_curse 

Shovel: 
  [5] efficiency
  [3] fortune
  [1] silk_touch 

Sword: 
  [5] bane_of_arthropods
  [2] fire_aspect
  [2] knockback
  [3] looting
  [1] mending
  [5] sharpness
  [5] smite
  [3] sweeping
  [3] unbreaking
  [1] vanishing_curse 

Trident: 
  [1] channeling
  [5] impaling
  [3] loyalty
  [3] riptide
"""