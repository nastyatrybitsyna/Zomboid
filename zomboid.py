import csv

class InventoryManager:
    """
    A class to manage inventory items by reading from a CSV file, displaying items, 
    fetching items by ID, and searching items by name.
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
        
        CSV file format:
        - Each row should contain item information with column headers matching field names.
        
        Exceptions:
        - Prints an error message if the file is not found or cannot be read.
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
        
        Parameters:
        - page_size (int): The number of items to display per page (default is 10).
        
        User Interaction:
        - Displays items in pages. Users can view the next page by pressing Enter 
          or type 'exit' to quit viewing.
          
        Prints a message if there are no items to display.
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
        
        Parameters:
        - item_id (int or str): The ID of the item to retrieve.
        
        Returns:
        - dict: The item data if found, or None if the item is not found.
        
        Prints a message if no item with the specified ID is found.
        """
        for item in self.items:
            if item.get('ID') == str(item_id):
                return item
        print(f"Item with ID {item_id} not found.")
        return None

    def search_item_by_name(self, name):
        """
        Searches for items by name and returns all items containing the specified name.
        
        Parameters:
        - name (str): The name or part of the name to search for in the inventory.
        
        Returns:
        - list of dict: A list of items matching the search criteria.
        
        Prints a message if no items match the search criteria.
        """
        results = [item for item in self.items if name.lower() in item.get('Name', '').lower()]
        if not results:
            print(f"No items found with name containing '{name}'.")
        return results

# Example usage
if __name__ == "__main__":
    manager = InventoryManager()
    # Specify the correct path to your CSV file
    manager.read_csv("inventory.csv")

    # Display items with pagination
    manager.display_items(page_size=5)

    # Retrieve item by ID
    item = manager.get_item_by_id(2)
    if item:
        print("Item by ID:", item)

    # Search for an item by name
    search_results = manager.search_item_by_name("Chicken")
    if search_results:
        print("Search results:", search_results)