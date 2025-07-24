import random
from ..data.scripture_data import scripture_data

keywords_map = {
    "anxious": "anxiety",
    "worried": "anxiety",
    "grieving": "grief",
    "sad": "grief",
    "afraid": "fear",
    "scared": "fear",
    "happy": "happy",
    "nervous": "anxiety",
    "lonely": "grief"
}

DEFAULT_VERSE = "Romans 8:28 - And we know that in all things God works for the good of those who love him."

def get_scripture_for_feeling(feeling_input: str) -> str:
    feeling_input = feeling_input.lower()
    matched_themes = set()

    #Find all themes whose keywords appear in the input
    for word, theme in keywords_map.items():
        if word in feeling_input:
            matched_themes.add(theme)
        
    if not matched_themes:
        return [DEFAULT_VERSE]
    
    print("Matched themes:", matched_themes)
    # Collect all verses for matched themes
    verses = []
    for theme in matched_themes:
        verses.extend(scripture_data.get(theme, []))

    return verses