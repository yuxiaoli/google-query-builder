#!/usr/bin/env python3
import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Generate a Google search query string with various filters."
    )
    # Positional argument for the main search query
    parser.add_argument('query', help='The main search query text')
    
    # Flag to translate the query to English if it is in another language
    parser.add_argument('--translate', action='store_true',
                        help='Translate the query into English if not already in English')
    
    # Google Search operators
    parser.add_argument('--site', help='Restrict results to a specific website (e.g., moz.com)')
    parser.add_argument('--filetype', help='Filter results by file type (e.g., pdf)')
    parser.add_argument('--intitle', help='Restrict results to pages that contain specific words in the title')
    parser.add_argument('--inurl', help='Filter results to pages with certain words in the URL')
    parser.add_argument('--related', help='Find websites that are similar or related to a given domain')
    parser.add_argument('--allintitle', help='Ensure all specified words appear in the page title')
    parser.add_argument('--wildcard', action='store_true', help='Include a wildcard placeholder "_" in the query')
    parser.add_argument('--exclude', action='append', help='Exclude results containing a specific term (can be used multiple times)')
    parser.add_argument('--after', help='Filter results published after a specific date (YYYY-MM-DD)')
    parser.add_argument('--before', help='Filter results published before a specific date (YYYY-MM-DD)')
    
    # Optional Ahrefs filters (for informational purposes)
    parser.add_argument('--dr', help='Domain Rating filter (e.g., 30 for "DR > 30")')
    parser.add_argument('--traffic', help='Traffic filter (e.g., "5K" for ">= 5K visits/month")')
    parser.add_argument('--unique', action='store_true', help='Limit results to one page per domain (Unique Domain Filter)')
    parser.add_argument('--once', action='store_true', help='Filter pages that were published only once (Publication Frequency Filter)')
    
    args = parser.parse_args()

    # If translation is requested, attempt to translate the query to English using deep-translator.
    if args.translate:
        try:
            from deep_translator import GoogleTranslator
            translated = GoogleTranslator(source='auto', target='en').translate(args.query)
            args.query = translated
        except Exception as e:
            print(f"Translation error: {e}")
            # Continue with the original query if translation fails

    query_parts = []

    # Add the main search query (translated if applicable)
    query_parts.append(args.query)

    # Append the Google search parameters
    if args.site:
        query_parts.append(f"site:{args.site}")
    if args.filetype:
        query_parts.append(f"filetype:{args.filetype}")
    if args.intitle:
        query_parts.append(f'intitle:"{args.intitle}"')
    if args.inurl:
        query_parts.append(f"inurl:{args.inurl}")
    if args.related:
        query_parts.append(f"related:{args.related}")
    if args.allintitle:
        query_parts.append(f"allintitle:{args.allintitle}")
    if args.wildcard:
        query_parts.append("_")
    if args.exclude:
        for term in args.exclude:
            query_parts.append(f"-{term}")
    if args.after:
        query_parts.append(f"after:{args.after}")
    if args.before:
        query_parts.append(f"before:{args.before}")
    
    # Append optional Ahrefs filters (for informational purposes)
    if args.dr:
        query_parts.append(f"DR > {args.dr}")
    if args.traffic:
        query_parts.append(f">= {args.traffic} visits/month")
    if args.unique:
        query_parts.append("(one page per domain)")
    if args.once:
        query_parts.append("(Pages published once)")

    # Combine all parts into a single query string and output it
    query_string = " ".join(query_parts)
    print(query_string)

if __name__ == "__main__":
    main()
