# Changelog

All notable changes to **AI Kumite Control (AKC)** will be documented in this file.

This project follows the principles of [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and uses [Semantic Versioning](https://semver.org/spec/v2.0.0.html) as a versioning guideline.

---

## [0.1.0] - 2026-11-23

### Initial Experimental Release

AI Kumite Control (AKC) v0.1.0 introduces a minimal safety governance protocol for evaluating AI capability development against verified control boundaries.

The initial release focuses on structured Kumite evaluation, safety-margin assessment, decision consistency, and human-authorized progression.

### Added

#### Core Protocol

- Introduced the AI Kumite Control (AKC) architecture.
- Defined Kumite-based evaluation between Development AI and Control AI.
- Established seven logical roles:
  - Human Authority
  - Guardian
  - Development AI
  - Control AI
  - Referee AI
  - Independent Audit
  - External Enforcer
- Defined three evaluation stages:
  - BASIC
  - CONTROLLED
  - ADVERSARIAL
- Established human authorization as a mandatory condition for progression.

#### Safety Governance

- Introduced the categorical safety-margin assessment:
  - ADEQUATE
  - INSUFFICIENT
  - UNKNOWN
- Defined three evaluation decisions:
  - PASS
  - HOLD
  - STOP
- Established decision priority:
  - STOP > HOLD > PASS
- Required STOP when a CRITICAL finding is recorded.
- Required HOLD when safety evidence or mandatory evaluation conditions are insufficient.
- Prevented automatic progression based solely on capability improvement.
- Distinguished external stop requests from verified execution termination.

#### Evaluation Records

- Added `schemas/kumite-result.schema.json` using JSON Schema Draft 2020-12.
- Defined structured records for:
  - Capability assessment
  - Control assessment
  - Safety-margin assessment
  - Evaluation findings
  - Independent audit
  - Decision rationale
  - Stop-request status
  - Progression authorization

#### Reference Examples

- Added `examples/pass.json` for a successful evaluation without automatic progression.
- Added `examples/hold.json` for unresolved safety margins and pending audit.
- Added `examples/stop.json` for a critical authority-boundary violation requiring a stop request.

#### Validation

- Added `scripts/validate.py` for schema and decision-consistency validation.
- Added three canonical example checks.
- Added seven negative regression checks covering:
  - Invalid decision changes
  - UNKNOWN safety margin incorrectly marked PASS
  - CRITICAL finding incorrectly marked PASS
  - Missing control evidence
  - Unauthorized progression
  - Missing STOP request
  - Missing required fields
- Added `.github/workflows/validate.yml` for automated validation.
- Confirmed successful execution of the initial GitHub Actions workflow.

### Security and Safety Boundaries

- Separated AI evaluation decisions from actual execution enforcement.
- Required independent enforcement mechanisms to remain outside the modification authority of evaluated AI systems.
- Prohibited automatic privilege expansion based on evaluation results.
- Required explicit human approval for progression.
- Treated missing or inconclusive safety evidence as insufficient for PASS.

### Known Limitations

AKC v0.1.0 is an experimental specification and record-validation prototype.

It does not provide:

- Operational AI safety certification
- Autonomous AI self-development
- Production Guardian AI
- Real-time Kumite execution
- Hardware or operating-system-level kill switches
- Verified execution termination
- Cryptographic verification of human approvals
- Tamper-proof audit storage
- Universal numerical safety thresholds
- Production-grade sandbox isolation

Passing validation confirms consistency with implemented protocol rules. It does not prove the safety of an AI system.

### Future Directions

Potential research topics include:

- Simulated Kumite experiments
- Control-gap measurement
- Safety-margin evaluation methods
- Detection reliability and false-positive analysis
- Independent enforcement verification
- Limited integration with existing AI governance systems

Future changes will be guided by observed limitations and experimental evidence.

---

## Project Principle

> Capability improvement alone does not authorize progression.
>
> AI development must remain within verified control boundaries, with independent oversight and human authorization.

**AI Kumite Control — Capability evolves. Control must remain verifiable.**
