import yql_finance_app_base
import wx
import threading

class FinanceAppGui(yql_finance_app_base.FinanceAppGuiBase):
    def __init__(self, parent, app):
        super(FinanceAppGui, self).__init__(parent)
        self.app = app
        self.updateSymbolsList()
        self.updateSectorsList()
        self.updateIndustriesList()

    def onUpdateSymbolsClick(self, event):
        self.app.updateSymbols()
        self.updateSymbolsList()

    def onSelectSymbol(self, event):
        def threadFn(id, frame):
            try:
                status_str = frame.app.genStatusStringFromSymbol(
                    frame.app.symbols[id])
                frame.m_txtStockProperties.SetValue(status_str)
            except Exception as e:
                print e
                import pdb
                pdb.set_trace()

        if event.IsSelection():
            thread = threading.Thread(target=threadFn, args=(event.GetSelection(),self))
            thread.start()

    def updateSymbolsList(self):
        self.m_symbolsList.Set(self.app.symbols_strings)

    # ===================== Sectors =====================
    def onUpdateSectorsClick(self, event):
        self.app.updateSectors()
        self.updateSectorsList()
        self.app.updateIndustries()
        self.updateIndustriesList()

    def onSectorsListToggled(self, event):
        self.app.updateIndustries(self.m_sectorsList.GetChecked())
        self.updateIndustriesList()

    def updateSectorsList(self):
        self.m_sectorsList.Set(self.app.sectors_strings)

    def updateIndustriesList(self):
        self.m_industriesList.Set(self.app.industries_strings)
