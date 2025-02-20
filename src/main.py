from rich.console import Console
from rich.prompt import Prompt, IntPrompt, FloatPrompt
from rich.table import Table
from item_manager import load_items, add_item, remove_item
from calculator import calculate_quantity
from receipt_handler import generate_receipt, save_receipt
import os

# Initialize Rich console
console = Console()

def display_items():
    """Display all items in a formatted table."""
    items = load_items()
    if not items:
        console.print("[yellow]No items in inventory![/yellow]")
        return

    table = Table(title="Available Products")
    table.add_column("Name", style="cyan")
    table.add_column("Price (₹)", style="green")
    table.add_column("Unit", style="magenta")

    for name, details in items.items():
        table.add_row(name, f"₹{details['price']}", details['unit'])

    console.print(table)

def manage_products():
    """Handle product management operations."""
    while True:
        try:
            console.print("\n[bold blue]===== Manage Products =====[/bold blue]")
            console.print("1. Add product")
            console.print("2. Remove product")
            console.print("3. List products")
            console.print("4. Back to main menu")
            
            choice = Prompt.ask("Enter your choice", choices=["1", "2", "3", "4"])
            
            if choice == "1":
                name = Prompt.ask("Enter product name").strip()
                if not name:
                    console.print("[red]Product name cannot be empty![/red]")
                    continue

                try:
                    price = FloatPrompt.ask("Enter price per unit")
                    if price <= 0:
                        console.print("[red]Price must be greater than 0![/red]")
                        continue
                except ValueError:
                    console.print("[red]Please enter a valid price![/red]")
                    continue

                unit = Prompt.ask("Enter unit", choices=["kg", "packet"])
                
                try:
                    add_item(name, price, unit)
                    console.print("[green]Product added successfully![/green]")
                except ValueError as e:
                    console.print(f"[red]Error: {str(e)}[/red]")
                    
            elif choice == "2":
                display_items()
                name = Prompt.ask("Enter product name to remove").strip()
                try:
                    remove_item(name)
                    console.print("[green]Product removed successfully![/green]")
                except ValueError as e:
                    console.print(f"[red]Error: {str(e)}[/red]")
                    
            elif choice == "3":
                display_items()
                
            elif choice == "4":
                break

        except Exception as e:
            console.print(f"[red]An unexpected error occurred: {str(e)}[/red]")

def new_transaction():
    """Handle new transaction operations."""
    items = load_items()
    receipt_items = {}
    
    if not items:
        console.print("[red]No products available. Please add products first![/red]")
        return
    
    while True:
        try:
            console.print("\n[bold blue]===== New Transaction =====[/bold blue]")
            display_items()
            
            item_name = Prompt.ask("\nEnter item name (or 'done' to finish)").strip()
            if item_name.lower() == 'done':
                break
                
            if item_name not in items:
                console.print("[red]Product not found![/red]")
                continue
                
            try:
                amount = FloatPrompt.ask("Enter amount (₹)")
                if amount <= 0:
                    console.print("[red]Amount must be greater than 0![/red]")
                    continue

                item = items[item_name]
                quantity = calculate_quantity(item['price'], item['unit'], amount)
                
                console.print(f"\nQuantity: [green]{quantity} {item['unit']}[/green]")
                
                if Prompt.ask("Add to receipt? (y/n)", choices=["y", "n"]) == 'y':
                    receipt_items[item_name] = {
                        "quantity": quantity,
                        "price": item['price'],
                        "unit": item['unit']
                    }
                    console.print("[green]Item added to receipt![/green]")
            except ValueError as e:
                console.print(f"[red]Error: {str(e)}[/red]")
                
        except Exception as e:
            console.print(f"[red]An unexpected error occurred: {str(e)}[/red]")
            
    if receipt_items:
        try:
            receipt = generate_receipt(receipt_items)
            console.print("\n[bold]Receipt:[/bold]")
            console.print(receipt)
            filename = save_receipt(receipt)
            console.print(f"\n[green]Receipt saved as: {filename}[/green]")
        except Exception as e:
            console.print(f"[red]Error generating receipt: {str(e)}[/red]")

def main():
    """Main application loop."""
    console.print("[bold blue]Welcome to Grocery Shop Manager![/bold blue]")
    
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    while True:
        try:
            console.print("\n[bold blue]===== Main Menu =====[/bold blue]")
            console.print("1. New Transaction")
            console.print("2. Manage Products")
            console.print("3. Exit")
            
            choice = Prompt.ask("Enter your choice", choices=["1", "2", "3"])
            
            if choice == "1":
                new_transaction()
            elif choice == "2":
                manage_products()
            elif choice == "3":
                console.print("[yellow]Thank you for using Grocery Shop Manager![/yellow]")
                break
                
        except Exception as e:
            console.print(f"[red]An unexpected error occurred: {str(e)}[/red]")
            console.print("[yellow]Please try again.[/yellow]")

if __name__ == "__main__":
    main()