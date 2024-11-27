import csv
import argparse

class CSVReader:
    """Class for reading CSV files and returning data as a list of dictionaries."""
    
    @staticmethod
    def read_csv(file_path):
        """Reads data from a CSV file and returns it as a list of dictionaries."""
        with open(file_path, mode='r') as file:
            csv_reader = csv.DictReader(file)
            return list(csv_reader)


class SurvivalInventory:
    """Class to manage items from a CSV file, allowing loading, searching, and viewing data."""
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.inventory = CSVReader.read_csv(file_path)

    def get_item_by_id(self, item_id):
        """Finds an item by ID."""
        return [item for item in self.inventory if item.get('ID') == str(item_id)]

    def search_items_by_name(self, search_term):
        """Finds items by a partial name match."""
        return [item for item in self.inventory if search_term.lower() in item.get('Name', '').lower()]

    def display_all_items_with_condition_percentage(self):
        """Displays all items with their condition and percentage of the total inventory."""
        total_items = len(self.inventory)
        condition_counts = {}

        """Count items by condition"""
        for item in self.inventory:
            condition = item['Condition']
            condition_counts[condition] = condition_counts.get(condition, 0) + 1

        print(f"{'Name':<20}{'Condition':<15}{'Percentage':<10}")
        print('-' * 45)

        for item in self.inventory:
            condition = item['Condition']
            percentage = (condition_counts[condition] / total_items) * 100
            print(f"{item['Name']:<20}{condition:<15}{percentage:<10.2f}")

    def get_condition_percentage_by_name(self, name):
        """Calculates the percentage of items matching a condition filtered by name."""
        filtered_items = [item for item in self.inventory if name.lower() in item['Name'].lower()]
        total_filtered = len(filtered_items)

        if total_filtered == 0:
            print(f"No items found with the name containing '{name}'.")
            return

        condition_counts = {}
        for item in filtered_items:
            condition = item['Condition']
            condition_counts[condition] = condition_counts.get(condition, 0) + 1

        print(f"Condition percentages for items with name '{name}':")
        for condition, count in condition_counts.items():
            percentage = (count / total_filtered) * 100
            print(f"  {condition}: {percentage:.2f}%")


def main():
    parser = argparse.ArgumentParser(description="Manage and analyze survival inventory from a CSV file.")
    parser.add_argument('file', help="Path to the inventory CSV file.")
    subparsers = parser.add_subparsers(dest='command', required=True)

    """Subparser for displaying all items"""
    parser_display_all = subparsers.add_parser('display_all', help="Display all items with condition and percentages.")

    """Subparser for getting condition percentage by name"""
    parser_condition_percentage = subparsers.add_parser('state_percentage', help="Get condition percentage by item name.")
    parser_condition_percentage.add_argument('name', help="Name of the item to filter by.")

    args = parser.parse_args()

    manager = SurvivalInventory(args.file)

    if args.command == 'display_all':
        manager.display_all_items_with_condition_percentage()
    elif args.command == 'state_percentage':
        manager.get_condition_percentage_by_name(args.name)


if __name__ == "__main__":
    main()
