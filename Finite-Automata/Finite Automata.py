

#Part for getting the states
states = input() #part for getting states
states1 = states.split(',')
states1[0] = states1[0].split('{')[1]
states1[-1] = states1[-1].split('}')[0]
start = states1[0]

alphabet = input() #part for getting alphabet
alphabet1 = alphabet.split(',')
alphabet1[0] = alphabet1[0].split('{')[1]
alphabet1[-1] = alphabet1[-1].split('}')[0]

final_states = input().split(',') #part for getting final states
if len(final_states)==1:
    a = final_states[0].split('{')[1]
    b = a.split('}')[0]
    final_states1 = b
else:
    final_states[0] = final_states[0].split('{')[1]
    final_states[-1] = final_states[-1].split('}')[0]
    final_states1 = final_states

automata = [] #part for getting the language
rules_count = int(input())
for i in range(rules_count):
    rule = input()
    rule1 = rule.split(',')
    automata.append(rule1)


language = input()
error = False
for i in range(len(language)):
    letter = language[i]
    check = False
    for k in range(rules_count):
        if (automata[k][0] == start and automata[k][1] == '$'):
            check = True
            start = automata[k][2]
    for j in range(rules_count):
        if(automata[j][0] == start and automata[j][1] == letter):
            check = True
            start = automata[j][2]
            break
    if(check == False):
        error = True
        break

if error == True:
    print("Rejected")
else:
    if start in final_states1:
        print("Accepted")
    else:
        print("Rejected")




#print(states1)
#print(alphabet1)
#print(final_states1)
#print(automata)