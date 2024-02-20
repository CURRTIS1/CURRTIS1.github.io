# Syncing Github repository to Bitbucket

## Bitbucket

Log into your Bitbucket account, go to your chosen Repository.

Under `Security` choose `Access Tokens` and `Create Repository Access Token`.

Set a `Name` and allow the permissions:

- Repositories:Read
- Repositories:Write

Copy your x-token-auth URL it should look like:

`git clone https://x-token-auth:abcdefghijklmnopqrstuvwxyz1234567890@bitbucket.org/workspace/repository.git`

## Github

Log into your Github account, go to your chosen Repository.

Under `Settings` choose `Settings`, under `Security` and `Secrets and Variables` choose `Actions`.

Create a `New Repository Secret` named `AUTH_TOKEN`.

## Github Actions

Then in your repository add the following to your workflow file located in `.github/workflows`.

```YAML
bitbucket_mirror:
    name: Mirror to Bitbucket
    runs-on: ubuntu-latest
    steps:
      - name: Checkout the repository to the runner
        uses: actions/checkout@v4
        with:
          fetch-depth: 'true'
      - name: Checkout repo
        run: git push --mirror https://x-token-auth:${{ secrets.AUTH_TOKEN }}@bitbucket.org/workspace/repository.git
```
