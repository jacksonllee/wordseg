# Contributing

Thank you for your interest in contributing to the `wordseg` codebase!

## Setting up a Local Development Environment

To work on this codebase, you can obtain the source code through GitHub and `git`:

1.  Create a fork of the `wordseg` repo on your GitHub account.

2.  Locally, make sure you are in some sort of a virtual environment (venv,
    virtualenv, conda, etc).

3.  Download and install the library in the "editable" mode together with the
    core and dev dependencies within the virtual environment:

    ```bash
    git clone https://github.com/<your-github-username>/wordseg.git
    cd wordseg
    pip install --upgrade pip setuptools
    pip install -e ".[dev]"
    ```

## Working on a Feature or Bug Fix

The development steps below assume that your local Git repo has a remote
`upstream` link to `jacksonllee/wordseg`:
   
```bash
git remote add upstream https://github.com/jacksonllee/wordseg.git
```

After this step (which you only have to do once),
running `git remote -v` should show your local Git repo
has links to both "origin"
(pointing to your fork `<your-github-username>/wordseg`)
and "upstream" (pointing to `jacksonllee/wordseg`).

To work on a feature or bug fix, here are the development steps: 

1. Before doing any work, check out the `main` branch and
   make sure that your local `main` branch is up-to-date with upstream `main`:
   
   ```bash
   git checkout main
   git pull upstream main
   ``` 
   
2. Create a new branch.
   This branch is where you will make commits of your work.
   (As a best practice, never make commits while on a `main` branch.
   Running `git branch` tells you which branch you are on.)
   
   ```bash
   git checkout -b new-branch-name
   ```
   
3. Make as many commits as needed for your work.
4. When you feel your work is ready for a pull request,
   push your branch to your fork.

   ```bash
   git push origin new-branch-name
   ```
5. Go to your fork `https://github.com/<your-github-username>/wordseg` and
   create a pull request off of your branch against the `jacksonllee/wordseg`
   repo.

6. Add an entry to
   [CHANGELOG.md](https://github.com/jacksonllee/wordseg/blob/main/CHANGELOG.md),
   commit this change, and push this commit to your branch.

## Running Tests and Style Checks

The `wordseg` repo has continuous integration (CI) turned on,
with autobuilds running flake8 and black (for styling consistency)
as well as pytest (for the test suite);
the tests are in the [`tests/`](tests) directory.
If an autobuild at an open pull request fails due to any of pytest, flake8,
or black, 
then the pull request' author should fix the errors
with further commits pushed to the branch.

If you would like to help avoid wasting free Internet resources
(every push triggers a new CI autobuild),
you can run the following checks locally before pushing commits:

```bash
flake8 src tests
black --check src tests
pytest
```

For errors related to black, run
`black src tests` (without the `--check` flag)
to update the code.
