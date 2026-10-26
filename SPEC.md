# Rock, Paper, Scissors

## RPS-001: Play a round

**Purpose:** one person plays a quick round against the computer.

- Choose rock, paper, or scissors. The computer chooses one move for that round.
- Display both choices and the result: **You win!**, **Computer wins**, or **It’s a tie**.
- Choosing again starts an independent round. No score or saved history.
- Keep the supplied interface and server. Name/color changes can wait until the rules work.

### Expected results

Results are from the **player’s perspective**. `determine_winner(player, computer)` in `game.py` returns `win`, `lose`, or `tie`. Inputs are the lowercase moves below; the supplied server rejects other choices.

| Player | Computer | Expected return |
| --- | --- | --- |
| rock | rock | tie |
| rock | paper | lose |
| rock | scissors | win |
| paper | rock | win |
| paper | paper | tie |
| paper | scissors | lose |
| scissors | rock | lose |
| scissors | paper | win |
| scissors | scissors | tie |

### Agreed plan

- Implement one independent round in `game.py`, keeping the supplied interface and server, with no score or saved history.
- Predicted example: player rock versus computer paper returns `lose` and displays **Computer wins**, because paper covers rock. This valid losing round is a positive case.
- Add nine explicit unit outcomes from the table above, including wins, losses, and ties.
- Add a submitted-round integration check that fixes only the computer choice and verifies both moves and the correct result using the real rules.
- Reuse the supplied missing/unsupported-input integration checks; an unsupported move such as `lizard` must return HTTP 400 with a helpful explanation without calling the rules.
- Add a real-browser round and replay using the supplied fixtures and real rules, fixing only the computer choice.
- Run the full `.venv/bin/python check.py`, review the diff against this spec, discuss the test for rock versus paper, then play and review an actual round.

### Checks

Before coding, agree this small test plan with AI:

| Level | Cases and evidence |
| --- | --- |
| Unit — positive | All nine literal expected results above, including valid losses and ties. |
| Integration — positive | A submitted round uses the real rule function and displays both choices and the correct result. Fix the computer choice for the test. |
| Integration — negative | Reuse supplied missing/unsupported-move tests: HTTP 400 and a helpful explanation, without calling the rules. A crash is not the intended result. |
| E2E — positive | Add a real-browser round and replay in tests/e2e/test_round.py using the supplied live_server/page fixtures. Fix only the computer choice; use real rules and real HTTP. |

Use `unit`, `integration`, and `e2e` pytest markers. Run `.venv/bin/python check.py` for Black, Pylint, fast tests, and browser checks; then review the diff. Keep shared settings and meaningful assertions intact. The student still plays, inspects a rule and its test, and gives feedback. Browser automation does not establish every aspect of usability or application performance.

### Work record

- Issue: [RPS-001: Play a round](https://github.com/kaw393939/is218rp003/issues/1).
- Pull request: [RPS-001: Play a round #2](https://github.com/kaw393939/is218rp003/pull/2).
- CI: [Python checks run](https://github.com/kaw393939/is218rp003/actions/runs/40372360126) for commit `d9c5370e49a7e6c19acf185e774ebb80c19e0323`.
- Implementation: [game.py](game.py) returns the result of one independent round. The supplied server and interface are unchanged.
- Checks (2026-10-26): `.venv/bin/python check.py` passed Black, Pylint, 23 non-browser tests, and 6 Chromium tests. [Rule and request tests](tests/test_game.py) cover all nine literal matchups and a submitted rock-versus-paper loss. [Browser round and replay](tests/e2e/test_round.py) checks a loss followed by a win using real rules. Supplied missing/unsupported-input checks remain in use.
- Review: inspected the changed code, both new test files, and the diff against the agreed plan; no issues found. `git diff --check` passed.
- Student browser observation: chose scissors, the computer chose paper, and the game displayed a player win, matching the expected result. Automated checks do not establish every aspect of usability or performance.
- Keyboard review: the student confirmed that Tab to select a move and Enter to submit another round worked.
- Test discussion: the student identified that the rock-versus-paper test catches an incorrect player win. Provided help explaining `assert`, the real request test, and browser round/replay assertions.
