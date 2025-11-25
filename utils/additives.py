from typing import Dict, List

class AdditiveDatabase:
    def __init__(self):
        self.additives = self._load_additives()
    
    def _load_additives(self) -> Dict[str, Dict]:
        return {
            'E100': {'name': 'Curcumin', 'type': 'Colorant', 'concern': 'Safe', 'vegan': True},
            'E101': {'name': 'Riboflavin', 'type': 'Colorant', 'concern': 'Safe', 'vegan': True},
            'E102': {'name': 'Tartrazine', 'type': 'Colorant', 'concern': 'Caution', 'vegan': True},
            'E110': {'name': 'Sunset Yellow', 'type': 'Colorant', 'concern': 'Caution', 'vegan': True},
            'E120': {'name': 'Carmine', 'type': 'Colorant', 'concern': 'Caution', 'vegan': False},
            'E130': {'name': 'Indigo Carmine', 'type': 'Colorant', 'concern': 'Safe', 'vegan': True},
            'E140': {'name': 'Chlorophyll', 'type': 'Colorant', 'concern': 'Safe', 'vegan': True},
            'E141': {'name': 'Chlorophyll Copper', 'type': 'Colorant', 'concern': 'Safe', 'vegan': True},
            'E150': {'name': 'Caramel', 'type': 'Colorant', 'concern': 'Safe', 'vegan': True},
            'E160': {'name': 'Beta-carotene', 'type': 'Colorant', 'concern': 'Safe', 'vegan': True},
            'E170': {'name': 'Calcium Carbonate', 'type': 'Colorant', 'concern': 'Safe', 'vegan': True},
            'E200': {'name': 'Sorbic Acid', 'type': 'Preservative', 'concern': 'Safe', 'vegan': True},
            'E201': {'name': 'Sodium Sorbate', 'type': 'Preservative', 'concern': 'Safe', 'vegan': True},
            'E202': {'name': 'Potassium Sorbate', 'type': 'Preservative', 'concern': 'Safe', 'vegan': True},
            'E210': {'name': 'Benzoic Acid', 'type': 'Preservative', 'concern': 'Safe', 'vegan': True},
            'E211': {'name': 'Sodium Benzoate', 'type': 'Preservative', 'concern': 'Safe', 'vegan': True},
            'E220': {'name': 'Sulfur Dioxide', 'type': 'Preservative', 'concern': 'Caution', 'vegan': True},
            'E300': {'name': 'Ascorbic Acid', 'type': 'Antioxidant', 'concern': 'Safe', 'vegan': True},
            'E301': {'name': 'Sodium Ascorbate', 'type': 'Antioxidant', 'concern': 'Safe', 'vegan': True},
            'E306': {'name': 'Tocopherol', 'type': 'Antioxidant', 'concern': 'Safe', 'vegan': True},
            'E307': {'name': 'Alpha Tocopherol', 'type': 'Antioxidant', 'concern': 'Safe', 'vegan': True},
            'E320': {'name': 'BHA', 'type': 'Antioxidant', 'concern': 'Caution', 'vegan': True},
            'E321': {'name': 'BHT', 'type': 'Antioxidant', 'concern': 'Caution', 'vegan': True},
            'E330': {'name': 'Citric Acid', 'type': 'Preservative', 'concern': 'Safe', 'vegan': True},
            'E331': {'name': 'Sodium Citrate', 'type': 'Preservative', 'concern': 'Safe', 'vegan': True},
            'E400': {'name': 'Alginic Acid', 'type': 'Thickener', 'concern': 'Safe', 'vegan': True},
            'E401': {'name': 'Sodium Alginate', 'type': 'Thickener', 'concern': 'Safe', 'vegan': True},
            'E406': {'name': 'Agar', 'type': 'Thickener', 'concern': 'Safe', 'vegan': True},
            'E407': {'name': 'Carrageenan', 'type': 'Thickener', 'concern': 'Safe', 'vegan': True},
            'E410': {'name': 'Locust Bean Gum', 'type': 'Thickener', 'concern': 'Safe', 'vegan': True},
            'E412': {'name': 'Guar Gum', 'type': 'Thickener', 'concern': 'Safe', 'vegan': True},
            'E414': {'name': 'Acacia Gum', 'type': 'Thickener', 'concern': 'Safe', 'vegan': True},
            'E415': {'name': 'Xanthan Gum', 'type': 'Thickener', 'concern': 'Safe', 'vegan': True},
            'E440': {'name': 'Pectin', 'type': 'Thickener', 'concern': 'Safe', 'vegan': True},
            'E460': {'name': 'Cellulose', 'type': 'Thickener', 'concern': 'Safe', 'vegan': True},
            'E471': {'name': 'Mono/Diglycerides', 'type': 'Emulsifier', 'concern': 'Safe', 'vegan': False},
            'E472': {'name': 'Fatty Acid Esters', 'type': 'Emulsifier', 'concern': 'Safe', 'vegan': False},
            'E475': {'name': 'Polyglycerol Esters', 'type': 'Emulsifier', 'concern': 'Safe', 'vegan': False},
            'E500': {'name': 'Sodium Carbonate', 'type': 'Raising Agent', 'concern': 'Safe', 'vegan': True},
            'E501': {'name': 'Potassium Carbonate', 'type': 'Raising Agent', 'concern': 'Safe', 'vegan': True},
            'E503': {'name': 'Ammonium Carbonate', 'type': 'Raising Agent', 'concern': 'Safe', 'vegan': True},
            'E504': {'name': 'Magnesium Carbonate', 'type': 'Raising Agent', 'concern': 'Safe', 'vegan': True},
            'E536': {'name': 'Potassium Ferrocyanide', 'type': 'Anti-caking', 'concern': 'Safe', 'vegan': True},
            'E551': {'name': 'Silicon Dioxide', 'type': 'Anti-caking', 'concern': 'Safe', 'vegan': True},
            'E552': {'name': 'Calcium Silicate', 'type': 'Anti-caking', 'concern': 'Safe', 'vegan': True},
            'E621': {'name': 'Monosodium Glutamate', 'type': 'Flavor Enhancer', 'concern': 'Safe', 'vegan': True},
            'E622': {'name': 'Disodium Glutamate', 'type': 'Flavor Enhancer', 'concern': 'Safe', 'vegan': True},
        }
    
    def get_additive_info(self, additive_code: str) -> Dict:
        additive_code = additive_code.upper().strip()
        
        if additive_code in self.additives:
            return self.additives[additive_code]
        
        return {
            'name': additive_code,
            'type': 'Unknown',
            'concern': 'Unknown',
            'vegan': None
        }
    
    def find_additives_in_ingredients(self, ingredients: List[str]) -> List[Dict]:
        found_additives = []
        
        for ingredient in ingredients:
            ingredient_upper = ingredient.upper()
            
            if 'E' in ingredient_upper:
                parts = ingredient_upper.split()
                for part in parts:
                    if part.startswith('E') and len(part) > 1:
                        code = part[:4]
                        if code in self.additives:
                            found_additives.append({
                                'code': code,
                                'info': self.additives[code]
                            })
        
        return found_additives
