# Helper functions for process_transaction to reduce complexity
def _process_usd_vip_transaction(is_verified: bool, risk_score: int) -> str:
    """Handles USD VIP user transactions."""
    if is_verified:
        if risk_score < 20:
            return "APPROVED_INSTANT"
        else:
            return "MANUAL_REVIEW"
    else:
        return "VERIFICATION_REQUIRED"

def _process_usd_standard_transaction(risk_score: int) -> str:
    """Handles USD STANDARD user transactions."""
    if risk_score < 10:
        return "APPROVED_TIER2"
    else:
        return "HOLD"

def _process_eur_transaction(is_verified: bool, risk_score: int) -> str:
    """Handles EUR transactions."""
    if is_verified and risk_score < 15:
        return "APPROVED_EU"
    else:
        return "DECLINED_RISK"

def _process_large_transaction(currency: str, user_status: str, is_verified: bool, risk_score: int) -> str:
    """Handles transactions with amount > 1000."""
    if currency == "USD":
        if user_status == "VIP":
            return _process_usd_vip_transaction(is_verified, risk_score)
        elif user_status == "STANDARD":
            return _process_usd_standard_transaction(risk_score)
        # If user_status is neither VIP nor STANDARD for USD, result is UNKNOWN
        return "UNKNOWN"
    elif currency == "EUR":
        return _process_eur_transaction(is_verified, risk_score)
    # If currency is neither USD nor EUR for large amount, result is UNKNOWN
    return "UNKNOWN"

def _process_small_transaction(risk_score: int) -> str:
    """Handles transactions with amount <= 1000."""
    if risk_score > 80:
        return "DECLINED_HIGH_RISK"
    else:
        return "APPROVED_SMALL"

# High Cyclomatic Complexity Hotspot (Radon Complexity > 10)
def process_transaction(amount, currency, user_status, is_verified, risk_score):
    """Process high-risk multi-tier financial transaction."""
    if amount > 1000:
        return _process_large_transaction(currency, user_status, is_verified, risk_score)
    else:
        return _process_small_transaction(risk_score)

def run_service():
    # The 'conn' variable was assigned but never used. Removed for quality improvement.
    # If a database connection is needed, it should be explicitly used or closed.
    # conn = get_connection()
    status = process_transaction(2500, "USD", "VIP", True, 5)
    print(f"Transaction status: {status}")
    return status

if __name__ == "__main__":
    run_service()