# Info

Run `translate.py` before each release.

Before running for the first time, you need to run:

Use Python 3.12.0 for stability

```pwsh
# Instructions are different for *nix
# Create and Activate the virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# Get dependencies
python -m pip install -r requirements.txt

# Initialize required language models
libretranslate --load-only es,en,zh --update-models                             

# Run translate.py
```

Edit corresponding json cache file so that the next time translation runs the
translation service uses the translation from cache over a potentially incorrect
translation.

## TODO

- Add more languages?

## TODO
- [ ] Split file into modules
- [ ] Continue refactor 
