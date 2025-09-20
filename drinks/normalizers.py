"""
Name normalization utilities.
"""
import re
import unicodedata
from typing import Optional


class NameNormalizer:
    """
    A class to handle name normalization with various strategies.
    """
    
    # City mapping dictionary: normalized_name -> set of aliases
    CITY_MAPPING = {
        # US Cities
        'new york': {'nyc', 'new york city', 'manhattan', 'ny'},
        'los angeles': {'la', 'los angeles city'},
        
        # Italian Cities (with both Italian and English names)
        'rome': {'roma', 'rome', 'eternal city'},
        'milan': {'milano', 'milan', 'mi'},
        'naples': {'napoli', 'naples', 'na'},
        'turin': {'torino', 'turin', 'to'},
        'palermo': {'palermo', 'pa'},
        'genoa': {'genova', 'genoa', 'ge'},
        'bologna': {'bologna', 'bo'},
        'florence': {'firenze', 'florence', 'fi'},
        'bari': {'bari', 'ba'},
        'catania': {'catania', 'ct'},
        'venice': {'venezia', 'venice', 've'},
        'verona': {'verona', 'vr'},
        'messina': {'messina', 'me'},
        'padua': {'padova', 'padua', 'pd'},
        'trieste': {'trieste', 'ts'},
        'lecce': {'lecce', 'le'},
        'galatina': {'galatina', 'la città del pasticciotto', 'galatown', 'gala'},
        
        # Major European Cities (with local, English, and Italian names)
        'london': {'london', 'greater london', 'londra', 'ldn'},
        'paris': {'paris', 'city of light', 'parigi'},
        'berlin': {'berlin', 'berlino'},
        'madrid': {'madrid'},
        'barcelona': {'barcelona', 'barcellona', 'bcn'},
        'amsterdam': {'amsterdam', 'ams'},
        'vienna': {'wien', 'vienna'},
        'prague': {'praha', 'prague', 'praga'},
        'warsaw': {'warszawa', 'warsaw', 'varsavia'},
        'budapest': {'budapest'},
        'bucharest': {'bucuresti', 'bucharest', 'bucarest'},
        'sofia': {'sofia'},
        'athens': {'athenai', 'athens', 'atenne'},
        'lisbon': {'lisboa', 'lisbon', 'lisbona'},
        'porto': {'porto', 'oporto'},
        'dublin': {'dublin', 'dublino'},
        'copenhagen': {'kobenhavn', 'copenhagen', 'copenaghen', 'cph'},
        'stockholm': {'stockholm', 'stoccolma', 'arn'},
        'oslo': {'oslo'},
        'helsinki': {'helsingfors', 'helsinki', 'hel'},
        'brussels': {'bruxelles', 'brussels', 'bru'},
        'zurich': {'zurich', 'zurigo', 'zrh'},
        'geneva': {'geneva', 'ginevra', 'gva'},
    }
    
    def __init__(self):
        """Initialize the normalizer with default settings."""
        self.preserve_case = False
        self.remove_extra_spaces = True
        self.normalize_unicode = True
        
        self.alias_to_city = self._build_alias_to_city_mapping()
    
    def _build_alias_to_city_mapping(self) -> dict:
        """
        Build a mapping from aliases to normalized city names.
        
        Returns:
            Dictionary mapping aliases to normalized city names
        """
        alias_to_city = {}
        for normalized, aliases in self.CITY_MAPPING.items():
            for alias in aliases:
                alias_to_city[alias.lower()] = normalized
        return alias_to_city
    
    
    def normalize(self, name: str) -> Optional[str]:
        """
        Normalize a name using all configured strategies.
        
        Args:
            name: The name to normalize
            
        Returns:
            The normalized name
        """
        if not name:
            return None
        
        normalized = name
        
        # Put everything in lowercase
        normalized = (normalized
                      .lower()
                      .strip()
                      .replace('-', ' ')
                      )
        normalized = self.alias_to_city.get(normalized, None)
        
        return normalized
 