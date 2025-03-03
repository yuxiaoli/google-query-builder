# Google Search Query Builder

Google Search Query Builder is a Python command-line tool that generates a Google search query string with various filters. It supports adding standard Google search operators as well as optional Ahrefs filters. Additionally, it can translate the main search query into English if it is in a different language using the [deep-translator](https://pypi.org/project/deep-translator/) library.

## Features

- **Positional Search Query:**  
  Provide your main search query as a required positional argument.

- **Google Search Operators:**  
  Easily append common search operators:
  - `site:` (restrict to a specific website)
  - `filetype:` (filter by file type)
  - `intitle:` (restrict words in the page title)
  - `inurl:` (filter by words in the URL)
  - `related:` (find related websites)
  - `allintitle:` (ensure all specified words appear in the title)
  - Wildcard `_` placeholder
  - Exclusion (`-` operator)
  - Date range filters (`after:` and `before:`)

- **Optional Ahrefs Filters:**  
  Append additional filters such as Domain Rating (DR), Traffic, Unique Domain, and Publication Frequency.

- **Translation:**  
  Use the `--translate` flag to automatically translate your query into English if it's in another language.

## Requirements

- Python 3.x
- [deep-translator](https://pypi.org/project/deep-translator/)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/google-search-query-builder.git
   cd google-search-query-builder
   ```

2. **Install the required dependency:**

   ```bash
   pip install deep-translator
   ```

## Usage

Run the script using Python with the required positional query argument and any additional options.

### Basic Example

```bash
python script.py "python argparse"
```

This will output:

```
python argparse
```

### With Translation and a Filter

For example, to translate a non-English query and add a site filter:

```bash
python script.py "résultats de recherche" --translate --site "example.com"
```

This command will translate `"résultats de recherche"` into English (e.g., `"search results"`) and output a query similar to:

```
search results site:example.com
```

### Available Options

- **Positional Argument:**
  - `query`  
    The main search query text.

- **Optional Arguments:**
  - `--translate`  
    Translate the query into English if it is not already.
  - `--site`  
    Restrict results to a specific website (e.g., `moz.com`).
  - `--filetype`  
    Filter results by file type (e.g., `pdf`).
  - `--intitle`  
    Restrict results to pages that contain specific words in the title.
  - `--inurl`  
    Filter results to pages with certain words in the URL.
  - `--related`  
    Find websites that are similar or related to a given domain.
  - `--allintitle`  
    Ensure all specified words appear in the page title.
  - `--wildcard`  
    Include a wildcard placeholder `_` in the query.
  - `--exclude`  
    Exclude results containing a specific term (can be used multiple times).
  - `--after`  
    Filter results published after a specific date (YYYY-MM-DD).
  - `--before`  
    Filter results published before a specific date (YYYY-MM-DD).
  - `--dr`  
    Domain Rating filter (e.g., `30` for "DR > 30").
  - `--traffic`  
    Traffic filter (e.g., `"5K"` for ">= 5K visits/month").
  - `--unique`  
    Limit results to one page per domain.
  - `--once`  
    Filter pages that were published only once.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## Contact

For questions or feedback, please open an issue in the GitHub repository.
