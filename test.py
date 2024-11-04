import unittest
from zomboid import InventoryManager  

class TestInventoryManagerGetItemById(unittest.TestCase):
    def setUp(self):
        """Set up an InventoryManager instance and preload items for testing."""
        self.manager = InventoryManager()
        # Pre-load some items directly
        self.manager.items = [
            {"ID": "1", "Name": "Chicken", "Type": "Food", "Condition": "Good", "Amount": "10"},
            {"ID": "2", "Name": "Hammer", "Type": "Tool", "Condition": "Mint", "Amount": "5"},
        ]

    def test_get_item_by_existing_id(self):
        """Test that get_item_by_id returns the correct item when the ID exists."""
        item = self.manager.get_item_by_id("2")
        self.assertIsNotNone(item)
        self.assertEqual(item['Name'], "Hammer")

    def test_get_item_by_nonexistent_id(self):
        """Test that get_item_by_id returns None when the ID does not exist."""
        item = self.manager.get_item_by_id("999")
        self.assertIsNone(item)

if __name__ == "__main__":
    unittest.main()
