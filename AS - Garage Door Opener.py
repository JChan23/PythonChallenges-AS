#Inputs: button_clicked OR cycle_complete
#States: CLOSED, OPEN, OPENING, CLOSING, STOPPED_WHILE_OPENING, STOPPED_WHILE_CLOSING
a = False
state = 'CLOSED'
print('Door: CLOSED')

while a == False:
    print('\nDid you click the button or is the cycle complete?')
    action = input("Please enter either 'button clicked' or 'cycle complete': ")
    if action == 'button clicked' and state == 'CLOSED':
        state = 'OPENING'
        print('Door: OPENING')
    elif action == 'button clicked' and state == 'OPEN':
        state = 'CLOSING'
        print('Door: CLOSING')
    elif action == 'button clicked' and state == 'OPENING':
        state = 'STOPPED_WHILE_OPENING'
        print('Door: STOPPED_WHILE_OPENING')
    elif action == 'button clicked' and state == 'CLOSING':
        state = 'STOPPED_WHILE_CLOSING'
        print('Door: STOPPED_WHILE_CLOSING')
    elif action == 'button clicked' and state == 'STOPPED_WHILE_OPENING':
        state = 'CLOSING'
        print('Door: CLOSING')
    elif action == 'button clicked' and state == 'STOPPED_WHILE_CLOSING':
        state = 'OPENING'
        print('Door: OPENING')
    elif action == 'cycle complete' and state == 'OPENING':
        state = 'OPEN'
        print('Door: OPEN')
    elif action == 'cycle complete' and state == 'CLOSING':
        state = 'CLOSED'
        print('Door: CLOSED')
    else:
        print('Error. Please try again')


