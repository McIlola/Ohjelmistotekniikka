import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    
    def test_saldo_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    
    def test_kortille_voi_ladata_rahaa(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 35.0)
    
    def test_rahan_ottaminen_toimii(self):
        self.assertEqual(self.maksukortti.ota_rahaa(250), True)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.5)
        self.assertEqual(self.maksukortti.ota_rahaa(2500), False)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.5)
