# WorldOS — Jurisdiction and Epistemic Boundary

## 1. Why this document exists

WorldOS deals with public information about real countries, governments, institutions, companies, communities, and people.

That makes restraint a product requirement.

The system must be clear about what belongs inside its jurisdiction and what belongs to downstream analysis.

## 2. WorldOS jurisdiction

WorldOS has jurisdiction over the **information flow**.

It may acquire, preserve, normalize, index, segment, structure, and expose publicly available information.

It may preserve contextual metadata that allows later systems to understand where information came from and how it appeared.

It should avoid turning those operations into unearned judgments.

## 3. The safest foundational assertion

WorldOS should always be able to fall back to the following:

> **This source communicated this material, in this context, at this time, and WorldOS preserved it here.**

That is the fundamental unit of accountability.

## 4. Mechanical and contextual transformations

Some transformations are necessary to make text computationally useful.

Examples may include:

- language identification;
- character/encoding normalization;
- document segmentation;
- title extraction;
- publication-date extraction;
- named-string/entity candidate extraction;
- geographic references;
- numeric values;
- quoted passages;
- source links;
- document revision/version tracking;
- search indexing.

Each transformation should preserve lineage back to the original source.

## 5. Do not prematurely decide semantics

WorldOS should be cautious with labels that sound objective but may contain hidden judgment.

For example, the core should not casually classify material as:

- fact;
- opinion;
- propaganda;
- misinformation;
- trustworthy;
- deceptive;
- unbiased;
- dangerous;
- good;
- bad.

Even apparently simple labels can require interpretation.

If such analysis is useful, it belongs in an explicit downstream model/run whose assumptions and purpose are visible.

## 6. Government example

Suppose a government publication says:

> Crime declined by 40%.

WorldOS can preserve:

- which government body published the material;
- the text and relevant surrounding context;
- the date;
- the geography;
- any linked methodology;
- the numeric value;
- the source URL;
- revisions to the page if observed.

Suppose another public source reports a different value.

WorldOS can preserve that source too.

It should not automatically publish:

> The government lied.

Nor must it decide which number is true.

A downstream analysis may compare methodology, definitions, time windows, source histories, and other material before drawing a conclusion.

## 7. Relationship without verdict

WorldOS may need to expose that records are potentially related so that downstream systems can retrieve them together.

That relationship should be framed conservatively.

For example:

> These records contain references to the same named institution and apparently related crime statistics during overlapping time periods.

That is different from:

> These sources contradict one another and source A is wrong.

## 8. Source neutrality

WorldOS should not maintain a canonical preferred-media list as a founding feature.

A source's identity and characteristics should be preserved.

Downstream systems may decide that different sources deserve different analytical treatment.

WorldOS itself should not require every user to inherit AiBC's or any contributor's worldview.

## 9. Neutrality is not blindness

Avoiding public judgments does not mean stripping away useful context.

Provenance matters.

Dates matter.

Authors matter.

Institutional origin matters.

Source revisions matter.

Links between material matter.

The goal is to maximize what later systems can reason from while minimizing unearned conclusions embedded in the substrate itself.

## 10. Governing rule

Before adding a WorldOS field or label, ask:

> **Is this describing the source and its context, or is it interpreting the world?**

If it is primarily interpretation, it probably belongs downstream.
