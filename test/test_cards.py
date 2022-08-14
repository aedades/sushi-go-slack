from services.game_worker.game.cards import *
import emoji

CARD_COUNT = 1

class TestCards:
    def test_chopsticks(self):
        chopsticks = Chopsticks(CARD_COUNT)
        assert chopsticks.emoji == CHOPSTICKS_EMOJI

    def test_dumpling(self):
        dumpling = Dumpling(CARD_COUNT)
        assert dumpling.emoji == DUMPLING_EMOJI

    def test_maki_one(self):
        maki = MakiOne(CARD_COUNT)
        assert maki.name == f'maki_one_{CARD_COUNT}'
        assert maki.emoji == f'1{MAKI_EMOJI}'
        assert maki.value == 1

    def test_nigiri_egg(self):
        nigiri_egg = NigiriEgg(CARD_COUNT)
        assert nigiri_egg.emoji == NIGIRI_EGG_EMOJI

    def test_nigiri_salmon(self):
        nigiri_salmon = NigiriSalmon(CARD_COUNT)
        assert nigiri_salmon.emoji == NIGIRI_SALMON_EMOJI

    def test_nigiri_squid(self):
        nigiri_squid = NigiriSquid(CARD_COUNT)
        assert nigiri_squid.emoji == NIGIRI_SQUID_EMOJI

    def test_pudding(self):
        pudding = Pudding(CARD_COUNT)
        assert pudding.emoji == PUDDING_EMOJI

    def test_sashimi(self):
        sashimi = Sashimi(CARD_COUNT)
        assert sashimi.emoji == SASHIMI_EMOJI

    def test_tempura(self):
        tempura = Tempura(CARD_COUNT)
        assert tempura.emoji == TEMPURA_EMOJI

    def test_wasabi(self):
        wasabi = Wasabi(CARD_COUNT)
        assert wasabi.emoji == WASABI_EMOJI
