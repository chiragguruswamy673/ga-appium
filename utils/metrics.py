# utils/metrics.py
def penalize_redundancy(sequence):
    taps = sum(1 for s in sequence if s[0] == "tap")
    swipes = sum(1 for s in sequence if s[0] == "swipe")
    inputs = sum(1 for s in sequence if s[0] == "input")
    # Penalize excessive swipes and duplicate taps
    return max(0, 10 - (swipes * 0.5 + max(0, taps - inputs) * 0.2))

def reward_credentials_outcome(context):
    # context is set by fitness.run_sequence e.g., {"login_success": True, "error_banner": False}
    base = 0
    if context.get("login_success"): base += 5
    if context.get("error_banner"): base -= 3
    return base

def length_cost(sequence):
    # Encourage shorter sequences
    return -0.05 * len(sequence)