from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_bug_log_34_vs_60():
    # Bug 1 from the reproduction log: 34 against 60 should say go higher
    outcome, message = check_guess(34, 60)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_single_digit_vs_two_digit():
    # String comparison would say "9" > "60"; numbers must compare as ints
    outcome, _ = check_guess(9, 60)
    assert outcome == "Too Low"
