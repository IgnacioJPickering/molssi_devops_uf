"""
molssi_math.py
Some molssi stuff

Some math functions
"""

def mean(num_list):
    '''
    Takes the mean of a set of numbers

    Parameters
    -----------
    num_list : list
        The list to take the average of
    Returns
    ----------
    mean_list : float
        The mean of the list
    '''
    if not isinstance(num_list, list):
        raise TypeError("Input should be a list.")
    #looks like it is a good idea to check for empty lists by checking
    #if they are false (if they are empty then they are false)
    if not num_list:
        raise ValueError("List of numbers should be non-empty.")
    meanv = 0.
    tot_n = len(num_list)
    try:
        for j in range(tot_n):
            meanv += num_list[j]
    except TypeError:
        raise TypeError("Cannot calculate mean of list - all list elements must be numbers")
    meanv /= tot_n
    return meanv

def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format)

    Replace this function and doc string for your own project

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
