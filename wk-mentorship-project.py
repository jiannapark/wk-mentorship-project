'''
1. Assign numbers to everyone in dictionaries (not shown here). 24 people in mentors_names dict were assigned to integer-keys from 1 to 24, and 49 people in mentees_names dict were assigned to integer-keys from 1 to 49.
2. Choose 1 random number from mentors list. If it hasn't been chosen before, that number is added to mentors_chosen list.
3. Choose 1 random number from mentees list. If it hasn't been chosen before, that number is added to mentees1_chosen list.
4. Choose 1 random number from mentees list. If it hasn't been chosen before, that number is added to mentees2_chosen list.
5. The mentors will be paired with the mentees from both mentees lists with the same index-position as their own.
(ex. the 7th person in mentors_chosen list will mentor the 7th person in mentees1_chosen list and the 7th person in mentees2_chosen list.)
'''


import random

mentors = list(range(1, 25))
mentees = list(range(1, 50))

def mentor_until_new():
    mentor = random.choice(mentors)
    if mentor not in mentors_chosen:
        mentors_chosen.append(mentor)
    else:
        mentor_until_new()

def mentee1_until_new():
    mentee1 = random.choice(mentees)
    if mentee1 not in mentees1_chosen and mentee1 not in mentees2_chosen:
        mentees1_chosen.append(mentee1)
    else:
        mentee1_until_new()

def mentee2_until_new():
    mentee2 = random.choice(mentees)
    if mentee2 not in mentees1_chosen and mentee2 not in mentees2_chosen:
        mentees2_chosen.append(mentee2)
    else:
        mentee2_until_new()

mentors_chosen = []
mentees1_chosen = []
mentees2_chosen = []

def random_pairing():

    for i in range(24):
        mentor_until_new()
        mentee1_until_new() 
        mentee2_until_new()

    left = [x for x in mentees if x not in mentees1_chosen and x not in mentees2_chosen]

    mentees_chosen = []
    for j in range(24):
        two_mentees = [mentees1_chosen[j], mentees2_chosen[j]]
        mentees_chosen.append(two_mentees)
    pairs = dict(zip(mentors_chosen, mentees_chosen))
    # then manually add last person to anyone of the 24 mentors who have not had 3 mentees before

    return pairs, left

pairs, last = random_pairing()


'''
6. Finally, replace numbers with actual names using dictionaries.
'''

import pandas as pd

keys = list(pairs.keys())
values = list(pairs.values())

pair_mentors = pd.DataFrame(keys, columns=['Mentor'])
pair_mentors = pair_mentors.replace(mentors_names)

pair_mentees = pd.DataFrame(values, columns=['Mentee1', 'Mentee2'])
pair_mentees = pair_mentees.replace(mentees_names)

result_pairs = pair_mentors.join(pair_mentees)
