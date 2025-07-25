import random
from collections import Counter
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
    "lonely": "grief",
    "joyful": "happy",
    "glad": "happy",
    "fearful":"fear",
}

DEFAULT_VERSE = "Romans 8:28 - And we know that in all things God works for the good of those who love him."

def get_scripture_for_feeling(feeling_input: str) -> str:
    feeling_input = feeling_input.lower()
    matched_themes = []

    #Find all themes whose keywords appear in the input
    for word, theme in keywords_map.items():
        if word in feeling_input:
            matched_themes.append(theme)
        
    if not matched_themes:
        return DEFAULT_VERSE
    
    #Count most common matched theme
    theme_counts = Counter(matched_themes)
    most_common_theme = theme_counts.most_common(1)[0][0]


    return random.choice(scripture_data.get(most_common_theme, [DEFAULT_VERSE]))