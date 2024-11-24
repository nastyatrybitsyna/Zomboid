import csv
from collections import Counter

class InventoryManager:
    """
    A class to manage inventory items by reading from a CSV file, displaying items, 
    fetching items by ID, searching items by name, and calculating condition statistics.
    """
    
    def __init__(self):
        """
        Initializes an instance of the InventoryManager class.
        Sets up an empty list to store inventory items.
        """
        self.items = []

    def read_csv(self, file_path):
        """
        Reads items from a CSV file and stores them in the items list.
        
        Parameters:
        - file_path (str): The path to the CSV file containing the inventory data.
        """
        try:
            with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                self.items = [row for row in reader if row]  # Ensure no empty rows are added
        except FileNotFoundError:
            print("File not found. Please check the file path and try again.")
        except csv.Error as e:
            print(f"Error reading CSV file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def display_items(self, page_size=10):
        """
        Displays items in a paginated format, showing a specified number of items per page.
        """
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
        """
        Fetches an item by its ID.
        """
        for item in self.items:
            if item.get('ID') == str(item_id):
                return item
        print(f"Item with ID {item_id} not found.")
        return None

    def search_item_by_name(self, name):
        """
        Searches for items by name and returns all items containing the specified name.
        """
        results = [item for item in self.items if name.lower() in item.get('Name', '').lower()]
        if not results:
            print(f"No items found with name containing '{name}'.")
        return results

    def get_condition_percentage(self):
        """
        Calculates the percentage distribution of items by condition.
        """
        if not self.items:
            print("No items available to analyze.")
            return {}

        condition_counts = Counter(item.get('Condition', 'Unknown') for item in self.items)
        total_items = len(self.items)
        percentages = {condition: (count / total_items) * 100 for condition, count in condition_counts.items()}
        return percentages

    def get_condition_percentage_by_name(self, name):
        """
        Retrieves the condition of items with a specific name and calculates percentage distribution for them.
        """
        filtered_items = [item for item in self.items if name.lower() in item.get('Name', '').lower()]
        if not filtered_items:
            print(f"No items found with name containing '{name}'.")
            return {}

        condition_counts = Counter(item.get('Condition', 'Unknown') for item in filtered_items)
        total_filtered_items = len(filtered_items)
        percentages = {condition: (count / total_filtered_items) * 100 for condition, count in condition_counts.items()}
        return percentages


def main():
    """
    CLI for the InventoryManager class.
    """
    manager = InventoryManager()
    manager.read_csv("inventory.csv")

    while True:
        print("\nOptions:")
        print("1. Display items")
        print("2. Get item by ID")
        print("3. Search item by name")
        print("4. Get condition percentage")
        print("5. Get condition percentages for items with a specific name")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            page_size = int(input("Enter page size (default 10): ") or 10)
            manager.display_items(page_size=page_size)
        elif choice == '2':
            item_id = input("Enter item ID: ")
            item = manager.get_item_by_id(item_id)
            if item:
                print("Item:", item)
        elif choice == '3':
            name = input("Enter item name to search: ")
            results = manager.search_item_by_name(name)
            if results:
                print("Search results:")
                for result in results:
                    print(result)
        elif choice == '4':
            percentages = manager.get_condition_percentage()
            if not percentages:
                print("No data available to calculate condition percentages.")
            else:
                print("\nCondition percentages:")
                for condition, percentage in percentages.items():
                    print(f"{condition} — {percentage:.2f}%")
                print("\nItems with their conditions:")
                for item in manager.items:
                    item_name = item.get('Name', 'Unknown')
                    item_condition = item.get('Condition', 'Unknown')
                    print(f"{item_name} ({item_condition})")
        elif choice == '5':
            name = input("Enter item name to search for condition percentages: ")
            filtered_items = [item for item in manager.items if name.lower() in item.get('Name', '').lower()]
            if not filtered_items:
                print(f"No items found with name containing '{name}'.")
            else:
                print(f"\nItems with their conditions for name containing '{name}':")
                condition_counts = Counter(item.get('Condition', 'Unknown') for item in filtered_items)
                total_items = len(filtered_items)
                for condition, count in condition_counts.items():
                    percentage = (count / total_items) * 100
                    print(f"{condition} — {percentage:.2f}%")
                for item in filtered_items:
                    item_name = item.get('Name', 'Unknown')
                    item_condition = item.get('Condition', 'Unknown')
                    print(f"{item_name} ({item_condition})")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
