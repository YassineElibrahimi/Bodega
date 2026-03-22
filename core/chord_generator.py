"""
Load chord progression data from JSON file (the Gas)

Define a function to get a random progression:
    Input: genre, theme
    Construct a key string like "genre_theme"
    If the key exists in the loaded data:
        Pick a random progression from the list
        Return that progression (list of Roman numerals)
    Else:
        Raise an error (progression not found)

Define a function to convert Roman numerals to actual chords:
    Input: list of Roman numeral strings, key name (e.g., "C")
    Create a music21 key object
    For each numeral:
        Create a RomanNumeral object using music21
        Set its duration (e.g., whole note)
        Append to result list
    Return the list of chord objects

Define the main generation function:
    Input: genre, theme, key name
    Get a random progression (Roman numerals)
    Convert it to chords
    Return the chords
"""