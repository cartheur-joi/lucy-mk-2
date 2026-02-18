# Risk Register (v0.1)

| ID | Risk | Severity | Likelihood | Mitigation | Trigger |
|---|---|---|---|---|---|
| RSK-01 | Shoulder torque insufficient for planned arm mass | High | Medium | early torque budget, bench module test, gear/belt reduction option | failure to hold arm posture under load |
| RSK-02 | Printed structural parts crack at joints | High | Medium | move load paths to metal, add fillets, higher-temp polymers | visible crack growth in cycle tests |
| RSK-03 | Harness fatigue at moving joints | High | Medium | strain relief, bend radius control, silicone wire, cycle test | intermittent sensor or motor signal loss |
| RSK-04 | Controller brownout under transient load | High | Medium | separate rails, bulk capacitance, inrush management | unexpected reset during multi-joint motion |
| RSK-05 | Thermal runaway in compact actuator zones | High | Medium | thermal sensors, duty limiting, venting | temperature excursions above threshold |
| RSK-06 | Excess backlash degrades control quality | Medium | High | preload strategy, better bearings, stiffer interfaces | growing tracking error over time |
| RSK-07 | Vendor metal tolerances break fit-up | Medium | Medium | first article inspection, tolerance stack review, adjustable slots | repeated rework at assembly stage |
| RSK-08 | Integration schedule slips due to reprint/rework loops | Medium | High | subsystem gates, fixture-driven validation, weekly freeze windows | milestone misses on two consecutive checkpoints |

## Review Cadence

- Weekly risk review during active build.
- Update severity/likelihood after each integration checkpoint.

[Back to README](../../README.md)
