def calculate_emi(principal, monthly_interest_rate, tenure_in_months):
    emi = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure_in_months / ((1 + monthly_interest_rate) ** tenure_in_months - 1)
    return emi

# Example usage:
principal = 100000
monthly_interest_rate = 0.005
tenure_in_months = 60
print(calculate_emi(principal, monthly_interest_rate, tenure_in_months))