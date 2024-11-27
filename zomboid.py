import csv
import argparse

class InventoryManager:
    """
    A class to manage inventory items by reading from a CSV file, displaying items, 
    fetching items by ID, and searching items by name.
    """
    
    def __init__(self):
        self.items = []

    def read_csv(self, file_path):
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.items = [row for row in reader if row]
        except FileNotFoundError:
            print("File not found. Please check the file path and try again.")
        except csv.Error as e:
            print(f"Error reading CSV file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_items(self, page_size=10):
        if not self.items:
            print("No items available to display.")
            return

        total_items = len(self.items)
        current_page = 0

        while True:
            start_index = current_page * page_size
            end_index = min(start_index + page_size, total_items)
            page_items = self.items[start_index:end_index]

            print(f"\nPage {current_page + 1}")
            for item in page_items:
                print(item)

            if end_index >= total_items:
                print("No more items to display.")
                break

            user_input = input("Press Enter to view the next page, or type 'exit' to quit: ")
            if user_input.lower() == 'exit':
                break

            current_page += 1

    def get_item_by_id(self, item_id):
        for item in self.items:
            if item.get('ID') == str(item_id):
                return item
        print(f"Item with ID {item_id} not found.")
        return None

    def search_item_by_name(self, name):
        results = [item for item in self.items if name.lower() in item.get('Name', '').lower()]
        if not results:
            print(f"No items found with name containing '{name}'.")
        return results

    def get_condition_percentage(self, name_filter=None):
        if not self.items:
            print("Inventory is empty.")
            return

        filtered_items = self.items
        if name_filter:
            filtered_items = [item for item in self.items if name_filter.lower() in item.get('Name', '').lower()]

        if not filtered_items:
            print(f"No items found for the filter '{name_filter}'.")
            return

        """Count the occurrences of each condition"""
        condition_counts = {}
        for item in filtered_items:
            condition = item.get('Condition', 'Unknown')
            condition_counts[condition] = condition_counts.get(condition, 0) + 1

        """Calculate the total and percentages"""
        total_filtered = len(filtered_items)
        condition_percentages = {k: (v / total_filtered) * 100 for k, v in condition_counts.items()}

        """Display all items with their condition and percentage"""
        print("\nItems with their condition percentages:")
        for item in filtered_items:
            condition = item.get('Condition', 'Unknown')
            percentage = condition_percentages.get(condition, 0)
            print(f"ID: {item.get('ID', 'N/A')}, Name: {item.get('Name', 'N/A')}, "
                  f"Condition: {condition}, Percentage: {percentage:.2f}%")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manage inventory items.")
    parser.add_argument("file", help="Path to the CSV file containing inventory data.")
    parser.add_argument("--display", action="store_true", help="Display items in the inventory.")
    parser.add_argument("--id", type=str, help="Get item by ID.")
    parser.add_argument("--search", type=str, help="Search items by name.")
    parser.add_argument("--percentage", action="store_true", help="Get percentage by condition for all items.")
    parser.add_argument("--percentage-filter", type=str, help="Get percentage by condition for items matching a name.")

    args = parser.parse_args()
    manager = InventoryManager()

    """Read the CSV file"""
    manager.read_csv(args.file)

    """Execute CLI commands"""
    if args.display:
        manager.display_items()

    if args.id:
        item = manager.get_item_by_id(args.id)
        if item:
            print("Item by ID:", item)

    if args.search:
        results = manager.search_item_by_name(args.search)
        if results:
            print("Search results:", results)

    if args.percentage:
        manager.get_condition_percentage()

    if args.percentage_filter:
        manager.get_condition_percentage(name_filter=args.percentage_filter)
