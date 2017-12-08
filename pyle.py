####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Pyle'
strategy_name = 'Copy Cat'
strategy_description = 'Collude on first round and then copy their previous move.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    # Collude on first round and then copy their previous move.
    my_move = 'c'
    if len(their_history) > 0:
        my_move = their_history[-1]
    if len(their_history) > 2:
        if their_history[-3:-1].count('b') > 1:
            my_move = 'b'
    return my_move