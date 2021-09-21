import argparse

parser = argparse.ArgumentParser(prog='SpaCy features')
parser.add_argument('feature', type=int, choices={0, 1, 2, 3, 4}, help='Selecting the function to execute. '
                                                                       '0 - Displaying information about tokens, '
                                                                       '1 - Vector representation of text tokens, '
                                                                       '2 - Search for text by pattern, '
                                                                       '3 - Identifying the token and assigning the '
                                                                       'provided attributes to it, '
                                                                       '4 - Named Entity Recognition.')

cl_args = parser.parse_args()
