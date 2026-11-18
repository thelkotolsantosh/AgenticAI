# Frequently asked questions

### 1. Which fields are required?

`vendor`, `invoice`, and `amount`.

### 2. How are duplicates grouped?

By vendor and invoice number after trimming and case folding.

### 3. Which amounts are flagged?

Unreadable, nonfinite, zero, and negative amounts.

### 4. Does the assistant approve payments?

It produces a review queue. A person decides what to do.

### 5. Does it need a model or API key?

The workflow uses local rules.

### 6. Which file starts the program?

`app.py` is the command-line entry point.

### 7. Which Python version should I use?

Use Python 3.8 or newer.

### 8. Do I need to install packages?

The program uses the Python standard library.

### 9. Why include requirements.txt?

It records that the project has no third-party runtime dependencies.

### 10. How do I check my Python version?

Run `python --version`.

### 11. Can I run it on Windows?

Use `py` in place of `python` if the Windows launcher is installed. Shell quoting can vary.

### 12. Where should I run the example?

Open a terminal in the folder containing `app.py`.

### 13. How do I see the command options?

Run `python app.py --help`.

### 14. What is a first command to try?

`python app.py invoices.csv`.

### 15. Where can I find the walkthrough?

The README contains a runnable example.

### 16. Which sample files are included?

`invoices.csv`.

### 17. What if a path contains spaces?

Enclose the path in quotes.

### 18. Do I need an internet connection?

Once the files and Python are installed, the command runs locally.

### 19. How do I run the tests?

Run `python -m unittest -v` from the repository folder.

### 20. Which file describes the test cases?

Open `test_app.py`.

### 21. How are the tests run?

They invoke the actual CLI in a subprocess and inspect its output and exit status.

### 22. Where do tests put temporary files?

They run in a temporary directory that is removed afterward.

### 23. Can I inspect the input used in a test?

Each case in `test_app.py` lists its arguments and expected result.

### 24. How do I see an error from an automated run?

Capture standard error alongside the process exit code.

### 25. Where can I change the behavior?

Edit `app.py`, then run the tests and add a case for the new behavior.
