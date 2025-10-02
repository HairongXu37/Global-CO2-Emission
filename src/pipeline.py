import pandas as pd

def load_emissions_data(path: str) -> pd.DataFrame:
    """
    Load and clean the emissions dataset from a CSV file.

    This function performs the following steps:
    - Loads the dataset from the specified CSV path.
    - Drops rows with missing ISO country codes (non-country entities).
    - Fills missing numerical values with 0.
    - Removes rows for 'Global' and 'International Transport', as they are not individual countries.

    Parameters:
        path (str): Path to the emissions CSV file.

    Returns:
        pd.DataFrame: A cleaned DataFrame ready for analysis.
    """
    # Load raw emissions data from CSV
    df = pd.read_csv(path)

    # Drop rows with missing ISO codes (typically non-country entries)
    df = df[~df['ISO 3166-1 alpha-3'].isna()]

    # Fill missing values in numeric columns with 0
    df = df.fillna(0)

    # Remove global aggregates that are not individual countries
    df = df[~df['Country'].isin(['Global', 'International Transport'])]

    return df


def extract_special_cases(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Extract special-case rows like 'World' and 'International Transport' for separate analysis.

    Parameters:
        df (pd.DataFrame): Cleaned emissions DataFrame.

    Returns:
        tuple:
            - world_data (pd.DataFrame): Rows with ISO code 'WLD' (world total).
            - transport_data (pd.DataFrame): Rows labeled as 'International Transport'.
    """
    # Extract rows for 'World' based on ISO code
    world_data = df[df['ISO 3166-1 alpha-3'] == 'WLD']

    # Extract rows for international transport by name
    transport_data = df[df['Country'] == 'International Transport']

    return world_data, transport_data
