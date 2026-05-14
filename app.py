# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "marimo>=0.10",
#   "numpy>=2.0",
#   "scipy>=1.13",
#   "scikit-learn>=1.3",
#   "polars>=1.0",
#   "plotly>=5.0",
#   "altair>=5.0",
# ]
# ///

import marimo

__generated_with = "0.10.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # CAIE Prototype

        _TBD_

        > **Status**: Work in progress.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Background""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "What is APOLLO-sv?": mo.md("_TBD_"),
            "What is the Conceptual Spaces Model (CSM)?": mo.md("_TBD_"),
            "Why this domain?": mo.md("_TBD_"),
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## This is a cell """)
    return

@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md("**This is a box.**"), kind="warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---

        **Source code**: [github.com/humane-intelligence/caie-prototype](https://github.com/humane-intelligence/caie-prototype)
        """
    )
    return


if __name__ == "__main__":
    app.run()
