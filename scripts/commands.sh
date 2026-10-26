# Command reference only. Copy and run individual examples; do not execute/source this file.
# Run shell examples from the project root in Bash. Replace YOUR_* paths with your own.
# Prerequisites: Poetry and Python >=3.11,<4.0 (not the README's unspecified Python 3.x).
# Install the package and locked deep-translator dependency.
poetry install

# Display all options; the source entry point is google.py, not README's placeholder script.py.
poetry run python -m google_query_builder.google --help

# Generate a plain query on stdout; this does not perform a Google search.
poetry run python -m google_query_builder.google "python argparse"

# Combine domain, file type, title, URL, exclusions, and a bounded publication-date range.
poetry run python -m google_query_builder.google "climate research" --site "example.com" --filetype pdf --intitle "annual report" --inurl reports --exclude jobs --exclude advertising --after 2025-01-01 --before 2026-01-01

# Alternative: append related-domain and all-title operators plus the implemented underscore wildcard.
# The program only assembles text; it does not validate search-engine operator support.
poetry run python -m google_query_builder.google "renewable energy" --related "example.com" --allintitle "renewable energy" --wildcard

# Append informational Ahrefs annotations; these are NOT API calls or enforced Google filters.
poetry run python -m google_query_builder.google "public research" --dr 30 --traffic 5K --unique --once

# Translate only the main query to English, then append filters.
# NETWORK/PRIVACY: sends query text to Google's translation service; never use confidential text.
# On translation failure an error is printed and generation continues using the original query.
poetry run python -m google_query_builder.google "résultats de recherche" --translate --site "example.com"

# Save stdout using shell redirection (not a CLI output flag); parent must exist, file is overwritten.
# Prefer no --translate here if you need query-only output without translation-error messages.
poetry run python -m google_query_builder.google "python argparse" --site "docs.python.org" > "YOUR_OUTPUT/query.txt"

# No console-script entry point, nonempty tests, lint, deployment, or publishing workflow is defined.
