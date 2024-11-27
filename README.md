# Zomboid
**InventoryManager Library**
This library is designed for working with inventory lists in CSV format, specifically developed for survivalists and those who want to manage essential supplies effectively.

# Key Features of the Library:
- Reading CSV files with items: The library supports reading CSV files that contain inventory data (such as item name, condition, and quantity).
- Quickly locating needed items: You can retrieve items by their unique identifier (ID) or by their name.
- Paginated data display: Allows easy viewing of large lists of items, with configurable items per page.
- Filter support: Enables convenient display of items based on name or condition criteria.
- Condition percentages: View condition distribution percentages for the entire inventory or filtered items.
- Search by item name: Allows filtering the inventory by item name to view condition distributions.

# Requirements:
- CSV module (included in Python's standard library)
- Python 3.6+

# Installation:
- To run the program, you need Python 3.6 or higher.

- Download or copy the source code of the program. Ensure that the inventory.csv file is in the same folder as the project, or specify its path in the code.

# CSV File Structure:
The CSV file should have the following columns:

| ID | Name    | Type       | Condition | Amount |
|----|---------|------------|-----------|--------|
| 1  | Shovel  | Weapon     | Mint      | 1      |
| 2  | Hammer  | Tool       | Good      | 1      |
| 3  | Chicken | Food       | Bad       | 6      |
| 3  | Chicken | Food       | Good      | 10     |
| 4  | Bandage | First Aid  | Good      | 12     |

# Usage
- Initialize the Manager:
```python
manager = InventoryManager()
```
- Read Inventory Data:
- Use read_csv(file_path) to load inventory items from a specified CSV file.
```python
manager.read_csv("path/to/inventory.csv")
```
- Display Items:
- Call display_items(page_size=10) to display inventory items. Adjust the page_size to control the number of items shown per page.
```python
manager.display_items(page_size=5)
```
- Retrieve Item by ID:
- Use get_item_by_id(item_id) to fetch a specific item using its ID.
```python
item = manager.get_item_by_id(2)
if item:
    print("Item by ID:", item)
```
NEW:

# Display Condition Percentages. 
In the updated version of the program, the InventoryManager now provides functionality to display the condition distribution for items, and percentage breakdowns of conditions:

# How to use:
- All Items:
```python
python zomboid.py inventory.csv --display
```
- Retrieve Item by ID:
```python
python zomboid.py inventory.csv --id 2
```
- Search by name:
```python
python zomboid.py inventory.csv --search Chicken
```
- Percentage by condition for all items:
```python
python zomboid.py inventory.csv --percentage
```
- Percentage by condition for items with a specific name:
```python
python zomboid.py inventory.csv --percentage-filter Chicken
```

# Future Support for JSON
Support for JSON will be added to allow more flexible data structures, easier integration with APIs, and improved readability. Methods to read from JSON files will be introduced.

# Author
[Trubitsyna Anastasia Ruslanivna]

```mermaid
classDiagram
    class InventoryManager {
        +__init__()
        +read_csv(file_path: str)
        +display_items(page_size: int)
        +get_item_by_id(item_id: str) : Dict[str, str] 
        +search_item_by_name(name: str) : List[Dict[str, str]]
        +get_condition_percentage(name_filter: str) : Dict[str, float]
    }

    class Item {
        +ID: str
        +Name: str
        +Type: str
        +Condition: str
        +Amount: int
    }

    InventoryManager "1" *-- "*" Item : manages >





