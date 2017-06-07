								#GIT DISTRIBUTED CONTROL SYSTEM##
#############################################
Author = "Gilad Amar"						#
Email = "giladamar@gmail.com"				#
Created = "19/05/2016"						#
Last_Modified  =  "18/07/2016"				#
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
''' GIT STRUCTURE #TODO Improve representation
											
											

		# 	 git push origin branch_name*		  
		# 								.  .	   
		# 								.    .
		# 								.      .
		# 								.		 .  
		# update master branch from origin*		   * commit changes
		# 								.		   .
		# 								.		   .													   .
		# 								.		   .											
		# 								.		   .													   .
		# 								.		   .
		# 								*		   * new_branch
		# 								.       .
		# 								.     .
		# 								.   .  
		# 								. .
		# 					new commit	*
		# 								.
		# 								.
		# 								.
		# 								.
		# 								*
		# 								master
'''
# HELP COMMANDS
git help
git help <command>


# CHANGE CONFIGURATION SETTINGS
git config --global user.name "Gilad Amar" 				# Change user name
git config --global user.email "giladamar@gmail.com"	# Change user email
git config --global color.ui auto						# Use fancy UI colours
git config --global <cmd to open def editor>
git config --global push.default upstream
git config --global merge.conflictstyle diff3

git config --global core.autocrlf true
# Configure Git on Windows to properly handle line endings
    # Save these in ~
    https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash
    https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh
    https://www.udacity.com/api/nodes/3341718587/supplemental_media/bash-profile-course/download?_ga=1.37232743.672083044.1467344711 -> .bashrc

# SET UP LOCAL REPOSITORY
git init  			# Execute from within the directory


# START WATCHING A FILE FOR CHANGES
git add --all 		# Adds everything in directory
		*.txt 		# Adds all local txt files
		a.txt b.txt # Adds list of files
		docs/		# Adds all files within directory
		"*.txt" 	# Add all txt files within entire project


# SEE THE CURRENT STATUS
git status 			# See what has changed since last commit


# SAVE SNAPSHOT
git commit -m "commit description" # Use present tense


# SEE GIT COMMIT HISTORY
git log 
--stat 
--graph
--oneline

# SEE CHNAGES IN FILE SINCE LAST COMMIT
git diff <filename>                 # compare working dir file to staging are
git diff --staged                   # compare staged to most recent commit
git diff <commit_id1> <commit_id2>


# SHOW WHICH BRANCH IS THE CURRENT HEAD
git show HEAD


# REVERT CHANGES BY 
git checkout HEAD <file name> 		# Go back to file state at last commit 
git checkout <commit_id>
git reset HEAD <filename>			# Go back to file state at last commit 
			<1st 7 letters of SHA> 	# Restore entire state of last commit
git reset <filename>

*--hard


# BRANCHING
git branch 											# See what the current branch is
git branch <new branch name>						# Create a new branch
git checkout <branch name>							# Move to this branch
<run on recipient branch> git merge <changed branch># Merge changes together
													# May need to resolve conflicts
git branch -d <branch name>							# Destroy branch 


# REMOTE REPOSITORIES
git clone remote_location <clone_name>	# Download origin project
git remote -v							# See all remote projects
git fetch								# Update local origin branch from remote origin
git merge origin/master					# Merge local origin with master branch
git push origin <your_branch_name>		# Push up changes to remote origin for review

*So if you have branch1 checked out, and you run git merge branch2 branch3, the merged version will combine branch1 as well as branch2 and branch3.
git merge --abort # revers to state before the merge