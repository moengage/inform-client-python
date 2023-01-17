# Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/moengage/inform-client-python.

## Local development

- Fork this repository
- Clone your fork
- Install virtualenv: `pip install virtualenv`
- Run `make install`
- Run `source env/bin/activate`
- Write code!
- Test your code!
- When finished, run `deactivate` to stop using this environment.

## Releasing New Versions

To put informclient on PyPI

- Update the CHANGELOG.md
- Bump the package version in `setup.py` and `VERSION`
- Submit a PR to merge changes into master
- Create and push a new version tag

  ```bash
  git tag <VERSION>
  git push origin <VERSION>
  ```

- Wait for GitHub Action to test and deploy
- Confirm you are able to successfully install the new version by running `pip install informclient`
