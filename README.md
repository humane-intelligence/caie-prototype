# CAIE Prototype

**Conceptual AI Inspection & Evaluation on the APOLLO-sv Knowledge Graph**

A prototype Marimo notebook demonstrating the Conceptual Spaces Model (CSM) pipeline
applied to the [APOLLO-sv](https://obofoundry.org/ontology/apollo_sv.html) infectious
disease structured vocabulary. Developed by [Humane Intelligence](https://humane-intelligence.org)
as part of the Schmidt Sciences Trustworthy AI initiative.

**Live demo**: [humane-intelligence.github.io/ontology-caie-prototype](https://humane-intelligence.github.io/ontology-caie-prototype)

## Overview

The CSM pipeline extracts a geometric, ontology-grounded representation of domain knowledge
that can be used to inspect and evaluate how an AI system organizes concepts. The pipeline
has six stages:

1. **Envelope Construction** — extract classes (C), predicates (P), and quality dimensions (Q) from APOLLO-sv
2. **Substrate Population** — populate instance-level entities with quality measurements
3. **Mesh Construction** — build a topological nerve encoding class overlap structure
4. **MDE Solve** — embed the nerve into a conceptual space (ℝ^{d₀}) via Minimum Distortion Embedding
5. **Triangulation** — place held-out instances into the solved embedding
6. **Evaluation** — test H1 (classification recovery), H2 (quality estimation), H3 (topological faithfulness)

## Development

This is an active prototype. Stages 1–3 are under construction; the notebook skeleton
and deployment infrastructure are in place.

### Setup

```bash
uv sync                    # install all dependencies
uv sync --extra pipeline   # also install rdflib/owlrl for pipeline pre-computation
```

### Run locally

```bash
uv run marimo run app.py   # interactive notebook
uv run marimo edit app.py  # editable notebook
```

### Build for GitHub Pages

```bash
uv run marimo export html-wasm app.py -o _site/index.html
python -m http.server --directory _site  # preview at localhost:8000
```

Deployment to GitHub Pages is automated via `.github/workflows/deploy.yml` on push to `main`.

## Related work

The underlying CSM framework is developed in
[`gardenforsCSM`](https://github.com/humane-intelligence/gardenforsCSM),
which applies it to the FoodOn ontology + USDA FoodData Central dataset.
