"""Real rule outcomes and a submitted round for RPS-001."""

import pytest

import app as web
from game import determine_winner


@pytest.mark.unit
def test_rock_against_rock():
    """Matching rocks tie."""
    assert determine_winner("rock", "rock") == "tie"


@pytest.mark.unit
def test_rock_against_paper():
    """The player loses because paper covers rock."""
    assert determine_winner("rock", "paper") == "lose"


@pytest.mark.unit
def test_rock_against_scissors():
    """Rock beats scissors."""
    assert determine_winner("rock", "scissors") == "win"


@pytest.mark.unit
def test_paper_against_rock():
    """Paper beats rock."""
    assert determine_winner("paper", "rock") == "win"


@pytest.mark.unit
def test_paper_against_paper():
    """Matching papers tie."""
    assert determine_winner("paper", "paper") == "tie"


@pytest.mark.unit
def test_paper_against_scissors():
    """The player loses because scissors cut paper."""
    assert determine_winner("paper", "scissors") == "lose"


@pytest.mark.unit
def test_scissors_against_rock():
    """The player loses because rock beats scissors."""
    assert determine_winner("scissors", "rock") == "lose"


@pytest.mark.unit
def test_scissors_against_paper():
    """Scissors beat paper."""
    assert determine_winner("scissors", "paper") == "win"


@pytest.mark.unit
def test_scissors_against_scissors():
    """Matching scissors tie."""
    assert determine_winner("scissors", "scissors") == "tie"


@pytest.mark.integration
def test_submitted_rock_loses_to_paper(monkeypatch):
    """A real request displays the real rule result and both choices."""
    monkeypatch.setitem(web.app.config, "TESTING", True)
    monkeypatch.setattr(web.random, "choice", lambda _moves: "paper")
    with web.app.test_client() as client:
        response = client.post("/", data={"move": "rock"})
    body = response.get_data(as_text=True)
    assert response.status_code == 200
    assert 'data-outcome="lose"' in body
    assert "Computer wins" in body
    assert 'You chose</p><p class="choice-value">Rock' in body
    assert 'Computer chose</p><p class="choice-value">Paper' in body
    assert "game rules not built yet" not in body
