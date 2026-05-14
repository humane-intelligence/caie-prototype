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
        ### Conceptual AI Inspection & Evaluation on the APOLLO-sv Knowledge Graph

        ---

        This prototype demonstrates the **Conceptual Spaces Model (CSM)** pipeline applied
        to the [APOLLO-sv](https://obofoundry.org/ontology/apollo_sv.html) infectious
        disease structured vocabulary. It is developed as part of a research program on
        **trustworthy AI** funded by the Schmidt Sciences Trustworthy AI initiative at
        [Humane Intelligence](https://humane-intelligence.org).

        The core question: *can a geometric, ontology-grounded representation of domain
        knowledge be used to inspect and evaluate how an AI system organizes concepts?*
        The CSM provides a formal answer — an interpretable embedding of a knowledge graph
        into a conceptual space, against which an AI's internal representations can be
        compared.

        > **Status**: This is an active prototype. Pipeline stages 1–3 (Envelope,
        > Substrate, Mesh) are under construction; this notebook will be updated as
        > results become available. The framing, architecture, and visualizations below
        > reflect the current state of the research.
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
            "What is APOLLO-sv?": mo.md(
                r"""
                **APOLLO-sv** (Apollo Structured Vocabulary) is an OWL ontology developed
                for infectious disease surveillance and pandemic preparedness. It organizes
                concepts such as:

                - **Disease** and pathogen types (e.g., *Influenza A*, *SARS-CoV-2 infection*)
                - **Host** species and transmission routes
                - **Interventions** (vaccines, non-pharmaceutical interventions)
                - **Surveillance** and reporting structures
                - **Geographic** and temporal context

                It provides a rich class hierarchy (C), a set of typed relationships (P),
                and — crucially for our pipeline — concepts that can be grounded in
                empirical data (Q).
                """
            ),
            "What is the Conceptual Spaces Model (CSM)?": mo.md(
                r"""
                The **Conceptual Spaces Model** (Gärdenfors, 2000; extended here) is a
                geometric theory of meaning. Concepts are *convex regions* in a
                quality-dimensional metric space, not symbolic rules.

                Our pipeline operationalizes this by:

                1. Extracting an *Operational Envelope* (C, P, Q) from an ontology
                2. Populating a *Substrate* — instances with measured quality values
                3. Building a *Mesh* — a topological nerve encoding class overlap
                4. Solving a *Minimum Distortion Embedding* (MDE) into ℝ^{d₀}
                5. *Triangulating* held-out instances into the space
                6. *Evaluating* the embedding against three falsifiable hypotheses

                The result is an interpretable geometric map of the knowledge domain.
                """
            ),
            "Why infectious disease?": mo.md(
                r"""
                Infectious disease is an ideal domain for this prototype because:

                - APOLLO-sv is a mature, community-maintained OWL ontology
                - Surveillance data (outbreak reports, epidemiological records) provides
                  real instance-level measurements that can populate the substrate
                - The domain has clear public-health stakes — trustworthy AI in
                  epidemic preparedness directly affects lives
                - Class boundaries are *genuinely uncertain* (e.g., influenza-like illness
                  vs confirmed influenza), making geometric ambiguity representation valuable
                """
            ),
        }
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Pipeline Architecture""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The CSM pipeline has six stages. Each stage is a *bridge* with a defined
        input/output contract — separating the ontology-side modeling choices from
        the data-side empirical questions.

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

        Stages 1–3 depend only on the ontology and the choice of dataset.
        Stages 4–6 are dataset-agnostic given the outputs of stage 3.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Stage 1 — Operational Envelope""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "**Work in progress.** "
            "APOLLO-sv is being ingested via `rdflib` + `owlrl` closure. "
            "Results will appear here once the envelope is constructed."
        ),
        kind="warn",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The **Operational Envelope** is the triple (C, P, Q) extracted from the ontology:

        | Symbol | Meaning | Source in APOLLO-sv |
        |--------|---------|---------------------|
        | **C**  | Classes — concept types | OWL named classes under `apollo_sv:InfectiousDisease`, etc. |
        | **P**  | Predicates — typed relationships | Object properties (`has_host`, `transmitted_by`, …) |
        | **Q**  | Quality dimensions — numerical axes | To be determined by the pairing dataset |
        | **Ω**  | Class profiles — empirical class centroids | Derived from substrate after population |

        Once the envelope is built, the table below will show the extracted C/P inventory
        and a sunburst chart of the class hierarchy.
        """
    )
    return


@app.cell(hide_code=True)
def _():
    # Placeholder: will be replaced with live envelope data from pre-computed parquet
    envelope_stats = {
        "classes": "—",
        "predicates": "—",
        "quality_dims": "—",
        "essential_entities": "—",
    }
    return (envelope_stats,)


@app.cell(hide_code=True)
def _(envelope_stats, mo):
    mo.hstack(
        [
            mo.stat(envelope_stats["classes"], label="Classes |C|"),
            mo.stat(envelope_stats["predicates"], label="Predicates |P|"),
            mo.stat(envelope_stats["quality_dims"], label="Quality dims |Q|"),
            mo.stat(envelope_stats["essential_entities"], label="Essential entities"),
        ],
        justify="start",
        gap=2,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Stage 2 — Substrate Population""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "**Work in progress.** "
            "The pairing dataset (instance-level disease observations with quality measurements) "
            "is being identified. This section will show the substrate once populated."
        ),
        kind="warn",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The **Substrate** is the set of real-world entities (disease observations,
        outbreak records, surveillance reports) that:

        - Are classified under one or more classes in **C**
        - Have measured values for some or all quality dimensions in **Q**
        - Are split into *train* (class-pinned) and *test* (held-out) partitions

        This is the empirical heart of the pipeline. The quality of the final
        embedding depends directly on the coverage and accuracy of the substrate.

        *Candidate datasets under evaluation:*
        - WHO Disease Outbreak News (DON)
        - HealthMap / ProMED outbreak reports
        - GIDEON Infectious Disease Database
        - CDC NNDSS surveillance data
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Stage 3 — Mesh Construction""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "**Work in progress.** "
            "The nerve 𝒩 will be constructed once the substrate is populated."
        ),
        kind="warn",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The **Mesh** is a simplicial complex (nerve) built from the class structure:

        - Each class *c ∈ C* becomes a vertex
        - Pairs of classes sharing substrate entities become edges (1-simplices)
        - Higher-order overlaps become higher-dimensional simplices
        - The nerve encodes the *topological skeleton* of the knowledge domain

        The mesh is the key intermediate between the ontology (symbolic) and the
        embedding (geometric). Its structure determines what the MDE solver must
        preserve.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Stage 4 — MDE Solve""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "**Work in progress.** "
            "The conceptual space embedding will appear here once the mesh is built."
        ),
        kind="warn",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The **Minimum Distortion Embedding** finds a map Φ*: entities → ℝ^{d₀} that:

        - Places entities from the same class close together
        - Respects the quality-dimension structure (anchoring)
        - Preserves the topological structure of the nerve 𝒩

        The solve is a staged optimization: first embedding the class prototypes
        (using the nerve topology as the energy functional), then anchoring to
        quality-dimension centroids.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Stage 5 — Triangulation""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "**Work in progress.** "
            "Held-out instance placement will appear here once the embedding is solved."
        ),
        kind="warn",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        **Triangulation** places *held-out* substrate entities (the test partition)
        into the solved conceptual space — without retraining. Each held-out
        entity is placed by minimizing its local distortion given its
        k-nearest training neighbors.

        This is the test of *generalization*: does the geometric structure
        learned from training instances extend to unseen ones?
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""## Stage 6 — Evaluation""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.callout(
        mo.md(
            "**Work in progress.** "
            "H1, H2, and H3 evaluation results will appear here once the pipeline is complete."
        ),
        kind="warn",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The embedding is evaluated against three falsifiable hypotheses:

        | Hypothesis | Claim | Metric |
        |------------|-------|--------|
        | **H1** Classification recovery | A k-NN classifier in Φ* recovers ontology class labels | Weighted F1 on held-out entities |
        | **H2** Quality-dimension estimation | Linear regression in Φ* predicts quality values | RMSE per quality dimension |
        | **H3** Topological faithfulness | The realized nerve (from Φ*) matches the constructed nerve (from 𝒩) | Match barcode F/S/L scores |

        H3 is the framework's novel contribution: it uses persistent homology to compare
        the *topological shape* of the constructed and realized nerves, producing a
        precision/recall-like barcode that measures geometric faithfulness at multiple scales.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""---""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## About

        This prototype is developed by [Humane Intelligence](https://humane-intelligence.org)
        as part of research into trustworthy AI evaluation methods.

        The underlying CSM framework is described in:
        > *Geometric Conceptual Spaces as a Model for Trustworthy AI Evaluation*
        > (manuscript in preparation)

        **Source code**: [github.com/humane-intelligence/caie-prototype](https://github.com/humane-intelligence/caie-prototype)
        """
    )
    return


if __name__ == "__main__":
    app.run()
