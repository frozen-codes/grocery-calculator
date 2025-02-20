import json
import os
from typing import Dict, Any

# Constants
ITEMS_FILE = os.path.join("data", "items.json")

def load_items() -> Dict[str, Any]:
    """Load items from the JSON file."""
    try:
        if not os.path.exists(ITEMS_FILE):
            return {}
        with open(ITEMS_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

def save_items(items: Dict[str, Any]) -> None:
    """Save items to the JSON file."""
    # Create data directory if it doesn't exist
    os.makedirs(os.path.dirname(ITEMS_FILE), exist_ok=True)
    
    with open(ITEMS_FILE, 'w', encoding='utf-8') as file:
        json.dump(items, file, indent=4)

def add_item(name: str, price: float, unit: str) -> None:
    """Add a new item to the inventory."""
    items = load_items()
    
    # Validate inputs
    if not name.strip():
        raise ValueError("Item name cannot be empty")
    if price <= 0:
        raise ValueError("Price must be greater than 0")
    if unit not in ["kg", "packet"]:
        raise ValueError("Unit must be either 'kg' or 'packet'")
    if name in items:
        raise ValueError(f"Item '{name}' already exists")
    
    items[name] = {
        "price": float(price),
        "unit": unit
    }
    save_items(items)

def remove_item(name: str) -> None:
    """Remove an item from the inventory."""
    items = load_items()
    if name not in items:
        raise ValueError(f"Item '{name}' not found")
    
    del items[name]
    save_items(items)

def list_items() -> Dict[str, Any]:
    """List all items in the inventory."""
    return load_items() 