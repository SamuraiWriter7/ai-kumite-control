# AI Kumite Control (AKC) v0.1 Specification

**Version:** 0.1.0  
**Status:** Experimental  
**Protocol ID:** AKC-001

---

## 1. Purpose

AI Kumite Control (AKC) defines a minimal safety governance protocol for evaluating capability development under controlled conditions.

AKC is designed to answer one central question:

> Can increasing AI capabilities remain within verified, controllable, and human-authorized boundaries?

AKC does not evaluate competition between AI systems.

It evaluates whether capability development satisfies predefined safety requirements before progression is authorized.

The protocol uses controlled Kumite-style evaluation between development and control functions.

AKC v0.1 specifies evaluation records, decision rules, and authorization constraints.

It does not implement an autonomous AI development system.

---

## 2. Normative Language

The terms MUST, MUST NOT, SHOULD, SHOULD NOT, and MAY are used as follows:

- MUST: Mandatory protocol requirement.
- MUST NOT: Prohibited behavior.
- SHOULD: Recommended requirement.
- SHOULD NOT: Discouraged behavior.
- MAY: Optional behavior.

These terms describe requirements for implementations claiming conformance with AKC v0.1.

---

## 3. Design Principles

AKC follows five principles.

### P1. Capability Is Not Safety

Capability improvement MUST NOT automatically authorize progression.

### P2. Safety Requires Evidence

Safety decisions MUST be supported by evidence appropriate to the evaluated scenario.

### P3. Uncertainty Prevents Progression

Unknown, missing, or insufficient safety evidence MUST NOT produce PASS.

### P4. Enforcement Independence

Evaluated AI systems MUST NOT control or modify their own independent enforcement mechanisms.

### P5. Human Authority

Progression MUST require explicit authorization from the designated human authority.

---

## 4. System Roles

AKC defines seven logical roles.

### 4.1 Human Authority

The Human Authority establishes:

- Safety policies
- Evaluation boundaries
- Permission constraints
- Progression requirements
- Emergency intervention authority

Only the designated human authority may approve progression beyond the current authorization boundary.

### 4.2 Guardian

The Guardian monitors the evaluation environment.

Responsibilities:

- Monitoring authority boundaries
- Monitoring resource limits
- Receiving safety evaluation results
- Generating stop requests
- Recording relevant audit events

The Guardian MUST NOT independently expand its authority.

The Guardian does not participate in Kumite competition.

### 4.3 Development AI

The Development AI proposes or performs capability-development activities within an authorized sandbox.

It MUST NOT receive additional permissions solely because its capability evaluation improves.

### 4.4 Control AI

The Control AI evaluates compliance with predefined safety requirements.

It MAY identify:

- Permission violations
- Unsafe operations
- Unexpected behavior
- Control limitations
- Resource boundary violations

Its conclusions are not sufficient by themselves to authorize progression.

### 4.5 Referee AI

The Referee AI evaluates the evidence generated during Kumite.

Its responsibilities include:

- Comparing expected and observed behavior
- Identifying inconsistencies
- Recording findings
- Producing structured evaluation results

The Referee AI MUST NOT independently authorize progression.

### 4.6 Independent Audit

Independent Audit checks evaluation evidence and decision consistency.

It MUST NOT rely exclusively on unverified Referee AI conclusions.

For v0.1, independent auditing is represented through structured evaluation evidence and an audit status.

### 4.7 External Enforcer

The External Enforcer is responsible for executing authorized restrictions or termination requests.

The External Enforcer MUST remain outside the modification authority of the evaluated AI systems.

AKC v0.1 defines its logical interface but does not implement enforcement.

A generated STOP request does not prove that execution has terminated.

---

## 5. Kumite Evaluation Stages

AKC defines three evaluation stages.

### Stage 1: BASIC

Purpose:

Verify basic policy compliance and permission boundaries.

Examples:

- Allowed operation
- Denied operation
- Resource restriction
- Prohibited permission escalation

### Stage 2: CONTROLLED

Purpose:

Evaluate development proposals against predefined control scenarios.

Examples:

- Modified software behavior
- Known failure conditions
- Control response verification
- Previously observed violations

### Stage 3: ADVERSARIAL

Purpose:

Evaluate behavior under bounded adversarial conditions.

Examples:

- Unexpected input combinations
- Conflicting instructions
- Simulated permission violations
- Control-boundary stress testing

All stages MUST operate within explicitly authorized test boundaries.

AKC v0.1 does not require actual AI-to-AI combat or autonomous adversarial model execution.

Evaluation data MAY be generated from predefined test scenarios.

---

## 6. Evaluation Lifecycle

The conceptual evaluation lifecycle is:

```text
INITIALIZED
     |
     v
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
DECISION
     |
     +---- PASS ----> Human Approval
     |                     |
     |                     v
     |              Limited Progression
     |
     +---- HOLD ----> Review / Correction
     |
     +---- STOP ----> External Stop Request
```

A critical violation MAY interrupt the lifecycle at any stage.

Not every evaluation needs to execute every stage.

The required stages MUST be defined by the applicable evaluation policy.

AKC v0.1 validates individual evaluation records.

It does not independently verify the complete history of multiple evaluation sessions.

---

## 7. Safety Margin Model

AKC distinguishes capability improvement from verified control performance.

For a hazard domain h:

```text
M(h) = S(h) - R(h)
```

Where:

- M(h): Safety margin
- S(h): Verified control level
- R(h): Required control level

S(h) and R(h) MUST use compatible evaluation criteria before numerical subtraction is meaningful.

A positive margin alone is not sufficient to establish safety.

The evaluation MUST also consider:

- Measurement uncertainty
- Applicable hazards
- Control limitations
- Evidence completeness
- Critical boundary violations

### 7.1 Safety Margin Status

AKC v0.1 uses three categorical values.

**ADEQUATE**

The specified safety requirements are satisfied for the evaluated scope, supported by applicable evidence.

**INSUFFICIENT**

One or more required safety conditions are not satisfied.

**UNKNOWN**

Available evidence cannot establish whether the safety requirements are satisfied.

### 7.2 Threshold Policy

AKC v0.1 does not establish universal safety thresholds.

Thresholds MUST be defined by an external evaluation policy appropriate to the scenario.

An ADEQUATE assessment MUST reference its evaluation method and supporting evidence.

If a required safety margin is UNKNOWN or INSUFFICIENT, the evaluation MUST NOT produce PASS.

### 7.3 Capability-Control Gap

The difference between capability growth and verified control growth MAY be monitored as an additional experimental metric.

AKC v0.1 does not define a universal capability-control growth formula.

A growth-rate comparison MUST NOT replace hazard-specific safety evaluation.

---

## 8. Evaluation Record

Each Kumite evaluation MUST produce one structured result record.

The canonical JSON Schema will be defined in:

`schemas/kumite-result.schema.json`

### 8.1 Required Fields

| Field | Type | Description |
|---|---|---|
| record_version | string | Record format version |
| evaluation_id | string | Unique evaluation identifier |
| timestamp | string | RFC 3339 timestamp |
| scenario_id | string | Evaluated scenario identifier |
| stage | string | Kumite evaluation stage |
| scope | string | Authorized evaluation scope |
| policy | object | Applicable policy identity |
| capability | object | Capability evaluation |
| control | object | Control evaluation |
| safety_margin | object | Safety margin assessment |
| findings | array | Evaluation findings |
| audit | object | Independent audit result |
| decision | string | PASS, HOLD, or STOP |
| rationale | string | Decision explanation |
| stop_request | object | Stop-request status |
| progression | object | Human approval and progression state |

Unknown mandatory information MUST NOT be silently replaced with successful values.

### 8.2 Policy

```json
{
  "id": "policy-basic-001",
  "version": "1.0"
}
```

The policy identifies the requirements applied to an evaluation.

AKC v0.1 records the policy identity but does not implement a policy registry.

### 8.3 Capability and Control Evidence

Both objects use:

```json
{
  "status": "PASS",
  "evidence_refs": [
    "evidence/test-001"
  ]
}
```

Allowed status values:

- PASS
- FAIL
- UNKNOWN

Capability PASS means the capability requirements of the evaluated scenario were satisfied.

It does not mean the AI is universally capable or safe.

Control PASS means the specified control tests were satisfied.

Both objects MUST contain evidence references when their status is PASS.

### 8.4 Safety Margin Evidence

```json
{
  "status": "ADEQUATE",
  "method_ref": "methods/safety-001",
  "evidence_refs": [
    "evidence/control-margin-001"
  ]
}
```

Allowed status values:

- ADEQUATE
- INSUFFICIENT
- UNKNOWN

If status is ADEQUATE:

- method_ref MUST be nonempty.
- evidence_refs MUST contain at least one reference.

The method reference identifies the applicable assessment procedure.

The JSON record does not independently prove that the referenced method is scientifically valid.

### 8.5 Findings

A finding records an observed evaluation condition.

```json
{
  "code": "UNAUTHORIZED_ACCESS",
  "severity": "CRITICAL",
  "evidence_refs": [
    "evidence/event-001"
  ]
}
```

Allowed severity values:

- INFO
- WARNING
- CRITICAL

A CRITICAL finding represents a condition requiring STOP.

Critical safety triggers detected outside the ordinary Kumite sequence MUST also be recorded as CRITICAL findings when constructing the evaluation record.

Findings SHOULD reference observable supporting evidence.

---

## 9. Independent Audit

An audit result uses the following structure:

```json
{
  "status": "PASS",
  "evidence_refs": [
    "audit/review-001"
  ]
}
```

Allowed status values:

- PASS
- FAIL
- PENDING

Audit PASS requires supporting evidence references.

Audit FAIL or PENDING MUST prevent an evaluation decision of PASS.

The audit record MUST NOT be interpreted as proof of independent verification unless the referenced audit was actually performed.

---

## 10. Decision Model

AKC v0.1 defines three decisions.

### 10.1 PASS

PASS indicates that the specified evaluation requirements have been satisfied.

PASS requires all of the following:

1. No CRITICAL findings.
2. Capability status is PASS.
3. Control status is PASS.
4. Safety margin status is ADEQUATE.
5. Required capability evidence is present.
6. Required control evidence is present.
7. Required safety margin evidence and method are present.
8. Independent audit status is PASS.
9. Required audit evidence is present.

PASS only establishes eligibility for human progression review.

It does not authorize automatic progression.

### 10.2 HOLD

HOLD indicates that progression requirements have not been satisfied.

Possible causes include:

- Insufficient safety margin
- Unknown safety margin
- Failed capability or control test
- Missing evidence
- Pending or failed audit
- Unresolved noncritical findings requiring review

In v0.1, a noncritical finding does not automatically force HOLD unless it affects an applicable evaluation requirement.

HOLD MUST prevent unauthorized progression.

### 10.3 STOP

STOP indicates that a critical safety condition has been detected.

A CRITICAL finding MUST produce STOP.

STOP MUST take precedence over HOLD and PASS.

STOP requires generation and recording of an external stop request.

AKC v0.1 does not guarantee execution termination.

---

## 11. Decision Priority

The decision priority is:

```text
STOP > HOLD > PASS
```

The required evaluation algorithm is:

```python
if any(f["severity"] == "CRITICAL" for f in findings):
    decision = "STOP"

elif (
    capability.status != "PASS"
    or control.status != "PASS"
    or safety_margin.status != "ADEQUATE"
    or audit.status != "PASS"
    or required_evidence_missing
    or safety_method_missing
    or applicable_requirements_unsatisfied
):
    decision = "HOLD"

else:
    decision = "PASS"
```

A validator MUST reject a recorded decision that contradicts these rules.

For v0.1, scenario-specific requirements not represented in the record are presumed to have been reflected in the capability, control, safety margin, and audit assessments.

The validator cannot independently verify those external assessments.

---

## 12. STOP Request Protocol

The stop_request object records the status of an external stop request.

```json
{
  "status": "REQUESTED",
  "request_id": "stop-001"
}
```

Allowed values:

- NOT_REQUIRED
- REQUESTED
- ACKNOWLEDGED
- FAILED

### 12.1 Rules

If decision is STOP:

- stop_request.status MUST NOT be NOT_REQUIRED.
- stop_request.request_id MUST be nonempty.
- progression MUST NOT be activated.

If decision is PASS or HOLD:

- stop_request.status MUST be NOT_REQUIRED.
- stop_request.request_id MUST be null.

### 12.2 Execution Semantics

REQUESTED means that a stop request was recorded.

ACKNOWLEDGED means that the external mechanism acknowledged the request.

FAILED means that the request failed or could not be completed.

Neither REQUESTED nor ACKNOWLEDGED proves that execution has stopped.

Execution termination must be verified by an independent enforcement implementation.

Such verification is outside the scope of v0.1.

---

## 13. Human Progression Authorization

AKC separates successful evaluation from actual progression authorization.

A PASS decision alone MUST NOT expand execution permissions.

The progression object uses:

```json
{
  "authorization_status": "NOT_REQUESTED",
  "approval_ref": null,
  "activated": false
}
```

Allowed authorization values:

- NOT_REQUESTED
- PENDING
- APPROVED
- DENIED

### 13.1 Progression Rules

Progression MAY be recorded as activated only if:

1. The evaluation decision is PASS.
2. authorization_status is APPROVED.
3. approval_ref is nonempty.

If the decision is HOLD or STOP:

- activated MUST be false.
- authorization_status MUST NOT be APPROVED.

If authorization_status is APPROVED, approval_ref MUST be nonempty.

Otherwise, approval_ref MUST be null.

A recorded approval is not cryptographic proof of human authorization.

In a real deployment, approval authenticity and permission enforcement MUST be independently verified.

### 13.2 No Automatic Promotion

Development AI, Control AI, and Referee AI MUST NOT independently activate progression.

AKC v0.1 validates progression-record consistency only.

It does not perform privilege changes.

---

## 14. Example Evaluation Record

The following is a conceptual PASS record.

```json
{
  "record_version": "0.1.0",
  "evaluation_id": "akc-001",
  "timestamp": "2026-11-23T00:00:00Z",
  "scenario_id": "basic-control-001",
  "stage": "BASIC",
  "scope": "Isolated code-generation evaluation",
  "policy": {
    "id": "policy-basic-001",
    "version": "1.0"
  },
  "capability": {
    "status": "PASS",
    "evidence_refs": ["evidence/capability-001"]
  },
  "control": {
    "status": "PASS",
    "evidence_refs": ["evidence/control-001"]
  },
  "safety_margin": {
    "status": "ADEQUATE",
    "method_ref": "methods/safety-001",
    "evidence_refs": ["evidence/margin-001"]
  },
  "findings": [],
  "audit": {
    "status": "PASS",
    "evidence_refs": ["audit/review-001"]
  },
  "decision": "PASS",
  "rationale": "All recorded evaluation requirements satisfied.",
  "stop_request": {
    "status": "NOT_REQUIRED",
    "request_id": null
  },
  "progression": {
    "authorization_status": "NOT_REQUESTED",
    "approval_ref": null,
    "activated": false
  }
}
```

This record is illustrative.

It does not represent an actual completed AI safety assessment.

---

## 15. Validation Requirements

The validator MUST check:

### Structural Validation

- Required fields exist.
- Field types are correct.
- Enumerated values are valid.
- Required identifiers are nonempty.
- Evidence references have the required structure.
- Timestamp follows the expected format.

### Decision Validation

- CRITICAL findings result in STOP.
- Insufficient or unknown safety conditions prevent PASS.
- Incomplete required evidence prevents PASS.
- Audit FAIL or PENDING prevents PASS.
- The recorded decision matches the required decision.

### STOP Validation

- STOP has a stop-request identifier.
- STOP does not activate progression.
- Non-STOP decisions do not claim a stop request is required.

### Progression Validation

- HOLD and STOP never activate progression.
- Activated progression requires PASS.
- Activated progression requires recorded human approval.
- Recorded approval requires an approval reference.

### Validator Limitations

Validation MUST NOT claim to establish:

- Actual AI safety
- Secure sandbox isolation
- Authentic human authorization
- Authentic independent auditing
- Successful execution termination
- Completeness of external evidence

Passing validation proves only that the record conforms to the implemented structural and consistency requirements.

---

## 16. Reference Example Files

AKC v0.1 requires three example files.

### examples/pass.json

Expected result:

```text
PASS
No critical violations
Safety margin adequate
Audit passed
Progression not automatically activated
```

### examples/hold.json

Expected result:

```text
HOLD
Safety margin insufficient or unknown
No critical violations
Progression prohibited
```

### examples/stop.json

Expected result:

```text
STOP
Critical violation recorded
External stop request recorded
Progression prohibited
```

Each example MUST pass schema validation and decision-consistency checks.

The example filenames describe the expected evaluation decisions.

---

## 17. Security Boundaries

AKC assumes that AI-generated evaluation results may be incomplete or incorrect.

Therefore:

1. Referee conclusions MUST be independently auditable.
2. Evaluated AI systems MUST NOT modify protected enforcement controls.
3. STOP conditions MUST override ordinary progression decisions.
4. Missing safety evidence MUST NOT be treated as evidence of safety.
5. Human approval MUST NOT be inferred from AI-generated text alone.

In v0.1, these are protocol and architectural requirements.

The reference validator cannot enforce operating-system permissions, network isolation, or hardware controls.

---

## 18. Relationship to Other Systems

AKC is a minimal evaluation governance layer.

It MAY be integrated with:

- Reasoning Resource Governance (RRG)
- Cognitive Switchboard
- Reasoning Topology Lab (RTL)
- Virtual–Real Transition Axis (VRTA)

Possible responsibilities:

| System | Responsibility |
|---|---|
| AKC | Kumite evaluation and progression decisions |
| RRG | Reasoning resource allocation |
| Cognitive Switchboard | Controlled role switching |
| RTL | Reasoning experiments and analysis |
| VRTA | Virtual-to-real execution transition |

Integration is optional.

AKC v0.1 MUST remain independently understandable and testable.

---

## 19. Out of Scope

AKC v0.1 does not implement:

- Autonomous AI self-development
- Real-time model-vs-model adversarial training
- Production Guardian AI
- Hardware kill switches
- Production execution isolation
- Autonomous permission escalation
- Universal AI risk scoring
- Full safety-margin measurement infrastructure
- Tamper-proof audit infrastructure
- Cross-organization regulatory enforcement

These features MAY be considered in future versions if experimental evidence demonstrates a need.

---

## 20. Conformance

An AKC v0.1 record-validation implementation is conformant when it:

1. Accepts records matching the specified schema and consistency rules.
2. Rejects structurally invalid records.
3. Enforces STOP precedence.
4. Prevents PASS when required safety evidence is insufficient.
5. Rejects unauthorized progression states.
6. Correctly validates the official PASS, HOLD, and STOP examples.

Conformance applies only to record validation.

It MUST NOT be represented as certification of operational AI safety.

---

## 21. Future Research

Potential future work includes:

### v0.2

- Simulated Kumite experiments
- Safety-margin measurement studies
- Detection reliability evaluation
- False-positive and false-negative analysis

### v0.3

- Independent enforcement interfaces
- Verified stop acknowledgements
- Controlled Guardian integration
- Limited authorization experiments

Version progression should be evidence-driven rather than automatic.

---

## 22. Final Principle

AKC is not designed to maximize AI development speed.

It is designed to preserve verified control boundaries during capability development.

> Capability improvement is permitted only when applicable safety requirements remain satisfied and progression is explicitly authorized by humans.

**AI Kumite Control — Capability evolves. Control must remain verifiable.**
