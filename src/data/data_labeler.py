import pandas as pd
import pickle


print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

print('Starting data labelling...')

with open('cache/data_labeler_vars.pickle', 'rb') as f:
    lastIndex, datajobs  = pickle.load(f)

print('Starting from index: ' + str(lastIndex))

for i in range(lastIndex, datajobs.shape[0]):
    print('\n\n\n\n\n\n\n')
    print('Current Index: ' + str(i))
    print("JOB TITLE: " + datajobs.loc[i, "job_title"])
    print("JOB DESCRIPTION:")
    print(*datajobs.loc[i, "job_description"].split('.'), sep='\n')
    print('Entry level job? (Y/n) \n Type Q to quit.')
    while True:
        response = input()
        if response == 'Y':
            #Save response as 1
            datajobs.loc[i, "entry_level_q"] = 1
            print('Response saved as yes.')
            break
        elif response == 'n':
            #Save response as 0
            datajobs.loc[i, "entry_level_q"] = 0
            print('Response saved as no.')
            break
        elif response == 'Q':
            print('Quiting...')
            break
        else:
            print('Input not recognized. Please enter either Y for yes, n for no, or Q to quit.')
    if response == 'Q':
        break
    lastIndex += 1

#Save updated lastIndex
with open('cache/data_labeler_vars.pickle', 'wb') as f:
    pickle.dump((lastIndex, datajobs), f)
