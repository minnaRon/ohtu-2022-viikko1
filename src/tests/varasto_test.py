import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastoon_ei_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(12)

        #varastossa pitäisi olla saldona tilavuus, joka tässä on 10
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_varastosta_voi_ottaa_vain_saldon_verran(self):
        self.varasto.lisaa_varastoon(5)

        #varastosta voi ottaa vain 5, koska saldona on 5
        self.assertAlmostEqual(self.varasto.ota_varastosta(8), 5)

    def test_konstruktoriparametrissa_alkusaldo_negatiivinen_alkusaldoksi_nolla(self):
        self.varasto2 = Varasto(10,-2)

        #varaston saldon pitäisi olla 0, koska annettu alkusaldo oli negatiivinen
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_konstruktoriparametrissa_tilavuus_negatiivinen_tilavuudeksi_nolla(self):
        self.varasto2 = Varasto(-1)

        #varaston tilavuuden pitäisi olla 0, koska annettu tilavuus oli negatiivinen
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)

    def test_varastoon_ei_voi_lisata_negatiivista_maaraa(self):
        self.varasto.lisaa_varastoon(-2)

        #varaston saldon pitäisi olla 0, koska lisättävä määrä oli negatiivinen
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varastosta_ei_voi_ottaa_negatiivista_maaraa(self):
        self.varasto.ota_varastosta(-2)

        #varaston saldon pitäisi olla 0, koska otettava määrä oli negatiivinen
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_merkkijonoesityksessa_oikeat_tiedot(self):

        #f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
        self.assertAlmostEqual(str(self.varasto),"saldo = 0, vielä tilaa 10")

