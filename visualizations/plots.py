import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def plot_top_emitters(df, top_n=10):
    """
    Plot a bar chart and pie chart showing the top N countries by total CO₂ emissions.

    Parameters:
        df (pd.DataFrame): Cleaned emissions data.
        top_n (int): Number of top countries to display (default is 10).

    Returns:
        None. Displays plots inline.
    """
    # Group by country and calculate total emissions
    grouped = df.groupby('Country').sum(numeric_only=True).sort_values(by='Total', ascending=False)
    countries = grouped.index[:top_n]
    values = grouped['Total'].values[:top_n]

    # Create DataFrame for Seaborn barplot
    bar_df = pd.DataFrame({
        "Country": countries,
        "Emissions": values
    })

    # Bar plot
    plt.figure(figsize=(12, 5))
    sns.barplot(
        data=bar_df,
        x="Country",
        y="Emissions",
        hue="Country",           # Needed for future Seaborn compatibility
        palette="Set2",
        edgecolor=".2",
        legend=False
    )
    plt.xticks(rotation=45)
    plt.title(f"Top {top_n} Emitting Countries")
    plt.ylabel("Total Emissions (MtCO₂)")
    plt.tight_layout()
    plt.show()

    # Pie chart
    px.pie(
        names=countries,
        values=values,
        title=f"Top {top_n} Emitting Countries (Pie Chart)",
        width=600,
        height=400
    ).show()


def plot_usa_trends(df, years=10):
    """
    Plot USA total CO₂ emissions over the last N years using a line and bar chart.

    Parameters:
        df (pd.DataFrame): Cleaned emissions data.
        years (int): Number of recent years to include.

    Returns:
        None. Displays plots inline.
    """
    # ✅ Filter by ISO code to ensure reliable matching
    usa_df = df[df['ISO 3166-1 alpha-3'] == 'USA'].tail(years)

    plt.figure(figsize=(12, 5))

    # Line chart
    plt.subplot(1, 2, 1)
    sns.lineplot(x='Year', y='Total', data=usa_df)
    plt.title('USA Total Emissions (Line)')
    plt.xlabel('Year')
    plt.ylabel('Emissions (MtCO₂)')

    # Bar chart
    plt.subplot(1, 2, 2)
    sns.barplot(
        x='Year',
        y='Total',
        hue='Year',             # Needed to safely use palette
        data=usa_df,
        palette='Set3',
        edgecolor='.3',
        legend=False
    )
    plt.title('USA Total Emissions (Bar)')
    plt.xlabel('Year')
    plt.ylabel('Emissions (MtCO₂)')

    plt.tight_layout()
    plt.show()


def plot_emission_types(df, years=10):
    """
    Plot sector-wise USA emissions over the last N years as an interactive line chart.

    Parameters:
        df (pd.DataFrame): Cleaned emissions data.
        years (int): Number of recent years to include.

    Returns:
        None. Displays Plotly line chart.
    """
    # Define emission types to plot
    columns = ['Coal', 'Oil', 'Gas', 'Cement', 'Flaring', 'Other']

    # ✅ Filter by ISO code for consistency
    usa_df = df[df['ISO 3166-1 alpha-3'] == 'USA'].tail(years)

    # Create base figure with total emissions
    fig = px.line(
        x=usa_df['Year'],
        y=usa_df['Total'],
        labels={'x': 'Year', 'y': 'Total'},
        title='USA Emission Breakdown by Sector'
    )

    # Add sector lines
    for col in columns:
        fig.add_scatter(x=usa_df['Year'], y=usa_df[col], name=col)

    fig.show()
