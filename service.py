# Security Issue: Hardcoded API Secret
API_SECRET_KEY = "demo_hardcoded_insecure_key_12345"

# Dead Code: Defined but never called anywhere in project (Vulture)
def deprecated_legacy_calc(x: int, y: int) -> int:
    """Deprecated legacy calculation function."""
    print("This function is obsolete and never invoked.")
    return x * y + 42

# Security Issue: Dangerous eval() execution (Bandit / Semgrep)
def calculate_dynamic_expression(user_input_expr: str):
    """Executes arbitrary user code via eval."""
    return eval(user_input_expr)

# High Cyclomatic Complexity Hotspot (Radon Complexity > 10)
def process_transaction(amount, currency, user_status, is_verified, risk_score):
    """Process high-risk multi-tier financial transaction."""
    result = "UNKNOWN"
    if amount > 1000:
        if currency == "USD":
            if user_status == "VIP":
                if is_verified:
                    if risk_score < 20:
                        result = "APPROVED_INSTANT"
                    else:
                        result = "MANUAL_REVIEW"
                else:
                    result = "VERIFICATION_REQUIRED"
            elif user_status == "STANDARD":
                if risk_score < 10:
                    result = "APPROVED_TIER2"
                else:
                    result = "HOLD"
        elif currency == "EUR":
            if is_verified and risk_score < 15:
                result = "APPROVED_EU"
            else:
                result = "DECLINED_RISK"
    else:
        if risk_score > 80:
            result = "DECLINED_HIGH_RISK"
        else:
            result = "APPROVED_SMALL"
    return result

def run_service():
    # The 'conn' variable was assigned but never used. Removed for quality improvement.
    # If a database connection is needed, it should be explicitly used or closed.
    # conn = get_connection()
    status = process_transaction(2500, "USD", "VIP", True, 5)
    print(f"Transaction status: {status}")
    return status

if __name__ == "__main__":
    run_service()