def transposerEnglish(letter):
    """ Function to switch letters from "English" language
    Keep the change of indices negative to avoid the need to add letters   """
    voyel = "aeiouy"
    voyel_capital = str.upper(voyel)
    consonant = "bcdfghjklmnpqrstvwxz"
    consonant_capital = str.upper(consonant)

    if letter in voyel:
        new_letter = voyel.index(letter) - 2
        return voyel[new_letter]
    elif letter in voyel_capital:
        new_letter = voyel_capital.index(letter) - 2
        return voyel_capital[new_letter]
    elif letter in consonant: 
        new_letter = consonant.index(letter) - 5
        return consonant[new_letter]
    elif letter in consonant_capital: 
        new_letter = consonant_capital.index(letter) - 5
        return consonant_capital[new_letter]
    else : 
        return letter

def transposerArabian(letter):
    """ Function to switch letters from "Arabian" language
    Keep the change of indices negative to avoid the need to add letters   """
    lunar = "بجحخعغقفكمهويء"
    solar = "تثدذرزسشصضطظنل"

    if letter in lunar:
        new_letter = lunar.index(letter) - 2
        return lunar[new_letter]
    elif letter in solar: 
        new_letter = solar.index(letter) - 5
        return solar[new_letter]
    else : 
        return letter

def transposerFrancais(letter):
    """ Function to switch letters from "Français" language
    Keep the change of indices negative to avoid the need to add letters  """
    voyel = "aeiouy"
    voyel_capital = str.upper(voyel)
    voyel_accent = "éàèùâêîôûëïüÿœæ"
    accent_capital = str.upper(voyel_accent)
    consonant = "bcdfghjklmnpqrstvwxz" 
    cedille_tilde = "çÇñÑ"
    consonant_capital = str.upper(consonant)
  
    if letter in voyel:
        new_letter = voyel.index(letter) - 3
        return voyel[new_letter]
    elif letter in voyel_capital:
        new_letter = voyel_capital.index(letter) - 3
        return voyel_capital[new_letter]
    elif letter in voyel_accent:
        new_letter = voyel_accent.index(letter) - 3
        return voyel_accent[new_letter]
    elif letter in accent_capital:
        new_letter = accent_capital.index(letter) - 3
        return accent_capital[new_letter]
    elif letter in consonant: 
        new_letter = consonant.index(letter) - 2
        return consonant[new_letter]
    elif letter in consonant_capital: 
        new_letter = consonant_capital.index(letter) - 2
        return consonant_capital[new_letter]
    elif letter in cedille_tilde: 
        new_letter = cedille_tilde.index(letter) - 2
        return cedille_tilde[new_letter]
    else: 
        return letter
