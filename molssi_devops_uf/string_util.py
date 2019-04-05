"""
string_util.py
Some molssi stuff

Misc string processing functions
"""

def title_case(sentence):
    '''
    Convert to title case

    Parameters
    ------
    sentence: string

    Returns
    title_case_sentence: string
    converted to title case
    '''
    if not isinstance(sentence, str):
        raise TypeError("Invalid input %s - Input for must be type string")
    if sentence == "":
        raise ValueError("Your string should be non-empty")

    sent_list = sentence.split()
    newsent_list = []
    for string in sent_list:
        newstring = string[0].upper()+string[1:].lower()
        newsent_list.append(newstring)
    title_case_sentence = " ".join(newsent_list)
    return title_case_sentence
