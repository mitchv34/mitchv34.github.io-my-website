import marimo

__generated_with = "0.12.5"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import numpy as np
    import pandas as pd
    return mo, np, pd


@app.cell
def __(mo):
    mo.md(
        r"""
        # Economics Interactive Demo
        
        A simple demonstration of interactive economics concepts using marimo.
        """
    )
    return


@app.cell
def __(mo):
    mo.md(r"""## Supply and Demand Model""")
    return


@app.cell
def __(mo):
    # Create interactive sliders
    demand_slope = mo.ui.slider(
        start=-2, 
        stop=-0.5, 
        step=0.1, 
        value=-1.5,
        label="Demand Slope"
    )
    
    supply_slope = mo.ui.slider(
        start=0.5,
        stop=2,
        step=0.1,
        value=1.0,
        label="Supply Slope"
    )
    
    demand_intercept = mo.ui.slider(
        start=5,
        stop=20,
        step=1,
        value=10,
        label="Demand Intercept"
    )
    
    mo.hstack([demand_slope, supply_slope, demand_intercept])
    return demand_intercept, demand_slope, supply_slope


@app.cell
def __(demand_intercept, demand_slope, np, supply_slope):
    # Calculate equilibrium
    quantity = np.linspace(0, 10, 100)
    
    # Demand: P = intercept + slope * Q
    demand_price = demand_intercept.value + demand_slope.value * quantity
    
    # Supply: P = slope * Q
    supply_price = supply_slope.value * quantity
    
    # Find equilibrium
    eq_quantity = demand_intercept.value / (supply_slope.value - demand_slope.value)
    eq_price = supply_slope.value * eq_quantity
    return demand_price, eq_price, eq_quantity, quantity, supply_price


@app.cell
def __(eq_price, eq_quantity, mo):
    mo.md(
        f"""
        ### Equilibrium Point
        
        - **Equilibrium Quantity**: {eq_quantity:.2f}
        - **Equilibrium Price**: {eq_price:.2f}
        """
    )
    return


@app.cell
def __(demand_price, eq_price, eq_quantity, mo, quantity, supply_price):
    import altair as alt
    
    # Create DataFrame for plotting
    df = pd.DataFrame({
        'Quantity': list(quantity) + list(quantity),
        'Price': list(demand_price) + list(supply_price),
        'Curve': ['Demand'] * len(quantity) + ['Supply'] * len(quantity)
    })
    
    # Create the plot
    base = alt.Chart(df).mark_line().encode(
        x=alt.X('Quantity:Q', scale=alt.Scale(domain=[0, 10])),
        y=alt.Y('Price:Q', scale=alt.Scale(domain=[0, 20])),
        color='Curve:N'
    ).properties(
        width=600,
        height=400,
        title='Supply and Demand'
    )
    
    # Add equilibrium point
    eq_point = alt.Chart(pd.DataFrame({
        'Quantity': [eq_quantity],
        'Price': [eq_price]
    })).mark_point(size=100, filled=True, color='red').encode(
        x='Quantity:Q',
        y='Price:Q'
    )
    
    chart = base + eq_point
    mo.ui.altair_chart(chart)
    return alt, base, chart, df, eq_point, pd


@app.cell
def __(mo):
    mo.md(
        r"""
        ## Elasticity Calculator
        
        Calculate price elasticity of demand given two price-quantity points.
        """
    )
    return


@app.cell
def __(mo):
    p1 = mo.ui.number(start=1, stop=100, value=10, label="Initial Price")
    q1 = mo.ui.number(start=1, stop=1000, value=100, label="Initial Quantity")
    p2 = mo.ui.number(start=1, stop=100, value=12, label="New Price")
    q2 = mo.ui.number(start=1, stop=1000, value=80, label="New Quantity")
    
    mo.hstack([
        mo.vstack([p1, q1]),
        mo.vstack([p2, q2])
    ])
    return p1, p2, q1, q2


@app.cell
def __(mo, p1, p2, q1, q2):
    # Calculate elasticity
    percent_change_q = ((q2.value - q1.value) / q1.value) * 100
    percent_change_p = ((p2.value - p1.value) / p1.value) * 100
    
    if percent_change_p != 0:
        elasticity = percent_change_q / percent_change_p
        
        if abs(elasticity) > 1:
            interpretation = "Elastic (|E| > 1) - Demand is responsive to price changes"
        elif abs(elasticity) == 1:
            interpretation = "Unit Elastic (|E| = 1)"
        else:
            interpretation = "Inelastic (|E| < 1) - Demand is not very responsive to price changes"
    else:
        elasticity = "Undefined (no price change)"
        interpretation = ""
    
    mo.md(
        f"""
        ### Results
        
        - **Percent Change in Quantity**: {percent_change_q:.2f}%
        - **Percent Change in Price**: {percent_change_p:.2f}%
        - **Price Elasticity of Demand**: {elasticity if isinstance(elasticity, str) else f'{elasticity:.2f}'}
        
        {interpretation}
        """
    )
    return elasticity, interpretation, percent_change_p, percent_change_q


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()
