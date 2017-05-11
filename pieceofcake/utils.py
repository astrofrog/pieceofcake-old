import click


def click_prompt_multiple_choice(question, choices, default=0):

    full_question = question
    for ichoice, choice in enumerate(choices):
        full_question += '\n   {0} - {1}'.format(ichoice + 1, choice)
    full_question += '\n'

    result = click.prompt(full_question, type=click.IntRange(1, len(choices)), default=default + 1)

    return choices[result - 1]
