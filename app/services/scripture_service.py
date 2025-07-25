import random
from collections import Counter
from ..data.scripture_data import scripture_data

keywords_map = {
    "anxious": "anxiety",
    "worried": "anxiety",
    "grieving": "sad",
    "sad": "sad",
    "afraid": "fear",
    "scared": "fear",
    "happy": "happy",
    "nervous": "anxiety",
    "lonely": "sad",
    "joyful": "happy",
    "glad": "happy",
    "fearful":"fear",
}

DEFAULT_VERSE = "For this is how God loved the world. He gave His one and only Son, so that everyone who believes in Him will not perish but have eternal life. ~ John 3:16"

def get_scripture_for_feeling(feeling_input: str) -> dict:
    feeling_input = feeling_input.lower()
    matched_themes = set()

    #Find all themes whose keywords appear in the input
    for word, theme in keywords_map.items():
        if word in feeling_input:
            matched_themes.add(theme)
    
    # If there are no matches, return the default verse
    if not matched_themes:
        return {
            "matched_feelings": [],
            "verse": [DEFAULT_VERSE]
        }
    
    #Collect verses for each matched theme
    result = {}
    for theme in matched_themes:
        verses = scripture_data.get(theme, [])
        result[theme] = verses if verses else [DEFAULT_VERSE]

    return {
        "matched_feelings": list(matched_themes),
        "verses": result
    }

def get_verse_by_theme(theme: str) -> dict:
    theme_lower = theme.lower()
    verses = scripture_data.get(theme_lower)

    if verses:
        return {"verse": random.choice(verses)}
    else:
        return {
            "verse": DEFAULT_VERSE,
            "note": f"No exact match found for theme '{theme}', here's a defualt verse."
        }