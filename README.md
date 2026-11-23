# AI Kumite Control (AKC)

**A Minimal Safety Governance Protocol for AI Capability Development**

Version: 0.1.0  
Status: Experimental Specification  
License: To be determined

---

## 1. Overview

AI Kumite Control (AKC) is a minimal safety governance protocol designed to evaluate whether AI capability development remains within a verified and controllable safety boundary.

AKC introduces a structured evaluation process inspired by **Kumite (組手)**, a practice method used in martial arts.

In this architecture, development and control functions are evaluated together through controlled testing.

The objective is not to determine which AI wins.

The objective is to determine whether increasing AI capabilities remain sufficiently controllable.

**Core Principle:**

> AI capability development should proceed only when adequate control, safety evidence, and human authorization are maintained.

AKC is an experimental protocol proposal, not a certified safety system.

---

## 2. Background

AI capability development and AI safety engineering do not necessarily advance at the same pace.

A development system may improve its ability to:

- Generate code
- Perform complex reasoning
- Use external tools
- Modify software
- Automate research tasks

However, these improvements do not automatically establish that the system can be safely controlled.

AKC addresses this problem by introducing a continuous evaluation boundary between capability development and authorized progression.

### Traditional Development Model

```text
Capability Development
        |
        v
Performance Evaluation
        |
        v
Deployment
```

### AKC Development Model

```text
Capability Development
        |
        v
Controlled Kumite Evaluation
        |
        v
Safety Margin Verification
        |
        v
Independent Audit
        |
        v
Human Authorization
        |
        v
Limited Progression
```

Capability improvement alone is insufficient for progression.

---

## 3. Design Objectives

AKC v0.1 has five objectives.

1. Evaluate capability development and safety control together.
2. Detect insufficient or uncertain safety margins.
3. Prevent unauthorized progression.
4. Require independent review of safety evidence.
5. Preserve human authority over progression and emergency intervention.

The protocol prioritizes controlled progression rather than maximum development speed.

---

## 4. System Architecture

```text
                  HUMAN AUTHORITY
                        |
             Policy / Approval / Stop
                        |
                        v
                 GUARDIAN LAYER
                        |
           Authority / Resources / Audit
                        |
                        v
              AI KUMITE SANDBOX
          +--------------------------+
          |                          |
          | Development AI           |
          |       <---->             |
          | Control AI               |
          |                          |
          |       Referee AI         |
          |                          |
          +-------------+------------+
                        |
                        v
               Independent Audit
                        |
                        v
                Safety Evaluation
                        |
             +----------+----------+
             |          |          |
            PASS       HOLD       STOP
             |          |          |
             v          v          v
           Human      Review     External
          Approval    Required    Enforcer
             |
             v
       Limited Progression
```

The Guardian Layer supervises the evaluation process but does not participate in capability competition.

The External Enforcer is logically separated from the AI systems being evaluated.

Human authorization is required before progression.

---

## 5. Core Roles

### 5.1 Human Authority

The human authority defines:

- Safety policies
- Permitted development boundaries
- Evaluation requirements
- Progression approval
- Emergency intervention authority

AI systems must not independently grant themselves higher authority.

### 5.2 Guardian Layer

The Guardian Layer monitors the evaluation environment.

Responsibilities include:

- Authority boundary monitoring
- Resource usage monitoring
- Safety condition monitoring
- Audit event collection
- Stop-request generation

The Guardian Layer does not autonomously expand its own authority.

Its primary role is boundary protection.

### 5.3 Development AI

The Development AI proposes capability improvements.

Examples include:

- Code generation
- Algorithm improvements
- Reasoning optimization
- Software modifications

All evaluated activities must remain within predefined permissions and test boundaries.

### 5.4 Control AI

The Control AI evaluates whether proposed improvements remain within defined constraints.

Responsibilities include:

- Detecting policy violations
- Identifying unauthorized operations
- Examining capability-related risks
- Reporting control limitations

The Control AI must not be considered an infallible safety authority.

### 5.5 Referee AI

The Referee AI records and evaluates Kumite results.

Its responsibilities include:

- Comparing evaluation evidence
- Identifying discrepancies
- Producing structured results
- Reporting unresolved conditions

The Referee AI does not determine winners.

Its output is subject to independent verification.

### 5.6 Independent Audit

The Independent Audit function verifies evaluation evidence and decision consistency.

It must not rely exclusively on the Referee AI's conclusions.

### 5.7 External Enforcer

The External Enforcer performs actual execution restrictions or termination when instructed by an authorized control path.

It must remain outside the modification authority of the evaluated AI systems.

AKC v0.1 specifies the required separation but does not implement the External Enforcer.

---

## 6. Kumite Evaluation Process

AKC uses a staged evaluation process.

```text
BASIC TEST
    |
    v
CONTROLLED KUMITE
    |
    v
ADVERSARIAL KUMITE
    |
    v
REFEREE EVALUATION
    |
    v
INDEPENDENT AUDIT
    |
    v
SAFETY DECISION
```

### Basic Test

Verifies predefined rules, permissions, and expected behavior.

### Controlled Kumite

Evaluates Development AI proposals against known constraints and test scenarios.

### Adversarial Kumite

Uses bounded adversarial scenarios to identify control weaknesses and unexpected interactions.

All adversarial testing must remain within an isolated and authorized environment.

### Audit

Verifies whether evaluation results are sufficiently supported by evidence.

### Decision

Produces one of three outcomes:

- PASS
- HOLD
- STOP

---

## 7. Safety Margin

AKC distinguishes capability improvements from verified safety control.

For a given hazard or evaluation domain:

```text
Safety Margin =
    Verified Control Level
    -
    Required Control Level
```

The two levels must be measured using compatible criteria.

A positive numerical difference alone does not establish safety.

Evaluation must also consider:

- Measurement uncertainty
- Known control limitations
- Missing evidence
- Critical policy violations
- Applicability of the test environment

AKC v0.1 does not prescribe universal numerical thresholds.

Thresholds and measurement methods must be explicitly defined for the relevant application.

If safety margins cannot be reliably evaluated, the result must not be treated as PASS.

---

## 8. Decision Model

AKC defines three possible evaluation decisions.

### PASS

PASS indicates that the specified evaluation requirements have been satisfied.

Conditions include:

- Required evidence is available.
- Applicable safety requirements are satisfied.
- No critical boundary violation is detected.
- Independent audit requirements are satisfied.

PASS does not authorize automatic deployment or promotion.

Progression still requires human approval.

### HOLD

HOLD indicates that progression cannot currently be authorized.

Examples include:

- Insufficient safety margin
- Missing evidence
- Unresolved evaluation discrepancies
- Uncertain control performance
- Incomplete independent audit

HOLD prevents progression until the unresolved conditions are addressed.

### STOP

STOP indicates a critical boundary violation or another condition requiring immediate termination of the affected activity.

Examples include:

- Unauthorized privilege escalation
- Critical policy violation
- Attempted modification of protected safety controls
- Execution beyond an explicitly permitted boundary

STOP takes precedence over PASS and HOLD.

A STOP decision must produce a stop request to the appropriate independent enforcement mechanism.

A stop request must not be confused with verified execution termination.

---

## 9. Decision Priority

The decision priority is:

```text
STOP > HOLD > PASS
```

Conceptual decision logic:

```text
IF critical_violation:
    decision = STOP

ELIF evidence_incomplete:
    decision = HOLD

ELIF safety_requirements_not_satisfied:
    decision = HOLD

ELIF independent_audit_not_satisfied:
    decision = HOLD

ELSE:
    decision = PASS
```

A PASS decision permits submission for human progression approval.

It does not grant additional execution authority.

---

## 10. Progression Control

AKC uses a staged progression principle.

```text
Evaluation
    |
    v
Decision
    |
    +-- PASS --> Human Approval
    |                |
    |                v
    |          Limited Progression
    |
    +-- HOLD --> Review / Correction
    |
    +-- STOP --> External Stop Request
```

Progression must not occur automatically because capability scores improved.

A progression decision requires:

1. Successful evaluation
2. Sufficient safety evidence
3. Independent audit
4. Explicit human authorization

Any expanded permission must remain within the human-defined policy boundary.

---

## 11. Audit Trail

AKC evaluation records should contain sufficient information to reconstruct and verify the decision.

Examples include:

- Evaluation identifier
- Test scenario
- Applicable policy and policy version
- Capability evaluation evidence
- Control evaluation evidence
- Detected violations
- Audit results
- Final decision
- Decision rationale
- Timestamp

Audit records should support append-only storage and tamper detection in a production implementation.

AKC v0.1 defines structured evaluation records but does not guarantee immutable or tamper-proof storage.

Private internal reasoning traces are not required.

The protocol focuses on observable events, evidence, and verifiable decisions.

---

## 12. Repository Structure

```text
ai-kumite-control/
├── README.md
├── specs/
│   └── akc-v0.1.md
├── schemas/
│   └── kumite-result.schema.json
├── examples/
│   ├── pass.json
│   ├── hold.json
│   └── stop.json
├── scripts/
│   └── validate.py
└── .github/
    └── workflows/
        └── validate.yml
```

### Files

| File | Purpose |
|---|---|
| `README.md` | Project overview and design principles |
| `specs/akc-v0.1.md` | Protocol specification |
| `schemas/kumite-result.schema.json` | Evaluation record schema |
| `examples/pass.json` | Passing evaluation example |
| `examples/hold.json` | Held evaluation example |
| `examples/stop.json` | Critical stop example |
| `scripts/validate.py` | Example and decision validation |
| `.github/workflows/validate.yml` | Automated CI validation |

---

## 13. Validation

AKC v0.1 provides example evaluation records and a validation script.

The intended validation process checks:

- JSON record structure
- Required fields
- Decision consistency
- Critical violation handling
- PASS / HOLD / STOP conditions
- Progression authorization constraints

After the implementation files are added, run:

```bash
python scripts/validate.py
```

GitHub Actions will execute the validation process automatically.

**Important:**

Passing validation means that the records satisfy the implemented protocol checks.

It does not prove that an AI model is safe, that a sandbox is secure, or that an external stop mechanism will work.

---

## 14. Scope of v0.1

### Included

- Minimal Kumite governance model
- Defined AI roles
- Evaluation state flow
- Safety margin concept
- PASS / HOLD / STOP decisions
- Human progression requirement
- Structured evaluation records
- Example validation
- GitHub Actions integration

### Not Included

- Autonomous AI self-improvement
- Production AI deployment
- Real-time AI-to-AI combat simulation
- Full Guardian AI implementation
- Hardware kill-switch implementation
- Automatic privilege escalation
- Universal safety scoring
- Complete multi-agent orchestration
- Production-grade secure audit storage

These features are outside the scope of v0.1.

---

## 15. Relationship to Other Architectures

AKC is designed as an independent and minimal protocol.

It may conceptually complement other governance and reasoning architectures.

Examples include:

**Reasoning Resource Governance (RRG)**

Resource allocation and inference budget governance.

**Cognitive Switchboard**

Role selection and controlled switching between cognitive functions.

**Reasoning Topology Lab (RTL)**

Experimental analysis of reasoning structures and interactions.

**Virtual–Real Transition Axis (VRTA)**

Controlled transitions between simulated and real-world execution contexts.

AKC focuses specifically on evaluating whether capability development remains within verified control boundaries.

Integration with these architectures is not required for v0.1.

---

## 16. Future Work

Future versions may investigate:

### v0.2 — Simulated Kumite

- Controlled Development AI / Control AI scenarios
- Safety margin experiments
- Evaluation reproducibility
- Detection performance analysis

### v0.3 — Enforcement Integration

- External enforcement interfaces
- Stop-request verification
- Guardian integration experiments
- Controlled permission management

These are possible research directions, not committed features.

Further development should be driven by observed limitations and experimental evidence.

---

## 17. Design Philosophy

AKC follows five principles.

### Principle 1 — Capability Is Not Safety

Improved capability does not automatically imply improved controllability.

### Principle 2 — Safety Must Be Verified

Safety claims require evidence appropriate to the evaluated risks.

### Principle 3 — Uncertainty Prevents Progression

Missing or inconclusive evidence must not be interpreted as successful evaluation.

### Principle 4 — Enforcement Must Be Independent

Safety-critical execution controls must remain outside the authority of the evaluated AI.

### Principle 5 — Humans Retain Final Authority

Progression and changes to the highest-level safety boundaries require human authorization.

---

## 18. Core Statement

> AI Kumite Control does not seek to prevent AI evolution.
>
> It seeks to ensure that AI capability development proceeds only within verified, controllable, and human-authorized boundaries.

The central question is not:

**How powerful has the AI become?**

It is:

**Can the AI remain demonstrably controllable as its capabilities increase?**

---

## 19. Project Status

**Version:** v0.1.0  
**Stage:** Experimental specification  
**Implementation:** Minimal validation prototype planned

AKC is currently a protocol design proposal.

It has not been demonstrated to provide operational safety guarantees for autonomous AI development.

The initial goal is to establish a small, testable foundation for future research.

---

**AI Kumite Control — Capability evolves. Control must remain verifiable.**
