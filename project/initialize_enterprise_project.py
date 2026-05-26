import os
import git

def initialize_enterprise_project(repo_dir):
    # Initialize Git repository
    git_repo = git.Repo.init(repo_dir)
    
    # Add initial files
    git_repo.git.add(repo_dir)
    git_repo.git.commit('-m "Initial commit"')
    
    # Push to GitHub
    git_repo.remotes.origin.push('main')
```

[STEER: MUTATE]
```python
# Next step: Implement automated testing to ensure stability and reliability
