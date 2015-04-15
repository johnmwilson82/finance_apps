import gui
import wx
import sys

import symbols
import sectors
import keystats

class YqlFinanceApp(wx.App):

    def loadState(self):
        pass

    def saveState(self):
        pass

    def updateSymbols(self):
        self._symbols = symbols.update_symbols(self._symbol_filter)

    def updateSectors(self):
        self._sectors = sectors.update_sectors()

    def updateIndustries(self, sector_indices=[]):
        self._industries = sectors.update_industries(self._sectors,
                                                     sector_indices)

    def genStatusStringFromSymbol(self, symbol):
        stats = keystats.get_keystats([symbol.symbol])
        #import pdb
        #pdb.set_trace()
        stats = stats[symbol.symbol]
        ret = u'Symbol: ' + stats.symbol + '\n'
        ret += u'Market Cap.: ' + stats.MarketCap + '\n'
        ret += u'Book value: ' + stats.BookValuePerShare + '\n'
        ret += u'Diluted EPS: ' + stats.DilutedEPS + '\n'
        ret += u'Trailing P/E: ' + stats.TrailingPE + '\n'
        ret += u'Dividend/Yield: ' + stats.TrailingAnnualDividend + ' / ' + \
                                     stats.TrailingAnnualYield + '\n'
        return ret

    @property
    def symbols_strings(self):
        return [unicode(symb) for symb in self._symbols]

    @property
    def symbols(self):
        return self._symbols

    @property
    def sectors_strings(self):
        return [unicode(sect) for sect in self._sectors]

    @property
    def sectors(self):
        return self._sectors

    @property
    def industries_strings(self):
        return [unicode(ind) for ind in self._industries]

    @property
    def industries(self):
        return self._industries

    @property
    def symbol_filter(self):
        return self._symbol_filter

    @symbol_filter.setter
    def set_symbol_filter(self, val):
        self._symbol_filter = unicode(val)

    def OnInit(self):
        self._symbols = symbols.load_symbols_from_cache()
        self._sectors = sectors.load_sectors_from_cache()
        self._industries = sectors.update_industries(self._sectors)
        self._symbol_filter = '.L'
        self.main_frame = gui.FinanceAppGui(None, self)
        self.SetTopWindow(self.main_frame)
        self.main_frame.Show(True)

        return True

def main():
    financeapp = YqlFinanceApp(redirect=False)
    financeapp.MainLoop()

if __name__=='__main__':
    sys.exit(main())

