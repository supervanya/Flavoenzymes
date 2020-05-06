USE_CACHING = True
FILE_LOGGING_ENABLED = True

SCRAPE_OUTPUT_PATH = "export/scraped_flavoenzymes.json"

# less_verbose <---- 'none' | 'success' | 'error' | 'warning' | 'info' | 'debug' | 'silly' ----> more_verbose
VERBOSITY = (
    "info"  # set to 'none' to have almost no output, set to 'silly' for most verbosity
)

KEYWORDS = [
    "FAD",
    "FMN",
    "flavin",
    "flavoenzyme",
    "flavo enzyme",
    "flavo",
    "flavoprotein",
    "flavo protein",
]
