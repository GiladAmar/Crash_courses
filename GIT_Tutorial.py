                                #GIT DISTRIBUTED CONTROL SYSTEM##
#############################################
Author = "Gilad Amar"                        #
Email = "giladamar@gmail.com"                #
Created = "19/05/2016"                        #
Last_Modified  =  "18/07/2016"                #
#############################################
'''
    WELCOME TO THE GIT INTRODUCTORY CODE.
'''
''' Warning: the following pseudo-code will make you cry
     A safety pig has been provided for your benefit:
 _._ _..._ .-',     _.._(`))
'-. `     '  /-._.-'    ',/
   )         \            '.
  / _    _    |             \
 |  a    a    /              |
 \   .-.                     ;  
  '-('' ).-'       ,'       ;
     '-;           |      .'
        \           \    /
        | 7  .__  _.-\   \
        | |  |  ``/  /`  /
       /,_|  |   /,_/   /
          /,_/      '`-'
'''


    # Rebase your changes on top of the remote master
      git pull --rebase upstream master
    # Squash multiple commits into one for a cleaner git log
    # (on the following screen change the word pick to either 'f' or 's')
      git rebase -i $commit_ref


    # create a new branch
      git checkout -b $branchname
      git push origin $branchname --set-upstream

    # get a remote branch
      git fetch origin
      git checkout --track origin/$branchname

    # delete local remote-tracking branches (lol)
      git remote prune origin


    #git log:
        -n, --max-count=2
            --skip=2
            --since="1 week ago"
            --until="yesterday"
            --author="Rico"
            --committer="Rico"

    git ignore "*.log"
''' GIT STRUCTURE #TODO Improve representation
                                            
                                            

        #      git push origin branch_name*          
        #                                 .  .       
        #                                 .    .
        #                                 .      .
        #                                 .         .  
        # update master branch from origin*           * commit changes
        #                                 .           .
        #                                 .           .                                                       .
        #                                 .           .                                            
        #                                 .           .                                                       .
        #                                 .           .
        #                                 *           * new_branch
        #                                 .       .
        #                                 .     .
        #                                 .   .  
        #                                 . .
        #                     new commit    *
        #                                 .
        #                                 .
        #                                 .
        #                                 .
        #                                 *
        #                                 master
'''
# HELP COMMANDS
git help
git help <command>


# CHANGE CONFIGURATION SETTINGS
git config --global user.name "Gilad Amar"                 # Change user name
git config --global user.email "giladamar@gmail.com"    # Change user email
git config --global color.ui auto                        # Use fancy UI colours
git config --global <cmd to open def editor>
git config --global push.default upstream
git config --global merge.conflictstyle diff3

git config --global core.autocrlf true
git config --system core.longpaths true.

# Configure Git on Windows to properly handle line endings
    # Save these in ~
    https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash
    https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh
    https://www.udacity.com/api/nodes/3341718587/supplemental_media/bash-profile-course/download?_ga=1.37232743.672083044.1467344711 -> .bashrc

# SET UP LOCAL REPOSITORY
git init    # Execute from within the directory


# START WATCHING A FILE FOR CHANGES
git add --all       # Adds everything in directory
        *.txt       # Adds all local txt files
        a.txt b.txt # Adds list of files
        docs/       # Adds all files within directory
        *.txt       # Add all txt files within entire project
git ls-files
    --other
    --ignored
    --exclude-standard
.gitignore

git rm          # delete and stage deletion
git rm --cached # Remove from version control but DONT deletr
git mv          # Change file name and prep for commit

# Stashing
git stash       # Temporarily stores all modified tracked files
git stash pop   # Restores most recently stashed files
git stash list  # Lists all changed changesets
git stash drop  # Discards most recently stashed changeset

# SEE THE CURRENT STATUS
git status             # See what has changed since last commit


# SAVE SNAPSHOT
git commit -m "commit description" # Use present tense


# SEE GIT COMMIT HISTORY
git log 
    --stat 
    --graph
    --oneline
    -n <num_of_commits>


# SEE CHANGES IN FILE SINCE LAST COMMIT
git diff <filename>                 # Compare working dir file to staging are
git diff --staged                   # Compare staged to most recent commit
git diff <commit_id1> <commit_id2>
    --stat      #show files and num insets/deletes
    --summary   #only filenames


# SHOW WHICH BRANCH IS THE CURRENT HEAD
git show HEAD


# REVERT CHANGES BY 
git checkout HEAD <file name>       # Go back to file state at last commit 
git checkout <commit_id>
git checkout <commit_id> <filename> # Reset only that file to commit_id

git reset HEAD <filename>           # Go back to file state at last commit 
            <1st 7 letters of SHA>  # Restore entire state of last commit
git reset <filename>

*--hard <commit_id>


# BRANCHING
git branch                                              # See what the current branch is
git branch <new branch name>                            # Create a new branch

git checkout <branch name>                              # Move to this branch
<run on recipient branch> git merge <changed branch>    # Merge changes together
                                                        # May need to resolve conflicts
git branch -d <branch name>                             # Destroy branch 


# REMOTE REPOSITORIES
git clone remote_location <clone_name>  # Download origin project

*forking is cloning only on github

git remote -v                           # See all remote projects
git remote add <def_name: origin> <url>
git remote rm <name>                    # Remove remote repo

git fetch <remote name>                 # Update local origin branch from remote origin

git merge origin/master                 # Merge local origin with master branch
git merge --abort                       # revers to state before the merge
*So if you have branch1 checked out, and you run git merge branch2 branch3, the merged version will combine branch1 as well as branch2 and branch3.
        - resolve conflicts
        - then commit
git push  <remote name> <local branch_name> # Push up changes to remote origin for review

git pull  <remote> <branch>                 # downloads bookmark history and incorporates changes
* pull is just git fetch + git merge