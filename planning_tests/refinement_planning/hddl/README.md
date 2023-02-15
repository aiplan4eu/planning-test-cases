This provides access to 28 domains from the 2020 IPC for hierarchical planning.

The domains are distributed with `unified_planning` library in the set of tests. 
This module simply exposes a more convenient interface for them.
They can be retrieved problems can be retrieved with `planning_tests.refinement_planning.hddl.problems()`.




Omitted domains from IPC 2020:
 - 2020-po-UM-Translog: requires multiple inheritance for types.
 - 2020-po-Woodworking: has conflicting effects in at least somes actions
 - 2020-po-Barman-BDI, 2020-po-Barman-BDI, 2020-to-Freecell-Learned-ECAI-16: duplicated names in the domain
