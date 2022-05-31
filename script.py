from git import Repo
from os import path

print('\nWelcome to the commit-push-bot!')
print('This project was made by Fernando Alzueta for the purpose of learning git')
print('\nMake sure your project folder is inside the same folder as this script!')
print('\n------------------------------------------------------------------------------------------------------------------\n')

def git_push(x):
    i = 0
    while i < x:
        try:
            repo = Repo(PATH_OF_GIT_REPO)
            repo.git.add(update=True)
            repo.index.commit(COMMIT_MESSAGE)
            origin = repo.remote(name='origin')
            origin.push()
        except:
            print('Some error occured while pushing the code')    
        i += 1
        print('\nCommit {} pushed'.format(i))

project = input('Enter the project name: ')
PATH_OF_GIT_REPO = path.join(path.dirname(__file__), project)  # make sure the script is in the same folder as the project

message = input('Enter the commit message: ')
COMMIT_MESSAGE = message

push = int(input('Enter the number of times you want to push: '))
print('\nPushing...')
git_push(push)
print('\nDone!')