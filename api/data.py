from typing import Dict, List, Optional

from .common import Filter, Pagination


class Prize:
    def __init__(self, id: int, title: str, description: str, image: str):
        """Create a new instance of prize.

        Args:
            id (int): id of the prize
            title (str): name of the prize
            description (str): prize description
            image (str): url to the prize image
        """
        self.id = id
        self.title = title
        self.description = description
        self.image = image


class MockedData:
    def __init__(self):
        """Create a new instance of mocked data."""
        self.data: Dict[int, List[Prize]] = {}

        self.data[1] = [
            Prize(
                id=1,
                title="Dragon's Hoard",
                description="A chest filled with golden coins and jewels guarded by a mythical dragon.",
                image="https://example.com/image1.png",
            ),
            Prize(
                id=2,
                title="Enchanted Sword",
                description="A sword that glows with a magical aura and grants its wielder extraordinary powers.",
                image="https://example.com/image2.png",
            ),
            Prize(
                id=3,
                title="Mystic Amulet",
                description="An ancient amulet said to protect its wearer from all harm.",
                image="https://example.com/image3.png",
            ),
        ]

        self.data[2] = [
            Prize(
                id=4,
                title="Wizard's Grimoire",
                description="A book of spells and enchantments written by the greatest wizards of all time.",
                image="https://example.com/image4.png",
            ),
            Prize(
                id=5,
                title="Phoenix Feather",
                description="A rare and powerful feather from a legendary phoenix, said to bring good fortune.",
                image="https://example.com/image5.png",
            ),
            Prize(
                id=6,
                title="Elf's Bow",
                description="A finely crafted bow made by the master artisans of the Elven kingdom.",
                image="https://example.com/image6.png",
            ),
        ]

        self.data[3] = [
            Prize(
                id=7,
                title="Potion of Eternal Youth",
                description="A potion that grants the drinker everlasting youth and vitality.",
                image="https://example.com/image7.png",
            ),
            Prize(
                id=8,
                title="Invisibility Cloak",
                description="A magical cloak that renders its wearer completely invisible.",
                image="https://example.com/image8.png",
            ),
        ]

        self.data[4] = [
            Prize(
                id=9,
                title="Gryphon's Egg",
                description="A rare egg of a gryphon, said to hatch into a loyal and majestic creature.",
                image="https://example.com/image9.png",
            ),
            Prize(
                id=10,
                title="Dragon Scale Armor",
                description="Armor forged from the scales of a dragon, providing unmatched protection.",
                image="https://example.com/image10.png",
            ),
        ]

    def get_prizes(
        self,
        catalog_id: int,
        prize_filter: Optional[Filter] = None,
        pagination: Optional[Pagination] = None,
    ) -> List[Prize]:
        """Get prizes for this mocked data, filtering and paginating.

        Args:
            catalog_id (int): id of the catalog to search data from.
            prize_filter (Optional[Filter]): a dictionary with filtering rules.
            pagination (Optional[Pagination]): a dictionary with pagination rules.

        Returns:
            List[Prize]: a list containing all of the matching prizes.

        Raises:
            KeyError: if the catalog_id does not exists
        """
        catalog = self.data[catalog_id].copy()

        if prize_filter:
            prize_id = prize_filter.get("id")
            prize_description = prize_filter.get("description", "").strip()

            catalog_filterd = []

            for pr in catalog:
                is_in_description = (
                    False
                    if prize_description == ""
                    else prize_description in pr.description
                )
                if prize_id == pr.id or is_in_description:
                    catalog_filterd.append(pr)
            catalog = catalog_filterd

        if pagination:
            start_idx = (pagination["page"] - 1) * pagination["per_page"]
            end_idx = start_idx + pagination["per_page"]
            return catalog[start_idx:end_idx]

        return catalog
