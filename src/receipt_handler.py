import os
from datetime import datetime
from typing import Dict, Any

RECEIPTS_FOLDER = os.path.join("data", "receipts")

def generate_receipt(items: Dict[str, Any]) -> str:
    """Generate a formatted receipt string."""
    if not items:
        return "No items in receipt!"

    # Create receipt header
    receipt = [
        "=" * 40,
        "GROCERY SHOP RECEIPT".center(40),
        datetime.now().strftime("%Y-%m-%d %H:%M:%S").center(40),
        "=" * 40,
        f"{'Item':<15}{'Quantity':<10}{'Price':<8}{'Total':<7}",
        "-" * 40
    ]

    # Add items and calculate total
    total = 0.0
    for item_name, details in items.items():
        quantity = details["quantity"]
        price = details["price"]
        unit = details["unit"]
        item_total = quantity * price
        total += item_total

        receipt.append(
            f"{item_name:<15}{f'{quantity} {unit}':<10}₹{price:<7.2f}₹{item_total:<6.2f}"
        )

    # Add footer
    receipt.extend([
        "-" * 40,
        f"{'TOTAL:':<30}₹{total:.2f}",
        "=" * 40,
        "Thank you for shopping with us!".center(40),
        "=" * 40
    ])

    return "\n".join(receipt)

def save_receipt(receipt: str) -> str:
    """Save the receipt to a file."""
    # Create receipts directory if it doesn't exist
    os.makedirs(RECEIPTS_FOLDER, exist_ok=True)
    
    # Generate unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(RECEIPTS_FOLDER, f"receipt_{timestamp}.txt")
    
    # Save receipt
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(receipt)
    
    return filename 