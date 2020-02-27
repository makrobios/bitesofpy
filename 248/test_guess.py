from unittest.mock import patch

import pytest

from guess import GuessGame, InvalidNumber, MAX_NUMBER


# write test code to reach 100% coverage and a 100% mutpy score

@pytest.fixture()
def game():
    game = GuessGame(10)
    return game

def test_GuessGame_validate(game):
    with pytest.raises(InvalidNumber, match="Not a number"): 
        game._validate("spam")
    with pytest.raises(InvalidNumber, match="Negative number"):
        game._validate(-16)
    with pytest.raises(InvalidNumber, match="Number too high"):
        game._validate(16)
    assert game._validate(MAX_NUMBER) == MAX_NUMBER
    assert game._validate(0) == 0

@patch(target="guess.input", side_effect=[1,15, 10])
def test_GuessGame_call_number_range(mock_input, capsys, game):
    game()
    captured = capsys.readouterr().out.split("\n")
    assert captured[1] == "Too low"
    assert captured[3] == "Too high"
    assert captured[5] == "You guessed it!"

def test_GuessGame_call_max_guesses(capsys, game):
    game.attempt = 6
    game()
    captured = capsys.readouterr().out.strip()
    assert captured == f"Sorry, the number was {game.secret_number}"

@patch(target="guess.input", side_effect=["spam", 10])
def test_GuessGame_call_wrong_input(mock_input, capsys, game):
    game()
    captured = capsys.readouterr().out
    assert captured == ("Guess a number: \n" 
                        "Enter a number, try again\n"
                        "Guess a number: \n"
                        "You guessed it!\n")

@patch(target="guess.input", side_effect=[1,2,3,4,5])    
def test_Guess_Game_call_max_guesses(mock_input, capsys, game):
    game()
    captured = capsys.readouterr().out.split("\n")
    assert captured[-2] == f"Sorry, the number was {game.secret_number}"
    assert mock_input.call_count == 5
