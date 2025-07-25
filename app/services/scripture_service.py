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

DEFAULT_VERSE = "Romans 8:28 - And we know that in all things God works for the good of those who love him."

def get_scripture_for_feeling(feeling_input: str) -> str:
    feeling_input = feeling_input.lower()
    matched_themes = set()

    #Find all themes whose keywords appear in the input
    for word, theme in keywords_map.items():
        if word in feeling_input:
            matched_themes.add(theme)
    
    # If there are no matches, return the default verse
    if not matched_themes:
        return {"Important": [DEFAULT_VERSE]}
    
    #Collect verses for each matched theme
    result = {}
    for theme in matched_themes:
        verses = scripture_data.get(theme, [])
        result[theme] = verses if verses else [DEFAULT_VERSE]

    return result