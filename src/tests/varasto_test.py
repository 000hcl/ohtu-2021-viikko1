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

    def test_muuta_ei_mahdu_jos_lisataan_liikaa(self):
        self.varasto.lisaa_varastoon(20)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(),0)
    
    def test_negatiivinen_tilavuus_nollataan(self):
        varasto_b = Varasto(-20)
        self.assertAlmostEqual(varasto_b.tilavuus, 0)
    
    def test_negatiivinen_saldo_nollataan(self):
        varasto_b = Varasto(10, -20)
        self.assertAlmostEqual(varasto_b.saldo, 0)
    
    def test_jos_saldo_on_suurempi_kuin_tilavuus_varasto_tayteen(self):
        varasto_b = Varasto(10, 20)
        self.assertAlmostEqual(varasto_b.paljonko_mahtuu(), 0)
    
    def test_saldo_ei_muutu_jos_lisattava_maara_on_negatiivinen(self):
        self.varasto.lisaa_varastoon(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_saldo_ei_muutu_jos_otetaan_negatiivinen_maara(self):
        self.varasto.ota_varastosta(-10)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_saldo_nollataa_jos_yritetaan_ottaa_enemmän_kuin_voidaan(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(20)
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_eri_varastoilla_on_eri_string(self):
        varasto_b = Varasto(20, 5)
        self.assertNotEqual(str(self.varasto), str(varasto_b))