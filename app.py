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


# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # CAIE Prototype
        ### Contextual AI Evaluation on APOLLO-sv

        _[2–3 sentence pitch — you write this]_

        > **Working in the open.** This is active research. Results and content
        > will be updated as the pipeline is built out.

        [Humane Intelligence](https://humane-intelligence.org) ·
        [Source code](https://github.com/humane-intelligence/ontology-caie-prototype)
        """
    )
    return


# ---------------------------------------------------------------------------
# Background
# ---------------------------------------------------------------------------

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Background""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.accordion(
        {
            "What is APOLLO-sv?": mo.md("_TBD_"),
            "What is Contextual AI Evaluation?": mo.md("_TBD_"),
            "Why infectious disease?": mo.md("_TBD_"),
        }
    )
    return


# ---------------------------------------------------------------------------
# The Data
# ---------------------------------------------------------------------------

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## The Data""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### APOLLO-sv

        _[Brief description of what the ontology gives us — class hierarchy, predicates.
        Envelope stats will populate here once parsed.]_
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md("**Envelope not yet constructed.** Class and predicate counts will appear here."),
        kind="warn",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ### Pairing Dataset

        _[Description of the empirical dataset that provides instance-level
        measurements — TBD.]_
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md("**Dataset TBD.** Candidate datasets under evaluation."),
        kind="warn",
    )
    return


# ---------------------------------------------------------------------------
# Pipeline Walkthrough
# ---------------------------------------------------------------------------

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Pipeline Walkthrough""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ```
        Stage 1 │ Envelope Construction    APOLLO-sv OWL  →  (C, P, Q, Ω, d₀)
                 │
        Stage 2 │ Substrate Population     Instances + Q measurements  →  Substrate
                 │
        Stage 3 │ Mesh Construction        (C, P, Substrate)  →  Nerve 𝒩
                 │
        Stage 4 │ MDE Solve               𝒩 + Energy Φ  →  Embedding Φ*: ℝ^{d₀}
                 │
        Stage 5 │ Triangulation           Held-out instances  →  Placed in Φ*
                 │
        Stage 6 │ Evaluation              H1 (classification) · H2 (quality) · H3 (topology)
        ```
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Stage 1 — Operational Envelope""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("_Extract the classes (C), predicates (P), and quality dimensions (Q) from APOLLO-sv._")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md("**Work in progress.**"), kind="warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Stage 2 — Substrate Population""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("_Populate instance-level entities (from the pairing dataset) with quality measurements._")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md("**Work in progress.**"), kind="warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Stage 3 — Mesh Construction""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("_Build a topological nerve encoding which classes share instances._")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md("**Work in progress.**"), kind="warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Stage 4 — MDE Solve""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("_Embed the nerve into a low-dimensional conceptual space via Minimum Distortion Embedding._")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md("**Work in progress.**"), kind="warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Stage 5 — Triangulation""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("_Place held-out instances into the solved embedding without retraining._")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md("**Work in progress.**"), kind="warn")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""### Stage 6 — Evaluation""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("_Test the embedding against three falsifiable hypotheses._")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(mo.md("**Work in progress.**"), kind="warn")
    return


# ---------------------------------------------------------------------------
# What We're Building Toward
# ---------------------------------------------------------------------------

@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## What We're Building Toward""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The pipeline produces three measurable results:

        | | Hypothesis | What it shows |
        |---|---|---|
        | **H1** | Classification recovery | _TBD_ |
        | **H2** | Quality-dimension estimation | _TBD_ |
        | **H3** | Topological faithfulness | _TBD_ |

        _[One paragraph on what success looks like for a grant reviewer — you write this.]_
        """
    )
    return


# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------

@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ---

        [Humane Intelligence](https://humane-intelligence.org) ·
        [Source code](https://github.com/humane-intelligence/ontology-caie-prototype)
        """
    )
    return


if __name__ == "__main__":
    app.run()
