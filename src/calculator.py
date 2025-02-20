import decimal
from typing import Union, Tuple

def calculate_quantity(price: float, unit: str, customer_amount: float) -> Union[float, int]:
    """
    Calculate the quantity based on price and customer amount.
    
    Args:
        price: Price per unit
        unit: Unit of measurement ('kg' or 'packet')
        customer_amount: Amount paid by customer
    
    Returns:
        Calculated quantity (float for kg, int for packets)
    
    Raises:
        ValueError: If inputs are invalid
    """
    try:
        # Convert to Decimal for precise calculations
        price_decimal = decimal.Decimal(str(price))
        amount_decimal = decimal.Decimal(str(customer_amount))
        
        # Validate inputs
        if price_decimal <= 0:
            raise ValueError("Price must be greater than 0")
        if amount_decimal <= 0:
            raise ValueError("Amount must be greater than 0")
            
        # Calculate quantity
        quantity = amount_decimal / price_decimal
        
        if unit == "kg":
            return float(round(quantity, 3))  # Round to 3 decimal places for kg
        elif unit == "packet":
            return int(quantity)  # Round down for packets
        else:
            raise ValueError(f"Invalid unit: {unit}. Must be 'kg' or 'packet'")
            
    except decimal.InvalidOperation:
        raise ValueError("Invalid numeric input") 