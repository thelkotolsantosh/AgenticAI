# Invoice review assistant

The assistant applies fixed rules to each invoice and prints a review queue. It groups duplicate invoice numbers by vendor and flags missing identifiers and invalid or nonpositive amounts. All decisions stay with the reviewer.

## Run locally

Use Python 3.8 or newer. Run these commands in the project directory.

```sh
python app.py invoices.csv
```

Run `python app.py --help` for options and `python -m unittest -v` to check the command-line workflow.
