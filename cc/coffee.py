import argparse
from ast import arg

class Dilutions():
    buffer = 1.68/1000
    mg = 2.45/1000


def buffer_to_nahco3(buffer: float) -> float:
    """
    Converts buffer (ml) to baking soda (g)

    :param buffer: Amount of buffer in ml
    :type buffer: float
    :return: Amount of baking soda in grams
    :rtype: float
    """    
    return buffer * Dilutions.buffer


def mg_to_mgso4(mg: float) -> float:
    """
    Converts mg (ml) to epsom salt (g)

    :param mg: Amount of mg in ml
    :type mg: float
    :return: Amount of epsom salt  in grams
    :rtype: float
    """    
    return mg * Dilutions.mg

class SolidsRecipe:
    def __init__(self, name: str, nahco3: float, mgso4: float, water: float):
        """
        Coffee water recipe that has been converted into grams.

        :param name: Coffee recipe name
        :type name: str
        :param nahco3: Baking soda in grams
        :type nahco3: float
        :param mgso4: Epsom salt in grams
        :type mgso4: float
        :param water: Water in grams
        :type water: float
        """        
        self.name = name
        self.nahco3 = nahco3
        self.mgso4 = mgso4
        self.water = water
    
    def __str__(self):
        return f"{self.name}: \n    nahco3 {round(self.nahco3, 2)}g \n    mgs04  {round(self.mgso4, 2)}g \n    water  {round(self.water, 2)}g"

class DilutionRecipe:
    def __init__(self, name: str, buffer: float, mg: float, water: float):
        """
        
        Coffee water recipe based on the barista hustle method of using diluted solutions. These recipes can be found on the Barista Hustle website
        https://www.baristahustle.com/blog/diy-water-recipes-redux/

        :param name: Coffee recipe name
        :type name: str
        :param buffer: Buffer solution in ml
        :type buffer: float
        :param mg: Mg solution in ml
        :type mg: float
        :param water: Water in grams
        :type water: float
        """        
        self.name = name
        self.buffer = buffer
        self.mg = mg
        self.water = water

    def convert(self, output: float) -> SolidsRecipe:
        """
        _summary_

        :param output: Amount of water in grams
        :type output: float
        :return: Converted solution as a SolidsRecipe
        :rtype: SolidsRecipe
        """        
        water_ratio = output/self.water
        return SolidsRecipe(name=self.name, nahco3=buffer_to_nahco3(self.buffer * water_ratio), mgso4=mg_to_mgso4(self.mg * water_ratio), water=output)

def main():
    parser = argparse.ArgumentParser(description="Coffee Recipe Converter.")
    parser.add_argument("--name")
    parser.add_argument("--buffer", type=float)
    parser.add_argument("--mg", type=float)
    parser.add_argument("--water", type=float)
    parser.add_argument("--output", type=float)
    args = parser.parse_args()
    recipe = DilutionRecipe(name=args.name, buffer=args.buffer, mg=args.mg, water=args.mg)
    print(recipe.convert(output=args.output))

if __name__ == "__main__":
    # rao = DilutionRecipe(name="Rao", buffer=50.1, mg=75.7, water=874.2)
    # new_rao = rao.convert(output=500)
    # print(new_rao)
    main()
